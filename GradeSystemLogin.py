from tkinter import *
from tkinter.messagebox import *
from GradeSystemModify import *

class GradeSystemLogin(object):#登入
    def __init__(self, master=None):#設定視窗
        self.root = master #定義內部變數root
        self.root.geometry('%dx%d' % (1000, 800))
        self.username = StringVar()
        self.password = StringVar()
        self.usernameC = StringVar()
        self.passwordcheckC = StringVar()
        self.passwordC = StringVar()
        self.createLoginPage()
  
    def createLoginPage(self):#創建登入頁面
        self.page = Frame(self.root) #建立Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)#row橫的,column直的
        Label(self.page, text = '使用者名稱: ').grid(row=1, stick=W, pady=10)#grid是一種排版方式,用row跟column來排
        Entry(self.page, textvariable=self.username).grid(row=1, column=1)#stick=字貼的方向,ex:W=貼左邊
        Label(self.page, text = '密碼: ').grid(row=2, stick=W, pady=10)#pad=間距,padx=x間距,pady=y間距
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1)
        Button(self.page, text='登入', command=self.loginCheck).grid(row=3, stick=W, pady=10)
        Button(self.page, text='修改密碼', command=self.passwordChange).grid(row=3, column=1, stick=W, pady=10)
        Button(self.page, text='離開', command=self.page.quit).grid(row=3, column=2, stick=W)
  
    def loginCheck(self):#判斷是否可以登入,有就跳到Function
        name = self.username.get()
        password = self.password.get()
        if self.isLegalUser(name,password)==3:#管理員
            self.page.destroy()  
            GradeSystemFunction(self.root)#接到Function
        if self.isLegalUser(name,password)==2:#教授
            self.page.destroy() 
            GradeSystemFunctionProfessor(self.root)
        if self.isLegalUser(name,password)==1:#學生
            self.page.destroy()  
            GradeSystemFunctionStudent(self.root)
        if self.isLegalUser(name,password)==0:  
            showinfo(title='錯誤', message='帳號或密碼有誤,請重新輸入！')
    def isLegalUser(self,name,password):#判斷帳號密碼是否存在,是不是已經註冊成合格使用者了
        UserFile = open('./帳號密碼.csv','r',encoding='utf-8')#重要!csv檔裡面至少要先有一行東西,否則底下都會失敗
        for line in UserFile.readlines():
            info = line[:-1].split(",")#去除換行符號並以","分隔資料
            if len(info)<3:
                break
            if info[0].strip()==name and  info[1].strip()==password and info[2].strip()=="3":#strip(字元)=去除首尾的"字元",strip()=去除首尾空格
                UserFile.close()
                return 3#管理員權限
            if info[0].strip()==name and  info[1].strip()==password and info[2].strip()=="2":
                UserFile.close()
                return 2#教授權限
            if info[0].strip()==name and  info[1].strip()==password and info[2].strip()=="1":
                UserFile.close()
                return 1#學生權限
        return 0
    def passwordChange(self):
        newWindow = Toplevel(self.page)
        newWindow.attributes("-toolwindow", 1)
        newWindow.wm_attributes("-topmost", 1)#子視窗置頂
        newWindow.geometry('%dx%d' % (300, 200))
        Label(newWindow, text = '請輸入使用者名稱與新密碼').place(x=0,y=0)
        Label(newWindow, text = '使用者名稱: ').place(x=0,y=30)
        Entry(newWindow, textvariable=self.usernameC).place(x=70,y=35)
        Label(newWindow, text = '舊密碼: ').place(x=0,y=60)
        Entry(newWindow, textvariable=self.passwordcheckC,show="*").place(x=70,y=60)
        Label(newWindow, text = '新密碼: ').place(x=0,y=85)
        Entry(newWindow, textvariable=self.passwordC).place(x=70,y=85)
        Button(newWindow, text='修改', command=self.passwordCheck).place(x=100,y=110)
        Button(newWindow, text='關閉', command=newWindow.destroy).place(x=170,y=110)
    def passwordCheck(self):
        temp=0
        nameC = self.usernameC.get()  
        passwordcheckC = self.passwordcheckC.get()
        passwordC = self.passwordC.get()
        if len(nameC)==0 or len(passwordC)==0 or len(passwordcheckC)==0:
            showinfo(title='錯誤', message='名稱或密碼不能為空')
            return
        for i in passwordC:
            if i ==',' or i =='':
                showinfo(title='錯誤', message='密碼不可包含非法字符')
                return
        with open("./帳號密碼.csv","r",encoding="utf-8") as f:#注意!excel檔名前的"."代表相對位置,可以讀同個資料夾內的檔案,絕對位置=完整路徑且限制只能讀那個路徑的資料
            lines = f.readlines()
        with open("./帳號密碼.csv","w",encoding="utf-8") as fRewrite:#w模式覆蓋
            for line in lines:
                info = line[:-1].split(",")
                if info[0].strip() ==nameC and info[1].strip() ==passwordcheckC and info[2].strip()=="3":
                    temp=1
                    AuthorityC=3
                    NameC=info[3]
                    yearInC=info[4]
                    numC=info[5]
                    fRewrite.write('{},{},{},{},{},{}\n'.format(nameC,passwordC,AuthorityC,NameC,yearInC,numC))
                    continue#當查到資料相同時,將資料重新寫入修改後的並continue,相同時則寫入原本資訊
                if info[0].strip() ==nameC and info[1].strip() ==passwordcheckC and info[2].strip()=="2":
                    temp=1
                    AuthorityC=2
                    NameC=info[3]
                    yearInC=info[4]
                    numC=info[5]
                    fRewrite.write('{},{},{},{},{},{}\n'.format(nameC,passwordC,AuthorityC,NameC,yearInC,numC))
                    continue
                if info[0].strip() ==nameC and info[1].strip() ==passwordcheckC and info[2].strip()=="1":
                    temp=1
                    AuthorityC=1
                    NameC=info[3]
                    yearInC=info[4]
                    numC=info[5]
                    fRewrite.write('{},{},{},{},{},{}\n'.format(nameC,passwordC,AuthorityC,NameC,yearInC,numC))
                    continue
                fRewrite.write(line)
        if temp==1:
            showinfo(title='提示', message ="密碼已成功修改")
        if temp==0:
            showinfo(title='錯誤', message ="無此使用者")
    
