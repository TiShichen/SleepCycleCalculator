import math
import datetime
import tkinter as tk

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# .gitignore added build and dist folder

def calculateCycle():

    result.delete(0.0, tk.END)

    upHour = hour.get()
    upMinute = minute.get()

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

    # print(str(upHour) + ":" + str(upMinute))

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

    lengthHour = int(math.modf(sleepLength)[1])
    lengthMinute = int(round(math.modf(sleepLength)[0] * 60))

    # print(str(lengthHour) + ":" + str(lengthMinute))

    # List cycles
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
        lateUpHour = int(math.modf(lateUpTime)[1])
        lateUpMinute = int(round(math.modf(lateUpTime)[0] * 60))
        outList.append([maxCycles + 1, lateUpHour, lateUpMinute, 0])

    # print(outList)

    resultList = []

    for j in outList:
        if len(j) == 4:
            # print("Sleep now and get up at " + str(j[1]) + ":" + str(j[2]) + " for a " + str(j[0]) + " cycle sleep.")
            resultList.append(
                "Sleep now and get up at " + str(j[1]) + ":" + str(j[2]) + " for a " + str(j[0]) + " cycle sleep.")
        else:
            # print("Sleep at " + str(j[1]) + ":" + str(j[2]) + " for a " + str(j[0]) + " cycle sleep.")
            resultList.append("Sleep at " + str(j[1]) + ":" + str(j[2]) + " for a " + str(j[0]) + " cycle sleep.")

    # print(resultList)

    for m in resultList:
        result.insert(0.0, m + '\n')


def resetInputBox():
    hour.delete(0, tk.END)
    minute.delete(0, tk.END)
    result.delete(0.0, tk.END)


# Create tkinter GUI
window = tk.Tk()
window.title("Sleep Cycle Calculator")  # Window title
window.geometry('600x400')  # Window size
window["background"] = "#C9C9C9"  # Window background color
instruction = tk.Label(window, text="Input planned get up time below", fg="black",
                       font=('Times', 12, 'italic'))
# Create a Label called instruction, set background color, font color, font, size etc.
instruction.pack(pady=10)  # Put the Label inside the window

hour = tk.Entry(window)
hour.pack(padx=10, pady=10)

minute = tk.Entry(window)
minute.pack(padx=10, pady=10)

result = tk.Text(window, width=60, height=10)
result.pack(pady=10)

calButton = tk.Button(window, text="Calculate", command=calculateCycle)
resetButton = tk.Button(window, text="Reset", command=resetInputBox)

resetButton.pack(side="bottom", pady=10)
calButton.pack(side="bottom", pady=10)


window.mainloop()

if __name__ == '__main__':
    # currentTime = datetime.datetime.now()
    # curHour = currentTime.strftime('%H')
    # curMinute = currentTime.strftime('%M')

    # print(curHour + ":" + curMinute)

    calculateCycle()
