import cards_tools

while True:

    cards_tools.cards_menu()
    selection = input("请输入您要执行的选项： ")

    if selection in ["1", "2", "3"]:
        print("-" * 50)
        # 新增名片，查看名片，查找名片
        if selection == "1":
            cards_tools.action_1()

        elif selection == "2":
            cards_tools.action_2()

        else:
            cards_tools.action_3()

    elif selection == "0":
        print("-" * 50)
        print("感谢您使用名片管理系统，欢迎下次继续使用")
        break

    else:
        print("-" * 50)
        print("您输入的内容不正确，请重新输入")