class GradeSystemFunction(object):#管理員功能
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry('%dx%d' % (1000, 800))
        self.createPage()  
    def createPage(self):#主頁面 
        self.InputPage = InputFrame(self.root) #切換不同的頁面
        self.SearchPage = SearchFrame(self.root)
        self.OutputPage = OutputFrame(self.root)
        self.AddCoursePage = AddModifyCourseFrame(self.root)
        self.DeleteCoursePage = DeleteCourseFrame(self.root)
        self.ListCoursePage = ListCourseFrame(self.root)
        self.ListCourseStudentPage = ListCourseStudentFrame(self.root)
        self.AddCourseStudentPage = AddDeleteCourseStudentFrame(self.root)
        self.AddAccountPage = AddModifyAccountFrame(self.root)
        self.DeleteAccountPage=DeleteAccountFrame(self.root)
        self.InputPage.pack() #預設先出現的是"增加成績"的介面
        self.menu = Menu(self.root)#創建菜單
        self.menu.add_command(label='新增/修改成績', font=10,command = self.InputData)#增加命令(選項) 
        self.menu.add_command(label='查詢成績',font=10, command = self.SearchData)
        self.menu.add_command(label='產生成績單',font=10, command = self.OutputData)
        self.menu.add_command(label='新增/修改課程',font=10,command = self.AddCourse)
        self.menu.add_command(label='刪除課程',font=10,command = self.DeleteCourse)
        self.menu.add_command(label='列出課程清單',font=10,command = self.ListCourse)
        self.menu.add_command(label='新增/刪除課程學生',font=10,command = self.AddCourseStudent)
        self.menu.add_command(label='列出課程學生',font=10,command = self.ListCourseStudent)
        self.menu.add_command(label='新增/修改帳號',font=10,command = self.AddAccount)
        self.menu.add_command(label='刪除帳號',font=10,command = self.DeleteAccount) 
        self.menu.add_command(label='切換使用者',font=10, command = self.ChangeUser)
        self.root['menu'] = self.menu#菜單欄位 
    def InputData(self):
        self.InputPage.pack()#讓元件出現
        self.SearchPage.pack_forget()#讓元件消失
        self.OutputPage.pack_forget()
        self.AddCoursePage.pack_forget()
        self.DeleteCoursePage.pack_forget()
        self.ListCoursePage.pack_forget()
        self.ListCourseStudentPage.pack_forget()
        self.AddCourseStudentPage.pack_forget()
        self.AddAccountPage.pack_forget()
        self.DeleteAccountPage.pack_forget()     
    def SearchData(self):
        self.InputPage.pack_forget()  
        self.SearchPage.pack()
        self.OutputPage.pack_forget()
        self.AddCoursePage.pack_forget()
        self.DeleteCoursePage.pack_forget()
        self.ListCoursePage.pack_forget()
        self.ListCourseStudentPage.pack_forget()
        self.AddCourseStudentPage.pack_forget()
        self.AddAccountPage.pack_forget()
        self.DeleteAccountPage.pack_forget()
    def OutputData(self):
        self.InputPage.pack_forget()  
        self.SearchPage.pack_forget()
        self.OutputPage.pack()   
        self.AddCoursePage.pack_forget()
        self.DeleteCoursePage.pack_forget()
        self.ListCoursePage.pack_forget()
        self.ListCourseStudentPage.pack_forget()
        self.AddCourseStudentPage.pack_forget()
        self.AddAccountPage.pack_forget()
        self.DeleteAccountPage.pack_forget()
    def AddCourse(self):
        self.InputPage.pack_forget()  
        self.SearchPage.pack_forget()
        self.OutputPage.pack_forget()
        self.AddCoursePage.pack()
        self.DeleteCoursePage.pack_forget()
        self.ListCoursePage.pack_forget()
        self.ListCourseStudentPage.pack_forget()
        self.AddCourseStudentPage.pack_forget()
        self.AddAccountPage.pack_forget()
        self.DeleteAccountPage.pack_forget()
    def DeleteCourse(self):
        self.InputPage.pack_forget()  
        self.SearchPage.pack_forget()
        self.OutputPage.pack_forget()
        self.AddCoursePage.pack_forget()
        self.DeleteCoursePage.pack()
        self.ListCoursePage.pack_forget()
        self.ListCourseStudentPage.pack_forget()
        self.AddCourseStudentPage.pack_forget()
        self.AddAccountPage.pack_forget()
        self.DeleteAccountPage.pack_forget()
    def ListCourse(self):
        self.InputPage.pack_forget()  
        self.SearchPage.pack_forget()
        self.OutputPage.pack_forget()
        self.AddCoursePage.pack_forget()
        self.DeleteCoursePage.pack_forget()
        self.ListCoursePage.pack()
        self.ListCourseStudentPage.pack_forget()
        self.AddCourseStudentPage.pack_forget()
        self.AddAccountPage.pack_forget()
        self.DeleteAccountPage.pack_forget()
    def ListCourseStudent(self):
        self.InputPage.pack_forget()  
        self.SearchPage.pack_forget() 
        self.OutputPage.pack_forget()
        self.AddCoursePage.pack_forget()
        self.DeleteCoursePage.pack_forget()
        self.ListCoursePage.pack_forget()
        self.ListCourseStudentPage.pack()
        self.AddCourseStudentPage.pack_forget()
        self.AddAccountPage.pack_forget()
        self.DeleteAccountPage.pack_forget()
    def AddCourseStudent(self):
        self.InputPage.pack_forget()  
        self.SearchPage.pack_forget() 
        self.OutputPage.pack_forget()
        self.AddCoursePage.pack_forget()
        self.DeleteCoursePage.pack_forget()
        self.ListCoursePage.pack_forget()
        self.ListCourseStudentPage.pack_forget()
        self.AddCourseStudentPage.pack()
        self.AddAccountPage.pack_forget()
        self.DeleteAccountPage.pack_forget()
    def AddAccount(self):
        self.InputPage.pack_forget()  
        self.SearchPage.pack_forget()
        self.OutputPage.pack_forget()
        self.AddCoursePage.pack_forget()
        self.DeleteCoursePage.pack_forget()
        self.ListCoursePage.pack_forget()
        self.ListCourseStudentPage.pack_forget()
        self.AddCourseStudentPage.pack_forget()
        self.AddAccountPage.pack()
        self.DeleteAccountPage.pack_forget()
    def DeleteAccount(self):
        self.InputPage.pack_forget()  
        self.SearchPage.pack_forget() 
        self.OutputPage.pack_forget()
        self.AddCoursePage.pack_forget()
        self.DeleteCoursePage.pack_forget()
        self.ListCoursePage.pack_forget()
        self.ListCourseStudentPage.pack_forget()
        self.AddCourseStudentPage.pack_forget()
        self.AddAccountPage.pack_forget()
        self.DeleteAccountPage.pack()
    def ChangeUser(self):
        self.menu.destroy()
        self.InputPage.destroy()  
        self.SearchPage.destroy()
        self.OutputPage.destroy() 
        self.AddCoursePage.destroy()
        self.DeleteCoursePage.destroy()
        self.ListCoursePage.destroy()
        self.ListCourseStudentPage.destroy()
        self.AddCourseStudentPage.destroy()
        self.AddAccountPage.destroy()
        self.DeleteAccountPage.destroy()
        GradeSystemLogin(self.root)
        
