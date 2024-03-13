# -*- coding: utf-8 -*-
# @Time    : 2024/3/13 21:01
# @Author  : wenyichao
# @File    : add.py
# @Software: PyCharm 
# @Comment :

import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result = float(entry_num1.get()) + float(entry_num2.get())
        label_result.config(text="结果：" + str(result))
    except ValueError:
        messagebox.showerror("错误", "请输入有效的数字")

def subtract():
    try:
        result = float(entry_num1.get()) - float(entry_num2.get())
        label_result.config(text="结果：" + str(result))
    except ValueError:
        messagebox.showerror("错误", "请输入有效的数字")

# 创建主窗口
root = tk.Tk()
root.title("加法和减法计算器")

# 创建输入框和标签
label_num1 = tk.Label(root, text="数字1:")
label_num1.grid(row=0, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(root, text="数字2:")
label_num2.grid(row=1, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

# 创建按钮
button_add = tk.Button(root, text="加法", command=add)
button_add.grid(row=2, column=0)

button_subtract = tk.Button(root, text="减法", command=subtract)
button_subtract.grid(row=2, column=1)

# 显示结果
label_result = tk.Label(root, text="")
label_result.grid(row=3, columnspan=2)

# 运行主循环
root.mainloop()
