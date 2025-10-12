while True:
    first_number = input("请输入第一个数字：")
    if first_number == 'q':
        break
    second_number = input("请输入第二个数字：")
    if second_number == 'q':
        break
    # answer = int(first_number) / int(second_number)
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("除数不能为零，请重新输入。")
    else:
        print(answer)