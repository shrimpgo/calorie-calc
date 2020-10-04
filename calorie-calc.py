#!/usr/bin/python3

from sys import exit
from signal import signal, SIGINT

def basalRate(h, w, age):
    gender = input("\nWhat's your gender (M/F)? ").lower()
    if gender == "m":
        kcal = 66 + (13.7 * float(w)) + (5 * int(h)) - (6.8 * int(age))
        return kcal
    elif gender == "f":
        kcal = 665 + (9.6 * float(w)) + (1.8 * int(h)) - (4.7 * int(age))
        return kcal
    else:
        print("Please, choose Male (m) or Female (f)!")
        return(basalRate(h, w, age))


def workOut(met, hour, w):
    result = int(met) * float(hour) * float(w)
    return result


def handler(signal_received, frame):
    print("\nSIGINT or CTRL-C detected. Exiting gracefully")
    exit(0)


def main():
    signal(SIGINT, handler)

    print("Calorie Calculator based on Haris-Benedict formula!\n")
    age = input("What's your age? => ")
    w = input("\nWhat's your weight (kg)? => ")
    h = input("\nWhat's your heigth (cm)? => ")
    basal = basalRate(h, w, age)
    met = input("\nWhat's your MET? If you don't know about this, do a little \n\
search at Google and try to find out how many METs your work out type is. \n\
Ex.: calisthenics is 8 MET => ")
    hour = input("\nHow many time do you spend when you work out (hour)? ")
    actday = input("\nWhat's your activity at day? Do you work at home or \n\
walking or doing heavy stuffs? Feel free to fill this field. Recommended \n\
minimum 300 and maximum 500 (kcal) => ")

    workout = workOut(met, hour, w)
    total = basal + workout + int(actday)

    print("""
        Basal Rate = {} kcal
        Work out spent = {} kcal
        Total = {} kcal

        It means that your body spend {} kcal per day. If you want to:

        Keep your weight = consume the same value of total
        Gain muscle = increase between 600 kcal and 800 kcal of carb
        Lose Body Fat = decrease between 400 kcal and 600 kcal of carb

        Don't forget to work out hard. To build muscles... "NO PAIN, NO GAIN!"

        Good Luck!
        """.format(basal, workout, total, total))


if __name__ == '__main__':
    main()
