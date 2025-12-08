name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

'''
在 match name: 里，
name 只是一个普通变量名，
表示“要被匹配的那个值”。
match name: 这句的意思是：下面所有的 case 都拿来和 name 比较，
所以在 case 里面不用再写 name == ...。
比如 case "Harry" | "Hermione" | "Ron": 表示：如果 name 等于这三个名字里的任何一个，
就执行这一块代码；
case _: 里的下划线 _ 是“兜底情况”（相当于 if/elif/else 里的 else).
'''