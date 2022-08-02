# Slygolds' Retime Tool

# File: retime.py
# Version: 1.0
# Author: Knuutti
# Date: August 2nd 2022

import tkinter as tk
import pyperclip
import math
import webbrowser

def getFrame(frame):
    try:
        frame = frame.split("cmt\": \"")[1]
        timeFrame = float(frame.split("\"")[0])
    
    except Exception:
        timeFrame = ""

    return timeFrame

def calculateTotal(startTime, endTime):

    totalTime = endTime - startTime

    # Separating time into hours, minutes, seconds and milliseconds
    totalHours = int(math.floor(totalTime / 3600))
    totalMinutes = int(math.floor((totalTime - (3600 * totalHours)) / 60))
    totalSeconds = int(math.floor(totalTime - (3600 * totalHours) - (60 * totalMinutes)))
    totalMilliseconds = math.floor(1000 * (totalTime - (3600 * totalHours) - (60 * totalMinutes) - totalSeconds))

    # Formating the time string
    if totalSeconds < 10:
        total = "{0}m 0{1}s".format(totalMinutes, totalSeconds)
    else:
        total = "{0}m {1}s".format(totalMinutes, totalSeconds)

    if totalHours > 0:
        total = "{0}h ".format(totalHours) + total
    
    totalNoMs = total

    if totalMilliseconds >= 100:
        total = total + " {0}ms".format(totalMilliseconds)
    elif totalMilliseconds >= 10:
        total = total + " 0{0}ms".format(totalMilliseconds)
    else:
        total = total + " 00{0}ms".format(totalMilliseconds)

    totalNoAdjustment = total

    # Adjustments for 60 fps format
    firstDigit = math.floor(totalMilliseconds / 100)
    secondDigit = (math.floor(totalMilliseconds / 10)) - 10 * firstDigit
    if (secondDigit == 2 or secondDigit == 4 or secondDigit == 7):
        secondDigit = secondDigit + 1
    elif (secondDigit == 9):
        secondDigit = 0

    total60fps = totalNoMs + f" {firstDigit}{secondDigit}ms"


    # Adjustments for 30 fps format
    if (secondDigit == 1):
        secondDigit = 3
    elif (secondDigit == 5):
        secondDigit = 6
    elif (secondDigit == 8):
        secondDigit = 0

    total30fps = totalNoMs + f" {firstDigit}{secondDigit}ms"

    times = [totalNoAdjustment, total60fps, total30fps]

    return times

def pasteStartFrame():
    startFrame = getFrame(pyperclip.paste())
    if startFrame != "":
        lblStartFrame.configure(text = startFrame)
        checkData()

def pasteEndFrame():
    endFrame = getFrame(pyperclip.paste())
    if endFrame != "":
        lblEndFrame.configure(text = endFrame)
        checkData()

def checkData():
    if (lblStartFrame.cget("text") != "" and lblEndFrame.cget("text") != ""):
        total = calculateTotal(lblStartFrame.cget("text"), lblEndFrame.cget("text"))
        lblTotalTime.config(text = total[0])
        lblTotalTime60fps.config(text = total[1])
        lblTotalTime30fps.config(text = total[2])

def openSlygolds():
    webbrowser.open("https://slygolds.com")

# Configuring the window
window = tk.Tk()
window.title('SlyGolds\' Retime Tool')
window.resizable(0, 0)
window.attributes('-topmost', True) # Always on top
window.configure(background = '#121a22')
window.iconbitmap(r"C:\Users\eknut\AppData\Local\Programs\Python\Python310\Scripts\Retime Tool\favicon.ico")

# Defining the widgets
lblStartFrame = tk.Label(window, font = "Calibri 15", width = 15, background = 'white')
lblEndFrame = tk.Label(window, font = "Calibri 15", width = 15, background = 'white')
btnStartFrame = tk.Button(window, text = "Paste start frame", font = "Calibri 12 bold", command = pasteStartFrame, background = '#085097', foreground = 'white', width = 15)
btnEndFrame = tk.Button(window, text = "Paste end frame", font = "Calibri 12 bold", command = pasteEndFrame, background = '#085097', foreground = 'white', width = 15)
lblTotalTimeTitle60fps = tk.Label(window, text = "60 fps:", font = "Calibri 12 bold", anchor = 'e', width = 15, background = '#121a22', foreground = 'white')
lblTotalTime60fps = tk.Label(window, font = "Calibri 15", width = 15, background = 'white')
lblTotalTimeTitle30fps = tk.Label(window, text = "30 fps:", font = "Calibri 12 bold", anchor = 'e', width = 15, background = '#121a22', foreground = 'white')
lblTotalTime30fps = tk.Label(window, font = "Calibri 15", width = 15, background = 'white')
lblTotalTimeTitle = tk.Label(window, text = "Total:", font = "Calibri 12 bold", anchor = 'e', width = 15, background = '#121a22', foreground = 'white')
lblTotalTime = tk.Label(window, font = "Calibri 15", width = 15, background = 'white')
frmBorder1 = tk.Frame(window, height = 10, background = '#121a22')
frmBorder2 = tk.Frame(window, height = 30, background = '#121a22')
frmBorder3 = tk.Frame(window, height = 20, background = '#121a22')
btnWebsite = tk.Button(window, text = "Visit website", font = "Calibri 10 bold", command = openSlygolds, background = '#243447', foreground = 'white')

# Configuring the grid
frmBorder1.grid(row = 0, column = 0, columnspan = 4, sticky = 'ew')
lblStartFrame.grid(row = 1, column = 1, columnspan = 2)
lblEndFrame.grid(row = 2, column = 1, columnspan = 2)
btnStartFrame.grid(row = 1, column = 0, pady = 5, padx=20)
btnEndFrame.grid(row = 2, column = 0, pady = 5)
frmBorder2.grid(row = 3, column = 0, columnspan = 4, sticky = 'ew')
lblTotalTimeTitle.grid(row = 4, column = 0, padx = 10)
lblTotalTime.grid(row = 4, column = 1, columnspan = 2, padx = 10, pady = 5)
lblTotalTimeTitle60fps.grid(row = 5, column = 0, padx = 10)
lblTotalTime60fps.grid(row = 5, column = 1, columnspan = 2, padx = 20, pady = 5)
lblTotalTimeTitle30fps.grid(row = 6, column = 0, padx = 10)
lblTotalTime30fps.grid(row = 6, column = 1, columnspan = 2, padx = 10, pady = 5)
frmBorder3.grid(row = 7, column = 0, columnspan = 3, sticky = 'ew')
btnWebsite.grid(row = 8, column = 0, columnspan = 3, sticky = 'ew')

# Mainloop
window.mainloop()