import tkinter
import tkinter.filedialog
import tkinter.messagebox
import zipfile
import os




class Jys:
    #触发函数
    def __init__(self):

        #显示部分
        self.root = tkinter.Tk()
        #调用按键
        self.anjian()
        #全局变量
        self.filespath = None
        self.root.mainloop()
     #创建按钮
    def anjian(self):
        self.root.minsize(500, 400)
        self.root.title('压缩软件')
        # 创建标签
        # 创建标签显示框

        self.files = tkinter.StringVar()
        self.files.set('还么有选择文件')
        self.lable = tkinter.Label(self.root, textvariable=self.files, bg='pink', font=('楷体', 15), )
        self.lable.place(x=30, y=30, width=440, height=200)
        # 创建按键
        self.btn1 = tkinter.Button(self.root, text='选择文件', fg='yellow', command=self.choicefiles)
        self.btn1.place(x=130, y=250, width=240, height=50)
        self.btn2 = tkinter.Button(self.root, text='压缩文件', fg='green', command=self.yasuofiles)
        self.btn2.place(x=130, y=300, width=120, height=50)

        self.btn3 = tkinter.Button(self.root, text='解压文件', fg='blue', command=self.jieyafiles)
        self.btn3.place(x=250, y=300, width=120, height=50)
    #触发选择文件函数
    def choicefiles(self):

        self.filespath = tkinter.filedialog.askopenfilenames(title='请选择要进行操作的文件')
        # print(filespath)

        filesstr = '\n'.join(self.filespath)
        self.files.set(filesstr)
    #触发压缩文件函数
    def yasuofiles(self):

        dirname = tkinter.filedialog.asksaveasfilename(title='将文件保存到')
        # print(dirname)
        # 创建打开压缩文件
        zp = zipfile.ZipFile(dirname + '.zip', 'w', zipfile.ZIP_DEFLATED)
        # print(zp)
        # 将要压缩的文件添加到压缩文件当中
        for f in self.filespath:
            zp.write(f, os.path.basename(f))
        # 关闭文件
        zp.close()
        # 压缩完成后将压缩完成提示语放在显示框
        self.files.set('压缩完成')
    #触发压缩文件函数
    def jieyafiles(self):

        dirname = tkinter.filedialog.askdirectory(title='将文件解压到')
        # print(dirname)
        ab = ''.join(self.filespath)
        # print(ab)
        # 创建解压文件
        zp = zipfile.ZipFile(ab, 'r')
        # print(zp)
        # 解压所有文件
        zp.extractall(dirname)

        # 关闭文件
        zp.close()

        self.files.set('解压完成')

jys = Jys()











