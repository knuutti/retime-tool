# Knuutti's Retime Tool
# Version: 1.1.1

# File: retime.py
# Author: Knuutti
# Date: August 14th 2022

import tkinter as tk
import pyperclip
import math

# Function for parsing the time frame from the debug info
def getFrame(frame):
    try:
        frame = frame.split("cmt\": \"")[1]
        timeFrame = float(frame.split("\"")[0])
    
    except Exception:
        timeFrame = ""

    return timeFrame

# Function for calculating and forming the total time
def calculateTotal(startTime, endTime, modifier, fps):

    try:
        totalTime = float(endTime) - float(startTime)
    except Exception:
        return ""

    if modifier != "":
        division = modifier.split("/")
        if len(division) < 2:
            numerator = division[0]
            denominator = 1
        else:
            numerator = division[0]
            denominator = division[1]

        try:
            totalTime = totalTime + (float(numerator) / float(denominator))
        except Exception:
            totalTime = totalTime

    if totalTime < 0:
        digit = "- "
        totalTime = -1 * totalTime
    else:
        digit = ""

    # Separating time into hours, minutes, seconds and milliseconds
    totalHours = math.floor(totalTime / 3600)
    totalMinutes = math.floor((totalTime - (3600 * totalHours)) / 60)
    totalSecondsMs = round(totalTime - (3600 * totalHours) - (60 * totalMinutes), 3) # string with seconds and milliseconds, separated on the next two lines
    totalSeconds = int(f"{totalSecondsMs}".split(".")[0])
    totalMilliseconds = 1000 * float("0." + f"{totalSecondsMs}".split(".")[1])

    slygoldsTime = formatSlygolds(totalHours, totalMinutes, totalSeconds, totalMilliseconds)

    # Adjusting milliseconds for video FPS
    try:
        videoFps = int(fps)
        videoFpsDecimal = float(1 / videoFps)

        totalMilliseconds = totalMilliseconds / 1000

        totalMilliseconds = 1000 * round(videoFpsDecimal * (round(totalMilliseconds / videoFpsDecimal)), 3)

        # Checks if fps-adjusted ms rounds up to a whole second
        if (totalMilliseconds == 1000):
            totalMilliseconds = 0
            totalSeconds = totalSeconds + 1
            if (totalSeconds == 60):
                totalSeconds = 0
                totalMinutes = totalMinutes + 1
                if (totalMinutes == 60):
                    totalMinutes = 0
                    totalHours = totalHours + 1

        total = [
            formatTimes(digit, totalHours, totalMinutes, totalSeconds, totalMilliseconds), 
            slygoldsTime]

    except Exception:
        total = [
            formatTimes(digit, totalHours, totalMinutes, totalSeconds, totalMilliseconds), 
            slygoldsTime]

    return total

# Function for creating a string for displaying the total time
def formatTimes(d, h, m, s, ms):
    if s < 10:
        formattedTime = "{0}m 0{1}s".format(m, s)
    else:
        formattedTime = "{0}m {1}s".format(m, s)

    if h > 0:
        formattedTime = "{0}h ".format(h) + formattedTime

    if ms >= 100:
        formattedTime = formattedTime + " {0}ms".format(round(ms))
    elif ms >= 10:
        formattedTime = formattedTime + " 0{0}ms".format(round(ms))
    elif ms > 0:
        formattedTime = formattedTime + " 00{0}ms".format(round(ms))

    formattedTime = d + formattedTime

    return formattedTime

# Function for making Slygolds format for total time
def formatSlygolds(h, m, s, ms):

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

    slygoldsTime = slygoldsH + slygoldsM + slygoldsS + slygoldsMS

    return slygoldsTime

# Button command for updating the start frame
def pasteStartFrame():
    startFrame = getFrame(pyperclip.paste())
    if startFrame != "":
        entStartFrame.delete(0, tk.END)
        entStartFrame.insert(0, startFrame)
        checkData()

# Button command for updating the end frame
def pasteEndFrame():
    endFrame = getFrame(pyperclip.paste())
    if endFrame != "":
        entEndFrame.delete(0, tk.END)
        entEndFrame.insert(0, endFrame)
        checkData()

def copyTime():
    pyperclip.copy(lblTotalTime.cget("text"))

def copySlygolds():
    pyperclip.copy(lblSlygoldsTime.cget("text"))

# Method for checking if start and end frames are okay for calculating
def checkData(*args):
    if (entStartFrame.get() != "" and entEndFrame.get() != ""):
        total = calculateTotal(entStartFrame.get(), entEndFrame.get(), entModifier.get(), entFps.get())
        if total != "":
            lblTotalTime.config(text = total[0])
            lblSlygoldsTime.config(text = total[1])
    else:
        lblTotalTime.config(text = "")
        lblSlygoldsTime.config(text = "")

# Button command for clearing data
def clearData():
    entStartFrame.delete(0, tk.END)
    entEndFrame.delete(0, tk.END)
    entFps.delete(0, tk.END)
    entModifier.delete(0, tk.END)
    checkData()

# Configuring the window
window = tk.Tk()
window.title('Knuutti\'s Retime Tool')
window.resizable(0, 0)
window.attributes('-topmost', True) # Always on top
window.configure(background = '#121a22')
window.iconbitmap(r"favicon.ico")

