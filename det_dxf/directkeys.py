
from det_dxf.auto_control import *

def move(direct, action_cache=None):
    print(action_cache)
    if direct == "RIGHT":
        if action_cache is not None:
            if action_cache != "RIGHT":
                keyUp()
                go_right()
                keyUp()
                go_right()
                action_cache = "RIGHT"
                print("向右移动")
            else:
                print("向右移动")
        else:
            go_right()
            keyUp()
            go_right()
            action_cache = "RIGHT"
            print("向右移动")
        return action_cache

    elif direct == "LEFT":
        if action_cache is not None:
            if action_cache != "LEFT":
                keyUp()
                go_left()
                keyUp()
                go_left()
                action_cache = "LEFT"
                print("向左移动")
            else:
                print("向左移动")
        else:
            go_left()
            keyUp()
            go_left()
            action_cache = "LEFT"
            print("向左移动")
        return action_cache

    elif direct == "UP":
        if action_cache is not None:
            if action_cache != "UP":
                keyUp()
                go_top()
                keyUp()
                go_top()
                action_cache = "UP"
                print("向上移动")
            else:
                print("向上移动")
        else:
            go_top()
            keyUp()
            go_top()
            action_cache = "UP"
            print("向上移动")
        return action_cache

    elif direct == "DOWN":
        if action_cache is not None:
            if action_cache != "DOWN":
                keyUp()
                go_down()
                keyUp()
                go_down()
                action_cache = "DOWN"
                print("向下移动")
            else:
                print("向下移动")
        else:
            go_down()
            keyUp()
            go_down()
            action_cache = "DOWN"
            print("向下移动")
        return action_cache

    elif direct == "RIGHT_UP":
        if action_cache != None:
            if action_cache != "RIGHT_UP":
                if action_cache not in ["LEFT", "RIGHT", "UP", "DOWN"]:
                    keyUp()
                go_right()
                keyUp()
                go_right()
                go_top()
                action_cache = "RIGHT_UP"
                print("右上移动")
            else:
                print("右上移动")
        else:
            go_right()
            keyUp()
            go_right()
            go_top()
            action_cache = "RIGHT_UP"
            print("右上移动")
        return action_cache

    elif direct == "RIGHT_DOWN":
        if action_cache != None:
            if action_cache != "RIGHT_DOWN":
                if action_cache not in ["LEFT", "RIGHT", "UP", "DOWN"]:
                    keyUp()

                go_right()
                keyUp()
                go_right()
                go_down()
                action_cache = "RIGHT_DOWN"
                print("右上移动")
            else:
                print("右上移动")
        else:
            go_right()
            keyUp()
            go_right()
            go_down()
            # time.sleep(press_delay)
            action_cache = "RIGHT_DOWN"
            print("右上移动")
        return action_cache

    elif direct == "LEFT_UP":
        if action_cache != None:
            if action_cache != "LEFT_UP":
                if action_cache not in ["LEFT", "RIGHT", "UP", "DOWN"]:
                    keyUp()
                go_left()
                keyUp()
                go_left()
                go_top()
                action_cache = "LEFT_UP"
                print("左上移动")
            else:
                print("左上移动")
        else:
            go_left()
            keyUp()
            go_left()
            go_top()
            # time.sleep(press_delay)
            action_cache = "LEFT_UP"
            print("左上移动")
        return action_cache

    elif direct == "LEFT_DOWN":
        if action_cache != None:
            if action_cache != "LEFT_DOWN":
                if action_cache not in ["LEFT", "RIGHT", "UP", "DOWN"]:
                    keyUp()
                go_left()
                keyUp()
                go_left()
                go_down()
                # time.sleep(press_delay)
                action_cache = "LEFT_DOWN"
                print("左下移动")
            else:
                print("左下移动")
        else:
            go_left()
            keyUp()
            go_left()
            go_down()
            # time.sleep(press_delay)
            action_cache = "LEFT_DOWN"
            print("左下移动")
        return 0

def move1(direct):
    if direct == "RIGHT":
        keyUp()
        go_right()
        keyUp()
        go_right()
        print("向右移动")
    elif direct == "LEFT":
        keyUp()
        go_left()
        keyUp()
        go_left()
        print("向左移动")

    elif direct == "UP":
        keyUp()
        go_top()
        keyUp()
        go_top()
        print("向上移动")

    elif direct == "DOWN":
        keyUp()
        go_down()
        keyUp()
        go_down()
        action_cache = "DOWN"
        print("向下移动")

    elif direct == "RIGHT_UP":
        keyUp()
        go_top()
        keyUp()
        go_top()
        go_right()
        print("右上移动")

    elif direct == "RIGHT_DOWN":
        keyUp()
        go_right()
        keyUp()
        go_right()
        go_down()
        print("右下移动")

    elif direct == "LEFT_UP":
        keyUp()
        go_left()
        keyUp()
        go_left()
        go_top()
        print("左上移动")

    elif direct == "LEFT_DOWN":
        keyUp()
        go_left()
        keyUp()
        go_left()
        go_down()
        print("左下移动")

keyUp()