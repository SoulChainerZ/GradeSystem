from tkinter import *
from tkinter.messagebox import *  
import tkinter
from tkinter import ttk

class InputFrame(Frame): #輸入頁面,繼承Frame類別(似乎在Login程式碼中)
    def __init__(self, master=None):  
        Frame.__init__(self, master)
        self.root = master #定義內部變數root
        self.E1 = Entry(self,font=10)
        self.E2 = Entry(self,font=10)
        self.E3 = Entry(self,font=10)
        self.E4 = Entry(self,font=10)
        self.E5 = Entry(self,font=10)
        self.E6 = Entry(self,font=10)
        self.E7 = Entry(self,font=10)
        self.E8 = Entry(self,font=10,show="*")
        self.createPage()
    def createPage(self):#創造輸入介面
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, font=10,text = '學年: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1,stick=E)
        Label(self,  font=10,text = '學期: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=E)
        Label(self,  font=10,text = '課程代碼: ').grid(row=3, stick=W, pady=10) 
        self.E3.grid(row=3, column=1, stick=E) 
        Label(self,  font=10,text = '學號: ').grid(row=4, stick=W, pady=10)
        self.E4.grid(row=4, column=1, stick=E)
        Label(self,  font=10,text = '姓名: ').grid(row=5, stick=W, pady=10)
        self.E5.grid(row=5, column=1, stick=E)
        Label(self,  font=10,text = '成績: ').grid(row=6, stick=W, pady=10)
        self.E6.grid(row=6, column=1, stick=E)
        Label(self,  font=10,text = '使用者名稱: ').grid(row=7, stick=W, pady=10)
        self.E7.grid(row=7, column=1, stick=E)
        Label(self,  font=10,text = '密碼: ').grid(row=8, stick=W, pady=10)
        self.E8.grid(row=8, column=1, stick=E)
        Button(self,  font=10,text='修改',command=self.modify).grid(row=9, column=2, stick=E, pady=10)
    def modify(self):
        year = self.E1.get()
        semester = self.E2.get()
        num = self.E3.get()
        identify = self.E4.get()
        Name = self.E5.get()
        score = self.E6.get()
        username= self.E7.get()
        password= self.E8.get()
        if self.spacejudge(year) or self.spacejudge(semester) or self.spacejudge(num) or self.spacejudge(identify) or self.spacejudge(Name) or self.spacejudge(score) or self.spacejudge(username) or self.spacejudge(password):
            showinfo(title='提示', message ="任一輸入不可為空")
        elif self.isLegal(score)==False:
            showinfo(title='提示', message ="成績只可包含數字")
        elif score[0]=="0":
            showinfo(title='提示', message ="成績不可以0開頭")
        elif int(score)>100 or int(score)<0:
            showinfo(title='提示', message ="成績不可小於0或大於100")
        else:
            self.modifyInfo(year,semester,num,identify,Name,score,username,password)
    def isLegal(self,string):#判斷上面某些只能是數字
        alp = ['1','2','3','4','5','6','7','8','9','0']
        for i in string:
            if i in alp:
                pass
            else:
                return False
        return True
    def spacejudge(self,studentData):#空格判斷
        spaceJudge = 0
        for i in studentData:
            if not i.isspace():#isspace()判斷是否為空
                spaceJudge = 1
                break
        if spaceJudge==1:
            return 0
        else:
            return 1
    def modifyInfo(self,year,semester,num,identify,Name,score,username,password):
        temp2=0
        f = open('./課程資訊.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==year and info[1] ==semester and info[2] ==num:
                temp2=1
                proname=info[5]
                pronum=info[7]
                f.close()
        if temp2==0:
            showinfo(title='提示', message ="沒有此課程訊息")
            f.close()
            return
        else:
            f.close
        temp3=0
        f = open('./帳號密碼.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==username and info[1] ==password and info[2] =='2' and info[3]==proname and info[5]==pronum:
                temp3=1
                f.close()
            if info[0] ==username and info[1] ==password and info[2] =='3':
                temp3=1
                f.close()
        if temp3==0:
            showinfo(title='錯誤', message ="身分與課程教授不符")
            f.close
            return
        else:
            f.close
        temp = 0
        with open("./學生資訊.csv","r",encoding="utf-8") as f:
            lines = f.readlines()
        with open("./學生資訊.csv","w",encoding="utf-8") as fRewrite:#w模式覆蓋
            for line in lines:
                info = line[:-1].split(",")
                if info[0] ==year and info[1] ==semester and info[2] ==num and info[3] ==identify and info[4] ==Name:
                    temp = 1
                    fRewrite.write('{},{},{},{},{},{},{},{},{},{}\n'.format(year,semester,num,identify,Name,score,1,info[7],info[8],info[9]))
                    continue#當查到資料相同時,將資料重新寫入修改後的並continue,相同時則寫入原本資訊
                fRewrite.write(line)
        if temp==0:
            showinfo(title='錯誤', message ="沒有此學生的課程成績")
        else:
            showinfo(title='提示', message ="修改成功")
class SearchFrame(Frame): #查詢頁面,繼承Frame
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定義內部變數root
        self.E1 = Entry(self,font=10)
        self.E2 = Entry(self,font=10)
        self.E3 = Entry(self,font=10)
        self.E4 = Entry(self,font=10)
        self.E5 = Entry(self,font=10)
        self.E6 = Entry(self,font=10,show="*")
        self.createPage()
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, font=10, text = '學年: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)
        Label(self,  font=10,text = '學期: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=E)
        Label(self,  font=10,text = '課程代碼: ').grid(row=3, stick=W, pady=10)
        self.E3.grid(row=3, column=1, stick=E)
        Label(self,  font=10,text = '學號: ').grid(row=4, stick=W, pady=10)
        self.E4.grid(row=4, column=1, stick=E)
        Label(self,  font=10,text = '使用者名稱: ').grid(row=5, stick=W, pady=10)
        self.E5.grid(row=5, column=1, stick=E)
        Label(self,  font=10,text = '密碼: ').grid(row=6, stick=W, pady=10)
        self.E6.grid(row=6, column=1, stick=E)
        Button(self, font=10, text='查詢',command=self.search).grid(row=7, column=1, stick=E, pady=10)
    def search(self):
        year = self.E1.get()
        semester = self.E2.get()
        num = self.E3.get()
        identify = self.E4.get()
        username = self.E5.get()
        password = self.E6.get()
        if  self.spacejudge(year) or self.spacejudge(semester) or self.spacejudge(num) or self.spacejudge(identify) or self.spacejudge(username) or self.spacejudge(password):
            showinfo(title='提示', message ="任一輸入不可為空")
        else:
            self.searchInfo(year,semester,num,identify,username,password)
    def searchInfo(self,year,semester,num,identify,username,password):
        temp=0
        f = open('./課程資訊.csv','r',encoding='utf-8')#重要!要選格式為UTF-8的excel檔才可讀取
        for line in f.readlines():
            info = line[:-1].split(",")
            if len(info)<5:
                break
            if info[0]==year and info[1]==semester and info[2] ==num:
                temp=1
                classname=info[3]
                f.close()
        if temp==0:
            showinfo(title='錯誤',message ="沒有此課程!")
            f.close()
            return
        else:
            f.close()
        temp3=0
        f = open('./帳號密碼.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==username and info[1] ==password and info[2] =='1' and info[5]==identify:
                temp3=1
                f.close()
            if info[0] ==username and info[1] ==password and info[2]=='3':
                temp3=1
                f.close()
        if temp3==0:
            showinfo(title='錯誤', message ="身分與欲查詢學生不符")
            f.close
            return
        else:
            f.close
        f = open('./學生資訊.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==year and info[1] ==semester and info[2] ==num and info[3] ==identify and info[6]=="1":
                showinfo(title='查詢結果',message ="姓名："+info[4] +"\n學號:"+info[3] +"\n課程:"+classname +"\n成績:"+info[5] )
                f.close()
                return
        showinfo(title='提示', message ="沒有此學生的成績")
        f.close()
        return
    def spacejudge(self,text):
        spacejudge = 0
        for i in text:
            if not i.isspace():
                spacejudge = 1
                break
        if spacejudge==1:
            return 0
        else:
            return 1
class OutputFrame(Frame):
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定義內部變數root
        self.E1 = Entry(self,font=10)
        self.E2 = Entry(self,font=10)
        self.E3 = Entry(self,font=10)
        self.E4 = Entry(self,font=10)
        self.E5 = Entry(self,font=10)
        self.E6 = Entry(self,font=10,show="*")
        self.createPage()
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, font=10, text = '學年: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=W)
        Label(self,  font=10,text = '學期: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=W)
        Label(self,  font=10,text = '學號: ').grid(row=3, stick=W, pady=10)
        self.E3.grid(row=3, column=1, stick=W)
        Label(self,  font=10,text = '姓名: ').grid(row=4, stick=W, pady=10)
        self.E4.grid(row=4, column=1, stick=W)
        Label(self,  font=10,text = '使用者名稱: ').grid(row=5, stick=W, pady=10)
        self.E5.grid(row=5, column=1, stick=W)
        Label(self,  font=10,text = '密碼: ').grid(row=6, stick=W, pady=10)
        self.E6.grid(row=6, column=1, stick=W)
        self.tree=ttk.Treeview(self)#表格
        self.tree["columns"]=("課程","類型","學分","學號","學生姓名","成績")
        self.tree.column("課程",width=100)   #表示列,不顯示
        self.tree.column("類型",width=100)
        self.tree.column("學分",width=100)
        self.tree.column("學號",width=100)
        self.tree.column("學生姓名",width=100)
        self.tree.column("成績",width=100) 
        self.tree.heading("課程",text="課程")  #顯示錶頭
        self.tree.heading("類型",text="類型")
        self.tree.heading("學分",text="學分")
        self.tree.heading("學號",text="學號")
        self.tree.heading("學生姓名",text="學生姓名")
        self.tree.heading("成績",text="成績")
        self.tree.grid(row=7, column=1, stick=W, pady=10)
        Button(self, font=10, text='產生成績單',command=self.Output).grid(row=8, column=1, stick=E, pady=10)
    def Output(self):
        x=self.tree.get_children()
        for item in x:
            self.tree.delete(item)#刪除表格內元件
        year = self.E1.get()
        semester = self.E2.get()
        identify = self.E3.get()
        name = self.E4.get()
        username = self.E5.get()
        password = self.E6.get()
        if  self.spacejudge(year) or self.spacejudge(semester) or self.spacejudge(identify) or self.spacejudge(name) or self.spacejudge(username) or self.spacejudge(password):
            showinfo(title='提示', message ="任一輸入不可為空")
        else:
            self.OutputInfo(year,semester,identify,name,username,password)
    def OutputInfo(self,year,semester,identify,name,username,password):
        temp3=0
        f = open('./帳號密碼.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==username and info[1] ==password and info[2] =='1' and info[5]==identify:
                temp3=1
                f.close()
            if info[0] ==username and info[1] ==password and info[2]=='3':
                temp3=1
                f.close()
        if temp3==0:
            showinfo(title='錯誤', message ="身分與欲查詢學生不符")
            f.close
            return
        else:
            f.close
        temp=0
        i=0
        f = open('./學生資訊.csv','r',encoding='utf-8')#重要!要選格式為UTF-8的excel檔才可讀取
        for line in f.readlines():
            info = line[:-1].split(",")
            if len(info)<5:
                break
            if info[0]==year and info[1]==semester and info[3] ==identify and info[4] ==name and info[6]=='1':
                temp=1
                self.tree.insert("",i,text=year+" "+semester,values=(info[7],info[9],info[8],info[3],info[4],info[5])) #插入資料
                i+=1
                f.close()
        if temp==0:
            showinfo(title='錯誤',message ="沒有此學生訊息!")
            f.close()
            return
        else:
            showinfo(title='提示',message ="已列出成績單")
            f.close()
    def spacejudge(self,text):
        spacejudge = 0
        for i in text:
            if not i.isspace():
                spacejudge = 1
                break
        if spacejudge==1:
            return 0
        else:
            return 1
class ProfessorOutputFrame(Frame):
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定義內部變數root
        self.E1 = Entry(self,font=10)
        self.E2 = Entry(self,font=10)
        self.E3 = Entry(self,font=10)
        self.E4 = Entry(self,font=10)
        self.E5 = Entry(self,font=10,show="*")
        self.createPage()
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, font=10, text = '學年: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=W)
        Label(self,  font=10,text = '學期: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=W)
        Label(self,  font=10,text = '課程代碼: ').grid(row=3, stick=W, pady=10)
        self.E3.grid(row=3, column=1, stick=W)
        Label(self,  font=10,text = '使用者名稱: ').grid(row=4, stick=W, pady=10)
        self.E4.grid(row=4, column=1, stick=W)
        Label(self,  font=10,text = '密碼: ').grid(row=5, stick=W, pady=10)
        self.E5.grid(row=5, column=1, stick=W)
        self.tree=ttk.Treeview(self)#表格
        self.tree["columns"]=("學號","學生姓名","成績")
        self.tree.column("學號",width=100)#表示列,不顯示
        self.tree.column("學生姓名",width=100)  
        self.tree.column("成績",width=100)
        self.tree.heading("學號",text="學號")#顯示錶頭
        self.tree.heading("學生姓名",text="學生姓名")
        self.tree.heading("成績",text="成績")
        self.tree.grid(row=6, column=1, stick=W, pady=10)
        Button(self, font=10, text='列出',command=self.search).grid(row=7, column=1, stick=E, pady=10)
    def search(self):
        x=self.tree.get_children()
        for item in x:
            self.tree.delete(item)#刪除表格內元件
        year = self.E1.get()
        semester = self.E2.get()
        num = self.E3.get()
        username = self.E4.get()
        password = self.E5.get()
        if self.spacejudge(year) or self.spacejudge(semester) or self.spacejudge(num) or self.spacejudge(username) or self.spacejudge(password):
            showinfo(title='提示', message ="任一輸入不可為空")
        else:
            self.searchInfo(year,semester,num,username,password)
    def searchInfo(self,year,semester,num,username,password):
        temp2=0
        f = open('./課程資訊.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==year and info[1] ==semester and info[2] ==num:
                temp2=1
                classname=info[3]
                proname=info[5]
                f.close()
        if temp2==0:
            showinfo(title='提示', message ="沒有此學期課程訊息")
            f.close()
            return
        else:
            f.close
        temp3=0
        f = open('./帳號密碼.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==username and info[1] ==password and info[2] =='2' and info[3]==proname:
                temp3=1
                f.close()
        if temp3==0:
            showinfo(title='錯誤', message ="身分與課程教授不符")
            f.close
            return
        else:
            f.close
        temp=0
        i=0
        f = open('./學生資訊.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==year and info[1] ==semester and info[2] ==num and info[6]=='1':
                temp=1
                self.tree.insert("",i,text=classname ,values=(info[3],info[4],info[5])) #插入資料
                i+=1
        if temp==0:
            showinfo(title='提示', message ="此學期課程沒有此學生的訊息")
            f.close()
            return
        else:
            showinfo(title='提示', message ="已列出表格")
            f.close()
            return
    def spacejudge(self,text):
        spacejudge = 0
        for i in text:
            if not i.isspace():
                spacejudge = 1
                break
        if spacejudge==1:
            return 0
        else:
            return 1
class AddModifyCourseFrame(Frame):
    def __init__(self, master=None): 
        Frame.__init__(self, master)  
        self.root = master #定義內部變數root
        self.E1 = Entry(self,font=10)
        self.E2 = Entry(self,font=10)
        self.E3 = Entry(self,font=10)
        self.E4 = Entry(self,font=10)
        self.E5 = Entry(self,font=10)
        self.E6 = Entry(self,font=10)
        self.E7 = Entry(self,font=10)
        self.createPage()
    def createPage(self):
        Label(self,font=10,text='請輸入欲新增或修改的課程資訊').grid(row=0, stick=W, pady=10)
        Label(self, font=10,text = '年度: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1,stick=E)
        Label(self, font=10,text = '學期: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1,stick=E)
        Label(self, font=10,text = '代碼: ').grid(row=3, stick=W, pady=10)
        self.E3.grid(row=3, column=1,stick=E)
        Label(self,  font=10,text = '名稱: ').grid(row=4, stick=W, pady=10)
        self.E4.grid(row=4, column=1, stick=E)
        Label(self,  font=10,text = '學分: ').grid(row=5, stick=W, pady=10) 
        self.E5.grid(row=5, column=1, stick=E) 
        Label(self,  font=10,text = '授課教授: ').grid(row=6, stick=W, pady=10)
        self.E6.grid(row=6, column=1, stick=E)
        Label(self,  font=10,text = '類型: ').grid(row=7, stick=W, pady=10)
        self.E7.grid(row=7, column=1, stick=E)      
        Button(self,  font=10,text='新增',command=self.add).grid(row=8, column=1, stick=E, pady=10)
        Button(self,  font=10,text='修改',command=self.modify).grid(row=8, column=2, stick=E, pady=10)
    def add(self):
        year = self.E1.get()
        semester=self.E2.get()
        num = self.E3.get()
        name = self.E4.get()
        point = self.E5.get()
        professor = self.E6.get()
        classtype = self.E7.get()
        a='選修'
        b='必修'
        up='上'
        down='下'
        if self.spacejudge(year) or self.spacejudge(semester) or self.spacejudge(num) or self.spacejudge(name) or self.spacejudge(point) or self.spacejudge(professor) or self.spacejudge(classtype):
            showinfo(title='提示', message ="任一輸入不可為空")
        elif classtype !=a.strip() and classtype!=b.strip() :
            showinfo(title='提示', message ="類型請輸入'必修'或'選修'")
        elif semester !=up.strip() and semester!=down.strip() :
            showinfo(title='提示', message ="學期請輸入'上'或'下'")
        elif self.isLegal(year)==False:
            showinfo(title='提示', message ="年度只可包含數字")
        elif self.isLegalnum(num)==False :
            showinfo(title='提示', message ="代碼不可包含非法字元")
        elif num[0]=="0":
            showinfo(title='提示', message ="代碼不可以0開頭")
        elif self.isLegal(point)==False :
            showinfo(title='提示', message ="學分只可包含數字")
        else:
            self.addclass(year,semester,num,name,point,professor,classtype)
    def modify(self):
        year = self.E1.get()
        semester=self.E2.get()
        num = self.E3.get()
        name = self.E4.get()
        point = self.E5.get()
        professor = self.E6.get()
        classtype = self.E7.get()
        a='選修'
        b='必修'
        up='上'
        down='下'
        if self.spacejudge(year) or self.spacejudge(semester) or self.spacejudge(num) or self.spacejudge(name) or self.spacejudge(point) or self.spacejudge(professor) or self.spacejudge(classtype):
            showinfo(title='提示', message ="任一輸入不可為空")
        elif classtype !=a.strip() and classtype!=b.strip() :
            showinfo(title='提示', message ="類型請輸入'必修'或'選修'")
        elif semester !=up.strip() and semester!=down.strip() :
            showinfo(title='提示', message ="學期請輸入'上'或'下'")
        elif self.isLegal(year)==False:
            showinfo(title='提示', message ="年度只可包含數字")
        elif self.isLegalnum(num)==False :
            showinfo(title='提示', message ="代碼不可包含非法字元")
        elif self.isLegal(point)==False :
            showinfo(title='提示', message ="學分只可包含數字")
        else:
            self.modifyclass(year,semester,num,name,point,professor,classtype)
    def isLegal(self,string):#判斷上面某些只能是數字
        alp = ['1','2','3','4','5','6','7','8','9','0']
        for i in string:
            if i in alp:
                pass
            else:
                return False
        return True
    def isLegalnum(self,string):#代碼只可以有大小寫英文,數字
        alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
               'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
               '1','2','3','4','5','6','7','8','9','0']
        for i in string:
            if i in alp:
                pass
            else:
                return False
        return True
    def addclass(self,year,semester,num,name,point,professor,classtype):
        temp=0
        f = open('./帳號密碼.csv','r',encoding='utf-8')#開啟excel,模式:r=讀取(read),從頭開始
        for line in f.readlines():
            info = line[:-1].split(",")
            if len(info)<2:
                break
            if info[3].strip()==professor and info[2]=='2':
                pronum=info[5]
                yearIn=info[4]
                temp=1
        if int(yearIn)>int(year):
            showinfo(title='錯誤', message ="教授入職年份不可大於課程學年!")
            f.close
            return
        elif temp==1:
            f.close()
        else:
            showinfo(title='錯誤', message ="沒有此教授!")
            f.close()
            return
        f = open('./課程資訊.csv','r',encoding='utf-8')#重要!要選格式為UTF-8的excel檔才可讀取
        for line in f.readlines():
            info = line[:-1].split(",")
            if len(info)<5:
                break
            if info[0]==year and info[1]==semester and info[2] ==num:
                showinfo(title='提示', message ="已有課程使用該代號!")
                f.close()
                return
        f.close()
        f = open('./課程資訊.csv','a',encoding='utf-8')
        f.write('{},{},{},{},{},{},{},{}\n'.format(year,semester,num,name,point,professor,classtype,pronum))
        f.close()
        showinfo(title='提示', message ="輸入成功")
        return
    def modifyclass(self,year,semester,num,name,point,professor,classtype):
        temp2=0
        f = open('./帳號密碼.csv','r',encoding='utf-8')#開啟excel,模式:r=讀取(read),從頭開始
        for line in f.readlines():
            info = line[:-1].split(",")
            if len(info)<2:
                break
            if info[3].strip()==professor and info[2]=='2':
                pronum=info[5]
                yearIn=info[4]
                temp2=1
        if int(yearIn)>int(year):
            showinfo(title='錯誤', message ="教授入職年份不可大於課程學年!")
            f.close()
            return
        elif temp2==1:
            f.close()
        else:
            showinfo(title='錯誤', message ="沒有此教授!")
            f.close()
            return
        temp = 0
        with open("./課程資訊.csv","r",encoding="utf-8") as f:
            lines = f.readlines()
        with open("./課程資訊.csv","w",encoding="utf-8") as fRewrite:#w模式覆蓋
            for line in lines:
                info = line[:-1].split(",")
                if info[0]==year and info[1]==semester and info[2] ==num:
                    temp = 1
                    fRewrite.write('{},{},{},{},{},{},{},{}\n'.format(year,semester,num,name,point,professor,classtype,pronum))
                    continue#當查到資料相同時,將資料重新寫入修改後的並continue,相同時則寫入原本資訊
                if info[0]==year and info[1]==semester and info[2] !=num and info[3]==name and info[4]==point and info[5]==professor and info[6]==classtype:
                    temp = 2
                    fRewrite.write('{},{},{},{},{},{},{},{}\n'.format(year,semester,num,name,point,professor,classtype,pronum))
                    continue
                fRewrite.write(line)
        if temp==0:
            showinfo(title='提示', message ="沒有此課程的資訊")
        elif temp==1:
            with open("./學生資訊.csv","r",encoding="utf-8") as f:
                lines = f.readlines()
            with open("./學生資訊.csv","w",encoding="utf-8") as fRewrite:#模式w:檔案不存在會新建檔案，檔案存在會覆蓋檔案
                for line in lines:
                    info = line[:-1].split(",")
                    if info[0]==year and info[1]==semester and info[2] ==num:
                        continue
                    fRewrite.write(line)
            showinfo(title='提示', message ="修改成功")
        else:
            with open("./學生資訊.csv","r",encoding="utf-8") as f:
                lines = f.readlines()
            with open("./學生資訊.csv","w",encoding="utf-8") as fRewrite:#模式w:檔案不存在會新建檔案，檔案存在會覆蓋檔案
                for line in lines:
                    info = line[:-1].split(",")
                    if info[0]==year and info[1]==semester and info[2] !=num and info[7]==name and info[8]==point and info[9]==classtype:
                        continue
                    fRewrite.write(line)
            showinfo(title='提示', message ="修改成功")
    def spacejudge(self,text):
        spacejudge = 0
        for i in text:
            if not i.isspace():
                spacejudge = 1
                break
        if spacejudge==1:
            return 0
        else:
            return 1
class DeleteCourseFrame(Frame):
    def __init__(self, master=None): 
        Frame.__init__(self, master)  
        self.root = master #定義內部變數root
        self.E1 = Entry(self,font=10)
        self.E2 = Entry(self,font=10)
        self.E3 = Entry(self,font=10)
        self.createPage()
    def createPage(self):
        Label(self,font=10,text='請輸入要刪除的課程').grid(row=0, stick=W, pady=10)
        Label(self, font=10,text = '年度: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1,stick=E)
        Label(self, font=10,text = '學期: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1,stick=E)
        Label(self, font=10,text = '代碼: ').grid(row=3, stick=W, pady=10)
        self.E3.grid(row=3, column=1,stick=E)  
        Button(self,  font=10,text='刪除',command=self.deleteC).grid(row=4, column=1, stick=E, pady=10)
    def deleteC(self):
        year = self.E1.get()
        semester = self.E2.get()
        num = self.E3.get()
        up='上'
        down='下'
        if self.spacejudge(year) or self.spacejudge(semester) or self.spacejudge(num):
            showinfo(title='提示', message ="輸入不可為空")
        elif self.isLegalnum(num)==False :
            showinfo(title='提示', message ="代碼不可包含非法字元")
        elif semester !=up.strip() and semester!=down.strip() :
            showinfo(title='提示', message ="學期請輸入'上'或'下'")
        elif self.isLegal(year)==False:
            showinfo(title='提示', message ="年度只可包含數字")
        else:
            self.deleteclass(year,semester,num)
    def isLegalnum(self,string):#代碼只可以有大小寫英文,數字
        alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
               'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
               '1','2','3','4','5','6','7','8','9','0']
        for i in string:
            if i in alp:
                pass
            else:
                return False
        return True
    def deleteclass(self,year,semester,num): 
        with open("./學生資訊.csv","r",encoding="utf-8") as f:
            lines = f.readlines()
        with open("./學生資訊.csv","w",encoding="utf-8") as fRewrite:#模式w:檔案不存在會新建檔案，檔案存在會覆蓋檔案
            for line in lines:
                info = line[:-1].split(",")
                if info[0]==year and info[1]==semester and info[2] ==num:
                    continue
                fRewrite.write(line) 
        temp = 0
        with open("./課程資訊.csv","r",encoding="utf-8") as f:
            lines = f.readlines()
        with open("./課程資訊.csv","w",encoding="utf-8") as fRewrite:#模式w:檔案不存在會新建檔案，檔案存在會覆蓋檔案
            for line in lines:
                info = line[:-1].split(",")
                if info[0]==year and info[1]==semester and info[2] ==num:
                    temp = 1
                    continue
                fRewrite.write(line)#當資料不同時,將資料重新寫入,相同時則continue跳過此次迴圈繼續寫
        if temp==0:
            showinfo(title='提示', message ="沒有此課程的資訊")
        else:
            showinfo(title='提示', message ="刪除成功")
    def spacejudge(self,text):
        spacejudge = 0
        for i in text:
            if not i.isspace():
                spacejudge = 1
                break
        if spacejudge==1:
            return 0
        else:
            return 1
    def isLegal(self,string):
        alp = ['1','2','3','4','5','6','7','8','9','0']
        for i in string:
            if i in alp:
                pass
            else:
                return False
        return True
class ListCourseFrame(Frame):
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定義內部變數root
        self.E1 = Entry(self,font=10)
        self.E2 = Entry(self,font=10)
        self.createPage()
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, font=10, text = '學年: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=W)
        Label(self,  font=10,text = '學期: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=W)
        self.tree=ttk.Treeview(self)#表格
        self.tree["columns"]=("代碼","名稱","學分","教授","類型")
        self.tree.column("代碼",width=100)   #表示列,不顯示
        self.tree.column("名稱",width=100)
        self.tree.column("學分",width=100)
        self.tree.column("教授",width=100)
        self.tree.column("類型",width=100)     
        self.tree.heading("代碼",text="代碼")  #顯示錶頭
        self.tree.heading("名稱",text="名稱")
        self.tree.heading("學分",text="學分")
        self.tree.heading("教授",text="教授")
        self.tree.heading("類型",text="類型")
        self.tree.grid(row=3, column=1, stick=W, pady=10)
        Button(self, font=10, text='查詢',command=self.search).grid(row=6, column=1, stick=E, pady=10)
    def search(self):
        x=self.tree.get_children()
        for item in x:
            self.tree.delete(item)#刪除表格內元件
        year = self.E1.get()
        semester = self.E2.get()
        if self.spacejudge(year) or self.spacejudge(semester):
            showinfo(title='提示', message ="任一輸入不可為空")
        else:
            self.searchInfo(year,semester)
    def searchInfo(self,year,semester):
        temp=0
        i=0
        f = open('./課程資訊.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==year and info[1] ==semester:
                temp=1
                self.tree.insert("",i,text="課程" ,values=(info[2],info[3],info[4],info[5],info[6])) #插入資料
                i+=1
        if temp==0:
            showinfo(title='提示', message ="沒有此學期課程的訊息")
            f.close()
            return
        else:
            showinfo(title='提示', message ="已列出表格")
            f.close()
            return
    def spacejudge(self,text):
        spacejudge = 0
        for i in text:
            if not i.isspace():
                spacejudge = 1
                break
        if spacejudge==1:
            return 0
        else:
            return 1
class ListCourseStudentFrame(Frame):
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定義內部變數root
        self.E1 = Entry(self,font=10)
        self.E2 = Entry(self,font=10)
        self.E3 = Entry(self,font=10)
        self.createPage()
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, font=10, text = '學年: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=W)
        Label(self,  font=10,text = '學期: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=W)
        Label(self,  font=10,text = '課程代碼: ').grid(row=3, stick=W, pady=10)
        self.E3.grid(row=3, column=1, stick=W)
        self.tree=ttk.Treeview(self)#表格
        self.tree["columns"]=("代碼","學號","學生姓名")
        self.tree.column("代碼",width=100)   #表示列,不顯示
        self.tree.column("學號",width=100)
        self.tree.column("學生姓名",width=100)  
        self.tree.heading("代碼",text="代碼")  #顯示錶頭
        self.tree.heading("學號",text="學號")
        self.tree.heading("學生姓名",text="學生姓名")
        self.tree.grid(row=4, column=1, stick=W, pady=10)
        Button(self, font=10, text='查詢',command=self.search).grid(row=6, column=1, stick=E, pady=10)
    def search(self):
        x=self.tree.get_children()
        for item in x:
            self.tree.delete(item)#刪除表格內元件
        year = self.E1.get()
        semester = self.E2.get()
        num = self.E3.get()
        if self.spacejudge(year) or self.spacejudge(semester) or self.spacejudge(num):
            showinfo(title='提示', message ="任一輸入不可為空")
        else:
            self.searchInfo(year,semester,num)
    def searchInfo(self,year,semester,num):
        temp=0
        temp2=0
        i=0
        f = open('./課程資訊.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==year and info[1] ==semester and info[2] ==num:
                temp2=1
                classname=info[3]
                f.close()
        if temp2==0:
            showinfo(title='提示', message ="沒有此學期課程訊息")
            f.close()
            return
        else:
            f.close
        f = open('./學生資訊.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[0] ==year and info[1] ==semester and info[2] ==num:
                temp=1
                self.tree.insert("",i,text=classname ,values=(info[2],info[3],info[4])) #插入資料
                i+=1
        if temp==0:
            showinfo(title='提示', message ="沒有此學期課程的學生訊息")
            f.close()
            return
        else:
            showinfo(title='提示', message ="已列出表格")
            f.close()
            return
    def spacejudge(self,text):
        spacejudge = 0
        for i in text:
            if not i.isspace():
                spacejudge = 1
                break
        if spacejudge==1:
            return 0
        else:
            return 1
class AddDeleteCourseStudentFrame(Frame):
    def __init__(self, master=None):  
        Frame.__init__(self, master)
        self.root = master #定義內部變數root
        self.E1 = Entry(self,font=10)
        self.E2 = Entry(self,font=10)
        self.E3 = Entry(self,font=10)
        self.E4 = Entry(self,font=10)
        self.E5 = Entry(self,font=10)
        self.createPage()
    def createPage(self):#創造輸入介面
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, font=10,text = '學年: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1,stick=E)
        Label(self,  font=10,text = '學期: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=E)
        Label(self,  font=10,text = '課程代碼: ').grid(row=3, stick=W, pady=10) 
        self.E3.grid(row=3, column=1, stick=E) 
        Label(self,  font=10,text = '學號: ').grid(row=4, stick=W, pady=10)
        self.E4.grid(row=4, column=1, stick=E)
        Label(self,  font=10,text = '姓名: ').grid(row=5, stick=W, pady=10)
        self.E5.grid(row=5, column=1, stick=E)   
        Button(self,  font=10,text='增加學生',command=self.InputStudent).grid(row=7, column=1, stick=E, pady=10)
        Button(self,  font=10,text='刪除學生',command=self.DeleteStudent).grid(row=7, column=2, stick=E, pady=10)
    def InputStudent(self):#輸入資料判斷
        year = self.E1.get()
        semester = self.E2.get()
        num = self.E3.get()
        identify = self.E4.get()
        Name = self.E5.get()
        if self.spacejudge(year) or self.spacejudge(semester) or self.spacejudge(num) or self.spacejudge(identify) or self.spacejudge(Name):
            showinfo(title='提示', message ="任一輸入不可為空")
        else:
            self.writeInfo(year,semester,num,identify,Name)
    def DeleteStudent(self):
        year = self.E1.get()
        semester = self.E2.get()
        num = self.E3.get()
        identify = self.E4.get()
        Name = self.E5.get()
        if self.spacejudge(year) or self.spacejudge(semester) or self.spacejudge(num) or self.spacejudge(identify) or self.spacejudge(Name):
            showinfo(title='提示', message ="任一輸入不可為空")
        else:
            self.deleteInfo(year,semester,num,identify,Name)
    def spacejudge(self,studentData):#空格判斷
        spaceJudge = 0
        for i in studentData:
            if not i.isspace():#isspace()判斷是否為空
                spaceJudge = 1
                break
        if spaceJudge==1:
            return 0
        else:
            return 1
    def writeInfo(self,year,semester,num,identify,Name):
        temp=0
        f = open('./帳號密碼.csv','r',encoding='utf-8')#重要!要選格式為UTF-8的excel檔才可讀取
        for line in f.readlines():
            info = line[:-1].split(",")
            if len(info)<4:
                break
            if info[2] =="1" and info[3] ==Name and info[5] == identify:
                temp=1
                yearIn=info[4]
                f.close()
        if temp==0:
            showinfo(title='提示', message ="沒有該學生資訊!")
            f.close()
            return
        else:
            f.close()
        temp2=0
        f = open('./課程資訊.csv','r',encoding='utf-8')#重要!要選格式為UTF-8的excel檔才可讀取
        for line in f.readlines():
            info = line[:-1].split(",")
            if len(info)<4:
                break
            if info[0] ==year and info[1] ==semester and info[2] == num:
                classname=info[3]
                point=info[4]#學分
                type=info[6]
                temp2=1
                f.close()
            if info[0] ==year and info[1] ==semester and info[2] == num and info[0]<yearIn:
                temp2=2
                f.close()         
        if temp2==0:
            showinfo(title='提示', message ="沒有該課程資訊!")
            f.close()
            return
        elif temp2==2:
            showinfo(title='提示', message ="該學生入學年分大於課程開課年分!")
            f.close()
            return
        else:
            f.close()
        f = open('./學生資訊.csv','r',encoding='utf-8')#重要!要選格式為UTF-8的excel檔才可讀取
        for line in f.readlines():
            info = line[:-1].split(",")
            if len(info)<4:
                break
            if info[0] ==year and info[1] ==semester and info[2] == num and info[3] == identify:
                showinfo(title='提示', message ="此學生已選修該課程!")
                f.close()
                return
        f.close()
        f = open('./學生資訊.csv','a',encoding='utf-8')
        f.write('{},{},{},{},{},{},{},{},{},{}\n'.format(year,semester,num,identify,Name,'',0,classname,point,type))
        f.close()
        showinfo(title='提示', message ="輸入成功")
        return
    def deleteInfo(self,year,semester,num,identify,Name):
        temp = 0
        with open("./學生資訊.csv","r",encoding="utf-8") as f:
            lines = f.readlines()
        with open("./學生資訊.csv","w",encoding="utf-8") as fRewrite:#模式w:檔案不存在會新建檔案，檔案存在會覆蓋檔案
            for line in lines:
                info = line[:-1].split(",")
                if info[0] ==year and info[1] ==semester and info[2] ==num and info[3] ==identify:
                    temp = 1
                    continue
                fRewrite.write(line)#當資料不同時,將資料重新寫入,相同時則continue跳過此次迴圈繼續寫
        if temp==0:
            showinfo(title='提示', message ="沒有此學生的課程資訊")
        else:
            showinfo(title='提示', message ="刪除成功")
class AddModifyAccountFrame(Frame):
    def __init__(self, master=None): 
        Frame.__init__(self, master)  
        self.root = master #定義內部變數root
        self.E1 = Entry(self,font=10)
        self.E2 = Entry(self,font=10)
        self.E3 = Entry(self,font=10)
        self.E4 = Entry(self,font=10)
        self.E5 = Entry(self,font=10)
        self.E6 = Entry(self,font=10)
        self.createPage()
    def createPage(self):
        Label(self, font=10, text = "請輸入帳號資訊").grid(row=0, stick=W, pady=10)
        Label(self, font=10, text = '帳號: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)
        Label(self, font=10, text = '密碼: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=E)
        Label(self, font=10, text = '身分: ').grid(row=3, stick=W, pady=10)
        self.E3.grid(row=3, column=1, stick=E)
        Label(self, font=10, text = '姓名: ').grid(row=4, stick=W, pady=10)
        self.E4.grid(row=4, column=1, stick=E)
        Label(self, font=10, text = '入學年分: ').grid(row=5, stick=W, pady=10)
        self.E5.grid(row=5, column=1, stick=E)
        Label(self, font=10, text = '學號/教授號: ').grid(row=6, stick=W, pady=10)
        self.E6.grid(row=6, column=1, stick=E)
        Button(self, font=10, text='新增',command=self.check).grid(row=7, column=1, stick=E, pady=10)
        Button(self, font=10, text='修改',command=self.modify).grid(row=7, column=2, stick=E, pady=10)
    def check(self):
        name = self.E1.get()  
        password = self.E2.get()
        Identity = self.E3.get()
        Name = self.E4.get()
        yearIn = self.E5.get()
        Identify = self.E6.get()
        authority=0#權限
        if len(name)==0 or len(password)==0 or len(Identity)==0 or len(Identify)==0 or len(Name)==0 or len(yearIn)==0:
            showinfo(title='錯誤', message='任一輸入不能為空')
            return
        if name[0]=="0" or password[0]=="0":
            showinfo(title='錯誤', message='帳號密碼不可以0開頭')
            return
        if Identify[0]=="0":
            showinfo(title='錯誤', message='學號不可以0開頭')
            return
        for i in password:
            if i ==',' or i =='':
                showinfo(title='錯誤', message='密碼不可包含非法字符')
                return
        if self.isLegal(name):
            pass
        else:
            showinfo(title='錯誤', message='名稱不可包含非法字符')
            return
        if Identity !="學生" and Identity!="教授" :
            showinfo(title='提示', message ="身分請輸入'學生'或'教授'")
            return
        else:
            pass
        if self.isLegalnumber(Identify):
            pass
        else:
            showinfo(title='錯誤', message='學號/教授號不可包含非法字符')
            return
        if self.isLegalnumber(yearIn):
            pass
        else:
            showinfo(title='錯誤', message='入學年分不可包含非法字符')
            return
        if Identity =="學生":
            authority="1"
        else:
            authority="2"
        f = open('./帳號密碼.csv','r',encoding='utf-8')#開啟excel,模式:r=讀取(read),從頭開始
        for line in f.readlines():
            info = line[:-1].split(",")
            if len(info)<2:
                break
            if info[0].strip()==name:
                showinfo(title='錯誤', message ="此帳號已被使用")
                f.close()
                return
            if info[2].strip()==authority and info[5].strip()==Identify:
                showinfo(title='錯誤', message ="此學號/教授號已被使用")
                f.close()
                return
        f.close()
        f = open('./帳號密碼.csv','a',encoding='utf-8')#開啟excel,模式:a=加上(add),如果文件已存在會從尾端加
        f.write('{},{},{},{},{},{}\n'.format(name,password,authority,Name,yearIn,Identify))
        f.close()
        showinfo(title='提示', message ="註冊成功")
    def modify(self):
        name = self.E1.get()  
        password = self.E2.get()
        Identity = self.E3.get()
        Name = self.E4.get()
        yearIn = self.E5.get()
        Identify = self.E6.get()
        authority=0#權限
        if len(name)==0 or len(password)==0 or len(Identity)==0 or len(Identify)==0 or len(Name)==0 or len(yearIn)==0:
            showinfo(title='錯誤', message='任一輸入不能為空')
            return
        if password[0]=="0":
            showinfo(title='錯誤', message='密碼不可以0開頭')
            return
        if Identify[0]=="0":
            showinfo(title='錯誤', message='學號不可以0開頭')
            return
        for i in password:
            if i ==',' or i =='':
                showinfo(title='錯誤', message='密碼不可包含非法字符')
                return
        if self.isLegal(name):
            pass
        else:
            showinfo(title='錯誤', message='名稱不可包含非法字符')
            return
        if Identity !="學生" and Identity!="教授" :
            showinfo(title='提示', message ="身分請輸入'學生'或'教授'")
            return
        else:
            pass
        if self.isLegalnumber(Identify):
            pass
        else:
            showinfo(title='錯誤', message='學號/教授號不可包含非法字符')
            return
        if self.isLegalnumber(yearIn):
            pass
        else:
            showinfo(title='錯誤', message='入學年分不可包含非法字符')
            return
        if Identity =="學生":
            authority="1"
        else:
            authority="2"
        f = open('./帳號密碼.csv','r',encoding='utf-8')#開啟excel,模式:r=讀取(read),從頭開始
        for line in f.readlines():
            info = line[:-1].split(",")
            if len(info)<2:
                break
            if info[0].strip()!=name and info[2].strip()==authority and info[5].strip()==Identify:
                showinfo(title='錯誤', message ="此學號/教授號已被使用")
                f.close()
                return
        f.close()
        temp = 0
        with open("./帳號密碼.csv","r",encoding="utf-8") as f:
            lines = f.readlines()
        with open("./帳號密碼.csv","w",encoding="utf-8") as fRewrite:#w模式覆蓋
            for line in lines:
                info = line[:-1].split(",")
                if info[0] ==name:
                    identifynum=info[5]
                    temp = 1
                    fRewrite.write('{},{},{},{},{},{}\n'.format(name,password,authority,Name,yearIn,Identify))
                    continue#當查到資料相同時,將資料重新寫入修改後的並continue,相同時則寫入原本資訊
                fRewrite.write(line)
        if temp==0:
            showinfo(title='提示', message ="沒有此帳號的資訊")
        else:
            showinfo(title='提示', message ="修改成功")
        if authority=="1":
            with open("./學生資訊.csv","r",encoding="utf-8") as f:
                lines = f.readlines()
            with open("./學生資訊.csv","w",encoding="utf-8") as fRewrite:#模式w:檔案不存在會新建檔案，檔案存在會覆蓋檔案
                for line in lines:
                    info = line[:-1].split(",")
                    if info[3] ==identifynum:
                        continue
                    fRewrite.write(line)
        if authority=="2":
            with open("./課程資訊.csv","r",encoding="utf-8") as f:
                lines = f.readlines()
            with open("./課程資訊.csv","w",encoding="utf-8") as fRewrite:#模式w:檔案不存在會新建檔案，檔案存在會覆蓋檔案
                for line in lines:
                    info = line[:-1].split(",")
                    if info[7] ==identifynum:
                        yearnum=info[0]
                        semesternum=info[1]
                        classnum=info[2]
                        continue
                    fRewrite.write(line)
            with open("./學生資訊.csv","r",encoding="utf-8") as f:
                lines = f.readlines()
            with open("./學生資訊.csv","w",encoding="utf-8") as fRewrite:#模式w:檔案不存在會新建檔案，檔案存在會覆蓋檔案
                for line in lines:
                    info = line[:-1].split(",")
                    if info[0] ==yearnum and info[1]==semesternum and info[2]==classnum:
                        continue
                    fRewrite.write(line)
    def isLegal(self,string):#使用者名稱只可以有大小寫英文,數字
        alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
               'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
               '1','2','3','4','5','6','7','8','9','0']
        for i in string:
            if i in alp:
                pass
            else:
                return False
        return True
    def isLegalnumber(self,string):
        alp = ['1','2','3','4','5','6','7','8','9','0']
        for i in string:
            if i in alp:
                pass
            else:
                return False
        return True
class DeleteAccountFrame(Frame):
    def __init__(self, master=None): 
        Frame.__init__(self, master)  
        self.root = master #定義內部變數root
        self.E1 = Entry(self,font=10)
        self.createPage()
    def createPage(self):
        Label(self, font=10, text = "請輸入要刪除的帳號").grid(row=0, stick=W, pady=10)
        Label(self, font=10, text = '帳號: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)
        Button(self, font=10, text='刪除',command=self.search).grid(row=6, column=1, stick=E, pady=10)
    def search(self):
        Account = self.E1.get()
        if self.spacejudge(Account):
            showinfo(title='提示', message ="輸入不可為空")
        else:
            self.AccountDelete(Account)
    def AccountDelete(self,Account):
        temp = 0
        with open("./帳號密碼.csv","r",encoding="utf-8") as f:
            lines = f.readlines()
        with open("./帳號密碼.csv","w",encoding="utf-8") as fRewrite:#w模式覆蓋
            for line in lines:
                info = line[:-1].split(",")
                if info[0] ==Account and info[2]!='3':
                    identifynum=info[5]
                    authority=info[2]
                    temp = 1
                    fRewrite.write('{},{},{},{},{},{}\n'.format("","","","","",""))
                    continue#當查到資料相同時,將資料重新寫入修改後的並continue,相同時則寫入原本資訊
                fRewrite.write(line)
        if temp==0:
            showinfo(title='提示', message ="沒有此帳戶")
            return
        else:
            showinfo(title='提示', message ="刪除成功")
        if authority=="1":
            with open("./學生資訊.csv","r",encoding="utf-8") as f:
                lines = f.readlines()
            with open("./學生資訊.csv","w",encoding="utf-8") as fRewrite:#模式w:檔案不存在會新建檔案，檔案存在會覆蓋檔案
                for line in lines:
                    info = line[:-1].split(",")
                    if info[3] ==identifynum:
                        continue
                    fRewrite.write(line)
        if authority=="2":
            with open("./課程資訊.csv","r",encoding="utf-8") as f:
                lines = f.readlines()
            with open("./課程資訊.csv","w",encoding="utf-8") as fRewrite:#模式w:檔案不存在會新建檔案，檔案存在會覆蓋檔案
                for line in lines:
                    info = line[:-1].split(",")
                    if info[7] ==identifynum:
                        yearnum=info[0]
                        semesternum=info[1]
                        classnum=info[2]
                        continue
                    fRewrite.write(line)
            with open("./學生資訊.csv","r",encoding="utf-8") as f:
                lines = f.readlines()
            with open("./學生資訊.csv","w",encoding="utf-8") as fRewrite:#模式w:檔案不存在會新建檔案，檔案存在會覆蓋檔案
                for line in lines:
                    info = line[:-1].split(",")
                    if info[0] ==yearnum and info[1]==semesternum and info[2]==classnum:
                        continue
                    fRewrite.write(line)
    def spacejudge(self,text):
        spacejudge = 0
        for i in text:
            if not i.isspace():
                spacejudge = 1
                break
        if spacejudge==1:
            return 0
        else:
            return 1