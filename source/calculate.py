import math

def getFrame(cmt: float, fps_string: str) -> int:
    try:
        fps = int(fps_string)
    except TypeError:
        fps = 60
    
    frame = math.ceil(cmt*fps)

    return frame

# Function for calculating and forming the total time
def calculateTotalTime(start: float, end: str, modifier: str, fps: str):
    try:
        frames = int(end) - int(start)
        totalTime = frames / int(fps)
    except TypeError:
        return None

    # Adding the modifier to the total time
    if modifier != "":
        # If modifier is a fraction, separate numerator and denominator
        division = modifier.split("/")
        if len(division) < 2: # n
            numerator = division[0]
            denominator = 1
        else:
            numerator = division[0]
            denominator = division[1]

        try:
            totalTime = totalTime + (float(numerator) / float(denominator))
        except Exception:
            totalTime = totalTime