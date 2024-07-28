
from models.common import DetectMultiBackend
from utils1.torch_utils import select_device

#device = select_device(device=0)
device = select_device('')

data = r'C:\Users\S12\Desktop\Yolov5Learn\yolov5\data\dxf_data.yaml'
weights = r'C:\Users\S12\Desktop\Yolov5Learn\yolov5\det_dxf\best0327.pt'

def load_model():
    model = DetectMultiBackend(weights, device=device, dnn=False, data=data, fp16=False)
    model.warmup(imgsz=(1, 3, 640, 640))  # warmup
    return model

