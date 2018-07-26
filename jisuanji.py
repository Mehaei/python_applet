import tkinter
import tkinter.messagebox
import math

class Jsq:
    #初始化对象
    def __init__(self):
        # 定义一个空列表
        self.lt = []
        # 标志符
        self.flage = False

        self.root = tkinter.Tk()
        self.newwindow()

        self.eventButton()
        self.root.mainloop()

    # 未实现功能 弹出消息框
    def daikaifa(e):
        tkinter.messagebox.showinfo(title='提示', message='待开发')

    #显示页面
    def newwindow(self):
        self.root.title('测试版V5')
        self.root.minsize(260, 390)
        self.root.resizable(False, False)
        # 背景颜色
        fom = tkinter.Frame(self.root, bg='#99CCFF')
        fom.place(x=0, y=0, width=260, height=390)

        # 定义点击菜单触发的方法
        def hello():
            tkinter.messagebox.showinfo(title='消息框', message='待开发')

        def banben():
            tkinter.messagebox.showinfo(title='消息框', message='测试版  V1\n最终解释权归非凡软件公司所有')

        # 创建总菜单
        menubar = tkinter.Menu(self.root)

        # 创建下来菜单的并加入文件菜单（fmenu）
        fmenu = tkinter.Menu(menubar)

        # 创建下来菜单的并加入文件菜单(fmenu1)
        fmenu1 = tkinter.Menu(menubar)

        # 创建下拉菜单的选项 （查看）
        fmenu.add_command(label='标准型', command=hello)
        fmenu.add_command(label='科学型', command=hello)

        # 创建下拉菜单的选项 （编辑）
        fmenu1.add_command(label='复制 Ctrl + C')
        fmenu1.add_command(label='粘贴 Ctrl + V')

        # 将文件菜单作为下拉菜单添加到总菜单中，并且将命名
        menubar.add_cascade(label='查看', menu=fmenu)
        menubar.add_cascade(label='编辑', menu=fmenu1)
        menubar.add_cascade(label='关于', command=banben)
        menubar.add_cascade(label='退出', command=self.root.quit)
        self.root.config(menu=menubar)

        # 显示部分

        self.btn2 = tkinter.Label(self.root, font=('微软雅黑', '25'), anchor='se', text=' ', bg='#CCFFFF')
        self.btn2.place(x=10, y=20, width=240, height=50)

        self.btn = tkinter.Label(self.root, font=('微软雅黑', '25'), anchor='se', text='0', bg='#CCFFFF')
        self.btn.place(x=10, y=70, width=240, height=50)

        # 第一行按键
        self.btn1 = tkinter.Button(self.root, text='MC', bg='#1E90FF')
        self.btn1.place(x=10, y=150, width=40, height=30)

        self.btn1 = tkinter.Button(self.root, text='MR', bg='#1E90FF')
        self.btn1.place(x=60, y=150, width=40, height=30)

        self.btn1 = tkinter.Button(self.root, text='MS', bg='#1E90FF')
        self.btn1.place(x=110, y=150, width=40, height=30)

        self.btn1 = tkinter.Button(self.root, text='M+', bg='#1E90FF')
        self.btn1.place(x=160, y=150, width=40, height=30)

        self.btn1 = tkinter.Button(self.root, text='M-', bg='#1E90FF')
        self.btn1.place(x=210, y=150, width=40, height=30)

        # 第二行按键
        self.btn1 = tkinter.Button(self.root, text='←', bg='#1E90FF')
        self.btn1.place(x=10, y=190, width=40, height=30)

        self.btn1 = tkinter.Button(self.root, text='CE', bg='#1E90FF')
        self.btn1.place(x=60, y=190, width=40, height=30)

        self.btn1 = tkinter.Button(self.root, text='C', bg='#1E90FF')
        self.btn1.place(x=110, y=190, width=40, height=30)

        self.btn1 = tkinter.Button(self.root, text='±', bg='#1E90FF')
        self.btn1.place(x=160, y=190, width=40, height=30)

        self.btn1 = tkinter.Button(self.root, text='√', bg='#1E90FF')
        self.btn1.place(x=210, y=190, width=40, height=30)

        # 第三行按键
        self.btn1 = tkinter.Button(self.root, text='7', bg='#1E90FF')
        self.btn1.place(x=10, y=230, width=40, height=30)

        self.btn1 = tkinter.Button(self.root, text='8', bg='#1E90FF')
        self.btn1.place(x=60, y=230, width=40, height=30)

        self.btn1 = tkinter.Button(self.root, text='9', bg='#1E90FF')
        self.btn1.place(x=110, y=230, width=40, height=30)

        self.btn1 = tkinter.Button(self.root, text='/', bg='#1E90FF')
        self.btn1.place(x=160, y=230, width=40, height=30)

        self.btn1 = tkinter.Button(self.root, text='%', bg='#1E90FF')
        self.btn1.place(x=210, y=230, width=40, height=30)

        # 第四行按键
        self.btn1 = tkinter.Button(self.root, text='4', bg='#1E90FF')
        self.btn1.place(x=10, y=270, width=40, height=30)

        self.btn1 = tkinter.Button(self.root, text='5', bg='#1E90FF')
        self.btn1.place(x=60, y=270, width=40, height=30)

        self.btn1 = tkinter.Button(self.root, text='6', bg='#1E90FF')
        self.btn1.place(x=110, y=270, width=40, height=30)

        self.btn1 = tkinter.Button(self.root, text='*', bg='#1E90FF')
        self.btn1.place(x=160, y=270, width=40, height=30)

        self.btn1 = tkinter.Button(self.root, text='1/x', bg='#1E90FF')
        self.btn1.place(x=210, y=270, width=40, height=30)

        # 第五行按键
        self.btn1 = tkinter.Button(self.root, text='1', bg='#1E90FF')
        self.btn1.place(x=10, y=310, width=40, height=30)

        self.btn1 = tkinter.Button(self.root, text='2', bg='#1E90FF')
        self.btn1.place(x=60, y=310, width=40, height=30)

        self.btn1 = tkinter.Button(self.root, text='3', bg='#1E90FF')
        self.btn1.place(x=110, y=310, width=40, height=30)

        self.btn1 = tkinter.Button(self.root, text='-', bg='#1E90FF')
        self.btn1.place(x=160, y=310, width=40, height=30)

        # 第六行按键
        self.btn1 = tkinter.Button(self.root, text='0', bg='#1E90FF')
        self.btn1.place(x=10, y=350, width=90, height=30)

        self.btn1 = tkinter.Button(self.root, text='.', bg='#1E90FF')
        self.btn1.place(x=110, y=350, width=40, height=30)

        self.btn1 = tkinter.Button(self.root, text='+', bg='#1E90FF')
        self.btn1.place(x=160, y=350, width=40, height=30)

        self.btn1 = tkinter.Button(self.root, text='=', bg='#1E90FF')
        self.btn1.place(x=210, y=310, width=40, height=70)

    #绑定按钮
    def eventButton(self):
        # button绑定按键
        self.btn.bind_class('Button', '<Button-1>', self.demo)

        # 定义函数

    #触发事件
    def demo(self,e):

        # 判断当前按下的是数字还是运算符还是功能键
        # 数字
        if e.widget['text'] in '1234567890.':
            self.shuzi(e)
            # 运算符
        elif e.widget['text'] in '+-*/=':
            self.yuansuanfu(e)
        # 功能键
        elif e.widget['text'] in ['C', 'CE', '←']:
            self.gongnengjian(e)

        elif e.widget['text'] == '±':
            self.zhengfu(e)

        #如果按下开方符号
        elif e.widget['text'] == '√':
            self.kaifang(e)

        # 按下未开发按键 调用函数daikaifa
        elif e.widget['text'] in ['MC', 'MR', 'MS', 'M+', 'M-']:
            self.daikaifa()

    #按下数字键
    def shuzi(self,e):


        if self.flage == True:
            self.btn['text'] = '0'
            self.flage = False

        t = self.btn['text']
        # 解决点的问题

        if '.' in t and e.widget['text'] == '.':
            return
        # 判断t是否为0
        elif t == '0' and e.widget['text'] != '.':
            #print('-----------------------')
            # 若t为0则将按下的内容重新赋值并在显示框显示
            self.btn['text'] = e.widget['text']
        else:
            # 若t不为0，则获取当前显示框的内容与新按下的内容进行拼接
            self.btn['text'] = t + e.widget['text']


    #按下运算符
    def yuansuanfu(self,e):

        if self.flage == True :
            return

        # 将获取的label值 添加到列表当中
        self.lt.append(self.btn['text'])
        # 将当前按下的运算符也添加到列表当中
        self.lt.append(e.widget['text'])
        self.flage = True
        # 将列表中的内容在第二块显示框中显示
        self.btn2['text'] = str(''.join(self.lt[:-1]))


        # 当除数为0时  返回提示
        if self.lt[-2] == '0' and self.lt[-1] == '=' and self.lt[-3] == '/':
            self.btn['text'] = '除数不能为0'
            # 清空上面的显示框
            self.btn2['text'] = ''
            return
        if e.widget['text'] == '=':
            if self.flage == False:
                eq = ''.join(self.lt[:-1])
                # print(eq)
                self.btn['text'] = str(eval(eq))

            elif self.flage == True:
                eq = ''.join(self.lt[:-1])
                self.btn['text'] = str(eval(eq)) + str(eval(eq))

            #self.lt.clear()




        if len(self.lt) >= 3:
            eq = ''.join(self.lt[:-1])
            # print(eq)
            self.btn['text'] = str(eval(eq))
            # 清空列表
            self.lt.clear()
            # 将结果放入清空后的列表
            b = self.btn['text'][:8]
            self.lt.append(b)
            # 将运算符存入到列表当中
            self.lt.append(e.widget['text'])

            if e.widget['text'] == '=':
                b = self.btn['text']
                self.btn['text'] = b[:12]

#按下取反符号
    def zhengfu(self,e):
        if e.widget['text'] == '±':

            result =eval( ''.join(['-',self.btn['text']]))
            self.btn['text'] = str(result)

    #按下功能键
    def gongnengjian(self,e):
        # 按下C键
        if e.widget['text'] == 'C':
            # 屏幕显示为0
            self.btn['text'] = '0'
            # 列表中的内容显示到上面的显示框
            self.btn2['text'] = ' '
            # 清空列表
            self.lt.clear()
        # 按下退格键
        elif e.widget['text'] == '←':
            b = self.btn['text']
            # 当按下退格键上面的显示框为空
            self.btn2['text'] = ''
            # 获取显示框里除了最后一位的内容
            self.btn['text'] = b[:-1]
            if len(str(self.btn['text'])) == 0:
                self.btn['text'] = '0'
        # 按下CE键
        elif e.widget['text'] == 'CE':

            b = self.btn['text']
            self.btn['text'] = '0'

    #开方符号
    def kaifang(self,e):
        if e.widget['text'] == '√':
            result = self.btn['text']

            self.btn['text'] = math.sqrt(int(result))
            self.btn2['text'] = ' '

jsq = Jsq()