class GradeSystemFunctionProfessor(object):#教授功能
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry('%dx%d' % (1000, 800))
        self.createPage()  
    def createPage(self):#主頁面 
        self.InputPage = InputFrame(self.root) #切換不同的頁面
        self.ProfessorOutputPage = ProfessorOutputFrame(self.root)
        self.ListCoursePage = ListCourseFrame(self.root)
        self.ListCourseStudentPage = ListCourseStudentFrame(self.root)
        self.InputPage.pack() #預設先出現的是"增加成績"的介面
        self.menu = Menu(self.root)#創建菜單
        self.menu.add_command(label='新增/修改成績', font=10,command = self.InputData)#增加命令(選項)   
        self.menu.add_command(label='列出課程成績',font=10, command = self.ProfessorOutputData)
        self.menu.add_command(label='列出課程清單',font=10,command = self.ListCourse)
        self.menu.add_command(label='列出課程學生',font=10,command = self.ListCourseStudent)
        self.menu.add_command(label='切換使用者',font=10, command = self.ChangeUser)  
        self.root['menu'] = self.menu#菜單欄位 
    def InputData(self):
        self.InputPage.pack()#讓元件出現
        self.ProfessorOutputPage.pack_forget()#讓元件消失
        self.ListCoursePage.pack_forget()
        self.ListCourseStudentPage.pack_forget()     
    def ProfessorOutputData(self):
        self.InputPage.pack_forget()  
        self.ProfessorOutputPage.pack()
        self.ListCoursePage.pack_forget()
        self.ListCourseStudentPage.pack_forget()
    def ListCourse(self):
        self.InputPage.pack_forget()  
        self.ProfessorOutputPage.pack_forget()
        self.ListCoursePage.pack()
        self.ListCourseStudentPage.pack_forget()
    def ListCourseStudent(self):
        self.InputPage.pack_forget()  
        self.ProfessorOutputPage.pack_forget()  
        self.ListCoursePage.pack_forget()
        self.ListCourseStudentPage.pack()
    def ChangeUser(self):
        self.menu.destroy()
        self.InputPage.destroy()  
        self.ProfessorOutputPage.destroy()
        self.ListCoursePage.destroy()
        self.ListCourseStudentPage.destroy()
        GradeSystemLogin(self.root)
        
