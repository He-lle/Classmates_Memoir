import tkinter as tk       # 导入tkinter模块，用于创建GUI界面
import os                  # 导入os模块，用于操作文件和目录

# 设置窗口的宽度和高度
width = 500
height = 500

# 创建主窗口对象
root = tk.Tk()
root.geometry('500x500')   # 设置窗口大小为500x500像素
root.title('同学录')        # 设置窗口标题为"同学录"
root["background"] = '#00FFFF'   # 设置窗口背景颜色为"#00FFFF"（青色）

# 窗口居中
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
size_geo = '%dx%d+%d+%d' % ((width, height, (screenwidth-width)/2, (screenheight-height)/2))
root.geometry(size_geo)

# 添加文本标签
text = tk.Label(root, text="同学录软件", bg="#00BFFF", fg="#FFFF00", font=('楷体', 40, ''))    # 创建一个文本标签，显示"同学录软件"，背景颜色为"#00BFFF"（深蓝色），字体颜色为"#FFFF00"（黄色），字体为"楷体"，字号为40
text_1 = tk.Label(root, text="魏逸恺出品，必属精品", bg="#00BFFF", fg="#F08080", font=('楷体', 15, ''))   # 创建一个文本标签，显示"魏逸恺出品，必属精品"，背景颜色为"#00BFFF"（深蓝色），字体颜色为"#F08080"（淡红色），字体为"楷体"，字号为15
text.pack()   # 将文本标签显示在窗口中
text_1.pack()   # 将文本标签显示在窗口中

# 创建输入框窗口
root1_created = False   # 标识窗口是否已经创建

def Input_Name():
    global root1_created   # 在函数内部使用全局变量
    if not root1_created:   # 如果窗口还没有创建
        def save_name():
            name = input_box.get()   # 获取输入框中的文本
            if ' ' in name or any(char.isdigit() for char in name):   # 如果名字中有空格或包含数字
                error_label.config(text="名字输入错误")   # 在错误标签中显示错误信息
            else:
                if os.path.exists('data/' + name) == True:   # 如果已经存在该同学的目录
                    error_label.config(text="已有该同学!")   # 在错误标签中显示错误信息
                else:
                    os.makedirs('data/' + name)   # 创建该同学的目录
                    with open('data/' + name + '/name.txt', 'w') as file:   # 在该同学的目录下创建一个名为"name.txt"的文件
                        file.write(name)   # 将名字写入文件
                    year()   # 调用year函数
                    root1.destroy()   # 关闭窗口
        root1 = tk.Toplevel(root)   # 创建一个新的顶层窗口
        root1.geometry('300x300')   # 设置窗口大小为300x300像素
        root1.title("输入同学姓名")   # 设置窗口标题为"输入同学姓名"

        input_box = tk.Entry(root1)   # 创建一个输入框控件
        input_box.pack()   # 将输入框显示在窗口中
        input_box.insert(tk.END, "同学的名字")   # 在输入框中显示默认文本

        confirm_button = tk.Button(root1, text="确认", command=save_name)   # 创建一个按钮控件，点击按钮执行save_name函数
        confirm_button.pack()   # 将按钮显示在窗口中

        error_label = tk.Label(root1, text="", fg="red")   # 创建一个标签控件，用于显示错误信息，字体颜色为红色
        error_label.pack()   # 将标签显示在窗口中

        root1_created = True   # 标识窗口已经创建


def year():
    root2 = tk.Toplevel(root)   # 创建一个新的顶层窗口
    root2.geometry('300x300')   # 设置窗口大小为300x300像素
    root2.title("输入同学生日")   # 设置窗口标题为"输入同学生日"
    yaer = tk.Spinbox(root2,from_=0,to=20, increment=2,width = 15,bg='#9BCD9B')
    year.pack()
# 创建下一步按钮
button_frame = tk.Frame(root)   # 创建一个框架控件，用于存放按钮
button_frame.pack(side=tk.BOTTOM)   # 将框架显示在窗口底部
button = tk.Button(button_frame, text="新的同学录", command=Input_Name)   # 创建一个按钮控件，点击按钮执行Input_Name函数
button.pack()   # 将按钮显示在框架中

root.mainloop()   # 进入主循环，开始运行程序