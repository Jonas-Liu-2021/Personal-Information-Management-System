def cards_menu():
    """名片系统界面菜单

    """
    print("*" * 50)
    print("欢迎来到名片管理系统")
    print()
    print("1 新增名片")
    print("2 展示名片")
    print("3 查找名片")
    print()
    print("0 退出名片管理系统")
    print("*" * 50)


name_list = []


def action_1():

    print("请输入用户信息")
    name_str = input("请输入用户姓名： ")
    phone_str = input("请输入电话号码： ")
    qq_str = input("请输入qq号码： ")
    print("用户信息输入完成")

    name_list.append({"name": name_str,
                     "phone": phone_str,
                     "qq": qq_str})


def action_2():

    print("姓名\t\t电话\t\tQQ")
    print("=" * 70)

    if len(name_list) == 0:

        print("您还没有输入用户信息")

    else:

        for name_dict in name_list:

            print("%s\t\t%s\t\t%s" % (name_dict["name"], name_dict["phone"], name_dict["qq"]))


def action_3():

    name_find = input("请输入您要查找的姓名： ")

    for name_dict in name_list:

        if name_dict["name"] == name_find:

            print("姓名\t\t电话\t\tQQ")
            print("=" * 70)
            print("%s\t\t%s\t\t%s" % (name_dict["name"], name_dict["phone"], name_dict["qq"]))
            print("=" * 70)

            selection_find = input("请选择您接下来要执行的操作(1.修改名片 2.删除名片 0.返回主界面)： ")

            if selection_find == "1":

                name_dict["name"] = infor_edit(name_dict["name"], input("请输入您修改后的姓名（若不修改该项直接点击回车）： "))
                name_dict["phone"] = infor_edit(name_dict["phone"], input("请输入您修改后的电话（若不修改该项直接点击回车）： "))
                name_dict["qq"] = infor_edit(name_dict["qq"], input("请输入您修改后的QQ（若不修改该项直接点击回车）： "))
                print("修改完成！")
                break

            elif selection_find == "2":
                name_list.remove(name_dict)
                print("您已成功删除%s的个人信息" % name_find)
                break

            elif selection_find == "0":
                return

    else:
        print("抱歉，您查找的姓名不在系统中")


def infor_edit(dict_value, input_value):
    """个人信息修改

    :param dict_value: 字典中的信息
    :param input_value: 输入的信息
    :return: 若输入信息，返回输入值，否则返回原来的值
    """
    if len(input_value) == 0:
        return dict_value

    else:
        return input_value




