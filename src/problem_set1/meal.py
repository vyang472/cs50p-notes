"""def main():
    num = convert(input("what time is it? ").split(":"))
    if 7 <= num <= 8:
        print("breakfast time")
    elif 12 <= num <= 13:
        print("lunch time")
    elif 18<= num <= 19:
        print("dinner time")

def convert(time):
    num2 = time[1]
    num2 = int(num2)
    num2 = num2 / 60
    num1 = int(time[0])
    return num1 + num2


    



if __name__ == "__main__":
    main()上面的是我自己写的，下面的是 GPT 改的，它说题目要求我要把函数 convert 当成 str去处理，
    但是我在主函数提前分割了时间，当成了list 去处理，所以可能有问题。
    其实跑起来结果一样，但是 anyway ，我两种都写上了"""

def main():
    time = input("What time is it? ")
    num = convert(time)

    if 7 <= num <= 8:
        print("breakfast time")
    elif 12 <= num <= 13:
        print("lunch time")
    elif 18 <= num <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60


if __name__ == "__main__":
    main()