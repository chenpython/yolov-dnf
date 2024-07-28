
import cv2,torch
import win32gui,win32con
import numpy as np

from utils1.general import non_max_suppression
from utils1.augmentations import letterbox
from utils1.plots import Annotator, colors
from utils1.general import (cv2, non_max_suppression, scale_boxes, xyxy2xywh)

from det_dxf.grabScreen import grab_screen,screenshot
from det_dxf.dxf_model import load_model
from det_dxf.auto_control import *
from det_dxf.directkeys import move,move1

imgsz = 640
conf_thres=0.25
iou_thres=0.45
max_det=1000

obj_names = ['hero','door','moster','money','boss']
action_cache = ""

paused = False
frame = 0  # 帧
fs = 4 # 每四帧处理一次

model = load_model()

while True:
    if not paused:
        t_start = time.time()
        img0 = grab_screen(region=(0, 0, 800, 600))  # 捕获的窗口范围
        frame += 1
        if frame % fs == 0:
            im = letterbox(img0, imgsz, stride=model.stride, auto=model.pt)[0]  # padded resize
            im = im.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
            im = np.ascontiguousarray(im)  # contiguous

            # Run inference
            im = torch.from_numpy(im).to(model.device)
            im = im.half() if model.fp16 else im.float()  # uint8 to fp16/32
            im /= 255  # 0 - 255 to 0.0 - 1.0
            if len(im.shape) == 3:
                im = im[None]  # expand for batch dim

            pred = model(im, augment=False, visualize=False)
            pred = non_max_suppression(pred, conf_thres, iou_thres, None, False, max_det=max_det)
            #print(pred)

            # Process predictions
            for i, det in enumerate(pred):  # per image
                gn = torch.tensor(img0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
                annotator = Annotator(img0, line_width=3, example=str(model.names))
                if len(det):
                    # Rescale boxes from img_size to im0 size
                    det[:, :4] = scale_boxes(im.shape[2:], det[:, :4], img0.shape).round()

                    '''
                    # Print results
                    for c in det[:, 5].unique():
                        n = (det[:, 5] == c).sum()  # detections per class
                        s += f"{n} {model.names[int(c)]}{'s' * (n > 1)}, "  # add to string
                    '''

                    cls_object = []
                    img_object = []
                    hero_conf = 0
                    hero_index = 0
                    # Write results
                    for idx, (*xyxy, conf, cls) in enumerate(reversed(det)):
                        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4))).view(-1).tolist()  # normalized xywh


                        #view_img
                        cls = int(cls)
                        hide_labels = False
                        hide_conf = False
                        names = model.names
                        label = None if hide_labels else (names[cls] if hide_conf else f'{names[cls]} {conf:.2f}')
                        annotator.box_label(xyxy, label, color=colors(cls, True))

                        img_object.append(xywh)
                        cls_object.append(obj_names[cls])

                        if names[cls] == "hero" and conf > hero_conf:
                            hero_conf = conf
                            hero_index = idx

                    # 游戏
                    thx = 20  # 进门
                    thy = 20  # 进门的值

                    # 扫描英雄
                    if "hero" in cls_object:
                        # hero_xywh = img_object[cls_object.index("hero")]
                        hero_xywh = img_object[hero_index]
                        cv2.circle(img0, (int(hero_xywh[0]), int(hero_xywh[1])), 1, (0, 0, 255), 10)
                    else:
                        move1(direct="RIGHT")

                    #打怪
                    if "moster" in cls_object:
                        #随机释放技能
                        keyPress(f)
                        keyUp()
                        keyPress(x)
                        keyUp()

                    #打boss
                    if "boss" in cls_object:
                        #随机释放技能
                        keyPress(f)
                        keyUp()
                        keyPress(x)
                        keyUp()

                    #什么都没有，就往右边走
                    if "door" not in cls_object and "moster" not in cls_object and "boss" not in cls_object \
                            and "money" not in cls_object:
                        move1(direct="RIGHT")

                    door_box = []

                    #移动到下一个图
                    if "door" in cls_object and "moster" not in cls_object and "boss" not in cls_object \
                            and "money" not in cls_object:
                        for idx, (c, box) in enumerate(zip(cls_object, img_object)):
                            if c == 'door':
                                door_box = box
                                door_index = idx
                        if door_box[0] < img0.shape[0] // 2:
                            #action_cache = move(direct="RIGHT", action_cache=action_cache)
                            move1(direct="RIGHT")
                            # break
                        elif door_box[1] - hero_xywh[1] < 0 and door_box[0] - hero_xywh[0] > 0:
                            if abs(door_box[1] - hero_xywh[1]) < thy and abs(door_box[0] - hero_xywh[0]) < thx:
                                action_cache = None
                                print("进入下一地图")
                                # break
                            elif abs(door_box[1] - hero_xywh[1]) < thy:
                                #action_cache = move(direct="RIGHT", action_cache=action_cache)
                                move1(direct="RIGHT")
                                # break
                            elif hero_xywh[1] - door_box[1] < door_box[0] - hero_xywh[0]:
                                #action_cache = move(direct="RIGHT_UP", action_cache=action_cache)
                                move1(direct="RIGHT_UP")
                                # break
                            elif hero_xywh[1] - door_box[1] >= door_box[0] - hero_xywh[0]:
                                #action_cache = move(direct="UP", action_cache=action_cache)
                                move1(direct="UP")
                                # break
                        elif door_box[1] - hero_xywh[1] < 0 and door_box[0] - hero_xywh[0] < 0:
                            if abs(door_box[1] - hero_xywh[1]) < thy and abs(door_box[0] - hero_xywh[0]) < thx:
                                action_cache = None
                                print("进入下一地图")
                                # break
                            elif abs(door_box[1] - hero_xywh[1]) < thy:
                                #action_cache = move(direct="LEFT", action_cache=action_cache)
                                move1(direct="LEFT")
                                # break
                            elif hero_xywh[1] - door_box[1] < hero_xywh[0] - door_box[0]:
                                #action_cache = move(direct="LEFT_UP", action_cache=action_cache)
                                move1(direct="LEFT_UP")
                                # break
                            elif hero_xywh[1] - door_box[1] >= hero_xywh[0] - door_box[0]:
                                #action_cache = move(direct="UP", action_cache=action_cache)
                                move1(direct="UP")
                                # break
                        elif door_box[1] - hero_xywh[1] > 0 and door_box[0] - hero_xywh[0] < 0:
                            if abs(door_box[1] - hero_xywh[1]) < thy and abs(door_box[0] - hero_xywh[0]) < thx:
                                action_cache = None
                                print("进入下一地图")
                                # break
                            elif abs(door_box[1] - hero_xywh[1]) < thy:
                                #action_cache = move(direct="LEFT", action_cache=action_cache)
                                move1(direct="LEFT")
                                # break
                            elif door_box[1] - hero_xywh[1] < hero_xywh[0] - door_box[0]:
                                #action_cache = move(direct="LEFT_DOWN", action_cache=action_cache)
                                move1(direct="LEFT_DOWN")
                                # break
                            elif door_box[1] - hero_xywh[1] >= hero_xywh[0] - door_box[0]:
                                #action_cache = move(direct="DOWN", action_cache=action_cache)
                                move1(direct="DOWN")
                                # break
                        elif door_box[1] - hero_xywh[1] > 0 and door_box[0] - hero_xywh[0] > 0:
                            if abs(door_box[1] - hero_xywh[1]) < thy and abs(door_box[0] - hero_xywh[0]) < thx:
                                action_cache = None
                                print("进入下一地图")
                                # break
                            elif abs(door_box[1] - hero_xywh[1]) < thy:
                                #action_cache = move(direct="RIGHT", action_cache=action_cache)
                                move1(direct="RIGHT")
                                # break
                            elif door_box[1] - hero_xywh[1] < door_box[0] - hero_xywh[0]:
                                #action_cache = move(direct="RIGHT_DOWN", action_cache=action_cache)
                                move1(direct="RIGHT_DOWN")
                                # break
                            elif door_box[1] - hero_xywh[1] >= door_box[0] - hero_xywh[0]:
                                #action_cache = move(direct="DOWN", action_cache=action_cache)
                                move1(direct="DOWN")
                                # break

                #im0 = annotator.result()

                '''
                if len(aims):
                    for i, det in enumerate(aims):
                        _, x_center,y_center,width,height = det
                        x_center, width = 800 * float(x_center), 800 * float(width)
                        y_center, height = 640 * float(y_center), 640 * float(height)
                        top_left = (int(x_center - width / 2.), int(y_center - height / 2.))
                        bottom_right = (int(x_center + width / 2.), int(y_center + height / 2.))
                        color = (0, 255, 0)  # RGB
                        #画一个矩形框
                        cv2.rectangle(img0, top_left, bottom_right, color, thickness=1)
                '''

            t_end = time.time()
            #print("一帧游戏操作所用时间：", (t_end - t_start)/fs)
            cv2.namedWindow("dxf-detect",cv2.WINDOW_NORMAL)
            #cv2.resizeWindow('dxf-detect',1920//3, 1080//3)  #按比例缩放
            cv2.imshow('dxf-detect',img0)

            '''
            #窗口置顶
            hwnd = win32gui.FindWindow(None,'dxf-detect')
            CVRECT = cv2.getWindowImageRect('dxf-detect')
            win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,0,0,0,0,win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
            '''

            if cv2.waitKey(2) & 0xFF == ord('p'):
                keyUp()
                paused = "true"
                cv2.destroyAllWindows()
                break


