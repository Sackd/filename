
# from tkinter import *

# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()

#     def createWidgets(self):
#         self.hello1Label = Label(self, text='Hello, world!')
#         self.hello1Label.pack()
#         self.alertButton = Button(self, text='关不了', command=self.quit)
#         self.alertButton.pack()


#     #     self.hello1Label = Label(self,text = 'HELLO!')
#     #     self.helloL1abel.pack()
#     #     self.countinueButton = Button(self,text = 'continue',command=self.createWidgets)
#     #     self.countinueButton.pack()
# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()





# from tkinter import *
# import tkinter.messagebox as messagebox
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()

#     def createWidgets(self):#创建小部件
#         self.nameInput = Entry(self)#创建输入框
#         self.nameInput.pack()
#         self.alertButton = Button(self, text='Hello', command=self.hello)#创建一个按钮
#         self.alertButton.pack()

#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message', '哈个屁喽%s' % name)

# app = Application()
# # 设置窗口标题:
# app.master.title('Hello')
# # 主消息循环:
# app.mainloop()
import tkinter
import tkinter as tk
lis = ['明天来台球',
    '来啊',
    '快来',
    '快来',
    '快来',
    '9点',
    '快来',
    '老地方',
    '童乐双语对面',
    '别找借口说来不了，快来',
    '行不行',
    '说话算数啊',
    '明天老地方不见不散啊']
def create(mark):
    screen = tkinter.Tk()
    screen.title('tkinter_from')
    label = tkinter.Label(screen,text=lis[mark],font=('楷体',20))
    label.pack()
    screen.mainloop()

def main():
    for i in range(len(lis)):
        create(i)

if __name__ == '__main__':
    main()

