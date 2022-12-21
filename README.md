# Speedrun Retime Tool

This is a tool for timing speedruns, segments or anything that involves frame counts. You can use this tool to get accurate segment times from Youtube videos using the "Copy debug info" feature.

![image](https://user-images.githubusercontent.com/96994953/208797508-b467bd21-c3b0-42b9-8a29-4172fc0b9718.png)

### Opening the program
- Download the zip-file of the [latest version](https://github.com/knuutti/retime-tool/releases/latest)
- Extract the zip-file to the folder of your choosing
- Open the program


### Using the program
You can paste start and end frames by clicking the PASTE button. You can paste either the frame number as an integer (e.g. 23454) or then the DEBUG INFO from YouTube. Debug info will be automatically turned into the correct frame based on the video FPS (by default 60, can be changed by clicking the value in top left corner). After both start and end frames have been pasted, the program will calculate the total time. If you want to time another sample, just click CLEAR ALL to clear the window. If you need to adjust the calculated time (for example the start time should be decreased by -0.324) you can input that to the MODIFIER field. You can type both decimal numbers and fractions (such as 1/60).

SlyGolds field below the total time will show the total time in 60 FPS standards rounded down to two decimals. This field can be used when submitting golds to [SlyGolds](https://slygolds.com/home). You can copy the value in the field by clicking COPY.
