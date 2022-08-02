import math
import datetime
import tkinter as tk

def calculateCycle():

    result.delete(0.0, tk.END)

    upHour = hour.get()
    upMinute = minute.get()

    if len(upHour) == 0 or len(upMinute) == 0:
        result.insert(0.0, 'Please input the time you plan to get up')
        return

    if not upHour.isdigit() or not upMinute.isdigit():
        result.insert(0.0, 'Please input time in digits')
        return

    upHour = int(upHour)
    upMinute = int(upMinute)

    if upHour > 24:
        result.insert(0.0, 'Hour cannot be greater than 24')
        hour.delete(0, tk.END)
        return

    if upMinute >= 60:
        result.insert(0.0, 'Minute cannot be greater than 59')
        minute.delete(0, tk.END)
        return

    if upHour == 24 and upMinute > 0:
        result.insert(0.0, 'Time cannot be greater than 24:00')
        hour.delete(0, tk.END)
        minute.delete(0, tk.END)
        return

    doubleUpTime = float(upHour + (upMinute / 60))

    currentTime = datetime.datetime.now()
    curHour = int(currentTime.strftime('%H'))
    curMinute = int(currentTime.strftime('%M'))

    ###################################################
    # curHour = 22
    # curMinute = 45
    ###################################################

    doubleCurTime = curHour + (curMinute / 60)

    # 24's complement calculation
    # sleepLength = (doubleUpTime - 24) + (doubleCurTime - 24) + 24

    # Sleep length calculation
    if doubleUpTime > doubleCurTime:
        sleepLength = doubleUpTime - doubleCurTime
    else:
        sleepLength = doubleUpTime + (24 - doubleCurTime)

    # lengthHour = int(math.modf(sleepLength)[1])
    # lengthMinute = int(round(math.modf(sleepLength)[0] * 60))
    #
    # # print(str(lengthHour) + ":" + str(lengthMinute))

    # List cycles result
    outList = []
    maxCycles = int(sleepLength / 1.5)

    if maxCycles == 0:
        result.insert(0.0, 'Not enough time for a full cycle!')
        return

    for i in range(1, maxCycles + 1, 1):
        doubleBedTime = doubleUpTime - 1.5 * i

        if (doubleBedTime >= 0):
            doubleBedTime = doubleBedTime
        else:
            doubleBedTime = 24 + doubleBedTime

        bedHour = int(math.modf(doubleBedTime)[1])
        bedMinute = int(math.modf(doubleBedTime)[0] * 60)

        outList.append([i, bedHour, bedMinute])

    if (sleepLength - 1.5 * maxCycles) >= 1.35:
        lateUpTime = doubleCurTime + 1.5 * (maxCycles + 1) - 24
        if lateUpTime < 0:
            lateUpTime = lateUpTime + 24
        lateUpHour = int(math.modf(lateUpTime)[1])
        lateUpMinute = int(math.modf(lateUpTime)[0] * 60)
        outList.append([maxCycles + 1, lateUpHour, lateUpMinute, 0])

    # print(outList)

    resultList = []

    for j in outList:
        if len(j) == 4:
            resultList.append(
                "Sleep now and get up at " + str(j[1]) + ":" + str('%02d' % j[2]) + " for a " + str(j[0]) + " cycle "
                                                                                                            "sleep.")
        else:
            resultList.append("Sleep at " + str(j[1]) + ":" + str('%02d' % j[2]) + " for a " + str(j[0]) + " cycle "
                                                                                                           "sleep.")

    # Print out result in text box
    for m in resultList:
        result.insert(0.0, m + '\n')


def resetInputBox():
    hour.delete(0, tk.END)
    minute.delete(0, tk.END)
    result.delete(0.0, tk.END)


if __name__ == '__main__':
    count = 1
    # Create tkinter GUI
    window = tk.Tk()
    window.title("Sleep Cycle Calculator")  # Window title
    # window.geometry('600x400')  # Window size
    window["background"] = "#C9C9C9"  # Window background color
    instruction = tk.Label(window, text="Input planned get up time below", fg="black",
                           font=('Times', 12, 'italic'))
    # Create a Label called instruction, set background color, font color, font, size etc.

    # Create labels indicating what to input
    tagHour = tk.Label(window, text="Hour:", justify="right")
    tagMinute = tk.Label(window, text="Minute:", justify="right")

    # Create entry boxes for time inputs
    hour = tk.Entry(window)
    minute = tk.Entry(window)

    # Create text box for printing results and error messages
    result = tk.Text(window, height=10)

    # Creating calculate and reset button
    calButton = tk.Button(window, text="Calculate", command=calculateCycle, width=20)
    resetButton = tk.Button(window, text="Reset", command=resetInputBox, width=20)

    # Place all created elements using the grid feature
    instruction.grid(row=0, column=1, columnspan=4, pady=20)

    tagHour.grid(row=1, column=1, padx=20, )
    tagMinute.grid(row=1, column=3, padx=20)

    hour.grid(row=1, column=2)
    minute.grid(row=1, column=4)

    result.grid(row=2, column=1, columnspan=4, padx=20, pady=10)

    calButton.grid(row=3, column=2, pady=10)
    resetButton.grid(row=3, column=3, pady=10)

    # Show the GUI
    window.mainloop()
