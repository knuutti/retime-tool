import math

def get_frame(cmt: float, fps_string: str) -> int:
    try:
        fps = int(fps_string)
    except TypeError:
        fps = 60
    
    frame = math.ceil(cmt*fps)

    return frame