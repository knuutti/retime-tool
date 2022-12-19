import math

def get_time_parametres(time: float):

    time = abs(time)
    
    hours = math.floor(time / 3600)
    minutes = math.floor((time - (3600 * hours)) / 60)
    seconds_decimal = round(time - (3600 * hours) - (60 * minutes), 3)
    seconds = int(f"{seconds_decimal}".split(".")[0])
    milliseconds = 1000 * float("0." + f"{seconds_decimal}".split(".")[1])

    return [hours, minutes, seconds, milliseconds]

def format_total_time(time: float):

    times = get_time_parametres(time)

    if time < 0:
        d = '-'
    else:
        d = ''

    h = times[0]
    m = times[1]
    s = times[2]
    ms = times[3]

    if s < 10:
        formatted_time = "{0}m 0{1}s".format(m, s)
    else:
        formatted_time = "{0}m {1}s".format(m, s)

    if h > 0:
        formatted_time = "{0}h ".format(h) + formatted_time

    if ms >= 100:
        formatted_time = formatted_time + " {0}ms".format(round(ms))
    elif ms >= 10:
        formatted_time = formatted_time + " 0{0}ms".format(round(ms))
    elif ms > 0:
        formatted_time = formatted_time + " 00{0}ms".format(round(ms))

    return d + formatted_time



def format_slygolds_time(time: float):

    times = get_time_parametres(time)

    if time < 0:
        d = '-'
    else:
        d = ''

    h = times[0]
    m = times[1]
    s = times[2]
    ms = times[3]

    msFirst = math.floor(ms / 100)

    msSecond = int(math.floor(ms / 10) - (10 * msFirst))

    if (msSecond == 2 or msSecond == 4 or msSecond == 7):
        msSecond = msSecond + 1
    elif (msSecond == 9):
        msFirst = msFirst + 1
        msSecond = 0
        if (msFirst == 10):
            msFirst = 0
            s = s + 1
            if (s == 60):
                s = 0
                m = m + 1
                if (m == 60):
                    m = 0
                    h = h + 1
    
    slygoldsMS = f"{msFirst}{msSecond}"

    if h > 0:
        if h < 10:
            slygoldsH = "0" + f"{h}:"
        else:
            slygoldsH = f"{h}:"
    else:
        slygoldsH = ""

    if m > 0:
        if m < 10:
            slygoldsM = "0" + f"{m}:"
        else:
            slygoldsM = f"{m}:"
    else:
        slygoldsM = "00:"

    if s > 0:
        if s < 10:
            slygoldsS = "0" + f"{s}."
        else:
            slygoldsS = f"{s}."
    else:
        slygoldsS = "00."

    slygolds_time = d + slygoldsH + slygoldsM + slygoldsS + slygoldsMS

    return slygolds_time