# Defining variables
varStartFrame = tk.DoubleVar()
varEndFrame = tk.DoubleVar()
varFPS = tk.DoubleVar()
varModifier = tk.DoubleVar()

# Defining the widgets
entStartFrame = tk.Entry(window, font = "Calibri 15", width = 20, background = 'white', textvariable = varStartFrame)
entEndFrame = tk.Entry(window, font = "Calibri 15", width = 20, background = 'white', textvariable = varEndFrame)

btnStartFrame = tk.Button(window, text = "Paste debug info", font = "Calibri 12 bold", command = pasteStartFrame, background = '#085097', foreground = 'white', width = 15)
btnEndFrame = tk.Button(window, text = "Paste debug info", font = "Calibri 12 bold", command = pasteEndFrame, background = '#085097', foreground = 'white', width = 15)
btnClear = tk.Button(window,  text = "Clear", font = "Calibri 12 bold", command = clearData, background = '#085097', foreground = 'white', width = 20)
btnCopyTime = tk.Button(window, text = "Copy", font = "Calibri 12 bold", command = copyTime, background = '#085097', foreground = 'white', width = 6)
btnCopySlygolds = tk.Button(window, text = "Copy", font = "Calibri 12 bold", command = copySlygolds, background = '#085097', foreground = 'white', width = 6)

lblTotalTimeTitle = tk.Label(window, text = "Total", font = "Calibri 12 bold", width = 12, background = '#1e2b3a', foreground = 'white', relief=tk.SUNKEN)
lblSlygoldsTimeTitle = tk.Label(window, text = "SlyGolds", font = "Calibri 12 bold", width = 12, background = '#955707', foreground = 'white', relief=tk.SUNKEN)
lblModifierTitle = tk.Label(window, text = "Modifier", font = "Calibri 12 bold", width = 12, background = '#1e2b3a', foreground = 'white', relief=tk.SUNKEN)
lblStartTitle = tk.Label(window, text = "Start frame", font = "Calibri 12 bold", width = 12, background = '#1e2b3a', foreground = 'white', relief=tk.SUNKEN)
lblEndTitle = tk.Label(window, text = "End frame", font = "Calibri 12 bold", width = 12, background = '#1e2b3a', foreground = 'white', relief=tk.SUNKEN)
lblFpsTitle = tk.Label(window, text = "FPS", font = "Calibri 12 bold", width = 12, background = '#1e2b3a', foreground = 'white', relief=tk.SUNKEN)

lblTotalTime = tk.Label(window, font = "Calibri 15", width = 27, background = 'white')
lblSlygoldsTime = tk.Label(window, font = "Calibri 15", width = 27, background = 'white')

entModifier = tk.Entry(window, font = "Calibri 15", width = 20, background = 'white', textvariable = varModifier)
entFps = tk.Entry(window, font = "Calibri 15", width = 20, background = 'white', textvariable = varFPS)

frmBorder1 = tk.Frame(window, height = 10, background = '#121a22')
frmBorder2 = tk.Frame(window, height = 30, background = '#121a22')
frmBorder3 = tk.Frame(window, height = 10, background = '#121a22')
frmBorder4 = tk.Frame(window, height = 10, background = '#121a22')

clearData()

# Configuring the grid
frmBorder1.grid(row = 0, column = 0, columnspan = 4, sticky = 'ew')

lblStartTitle.grid(row = 1, column = 0, ipady = 3, padx = 7, pady = 3)
entStartFrame.grid(row = 1, column = 1)
btnStartFrame.grid(row = 1, column = 2, padx = 7)

lblEndTitle.grid(row = 2, column = 0, ipady = 3, padx = 7, pady = 3)
entEndFrame.grid(row = 2, column = 1)
btnEndFrame.grid(row = 2, column = 2, padx = 7)

lblFpsTitle.grid(row = 3, column = 0, ipady = 3, padx = 7, pady = 3)
entFps.grid(row = 3, column = 1)

lblModifierTitle.grid(row = 4, column = 0, ipady = 3, padx = 7, pady = 3)
entModifier.grid(row = 4, column = 1)

btnClear.grid(row = 5, column = 1, sticky = 'ew', pady = 10)

frmBorder2.grid(row = 6, column = 0, columnspan = 4, sticky = 'ew')

lblTotalTimeTitle.grid(row = 7, column = 0, ipady = 3)
lblTotalTime.grid(row = 7, column = 1, columnspan = 2, sticky = 'w', pady = 5)
btnCopyTime.grid(row = 7, column = 2, padx = 7, sticky = 'se', pady = 3, ipady = 1)

lblSlygoldsTimeTitle.grid(row = 8, column = 0, ipady = 3)
lblSlygoldsTime.grid(row = 8, column = 1, columnspan = 2, sticky = 'w', pady = 5)
btnCopySlygolds.grid(row = 8, column = 2, padx = 7, sticky = 'se', pady = 3, ipady = 1)

frmBorder3.grid(row = 10, column = 0, columnspan = 3, sticky = 'ew')

# Entry updates
varStartFrame.trace("w", checkData)
varEndFrame.trace("w", checkData)
varFPS.trace("w", checkData)
varModifier.trace("w", checkData)

# Mainloop
window.mainloop()



# eof 