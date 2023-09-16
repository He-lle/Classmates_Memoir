import tkinter as tk
import os
import sqlite3

# 设置窗口的宽度和高度
width = 500
height = 500

# 创建根窗口
root = tk.Tk()

# 设置根窗口的大小和标题
root.geometry('500x500')
root.title('同学录')

# 设置根窗口的背景颜色
root["background"] = '#00FFFF'

# 获取屏幕的宽度和高度
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()

# 计算根窗口的位置并设置
size_geo = '%dx%d+%d+%d' % ((width, height, (screenwidth-width)/2, (screenheight-height)/2))
root.geometry(size_geo)

# 创建标签控件并设置文本、背景颜色、前景颜色和字体
text = tk.Label(root, text="同学录软件", bg="#00BFFF", fg="#FFFF00", font=('楷体', 40, ''))
text_1 = tk.Label(root, text="魏逸恺出品，必属精品", bg="#00BFFF", fg="#F08080", font=('楷体', 15, ''))

# 将标签控件添加到根窗口中
text.pack()
text_1.pack()

# 创建数据库连接
conn = sqlite3.connect('data/records.db')
c = conn.cursor()

# 创建数据表
c.execute('''CREATE TABLE IF NOT EXISTS students
             (name TEXT, year INTEGER)''')
conn.commit()

# 记录创建了多少个名字输入窗口
root1_created = False

# 定义输入名字的函数
def Input_Name():
    global root1_created
    # 如果名字输入窗口还没有创建，则创建一个
    if not root1_created:

        # 定义保存名字的函数
        def save_name():
            name = input_box.get()

            # 检查名字是否包含空格或数字，如果是则显示错误信息
            if ' ' in name or any(char.isdigit() for char in name):
                error_label.config(text="名字输入错误")
            else:
                # 检查同名记录是否已存在，如果存在则显示错误信息
                c.execute("SELECT * FROM students WHERE name=?", (name,))
                if c.fetchone() is not None:
                    error_label.config(text="已有该同学!")
                else:
                    # 向数据库中插入记录
                    c.execute("INSERT INTO students VALUES (?, NULL)", (name,))
                    conn.commit()
                    try:
                        year()
                    except AttributeError:
                        pass
                    root1.destroy()

        # 创建一个顶级窗口作为名字输入窗口
        root1 = tk.Toplevel(root)
        root1.geometry('300x300')
        root1.title("输入同学姓名")

        # 创建输入框控件和确认按钮控件，并添加到名字输入窗口中
        input_box = tk.Entry(root1)
        input_box.pack()
        confirm_button = tk.Button(root1, text="确认", command=save_name)
        confirm_button.pack()

        # 创建错误信息标签控件，并添加到名字输入窗口中
        error_label = tk.Label(root1, text="", fg="red")
        error_label.pack()

        # 设置名字输入窗口已创建标志为True
        root1_created = True

# 定义输入生日的函数
def year():
    # 定义保存生日的函数
    def save_year():
        year = year_input.get()

        # 检查输入的生日是否为空或非数字，如果是则显示错误信息
        if not year or not year.isdigit() or int(year) <= 1900 or int(year) >= 2300:
            error_label.config(text="生日输入错误")
        else:
            # 获取最后一个记录的名字，并在该记录中更新生日
            c.execute("UPDATE students SET year=? WHERE rowid = (SELECT max(rowid) FROM students)", (year,))
            conn.commit()
            root2.destroy()

    # 创建一个顶级窗口作为生日输入窗口
    root2 = tk.Toplevel(root)
    root2.geometry('300x300')
    root2.title("输入同学生日")

    # 创建输入框控件和确认按钮控件，并添加到生日输入窗口中
    year_input = tk.Entry(root2)
    year_input.pack()
    confirm_button = tk.Button(root2, text="确认", command=save_year)
    confirm_button.pack()

    # 创建错误信息标签控件，并添加到生日输入窗口中
    error_label = tk.Label(root2, text="", fg="red")
    error_label.pack()

# 创建按钮和按钮框架，并添加到根窗口中
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM)
button = tk.Button(button_frame, text="新的同学录", command=Input_Name)
button.pack()

# 运行主循环
root.mainloop()

# 关闭数据库连接
conn.close()
