# -*- coding: utf-8 -*-


def math_test():
    a_contents = int(input("请输入第一种类型可以乘坐或拥有的个数:"))
    a_price =  int(input("请输入第一个类型的价格:"))
    b_contents = int(input("请输入第二种类型可以乘坐或拥有的个数:"))
    b_price =  int(input("请输入第二个类型的价格:"))

    print("--------------------------------------------------------------------------")
    print("第一步： 我们来选择出哪种类型的最划算(单价最低)")
    a_per_price = a_price/a_contents
    b_per_price = b_price/b_contents
    print("第一种类型的单价是: {}, 第二种类型的单价是：{}".format(a_per_price, b_per_price), end=". ")
    if a_per_price < b_per_price:
        print("所以我们尽可能多地选择第一种类型")
        selected_contents, selected_price = a_contents, a_price
        not_selected_contents, not_selected_price = b_contents, b_price
        select_type = "a"
    else:
        print("所以我们尽可能多地选择第二种类型")
        selected_contents, selected_price = b_contents, b_price
        not_selected_contents, not_selected_price = a_contents, a_price
        select_type = "b"

    total_number = int(input("请输入需要的总个数:"))
    print("--------------------------------------------------------------------------")
    print("第二步： 我们从尽可能多的使用便宜类型来挨个试试......")
    a_num = total_number/selected_contents
    if select_type == "a":
        print("最多需要{}第一种类型，还剩{}个未满足".format(int(a_num), total_number%selected_contents))
    else:
        print("最多需要{}第二种类型，还剩{}个未满足".format(int(a_num), total_number%selected_contents))
    if a_num > int(a_num):
        a_num = int(a_num) + 1

    for i_a in range(a_num, 0, -1):
        diff = total_number - i_a * selected_contents
        print("开始从最大的便宜类型开始， 使用{}个便宜类型, 差额是{}".format(i_a, diff))
        if diff == 0:
            print("使用了{}个便宜类型就可以满足".format(i_a, ))
        if diff % not_selected_contents == 0:
            i_b = int(diff/not_selected_contents)
            print("此时需要便宜类型 {}(个),较贵类型{} (个)".format(i_a, i_b))
            print("总价是：{}*{} + {}*{}={}".format(i_a, selected_price, i_b, not_selected_price, i_a*selected_price + i_b*not_selected_price))
            break


while True:
    math_test()
    input("请输入任何键做下一题。。。")