class GradeSystemFunctionStudent(object):#學生功能
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry('%dx%d' % (1000, 800))
        self.createPage()  
    def createPage(self):#主頁面 
        self.SearchPage = SearchFrame(self.root)
        self.OutputPage = OutputFrame(self.root)
        self.ListCoursePage = ListCourseFrame(self.root)
        self.ListCourseStudentPage = ListCourseStudentFrame(self.root)
        self.SearchPage.pack() #出現"查詢成績"的介面
        self.menu = Menu(self.root)#創建菜單 
        self.menu.add_command(label='查詢成績',font=10, command = self.SearchData)
        self.menu.add_command(label='產生成績單',font=10, command = self.OutputData)
        self.menu.add_command(label='列出課程清單',font=10,command = self.ListCourse)
        self.menu.add_command(label='列出課程學生',font=10,command = self.ListCourseStudent)
        self.menu.add_command(label='切換使用者',font=10, command = self.ChangeUser)  
        self.root['menu'] = self.menu#菜單欄位       
    def SearchData(self):
        self.SearchPage.pack()
        self.OutputPage.pack_forget()
        self.ListCoursePage.pack_forget()
        self.ListCourseStudentPage.pack_forget()
    def OutputData(self):
        self.SearchPage.pack_forget()
        self.OutputPage.pack()   
        self.ListCoursePage.pack_forget()
        self.ListCourseStudentPage.pack_forget()
    def ListCourse(self): 
        self.SearchPage.pack_forget()
        self.OutputPage.pack_forget()
        self.ListCoursePage.pack()
        self.ListCourseStudentPage.pack_forget()
    def ListCourseStudent(self):
        self.SearchPage.pack_forget()
        self.OutputPage.pack_forget()
        self.ListCoursePage.pack_forget()
        self.ListCourseStudentPage.pack()
    def ChangeUser(self):
        self.menu.destroy()
        self.SearchPage.destroy()
        self.OutputPage.destroy()
        self.ListCoursePage.destroy()
        self.ListCourseStudentPage.destroy()
        GradeSystemLogin(self.root)