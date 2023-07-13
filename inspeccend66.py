from tkinter import *
import tkinter as tk
from math import sqrt
import math
import tkinter.font as font
import time
import sqlite3 as sql

now = time.localtime()

#--------------------------------------------------------------------------------------------
class Ssb_db5:
    def __init__(self):
        self.conn=sql.connect('uuser.db')
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS lass (field1 TEXT,\
                                                                    field2 TEXT ,\
                                                                    field3 TEXT ,\
                                                                    field4 TEXT ,\
                                                                    field5 TEXT ,\
                                                                    field6 TEXT )")
        self.conn.commit()
    def view(self):
        self.cur.execute("SELECT field1,field2,field3,field4,field5,field6 FROM lass ORDER BY field1")
        rows = self.cur.fetchall()
        return rows
    def insert(self,field1,field2,field3,field4,field5,field6):
        self.cur.execute("INSERT INTO lass VALUES (?,?,?,?,?,?)",(field1,field2,field3,field4,field5,field6))
        self.conn.commit()
        self.view()
    def delete(self,ID):
        self.cur.execute("DELETE FROM lass WHERE field1=?",(ID,))
        self.conn.commit()
        self.view()
    def edit(self,field1,field2,field3,field4,field5,field6):
	    self.cur.execute("UPDATE lass SET  field2 = ?, field3 = ?, field4 = ?, field5 = ?, field6 = ?  WHERE field1 = ? ", (field2, field3, field4, field5, field6, field1))
      
db5 = Ssb_db5()

def search5(strr):
    serser="SELECT * FROM lass WHERE (field1 || field2 || field3 || field4 || field5 || field6 ) LIKE '%' || ? || '%'"
    db5.cur.execute(serser,[strr])
    return db5.cur

check=0
def view_command5():
 
    root5=Tk()

    def search_query(even):
        list1.delete(0,END)
        searchhh=str(search_bar.get())
        global check
        check = 1  
        search_bar.delete(0,END)
        for contact in search5(searchhh):
            list1.insert(END,str(contact[0])+" "+str(contact[1])+" "+str(contact[2])+" "+str(contact[3])+" "+str(contact[4])+" "+str(contact[5]))
          
    def delete_command():
        db5.delete(selected_tuple[0])
        root5.destroy()
        global check
        check=0
        view_command5()

    def command_add():
        db5.insert(e5.get(),e6.get(),e1.get(),e2.get(),e3.get(),e4.get())
        root5.destroy()
        view_command5()

    def command_edit():
        db5.edit(e5.get(),e6.get(),e1.get(),e2.get(),e3.get(),e4.get())
        db5.conn.commit()
        root5.destroy()
        view_command5()  
        db5.view()      

    def get_selected_row(event):
        global selected_tuple
        index = list1.curselection()
      
        if index:
            selected_tuple=list1.get(index[0])
            # print(selected_tuple)
            global check
            if check==1:
                aa=selected_tuple.split(" ",6)             
                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                e4.delete(0,END)
                e5.delete(0,END)
                e6.delete(0,END)
                e1.insert(0,aa[2])
                e2.insert(0,aa[3])
                e3.insert(0,aa[4])
                e4.insert(0,aa[5])
                e5.insert(0,aa[0])
                e6.insert(0,aa[1])
                selected_tuple=tuple(aa) 
            else:

                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                e4.delete(0,END)
                e5.delete(0,END)
                e6.delete(0,END)
                e1.insert(0,list1.get(index[0])[2])
                e2.insert(0,list1.get(index[0])[3])
                e3.insert(0,list1.get(index[0])[4])
                e4.insert(0,list1.get(index[0])[5])
                e5.insert(0,list1.get(index[0])[0])
                e6.insert(0,list1.get(index[0])[1])
             

    root5.geometry('%dx%d+%d+%d' % (600, 500,600,360))
    root5.title('사용자 현황')
    list1 = Listbox(root5, height=30, width=55)
    list1.grid(row=4, column=0, rowspan=6, columnspan=2)
    sb1 = Scrollbar(root5)
    sb1.grid(row=2, column=2, rowspan=6)
    
    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)
    list1.bind('<<ListboxSelect>>', get_selected_row)
    list1.delete(0,END)
    for row in db5.view():
        list1.insert(END,row)
     
    frame1 = LabelFrame(root5, text = "DATA")
    frame1.grid(row=3,column=3,rowspan=3)
   
    search_bar=Entry(frame1,width=10)
    search_bar.grid(row=7,column=3)
    search_return=Button(frame1,text='search',width=12,command=lambda: search_query(1))
    search_return.grid(row=7,column=4)
    search_bar.focus()
    search_bar.bind('<Return>',search_query)

    l5= Label(frame1,text="사용자번호")
    l6= Label(frame1,text="사용자명")
    l1= Label(frame1,text="계약면적")
    l2= Label(frame1,text="계약용량")
    l3= Label(frame1,text="연결열부하")
    l4= Label(frame1,text="열공급개시일")
    
    l5.grid(row=1,column=3)
    l6.grid(row=2,column=3)  
    
    l1.grid(row=3,column=3)
    l2.grid(row=4,column=3)
    l3.grid(row=5,column=3)
    l4.grid(row=6,column=3)
       
    e5 = Entry(frame1,width=15)
    e6 = Entry(frame1,width=15)  
    e1 = Entry(frame1,width=15)
    e2 = Entry(frame1,width=15)
    e3 = Entry(frame1,width=15)
    e4 = Entry(frame1,width=15)
    e5.grid(row=1,column=4)
    e6.grid(row=2,column=4)  
    e1.grid(row=3,column=4)
    e2.grid(row=4,column=4)
    e3.grid(row=5,column=4)
    e4.grid(row=6,column=4)

    e7=Button(frame1,width=12,text="delete",command=delete_command)
    e7.grid(row=8,column=4)

    e8=Button(frame1,width=12,text="add", command=command_add)
    e8.grid(row=9,column=4)
    e9=Button(frame1,width=12,text="edit", command=command_edit)
    e9.grid(row=10,column=4)
    root5.mainloop()

#-------------------------------------------------------------------------------------
class ssb_db1:
    def __init__(self):
        self.conn=sql.connect('first.db') 
        self.cur = self.conn.cursor() 
        self.cur.execute("CREATE TABLE IF NOT EXISTS Connecc (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
                                                                    Time TEXT NOT NULL,\
                                                                    Load TEXT NOT NULL,\
                                                                    Inlet TEXT NOT NULL,\
                                                                    PDCV TEXT NOT NULL,\
                                                                    Flow TEXT NOT NULL,\
                                                                    bigo TEXT )") 
        self.conn.commit() 
    def view(self):
        self.cur.execute("SELECT ID,Time,Load,Inlet,PDCV,Flow,bigo FROM Connecc") 
        rows = self.cur.fetchall() 
        return rows 
    def insert(self,Time,Load,Inlet,PDCV,Flow,bigo):
        self.cur.execute("INSERT INTO Connecc VALUES (NULL,?,?,?,?,?,?)",(Time,Load,Inlet,PDCV,Flow,bigo)) 
        self.conn.commit()
        self.view() 
    def delete(self,ID):
        self.cur.execute("DELETE FROM Connecc WHERE ID=?",(ID,))
        self.conn.commit()
        self.view()



class ssb_db2:
    def __init__(self):
        self.conn=sql.connect('second.db') 
        self.cur = self.conn.cursor() 
        self.cur.execute("CREATE TABLE IF NOT EXISTS Connecc (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
                                                                    Time TEXT NOT NULL,\
                                                                    heat_EX TEXT NOT NULL,\
                                                                    heat_pp TEXT NOT NULL,\
                                                                    heat1_dia TEXT NOT NULL,\
                                                                    heat2_dia TEXT NOT NULL,\
                                                                    expan TEXT NOT NULL,\
                                                                    heat_TCV TEXT NOT NULL,\
                                                                    bigo TEXT )") 
        self.conn.commit() 
    def view(self):
        self.cur.execute("SELECT ID,Time,heat_EX,heat_pp,heat1_dia,heat2_dia,expan,heat_TCV,bigo FROM Connecc") 
        rows = self.cur.fetchall() 
        return rows 
    def insert(self,Time,heat_EX,heat_PP,Heat1_dia,heat2_dia,expan,heat_TCV,bigo):
        self.cur.execute("INSERT INTO Connecc VALUES (NULL,?,?,?,?,?,?,?,?)",(Time,heat_EX,heat_PP,Heat1_dia,heat2_dia,expan,heat_TCV,bigo)) 
        self.conn.commit()
        self.view() 
    def delete(self,ID):
        self.cur.execute("DELETE FROM Connecc WHERE ID=?",(ID,))
        self.conn.commit()
        self.view()


class ssb_db3:
    def __init__(self):
        self.conn=sql.connect('third.db') 
        self.cur = self.conn.cursor() 
        self.cur.execute("CREATE TABLE IF NOT EXISTS Connecc (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
                                                                    Time TEXT NOT NULL,\
                                                                    hw_EX TEXT NOT NULL,\
                                                                    hw_pp TEXT NOT NULL,\
                                                                    hw1_dia TEXT NOT NULL,\
                                                                    hw2_dia TEXT NOT NULL,\
                                                                    hw_TCV TEXT NOT NULL,\
                                                                    bigo TEXT )") 
        self.conn.commit() 
    def view(self):
        self.cur.execute("SELECT ID,Time,hw_EX,hw_pp,hw1_dia,hw2_dia,hw_TCV,bigo FROM Connecc") 
        rows = self.cur.fetchall() 
        return rows 
    def insert(self,Time,hw_EX,hw_pp,hw1_dia,hw2_dia,hw_TCV,bigo):
        self.cur.execute("INSERT INTO Connecc VALUES (NULL,?,?,?,?,?,?,?)",(Time,hw_EX,hw_pp,hw1_dia,hw2_dia,hw_TCV,bigo)) 
        self.conn.commit()
        self.view() 
    def delete(self,ID):
        self.cur.execute("DELETE FROM Connecc WHERE ID=?",(ID,))
        self.conn.commit()
        self.view()



db1 = ssb_db1() 
db2 = ssb_db2()
db3 = ssb_db3()

nowis=str("%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)+"\n")

def search1(strr):
    serser="SELECT * FROM Connecc WHERE (ID || Time || Load || Inlet || PDCV || Flow || bigo) LIKE '%' || ? || '%'"
    db1.cur.execute(serser,[strr])
    return db1.cur
def search2(strr2):
    serser2="SELECT * FROM Connecc WHERE (ID || Time || heat_EX || heat_pp || heat1_dia || heat2_dia || expan || heat_TCV || bigo) LIKE '%' || ? || '%'"
    db2.cur.execute(serser2,[strr2])
    return db2.cur
def search3(strr3):
    serser3="SELECT * FROM Connecc WHERE (ID || Time || hw_EX || hw_pp || hw1_dia || hw2_dia|| hw_TCV || bigo) LIKE '%' || ? || '%'"
    db3.cur.execute(serser3,[strr3])
    return db3.cur

def view_command1(event):
    

    root3=Tk()
    
    def search_query():
        list1.delete(0,END)
        searchhh=str(search_bar.get())
        for contact in search1(searchhh):
            list1.insert(END,str(contact[0])+" "+str(contact[1])+" "+str(contact[2])+" "+str(contact[3])+" "+str(contact[4])+" "+str(contact[5])+" "+str(contact[6]))

    def delete_command():
        db1.delete(selected_tuple[0]) 
        root3.destroy()
        view_command1(1) 
    
    def get_selected_row(event): 
        global selected_tuple 
        index = list1.curselection() 
        if index: 
            selected_tuple=list1.get(index[0]) 

    b5 = Button(root3, text="Delete Selected", width=12, command=delete_command)
    b5.grid(row=1, column=1)


    root3.geometry('%dx%d+%d+%d' % (420, 540,500,260))
    root3.title('연결열부하/인입/PDCV/열량계')
    list1 = Listbox(root3, height=30, width=55)
    list1.grid(row=4, column=0, rowspan=6, columnspan=2)
    sb1 = Scrollbar(root3)
    sb1.grid(row=2, column=2, rowspan=6)
    
    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)
    list1.bind('<<ListboxSelect>>', get_selected_row)
    list1.delete(0,END) 
    for row in db1.view(): 
        list1.insert(END,row) 
    

    search_bar=Entry(root3,width=10)
    search_bar.grid(row=0,column=0)
    search_return=Button(root3,text='search',command=search_query)
    search_return.grid(row=1,column=0)
    


    root3.mainloop()

def add_command1():
    db1.insert(nowis,gg0.get(),gg1.get(),gg2.get(),gg3.get(),pre5.get()) 

def view_command2(event):
    root4=Tk()
    def search_query():
        list1.delete(0,END)
        searchhh=str(search_bar.get())
        for contact in search2(searchhh):
            list1.insert(END,str(contact[0])+" "+str(contact[1])+" "+str(contact[2])+" "+str(contact[3])+" "+str(contact[4])+" "+str(contact[5])+" "+str(contact[6])+" "+str(contact[7])+" "+str(contact[8]))

    def delete_command():
        db2.delete(selected_tuple[0]) 
        root4.destroy()
        view_command2(1) 
    
    def get_selected_row(event): 
        global selected_tuple 
        index = list1.curselection() 
        if index: 
            selected_tuple=list1.get(index[0]) 

    b5 = Button(root4, text="Delete Selected", width=12, command=delete_command)
    b5.grid(row=1, column=1)

    root4.geometry('%dx%d+%d+%d' % (560, 540,500,260))
    root4.title('난방HX용량/난방펌프/1차난방/2차난방/팽창/TCV')
    list1 = Listbox(root4, height=30, width=76)
    list1.grid(row=4, column=0, rowspan=6, columnspan=2)
    sb1 = Scrollbar(root4)
    sb1.grid(row=2, column=2, rowspan=6)
    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)
    list1.bind('<<ListboxSelect>>', get_selected_row)
    list1.delete(0,END) 
    for row in db2.view(): 
        list1.insert(END,row) 

    search_bar=Entry(root4,width=10)
    search_bar.grid(row=0,column=0)
    search_return=Button(root4,text='search',command=search_query)
    search_return.grid(row=1,column=0)
  
    root4.mainloop()

def add_command2():
    db2.insert(nowis,ggg0.get(),ggg1.get(),ggg2.get(),ggg3.get(),ggg4.get(),ggg5.get(),pre5.get()) 

def view_command3(even):
    root5=Tk()
    def search_query():
        list1.delete(0,END)
        searchhh=str(search_bar.get())
        for contact in search3(searchhh):
            list1.insert(END,str(contact[0])+" "+str(contact[1])+" "+str(contact[2])+" "+str(contact[3])+" "+str(contact[4])+" "+str(contact[5])+" "+str(contact[6])+" "+str(contact[7]))


    def delete_command():
        db3.delete(selected_tuple[0]) 
        root5.destroy()
        view_command3(1) 
    
    def get_selected_row(event): 
        global selected_tuple 
        index = list1.curselection() 
        if index: 
            selected_tuple=list1.get(index[0]) 

    b5 = Button(root5, text="Delete Selected", width=12, command=delete_command)
    b5.grid(row=1, column=1)    

    root5.geometry('%dx%d+%d+%d' % (500, 540,500,260))
    root5.title('급탕HX/급탕PP/1차재열/2차급탕/급TCV')
    list1 = Listbox(root5, height=30, width=65)
    list1.grid(row=4, column=0, rowspan=6, columnspan=2)
    sb1 = Scrollbar(root5)
    sb1.grid(row=2, column=2, rowspan=6)
    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)
    list1.bind('<<ListboxSelect>>', get_selected_row)
    list1.delete(0,END) 
    for row in db3.view(): 
        list1.insert(END,row) 

    search_bar=Entry(root5,width=10)
    search_bar.grid(row=0,column=0)
    search_return=Button(root5,text='search',command=search_query)
    search_return.grid(row=1,column=0)
            
    root5.mainloop()

def add_command3():
    db3.insert(nowis,gggg0.get(),gggg1.get(),gggg2.get(),gggg3.get(),gggg4.get(),pre5.get()) 

#-------------------------------------------시작시 화면크기------------------------------
def center_window(width, height):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height) - (height)
    # root.geometry('%dx%d+%d+%d' % (width, height*1.54, x+500,15))
    root.geometry('%dx%d+%d+%d' % (475, 700,1040,260))
#--------------------------------------------------------------------------------------


epp=1
eex1=0
eex12=0
# class RedFrame(Frame):
#     def __init__(self,root):
#         super().__init__()

#-----------------------------------------------------------옆의 해설화면 보기 /안보기---------------------------------

def remake():
    global epp
    if epp==1:
        root.geometry('%dx%d+%d+%d' % (810, 700,1040,260))
        epp=0
    else:
        root.geometry('%dx%d+%d+%d' % (475, 700,1040,260))
        epp=1 
#----------------------------------------------------------------------------------------------------------



root= Tk()


button_clear2 = Button(root,text="<  >",font= ("NanumGothicBold","9"),width=6,height=1,borderwidth=3,cursor="watch", command= remake).grid(row=0,sticky=E,column=4,padx=3,pady=3)

root.title("연결열부하/난방HX/급탕 HX(Mcal/hr) 또는 세대수")
def our_new():
    e.delete(0,END)
    gg0.delete(0,END)
    gg1.delete(0,END)
    gg2.delete(0,END)
    gg3.delete(0,END)
    ggg0.delete(0,END)
    ggg1.delete(0,END)
    ggg2.delete(0,END)
    ggg3.delete(0,END)
    ggg4.delete(0,END)
    ggg5.delete(0,END)
    gggg0.delete(0,END)
    gggg1.delete(0,END)
    gggg2.delete(0,END)
    gggg3.delete(0,END)
    gggg4.delete(0,END)
    ggggg0.delete(0,END)
    ggggg1.delete(0,END)
    ggggg2.delete(0,END)
    ggggg3.delete(0,END)
    f.delete('1.0',END)
    pre4.delete(0,END)
    pre5.delete(0,END)
    # f.grid_forget()
    # f2.grid(row=0, column=4, columnspan=3, rowspan=14)
    # Toplevel()
    global root2
    # root2=Tk()
    pass

def our_lmtd():
    
    root2=Tk()
    root2.geometry('%dx%d+%d+%d' % (280, 500,790,260))
    root2.title('HX 대수평균온도차')
    def hotinn():
        global eex1
        global hotint
        eex1=1
        hotint=e2.get()
        hotinla.delete(0,END)
        hotinla.insert(0,hotint)
    def hotoutn():
        global eex1
        global hotoutt
        eex1=1
        hotoutt=e2.get()
        hotoutla.delete(0,END)
        hotoutla.insert(0,hotoutt)
    def coldinn():
        global eex1
        global coldint
        eex1=1
        coldint=e2.get()
        coldinla.delete(0,END)
        coldinla.insert(0,coldint)
    def coldoutn():
        global eex1
        global coldoutt
        eex1=1
        coldoutt=e2.get()
        coldoutla.delete(0,END)
        coldoutla.insert(0,coldoutt)
    def calcal2():
        global eex1
        eex1=1
        tt1=int(hotint)-int(coldoutt)
        tt2=int(hotoutt)-int(coldint)
        answert=round((tt1-tt2)/math.log(tt1/tt2),2)
        answer2.delete(0,END)
        answer2.insert(0,answert)
    def clcls():
        global eex1
        eex1=1
        e2.delete(0,END)
        hotinla.delete(0,END)
        hotoutla.delete(0,END)
        coldoutla.delete(0,END)
        coldinla.delete(0,END)  
        answer2.delete(0,END)      
    button_1 = Button(root2, text="1", width=11,height=4, command=lambda : button2_click(1))
    button_1.configure(highlightbackground="red",cursor="target" ,relief="raised")
    button_1.grid(row=3, column=0)
    button_2 = Button(root2, text="2", width=11,height=4,cursor="target" ,command=lambda : button2_click(2)).grid(row=3, column=1)
    button_3 = Button(root2, text="3", width=11,height=4,cursor="target" ,command=lambda : button2_click(3)).grid(row=3, column=2)
    button_4 = Button(root2, text="4", width=11,height=4,cursor="target" ,command=lambda : button2_click(4)).grid(row=2, column=0)
    button_5 = Button(root2, text="5", width=11,height=4,cursor="target", command=lambda : button2_click(5)).grid(row=2, column=1)
    button_6 = Button(root2, text="6", width=11,height=4 ,cursor="target",command=lambda : button2_click(6)).grid(row=2, column=2)
    button_7 = Button(root2, text="7", width=11,height=4,cursor="target" ,command=lambda : button2_click(7)).grid(row=1, column=0)
    button_8 = Button(root2, text="8", width=11,height=4,cursor="target" ,command=lambda : button2_click(8)).grid(row=1, column=1)
    button_9 = Button(root2, text="9", width=11,height=4,cursor="target" ,command=lambda : button2_click(9)).grid(row=1, column=2)
    button_0 = Button(root2, text="0", width=11,height=4,cursor="target", command=lambda : button2_click(0)).grid(row=4, column=1)
    hotin=Button(root2,text="고온 입구온도",command=hotinn)
    hotin.grid(row=6,column=0)
    hotout=Button(root2,text="고온 출구온도",command=hotoutn)
    hotout.grid(row=7,column=0) 
    coldin=Button(root2,text="저온 입구온도",command=coldinn)
    coldin.grid(row=8,column=0)
    coldout=Button(root2,text="저온 출구온도",command=coldoutn)
    coldout.grid(row=9,column=0)
    answer=Button(root2,text="LMTD =", command=calcal2,width=11)
    answer.grid(row=10,column=0)
    clclsser=Button(root2,text="clear", command=clcls,width=12)
    clclsser.grid(row=10,column=2)

    answer2=Entry(root2,width=10,justify='center')
    answer2.grid(row=10,column=1)

    hotinla=Entry(root2,width=10,justify='center')
    hotinla.grid(row=6,column=1)
    hotoutla=Entry(root2,width=10,justify='center')
    hotoutla.grid(row=7,column=1)
    coldinla=Entry(root2,width=10,justify='center')
    coldinla.grid(row=8,column=1)
    coldoutla=Entry(root2,width=10,justify='center')
    coldoutla.grid(row=9,column=1)
    def button2_click(number):
        global eex1     
        if eex1==1:
            e2.delete(0,END)
            e2.insert(0,str(number))
            eex1=0
        else:
            current = e2.get()
            e2.delete(0, END)
            e2.insert(0, str(current) + str(number)) 
      
    e2 = Entry(root2, width=31, font= ("Calibri,350"), borderwidth=14, justify='right')
    e2.grid(row=0, column=0, columnspan=3)
    root2.mainloop()
#------------------------------------------------------------------------------------------------\
#==============================================================================================================

def our_dpv():
    
    root22=Tk()
    root22.geometry('%dx%d+%d+%d' % (280, 530,880,260))
    root22.title('난방 DPV 관경결정')
    def nanbang():
        global eex12
        global nanbang2
        eex12=1
        nanbang2=e22.get()
        hotinla2.delete(0,END)
        hotinla2.insert(0,nanbang2)

    def pumout():
        global eex12
        global yangjung
        eex1=1
        yangjung=e22.get()
        hotoutla2.delete(0,END)
        hotoutla2.insert(0,yangjung)

    def selectedttt(event):
        global afctt
        afctt = checkedttt.get()   
    
    optionttt = [15,10]

    checkedttt=StringVar(root22)
    checkedttt.set(optionttt[0])
    drop1000 = OptionMenu(root22, checkedttt, *optionttt, command = selectedttt)
    drop1000.config(width=7,font=("NanumGothicBold","9"),cursor="plus",borderwidth=4)
    drop1000.grid(row=8,column=1)
    myLabel100t=Label(root22, text="설계온도차",anchor=W,width=10,height=2)
    myLabel100t.config(anchor=E)
    myLabel100t.grid(row=8,column=0)

    def calcal2():
        global eex12
        eex12=1
        cvcvcv=1.167*((int(nanbang2)/int(afctt))/sqrt(int(yangjung)/30))*0.8
      


        if cvcvcv > pdd4[0]:
            valve3="250 A"
        elif cvcvcv > int((pdd4[0]-pdd4[1])*float(0.95)+pdd4[1]):
            valve3="250 A+"  
            valve3per=float(((cvcvcv-pdd4[1])/(pdd4[0]-pdd4[1]))*100)
        elif cvcvcv > pdd4[1]:
            valve3="200 A"
            valve3per=float(((cvcvcv-pdd4[1])/(pdd4[0]-pdd4[1]))*100)
        elif cvcvcv > int((pdd4[1]-pdd4[2])*float(0.95)+pdd4[2]):
            valve3="200 A+" 
            valve3per=float(((cvcvcv-pdd4[2])/(pdd4[1]-pdd4[2]))*100) 
        elif cvcvcv > pdd4[2]:
            valve3="150 A" 
            valve3per=float(((cvcvcv-pdd4[2])/(pdd4[1]-pdd4[2]))*100)    
        elif cvcvcv > int((pdd4[2]-pdd4[3])*float(0.95)+pdd4[3]):
            valve3="150 A+" 
            valve3per=float(((cvcvcv-pdd4[3])/(pdd4[2]-pdd4[3]))*100)  
        elif cvcvcv > pdd4[3]:
            valve3="125 A"
            valve3per=float(((cvcvcv-pdd4[3])/(pdd4[2]-pdd4[3]))*100)
        elif cvcvcv > int((pdd4[3]-pdd4[4])*float(0.95)+pdd4[4]):
            valve3="125 A+"
            valve3per=float(((cvcvcv-pdd4[4])/(pdd4[3]-pdd4[4]))*100)
        elif cvcvcv > pdd4[4]:
            valve3="100 A"
            valve3per=float(((cvcvcv-pdd4[4])/(pdd4[3]-pdd4[4]))*100)
        elif cvcvcv > int((pdd4[4]-pdd4[5])*float(0.95)+pdd4[5]):
            valve3="100 A+"
            valve3per=float(((cvcvcv-pdd4[5])/(pdd4[4]-pdd4[5]))*100)
        elif cvcvcv > pdd4[5]:
            valve3="80 A"  
            valve3per=float(((cvcvcv-pdd4[5])/(pdd4[4]-pdd4[5]))*100)  
        elif cvcvcv > int((pdd4[5]-pdd4[6])*float(0.95)+pdd4[6]):
            valve3="80 A+"
            valve3per=float(((cvcvcv-pdd4[6])/(pdd4[5]-pdd4[6]))*100)
        elif cvcvcv > pdd4[6]:
            valve3="65 A" 
            valve3per=float(((cvcvcv-pdd4[6])/(pdd4[5]-pdd4[6]))*100) 
        elif cvcvcv > int((pdd4[6]-pdd4[7])*float(0.95)+pdd4[7]):
            valve3="65 A+"
            valve3per=float(((cvcvcv-pdd4[7])/(pdd4[6]-pdd4[7]))*100)  
        elif cvcvcv > pdd4[7]:
            valve3="50 A"  
            valve3per=float(((cvcvcv-pdd4[7])/(pdd4[6]-pdd4[7]))*100) 
        elif cvcvcv > int((pdd4[7]-pdd4[8])*float(0.95)+pdd4[8]):
            valve3="50 A+" 
            valve3per=float(((cvcvcv-pdd4[8])/(pdd4[7]-pdd4[8]))*100)   
        elif cvcvcv > pdd4[8]:
            valve3="40 A"
            valve3per=float(((cvcvcv-pdd4[8])/(pdd4[7]-pdd4[8]))*100)
        elif cvcvcv > int((pdd4[8]-pdd4[9])*float(0.95)+pdd4[9]):
            valve3="40 A+" 
            valve3per=float(((cvcvcv-pdd4[9])/(pdd4[8]-pdd4[9]))*100)
        elif cvcvcv > pdd4[9]:
            valve3="32 A"
            valve3per=float(((cvcvcv-pdd4[9])/(pdd4[8]-pdd4[9]))*100)
        elif cvcvcv > int((pdd4[9]-pdd4[10])*float(0.95)+pdd4[10]):
            valve3="32 A+" 
            valve3per=float(((cvcvcv-pdd4[10])/(pdd4[9]-pdd4[10]))*100)
        elif cvcvcv < int(pdd4[9]):
            valve3="25 A" 
            valve3per=float(((cvcvcv-0)/(pdd4[9]-0))*100)


        answert2 = round(cvcvcv,2)
        answer22.delete(0,END)
        answer22.insert(0,answert2)

        answert2val = valve3
        answerval.delete(0,END)
        answerval.insert(0,answert2val)

        answert2per = round(valve3per,2)
        answerper.delete(0,END)
        answerper.insert(0,answert2per)                 



    def clcls2():
        global eex12
        eex12=1
        e22.delete(0,END)
        hotinla2.delete(0,END)
        hotoutla2.delete(0,END)
        answer22.delete(0,END)    
        answerval.delete(0,END)
        answerper.delete(0,END)  

    button_1 = Button(root22, text="1", width=11,height=4, command=lambda : button22_click(1))
    button_1.configure(highlightbackground="red",cursor="target" ,relief="raised")
    button_1.grid(row=3, column=0)
    button_2 = Button(root22, text="2", width=11,height=4,cursor="target" ,command=lambda : button22_click(2)).grid(row=3, column=1)
    button_3 = Button(root22, text="3", width=11,height=4,cursor="target" ,command=lambda : button22_click(3)).grid(row=3, column=2)
    button_4 = Button(root22, text="4", width=11,height=4,cursor="target" ,command=lambda : button22_click(4)).grid(row=2, column=0)
    button_5 = Button(root22, text="5", width=11,height=4,cursor="target", command=lambda : button22_click(5)).grid(row=2, column=1)
    button_6 = Button(root22, text="6", width=11,height=4 ,cursor="target",command=lambda : button22_click(6)).grid(row=2, column=2)
    button_7 = Button(root22, text="7", width=11,height=4,cursor="target" ,command=lambda : button22_click(7)).grid(row=1, column=0)
    button_8 = Button(root22, text="8", width=11,height=4,cursor="target" ,command=lambda : button22_click(8)).grid(row=1, column=1)
    button_9 = Button(root22, text="9", width=11,height=4,cursor="target" ,command=lambda : button22_click(9)).grid(row=1, column=2)
    button_0 = Button(root22, text="0", width=11,height=4,cursor="target", command=lambda : button22_click(0)).grid(row=4, column=1)

    nantin=Button(root22,text="HX(Mcal/hr)",command=nanbang)
    nantin.grid(row=6,column=0)
    pumhight=Button(root22,text="펌프 양정(M)",command=pumout)
    pumhight.grid(row=7,column=0) 

    answer2=Button(root22,text="CV 값 =", command=calcal2,width=11)
    answer2.grid(row=10,column=0)
    clclsser2=Button(root22,text="clear", command=clcls2,width=11)
    clclsser2.grid(row=10,column=2)


    def selecteddpv(event):
        global pdd4
        if checkedd4.get() == "신우" :
            pdd4=[400,260,170,100,75,68,44,25,17,11] 
        if checkedd4.get() == "신한" :
            pdd4=[350,240,142,98,78,58,43,28,22,12]     
        if checkedd4.get() == "삼양" :
            pdd4=[320,288,200,152,84,64,43,18,12.5,8]
        # print(pdd4)
    optiond4 = ["신우","신한","삼양"]
    # pdd4=[400,260,170,100,75,68,44,25,17,11]
    checkedd4=StringVar(root22)
    checkedd4.set(optiond4[0])
    dropd4 = OptionMenu(root22,checkedd4,*optiond4, command = selecteddpv)
    dropd4.config(width=7,font= ("NanumGothicBold","9"),cursor="plus",borderwidth=4)
    dropd4.grid(row=9,column=1)
    myLabeld4 = Label(root22,width=10, text="제조사")
    myLabeld4.config(anchor=E)
    myLabeld4.grid(row=9,column=0)

    myLabeld5 = Label(root22,width=10, text="DPV 관경")
    myLabeld5.config(anchor=E)
    myLabeld5.grid(row=11,column=0)

    myLabeld6 = Label(root22,width=10, text="관경선정%값")
    myLabeld6.config(anchor=E)
    myLabeld6.grid(row=12,column=0)




    answer22=Entry(root22,width=10,justify='center')
    answer22.grid(row=10,column=1)

    answerval=Entry(root22,width=10,justify='center')
    answerval.grid(row=11,column=1)

    answerper=Entry(root22,width=10,justify='center')
    answerper.grid(row=12,column=1)

    hotinla2=Entry(root22,width=10,justify='center')
    hotinla2.grid(row=6,column=1)
    hotoutla2=Entry(root22,width=10,justify='center')
    hotoutla2.grid(row=7,column=1)


    def button22_click(number):
        global eex12     
        if eex12==1:
            e22.delete(0,END)
            e22.insert(0,str(number))
            eex12=0
        else:
            current = e22.get()
            e22.delete(0, END)
            e22.insert(0, str(current) + str(number)) 
      
    e22 = Entry(root22, width=41,font= ("NanumGothicBold","9"), borderwidth=14, justify='right')
    e22.grid(row=0, column=0, columnspan=3)
    root22.mainloop()


#------------------------------------------------------------------------------------------------===================================================
#------------------------------------------------------------------------------------------------===================================================
def ourour_cal():

    import tkinter as tk
    from math import sqrt
    global calculation 
    calculation=""
    def add_to_calculation(symbol):
        global calculation
        calculation += str(symbol) 
        text_result.delete(1.0, "end")
        text_result.insert(1.0,calculation)
    def evaluate_calculation():
        global calculation
        try:
            result = str(eval(calculation))
            calculation=""
            text_result.delete(1.0, "end")
            text_result.insert(1.0, result)
        except:
            clear_field()
            text_result.insert(1.0,"Error")
    def clear_field():
        global calculation
        calculation=""
        text_result.delete(1.0,"end")
    rootcal = tk.Tk()
    rootcal.geometry("310x300")
    text_result = tk.Text(rootcal, height=3, width=20, font=("Arial", 20))
    text_result.grid(columnspan=5)
    btn_1 = tk.Button(rootcal,text="1", command=lambda: add_to_calculation(1),width=5, font=("Arial",14))
    btn_1.grid(row=2, column=1)
    btn_2 = tk.Button(rootcal,text="2", command=lambda: add_to_calculation(2),width=5, font=("Arial",14))
    btn_2.grid(row=2, column=2)
    btn_3 = tk.Button(rootcal,text="3", command=lambda: add_to_calculation(3),width=5, font=("Arial",14))
    btn_3.grid(row=2, column=3)
    btn_4 = tk.Button(rootcal,text="4", command=lambda: add_to_calculation(4),width=5, font=("Arial",14))
    btn_4.grid(row=3, column=1)
    btn_5 = tk.Button(rootcal,text="5", command=lambda: add_to_calculation(5),width=5, font=("Arial",14))
    btn_5.grid(row=3, column=2)
    btn_6 = tk.Button(rootcal,text="6", command=lambda: add_to_calculation(6),width=5, font=("Arial",14))
    btn_6.grid(row=3, column=3)
    btn_7 = tk.Button(rootcal,text="7", command=lambda: add_to_calculation(7),width=5, font=("Arial",14))
    btn_7.grid(row=4, column=1)
    btn_8 = tk.Button(rootcal,text="8", command=lambda: add_to_calculation(8),width=5, font=("Arial",14))
    btn_8.grid(row=4, column=2)
    btn_9 = tk.Button(rootcal,text="9", command=lambda: add_to_calculation(9),width=5, font=("Arial",14))
    btn_9.grid(row=4, column=3)
    btn_0 = tk.Button(rootcal,text="0", command=lambda: add_to_calculation(0),width=5, font=("Arial",14))
    btn_0.grid(row=5, column=2)
    btn_sqrt = tk.Button(rootcal,text="√", command=lambda: add_to_calculation("sqrt"),width=5, font=("Arial",14))
    btn_sqrt.grid(row=6, column=4)
    btn_plus = tk.Button(rootcal,text="+", command=lambda: add_to_calculation("+"),width=5, font=("Arial",14))
    btn_plus.grid(row=2, column=4)
    btn_minus = tk.Button(rootcal,text="-", command=lambda: add_to_calculation("-"),width=5, font=("Arial",14))
    btn_minus.grid(row=3, column=4)
    btn_mul = tk.Button(rootcal,text="*", command=lambda: add_to_calculation("*"),width=5, font=("Arial",14))
    btn_mul.grid(row=4, column=4)
    btn_div = tk.Button(rootcal,text="/", command=lambda: add_to_calculation("/"),width=5, font=("Arial",14))
    btn_div.grid(row=5, column=4)
    btn_open = tk.Button(rootcal,text="(", command=lambda: add_to_calculation("("),width=5, font=("Arial",14))
    btn_open.grid(row=5, column=1)
    btn_close = tk.Button(rootcal,text=")", command=lambda: add_to_calculation(")"),width=5, font=("Arial",14))
    btn_close.grid(row=5, column=3)
    btn_point = tk.Button(rootcal,text=".", command=lambda: add_to_calculation("."),width=5, font=("Arial",14))
    btn_point.grid(row=6, column=2)
    btn_equal = tk.Button(rootcal,text="=", command= evaluate_calculation, width=5, font=("Arial",14))
    btn_equal.grid(row=6, column=1)
    btn_clear = tk.Button(rootcal,text="C", command=clear_field,width=5, font=("Arial",14))
    btn_clear.grid(row=6, column=3)
    rootcal.mainloop()





#----------------------------------------------------------------------------------------------------------------------------------------------------------------






def simple():
    import PySimpleGUI as sg
    import math
    from math import sqrt
    sg.theme('DarkAmber')
    layout = [[sg.Text('냉동기 USRT 입력',key='_test_'),sg.Input(size=(17,1),background_color='white',text_color='black',tooltip="USRT입력",key='-in-',default_text=e.get()),sg.Text('냉수/냉각수 각각 입출구 온도차 ℃ :'),sg.Input(key='temp_in',tooltip="델타T 입력",default_text="5",background_color='white',text_color='black',size=(5,1)) ,sg.Text('COP 입력:'),sg.Input(key='_in2_',tooltip="COP 입력",default_text="0.73",background_color='white',text_color='black',size=(5,1)),sg.Text('1차△T:'),sg.Input(key='_in3_',tooltip="1차△T ",default_text="40",background_color='white',text_color='black',size=(5,1))],
            [sg.Text('냉수 유량 (lpm) : ', text_color='yellow'),sg.Text('',size=(8,1),key='_out_', text_color='white'),sg.Text('   냉각탑 냉각톤 (kcal/hr) :', text_color='yellow'),sg.Text('',size=(8,1),key='_out2_', text_color='white'),sg.Text('   냉각수 유량 (lpm) : ', text_color='yellow'),sg.Text('',size=(8,1),key='_out3_', text_color='white') ],
            [sg.Text('냉수 유량 (m3/hr) : ', text_color='yellow'),sg.Text('',size=(8,1),key='_out4_', text_color='white'),sg.Text('냉각탑 냉각톤 (CRT) :       ', text_color='yellow'),sg.Text('',size=(8,1),key='_out5_', text_color='white'),sg.Text('냉각수 유량 (m3/hr) : ', text_color='yellow'),sg.Text('',size=(8,1),key='_out6_', text_color='white') ],
            [sg.Text('냉각탑 용량산정 (CRT) =  [ 냉방부하 + (냉방부하 ÷ 냉동기COP) ] ÷ 3,900kcal'),sg.Text('← (냉방부하 단위는 Kcal/hr)',)],
            [sg.Text('냉각수 유량 (m3/hr) = [ 냉방부하 + (냉방부하 ÷ 냉동기COP) ] ÷ 냉각수 온도차'),sg.Text('← (냉방부하 단위는 Mcal/hr)')],
            [sg.Text('',key='_out7_',size=(4,1)),sg.Text('USRT X 3,024  ='),sg.Text('',key='_out8_',size=(7,1)),sg.Text('Kcal/hr  =  '),sg.Text('',key='_out9_',size=(5,1)),sg.Text('Mcal/hr ,  나누기 델타T →'),sg.Text('',key='_out10_',size=(4,1)),sg.Text('m3/hr (냉수 유량)')],
            [sg.Text('',key='_out11_',size=(7,1)),sg.Text('Kcal/hr 나누기 COP = '),sg.Text('',key='_out12_',size=(7,1))],
            [sg.Text('',key='_out13_',size=(7,1)),sg.Text('Mcal/hr 나누기 COP = '),sg.Text('',key='_out14_',size=(7,1)),sg.Text('1차측 중온수 유량 (m3/hr)=', text_color='yellow'),sg.Text('',key='_out15_',size=(7,1), text_color='white')],
            [sg.Text('냉동기 TCV 관경(Siemens) = ', text_color='yellow'),sg.Text('',key='_out16_',size=(7,1)),sg.Text('('),sg.Text('',key='_out16_v',size=(3,1)),sg.Text('% )'),sg.Text('냉동기 1차측배관경 = ', text_color='yellow'),sg.Text('',key='_out17_',size=(7,1)),sg.Text('('),sg.Text('',key='_out17_v',size=(3,1)),sg.Text('% )')], 
            [sg.Text('기계실 인입관경                = ', text_color='yellow'),sg.Text('',key='_out18_',size=(7,1)),sg.Text('('),sg.Text('',key='_out18_v',size=(3,1)),sg.Text('% )'),sg.Text('    열량계 관경         = ', text_color='yellow'),sg.Text('',key='_out19_',size=(7,1)),sg.Text('('),sg.Text('',key='_out19_v',size=(3,1)),sg.Text('% )')], 
            [sg.Text('냉수관경                           = ', text_color='yellow'),sg.Text('',key='_out20_',size=(7,1)),sg.Text('('),sg.Text('',key='_out20_v',size=(3,1)),sg.Text('% )'),sg.Text('    냉각수 관경         = ', text_color='yellow'),sg.Text('',key='_out21_',size=(7,1)),sg.Text('('),sg.Text('',key='_out21_v',size=(3,1)),sg.Text('% )')], 
            [sg.Button('ok',bind_return_key=True),sg.Button('cancel')]]

    window = sg.Window('냉동기(USRT) 입력',layout)
    # print("{:,}".format(int((int(values['-in-'])*3.024/5)*1000/60)))
# int(values['temp_in'])
    while True:
        event, values =window.read()
        if event == 'cancel' or event==sg.WIN_CLOSED:
            break
        
        
        if values['_in2_']: 
            window['_out_'].update(str("{:,}".format(int((int(values['-in-'])*3.024/int(values['temp_in']))*1000/60))))
            window['_out2_'].update(str("{:,}".format(int((int(values['-in-'])*3024/float(values['_in2_']) + int(values['-in-'])*3024)))))
            window['_out3_'].update(str("{:,}".format(int(((int(values['-in-'])*3.024/float(values['_in2_']) + int(values['-in-'])*3.024)/int(values['temp_in']))*1000/60))))
            window['_out4_'].update(str("{:,}".format(int((int(values['-in-'])*3.024/int(values['temp_in']))))))
            window['_out5_'].update(str("{:,}".format(int((int(values['-in-'])*3024/float(values['_in2_']) + int(values['-in-'])*3024)/3900))))
            window['_out6_'].update(str("{:,}".format(int((int(values['-in-'])*3.024/float(values['_in2_']) + int(values['-in-'])*3.024)/int(values['temp_in'])))))
            window['_out7_'].update(int(values['-in-'])) 
            window['_out8_'].update(str("{:,}".format(int(values['-in-'])*3024))) 
            window['_out9_'].update(str("{:,}".format(int(int(values['-in-'])*3.024)))) 
            window['_out10_'].update(str("{:,}".format(int(int(values['-in-'])*3.024/int(values['temp_in'])))))   
            window['_out11_'].update(str("{:,}".format(int(values['-in-'])*3024))) 
            window['_out12_'].update(str("{:,}".format(int(int(values['-in-'])*3024)/float(values['_in2_']))))
            window['_out13_'].update(str("{:,}".format(int(int(values['-in-'])*3.024)))) 
            window['_out14_'].update(str("{:,}".format(int(int(values['-in-'])*3.024/float(values['_in2_'])))))
            window['_out15_'].update(str("{:,}".format(int(int(values['-in-'])*3.024/float(values['_in2_'])/float(values['_in3_'])))))
            out16=float(float(float(values['-in-'])*3.024/float(values['_in2_'])/float(values['_in3_']))/sqrt(0.3))
            out17=float(float(values['-in-'])*3.024/float(values['_in2_']))
            out18=float(float(values['-in-'])*3.024/float(values['_in2_'])/float(values['_in3_']))
            out19=float(float(values['-in-'])*3.024/float(values['_in2_'])/float(values['_in3_']))
            out20=float((float(values['-in-'])*3.024/int(values['temp_in'])))
            out21=float((float(values['-in-'])*3.024/float(values['_in2_']) + int(values['-in-'])*3.024)/int(values['temp_in']))            
            if out16 > 8:
                window['_out16_'].update('25A')  
                window['_out16_v'].update(round(float((out16-8)/2)*100,1))          
            if out16 > 10:
                window['_out16_'].update('32A')
                window['_out16_v'].update(round(float((out16-10)/6)*100,1))
            if out16 > 16:
                window['_out16_'].update('40A')
                window['_out16_v'].update(round(float((out16-16)/9)*100,1))
            if out16 > 25:
                window['_out16_'].update('50A')
                window['_out16_v'].update(round(float((out16-25)/15)*100,1))
            if out16 > 40:
                window['_out16_'].update('65A')
                window['_out16_v'].update(round(float((out16-40)/23)*100,1))
            if out16 > 63:
                window['_out16_'].update('80A')
                window['_out16_v'].update(round(float((out16-63)/37)*100,1))
            if out16 > 100:
                window['_out16_'].update('100A')
                window['_out16_v'].update(round(float((out16-100)/60)*100,1))
            if out16 > 160:
                window['_out16_'].update('125A') 
                window['_out16_v'].update(round(float((out16-160)/90)*100,1))
            if out16 > 250:
                window['_out16_'].update('150A')              

               
            if out17 > 11.6:
                window['_out17_'].update('20A')     
                window['_out17_v'].update(round(float((out17-11.6)/14)*100,1)) 
            if out17 > 25.6:
                window['_out17_'].update('25A')
                window['_out17_v'].update(round(float((out17-25.6)/21.4)*100,1))
            if out17 > 47:
                window['_out17_'].update('32A')
                window['_out17_v'].update(round(float((out17-47)/49)*100,1))
            if out17 > 96:
                window['_out17_'].update('40A')
                window['_out17_v'].update(round(float((out17-96)/47)*100,1))
            if out17 > 143:
                window['_out17_'].update('50A')
                window['_out17_v'].update(round(float((out17-143)/132)*100,1))
            if out17 > 275:
                window['_out17_'].update('65A')
                window['_out17_v'].update(round(float((out17-275)/251)*100,1))
            if out17 > 526:
                window['_out17_'].update('80A')
                window['_out17_v'].update(round(float((out17-526)/307)*100,1))
            if out17 > 833:
                window['_out17_'].update('100A')
                window['_out17_v'].update(round(float((out17-833)/845)*100,1))
            if out17 > 1678:
                window['_out17_'].update('125A')
                window['_out17_v'].update(round(float((out17-1678)/1278)*100,1))
            if out17 > 2956:
                window['_out17_'].update('150A')
                window['_out17_v'].update(round(float((out17-2956)/1709)*100,1)) 
            if out17 > 4665:
                window['_out17_'].update('200A')
                window['_out17_v'].update(round(float((out17-4665)/4988)*100,1))               
            if out17 > 9653:
                window['_out17_'].update('250A')
                window['_out17_v'].update(round(float((out17-9653)/7698)*100,1))               
            if out17 > 17351:
                window['_out17_'].update('300A')
                window['_out17_v'].update(round(float((out17-17351)/10637)*100,1))               
            if out17 > 27988:
                window['_out17_'].update('350A')
                window['_out17_v'].update(round(float((out17-27988)/9760)*100,1))                               
            if out17 > 37748:
                window['_out17_'].update('400A')
                window['_out17_v'].update(round(float((out17-37748)/9760)*100,1))



            if out18 > 0.83:
                window['_out18_'].update('32A')  
                window['_out18_v'].update(round(float((out18-0.83)/0.85)*100,1))         
            if out18 > 1.68:
                window['_out18_'].update('40A')
                window['_out18_v'].update(round(float((out18-1.68)/0.82)*100,1))
            if out18 > 2.5:
                window['_out18_'].update('50A')
                window['_out18_v'].update(round(float((out18-2.5)/2.81)*100,1))
            if out18 > 4.81:
                window['_out18_'].update('65A')
                window['_out18_v'].update(round(float((out18-4.81)/4.4)*100,1))
            if out18 > 9.21:
                window['_out18_'].update('80A')
                window['_out18_v'].update(round(float((out18-9.21)/5.38)*100,1))
            if out18 > 14.59:
                window['_out18_'].update('100A')
                window['_out18_v'].update(round(float((out18-14.59)/14.85)*100,1))
            if out18 > 29.44:
                window['_out18_'].update('125A')
                window['_out18_v'].update(round(float((out18-29.44)/22.45)*100,1))
            if out18 > 51.89:
                window['_out18_'].update('150A')
                window['_out18_v'].update(round(float((out18-51.89)/30.06)*100,1))
            if out18 > 81.95:
                window['_out18_'].update('200A')
                window['_out18_v'].update(round(float((out18-81.95)/87.76)*100,1))
            if out18 > 169.71:
                window['_out18_'].update('250A')
                window['_out18_v'].update(round(float((out18-169.71)/135.49)*100,1)) 
            if out18 > 305.2:
                window['_out18_'].update('300A')
                window['_out18_v'].update(round(float((out18-305.2)/187.4)*100,1))               
            if out18 > 492.6:
                window['_out18_'].update('350A')
                window['_out18_v'].update(round(float((out18-492.6)/171.9)*100,1))               
            if out18 > 664.5:
                window['_out18_'].update('400A')
                window['_out18_v'].update(round(float((out18-664.5)/180)*100,1))               



            if out19 > 1.5:
                window['_out19_'].update('25A')
                window['_out19_v'].update(round(float((out19-1.5)/2)*100,1))            
            if out19 > 3.5:
                window['_out19_'].update('32A')
                window['_out19_v'].update(round(float((out19-3.5)/2.5)*100,1)) 
            if out19 > 6:
                window['_out19_'].update('40A')
                window['_out19_v'].update(round(float((out19-6)/4)*100,1))
            if out19 > 10:
                window['_out19_'].update('50A')
                window['_out19_v'].update(round(float((out19-10)/5)*100,1))
            if out19 > 15:
                window['_out19_'].update('65A')
                window['_out19_v'].update(round(float((out19-15)/10)*100,1))
            if out19 > 25:
                window['_out19_'].update('80A')
                window['_out19_v'].update(round(float((out19-25)/20)*100,1))
            if out19 > 45:
                window['_out19_'].update('100A')
                window['_out19_v'].update(round(float((out19-45)/35)*100,1))
            if out19 > 70:
                window['_out19_'].update('125A')
                window['_out19_v'].update(round(float((out19-70)/30)*100,1))
            if out19 > 100:
                window['_out19_'].update('150A')
                window['_out19_v'].update(round(float((out19-100)/50)*100,1))
            if out19 > 150:
                window['_out19_'].update('200A') 
                window['_out19_v'].update(round(float((out19-150)/100)*100,1))
            if out19 > 250:
                window['_out19_'].update('250A')               
                window['_out19_v'].update(round(float((out19-250)/250)*100,1))
            if out19 > 500:
                window['_out19_'].update('300A') 
                window['_out19_v'].update(round(float((out19-500)/300)*100,1))              



            if out20 > 0.33:
                window['_out20_'].update('20A')   
                window['_out20_v'].update(round(float((out20-0.33)/0.41)*100,1))         
            if out20 > 0.74:
                window['_out20_'].update('25A')
                window['_out20_v'].update(round(float((out20-0.74)/0.82)*100,1))
            if out20 > 1.56:
                window['_out20_'].update('32A')
                window['_out20_v'].update(round(float((out20-1.56)/1.67)*100,1))
            if out20 > 3.23:
                window['_out20_'].update('40A')
                window['_out20_v'].update(round(float((out20-3.23)/1.6)*100,1))
            if out20 > 4.83:
                window['_out20_'].update('50A')
                window['_out20_v'].update(round(float((out20-4.83)/4.51)*100,1))
            if out20 > 9.34:
                window['_out20_'].update('65A')
                window['_out20_v'].update(round(float((out20-9.34)/9.06)*100,1))
            if out20 > 18.4:
                window['_out20_'].update('80A')
                window['_out20_v'].update(round(float((out20-18.4)/10.4)*100,1))
            if out20 > 28.8:
                window['_out20_'].update('100A')
                window['_out20_v'].update(round(float((out20-28.8)/29.4)*100,1))
            if out20 > 58.2:
                window['_out20_'].update('125A')
                window['_out20_v'].update(round(float((out20-58.2)/43.8)*100,1))
            if out20 > 102.0:
                window['_out20_'].update('150A') 
                window['_out20_v'].update(round(float((out20-102.00)/59.6)*100,1))
            if out20 > 161.6:
                window['_out20_'].update('200A')               
                window['_out20_v'].update(round(float((out20-161.6)/175.8)*100,1))
            if out20 > 337.4:
                window['_out20_'].update('250A')               
                window['_out20_v'].update(round(float((out20-337.4)/261.6)*100,1))
            if out20 > 599.0:
                window['_out20_'].update('300A')           
                window['_out20_v'].update(round(float((out20-599)/360)*100,1))
            if out20 > 959:
                window['_out20_'].update('350A')                   
                window['_out20_v'].update(round(float((out20-959)/400)*100,1))



            if out21 > 0.36:
                window['_out21_'].update('20A')  
                window['_out21_v'].update(round(float((out21-0.36)/0.41)*100,1))           
            if out21 > 0.77:
                window['_out21_'].update('25A')
                window['_out21_v'].update(round(float((out21-0.77)/0.63)*100,1)) 
            if out21 > 1.40:
                window['_out21_'].update('32A')
                window['_out21_v'].update(round(float((out21-1.40)/1.49)*100,1)) 
            if out21 > 2.89:
                window['_out21_'].update('40A')
                window['_out21_v'].update(round(float((out21-2.89)/1.4)*100,1)) 
            if out21 > 4.29:
                window['_out21_'].update('50A')
                window['_out21_v'].update(round(float((out21-4.29)/3.62)*100,1)) 
            if out21 > 7.91:
                window['_out21_'].update('65A')
                window['_out21_v'].update(round(float((out21-7.91)/7.69)*100,1)) 
            if out21 > 15.6:
                window['_out21_'].update('80A')
                window['_out21_v'].update(round(float((out21-15.6)/8.1)*100,1)) 
            if out21 > 23.7:
                window['_out21_'].update('100A')
                window['_out21_v'].update(round(float((out21-23.7)/23.3)*100,1)) 
            if out21 > 47.0:
                window['_out21_'].update('125A')
                window['_out21_v'].update(round(float((out21-47)/34.5)*100,1)) 
            if out21 > 81.5:
                window['_out21_'].update('150A') 
                window['_out21_v'].update(round(float((out21-81.5)/48.1)*100,1)) 
            if out21 > 129.6:
                window['_out21_'].update('200A')               
                window['_out21_v'].update(round(float((out21-129.6)/135)*100,1)) 
            if out21 > 264.6:
                window['_out21_'].update('250A')               
                window['_out21_v'].update(round(float((out21-264.6)/202.3)*100,1)) 
            if out21 > 466.9:
                window['_out21_'].update('300A')               
                window['_out21_v'].update(round(float((out21-466.9)/276.1)*100,1)) 
            if out21 > 743:
                window['_out21_'].update('350A')      
                window['_out21_v'].update(round(float((out21-743)/300)*100,1)) 






        else:
            window['_out_'].update(str("{:,}".format(int((int(values['-in-'])*3.024/int(values['temp_in']))*1000/60))))
            window['_out2_'].update(str("{:,}".format(int((int(values['-in-'])*3024/float(values['_in2_']) + int(values['-in-'])*3024)))))
            window['_out3_'].update(str("{:,}".format(int(((int(values['-in-'])*3.024/float(values['_in2_']) + int(values['-in-'])*3.024)/int(values['temp_in']))*1000/60))))
            window['_out4_'].update(str("{:,}".format(int((int(values['-in-'])*3.024/int(values['temp_in']))))))
            window['_out5_'].update(str("{:,}".format(int((int(values['-in-'])*3024/float(values['_in2_']) + int(values['-in-'])*3024)/3900))))
            window['_out6_'].update(str("{:,}".format(int((int(values['-in-'])*3.024/float(values['_in2_']) + int(values['-in-'])*3.024)/int(values['temp_in']))))) 
            window['_out7_'].update(int(values['-in-'])) 
            window['_out8_'].update(str("{:,}".format(int(values['-in-'])*3024))) 
            window['_out9_'].update(str("{:,}".format(int(int(values['-in-'])*3.024)))) 
            window['_out10_'].update(str("{:,}".format(int(int(values['-in-'])*3.024/int(values['temp_in'])))))         
            window['_out11_'].update(str("{:,}".format(int(values['-in-'])*3024))) 
            window['_out12_'].update(str("{:,}".format(int(int(values['-in-'])*3024)/float(values['_in2_']))))
            window['_out13_'].update(str("{:,}".format(int(int(values['-in-'])*3.024)))) 
            window['_out14_'].update(str("{:,}".format(int(int(values['-in-'])*3.024/float(values['_in2_']))))) 
            window['_out15_'].update(str("{:,}".format(int(int(values['-in-'])*3.024/float(values['_in2_'])/float(values['_in3_'])))))
            out16=float(float(float(values['-in-'])*3.024/float(values['_in2_'])/float(values['_in3_']))/sqrt(0.3))
            out17=float(float(values['-in-'])*3.024/float(values['_in2_']))
            out18=float(float(values['-in-'])*3.024/float(values['_in2_'])/float(values['_in3_']))
            out19=float(float(values['-in-'])*3.024/float(values['_in2_'])/float(values['_in3_']))
            out20=float((float(values['-in-'])*3.024/int(values['temp_in'])))
            out21=float((float(values['-in-'])*3.024/float(values['_in2_']) + int(values['-in-'])*3.024)/int(values['temp_in']))


            if out16 > 8:
                window['_out16_'].update('25A')  
                window['_out16_v'].update(round(float((out16-8)/2)*100,1))          
            if out16 > 10:
                window['_out16_'].update('32A')
                window['_out16_v'].update(round(float((out16-10)/6)*100,1))
            if out16 > 16:
                window['_out16_'].update('40A')
                window['_out16_v'].update(round(float((out16-16)/9)*100,1))
            if out16 > 25:
                window['_out16_'].update('50A')
                window['_out16_v'].update(round(float((out16-25)/15)*100,1))
            if out16 > 40:
                window['_out16_'].update('65A')
                window['_out16_v'].update(round(float((out16-40)/23)*100,1))
            if out16 > 63:
                window['_out16_'].update('80A')
                window['_out16_v'].update(round(float((out16-63)/37)*100,1))
            if out16 > 100:
                window['_out16_'].update('100A')
                window['_out16_v'].update(round(float((out16-100)/60)*100,1))
            if out16 > 160:
                window['_out16_'].update('125A') 
                window['_out16_v'].update(round(float((out16-160)/90)*100,1))
            if out16 > 250:
                window['_out16_'].update('150A')              

            if out17 > 11.6:
                window['_out17_'].update('20A')     
                window['_out17_v'].update(round(float((out17-11.6)/14)*100,1)) 
            if out17 > 25.6:
                window['_out17_'].update('25A')
                window['_out17_v'].update(round(float((out17-25.6)/21.4)*100,1))
            if out17 > 47:
                window['_out17_'].update('32A')
                window['_out17_v'].update(round(float((out17-47)/49)*100,1))
            if out17 > 96:
                window['_out17_'].update('40A')
                window['_out17_v'].update(round(float((out17-96)/47)*100,1))
            if out17 > 143:
                window['_out17_'].update('50A')
                window['_out17_v'].update(round(float((out17-143)/132)*100,1))
            if out17 > 275:
                window['_out17_'].update('65A')
                window['_out17_v'].update(round(float((out17-275)/251)*100,1))
            if out17 > 526:
                window['_out17_'].update('80A')
                window['_out17_v'].update(round(float((out17-526)/307)*100,1))
            if out17 > 833:
                window['_out17_'].update('100A')
                window['_out17_v'].update(round(float((out17-833)/845)*100,1))
            if out17 > 1678:
                window['_out17_'].update('125A')
                window['_out17_v'].update(round(float((out17-1678)/1278)*100,1))
            if out17 > 2956:
                window['_out17_'].update('150A')
                window['_out17_v'].update(round(float((out17-2956)/1709)*100,1)) 
            if out17 > 4665:
                window['_out17_'].update('200A')
                window['_out17_v'].update(round(float((out17-4665)/4988)*100,1))               
            if out17 > 9653:
                window['_out17_'].update('250A')
                window['_out17_v'].update(round(float((out17-9653)/7698)*100,1))               
            if out17 > 17351:
                window['_out17_'].update('300A')
                window['_out17_v'].update(round(float((out17-17351)/10637)*100,1))               
            if out17 > 27988:
                window['_out17_'].update('350A')
                window['_out17_v'].update(round(float((out17-27988)/9760)*100,1))                               
            if out17 > 37748:
                window['_out17_'].update('400A')
                window['_out17_v'].update(round(float((out17-37748)/9760)*100,1))                       

            if out18 > 0.83:
                window['_out18_'].update('32A')  
                window['_out18_v'].update(round(float((out18-0.83)/0.85)*100,1))         
            if out18 > 1.68:
                window['_out18_'].update('40A')
                window['_out18_v'].update(round(float((out18-1.68)/0.82)*100,1))
            if out18 > 2.5:
                window['_out18_'].update('50A')
                window['_out18_v'].update(round(float((out18-2.5)/2.81)*100,1))
            if out18 > 4.81:
                window['_out18_'].update('65A')
                window['_out18_v'].update(round(float((out18-4.81)/4.4)*100,1))
            if out18 > 9.21:
                window['_out18_'].update('80A')
                window['_out18_v'].update(round(float((out18-9.21)/5.38)*100,1))
            if out18 > 14.59:
                window['_out18_'].update('100A')
                window['_out18_v'].update(round(float((out18-14.59)/14.85)*100,1))
            if out18 > 29.44:
                window['_out18_'].update('125A')
                window['_out18_v'].update(round(float((out18-29.44)/22.45)*100,1))
            if out18 > 51.89:
                window['_out18_'].update('150A')
                window['_out18_v'].update(round(float((out18-51.89)/30.06)*100,1))
            if out18 > 81.95:
                window['_out18_'].update('200A')
                window['_out18_v'].update(round(float((out18-81.95)/87.76)*100,1))
            if out18 > 169.71:
                window['_out18_'].update('250A')
                window['_out18_v'].update(round(float((out18-169.71)/135.49)*100,1)) 
            if out18 > 305.2:
                window['_out18_'].update('300A')
                window['_out18_v'].update(round(float((out18-305.2)/187.4)*100,1))               
            if out18 > 492.6:
                window['_out18_'].update('350A')
                window['_out18_v'].update(round(float((out18-492.6)/171.9)*100,1))               
            if out18 > 664.5:
                window['_out18_'].update('400A')
                window['_out18_v'].update(round(float((out18-664.5)/180)*100,1))    



            if out19 > 1.5:
                window['_out19_'].update('25A')
                window['_out19_v'].update(round(float((out19-1.5)/2)*100,1))            
            if out19 > 3.5:
                window['_out19_'].update('32A')
                window['_out19_v'].update(round(float((out19-3.5)/2.5)*100,1)) 
            if out19 > 6:
                window['_out19_'].update('40A')
                window['_out19_v'].update(round(float((out19-6)/4)*100,1))
            if out19 > 10:
                window['_out19_'].update('50A')
                window['_out19_v'].update(round(float((out19-10)/5)*100,1))
            if out19 > 15:
                window['_out19_'].update('65A')
                window['_out19_v'].update(round(float((out19-15)/10)*100,1))
            if out19 > 25:
                window['_out19_'].update('80A')
                window['_out19_v'].update(round(float((out19-25)/20)*100,1))
            if out19 > 45:
                window['_out19_'].update('100A')
                window['_out19_v'].update(round(float((out19-45)/35)*100,1))
            if out19 > 70:
                window['_out19_'].update('125A')
                window['_out19_v'].update(round(float((out19-70)/30)*100,1))
            if out19 > 100:
                window['_out19_'].update('150A')
                window['_out19_v'].update(round(float((out19-100)/50)*100,1))
            if out19 > 150:
                window['_out19_'].update('200A') 
                window['_out19_v'].update(round(float((out19-150)/100)*100,1))
            if out19 > 250:
                window['_out19_'].update('250A')               
                window['_out19_v'].update(round(float((out19-250)/250)*100,1))
            if out19 > 500:
                window['_out19_'].update('300A') 
                window['_out19_v'].update(round(float((out19-500)/300)*100,1))              
     



            if out20 > 0.33:
                window['_out20_'].update('20A')   
                window['_out20_v'].update(round(float((out20-0.33)/0.41)*100,1))         
            if out20 > 0.74:
                window['_out20_'].update('25A')
                window['_out20_v'].update(round(float((out20-0.74)/0.82)*100,1))
            if out20 > 1.56:
                window['_out20_'].update('32A')
                window['_out20_v'].update(round(float((out20-1.56)/1.67)*100,1))
            if out20 > 3.23:
                window['_out20_'].update('40A')
                window['_out20_v'].update(round(float((out20-3.23)/1.6)*100,1))
            if out20 > 4.83:
                window['_out20_'].update('50A')
                window['_out20_v'].update(round(float((out20-4.83)/4.51)*100,1))
            if out20 > 9.34:
                window['_out20_'].update('65A')
                window['_out20_v'].update(round(float((out20-9.34)/9.06)*100,1))
            if out20 > 18.4:
                window['_out20_'].update('80A')
                window['_out20_v'].update(round(float((out20-18.4)/10.4)*100,1))
            if out20 > 28.8:
                window['_out20_'].update('100A')
                window['_out20_v'].update(round(float((out20-28.8)/29.4)*100,1))
            if out20 > 58.2:
                window['_out20_'].update('125A')
                window['_out20_v'].update(round(float((out20-58.2)/43.8)*100,1))
            if out20 > 102.0:
                window['_out20_'].update('150A') 
                window['_out20_v'].update(round(float((out20-102.00)/59.6)*100,1))
            if out20 > 161.6:
                window['_out20_'].update('200A')               
                window['_out20_v'].update(round(float((out20-161.6)/175.8)*100,1))
            if out20 > 337.4:
                window['_out20_'].update('250A')               
                window['_out20_v'].update(round(float((out20-337.4)/261.6)*100,1))
            if out20 > 599.0:
                window['_out20_'].update('300A')           
                window['_out20_v'].update(round(float((out20-599)/360)*100,1))
            if out20 > 959:
                window['_out20_'].update('350A')                   
                window['_out20_v'].update(round(float((out20-959)/400)*100,1))
               


            if out21 > 0.36:
                window['_out21_'].update('20A')  
                window['_out21_v'].update(round(float((out21-0.36)/0.41)*100,1))           
            if out21 > 0.77:
                window['_out21_'].update('25A')
                window['_out21_v'].update(round(float((out21-0.77)/0.63)*100,1)) 
            if out21 > 1.40:
                window['_out21_'].update('32A')
                window['_out21_v'].update(round(float((out21-1.40)/1.49)*100,1)) 
            if out21 > 2.89:
                window['_out21_'].update('40A')
                window['_out21_v'].update(round(float((out21-2.89)/1.4)*100,1)) 
            if out21 > 4.29:
                window['_out21_'].update('50A')
                window['_out21_v'].update(round(float((out21-4.29)/3.62)*100,1)) 
            if out21 > 7.91:
                window['_out21_'].update('65A')
                window['_out21_v'].update(round(float((out21-7.91)/7.69)*100,1)) 
            if out21 > 15.6:
                window['_out21_'].update('80A')
                window['_out21_v'].update(round(float((out21-15.6)/8.1)*100,1)) 
            if out21 > 23.7:
                window['_out21_'].update('100A')
                window['_out21_v'].update(round(float((out21-23.7)/23.3)*100,1)) 
            if out21 > 47.0:
                window['_out21_'].update('125A')
                window['_out21_v'].update(round(float((out21-47)/34.5)*100,1)) 
            if out21 > 81.5:
                window['_out21_'].update('150A') 
                window['_out21_v'].update(round(float((out21-81.5)/48.1)*100,1)) 
            if out21 > 129.6:
                window['_out21_'].update('200A')               
                window['_out21_v'].update(round(float((out21-129.6)/135)*100,1)) 
            if out21 > 264.6:
                window['_out21_'].update('250A')               
                window['_out21_v'].update(round(float((out21-264.6)/202.3)*100,1)) 
            if out21 > 466.9:
                window['_out21_'].update('300A')               
                window['_out21_v'].update(round(float((out21-466.9)/276.1)*100,1)) 
            if out21 > 743:
                window['_out21_'].update('350A')      
                window['_out21_v'].update(round(float((out21-743)/300)*100,1)) 

   
    window.close()

#------------------------------------------------------------------------------------------------
def our_copy():
    view_command5()
    # print(f.get('1.0',END))
    # root2.destroy()
    pass
def our_save():
    with open('test1.txt','a') as wf:
        now = time.localtime()
        wf.write("%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)+"\n")
        # wf.write("{}/{} {}:{}".format(now.month,now.day,now.hour,now.minute)+"\n")
        for line in f.get('1.0',END):
            wf.write(line)
    f.delete('1.0',END)
    # print("%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)+"\n")

button_all = Button(root,text="new",font= ("NanumGothicBold","9"),width=6,height=1,borderwidth=3,cursor="watch", command= our_new).grid(row=13,sticky=E,column=4,padx=3,pady=3)



def our_exit():
    root.quit()
my_menu = Menu(root)
root.config(menu=my_menu)

file_menu= Menu(my_menu)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="new",command=our_new)
file_menu.add_separator()
file_menu.add_command(label="save to test1.txt",command=our_save)
file_menu.add_command(label="exit",command=our_exit)

edit_menu=Menu(my_menu)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="안양 사용자(uuser.db)",command=our_copy)
edit_menu.add_command(label="대수평균온도차",command=our_lmtd)
edit_menu.add_command(label="난방 DPV_관경선정",command=our_dpv)
edit_menu.add_command(label="냉동기 USRT",command=simple)
edit_menu.add_command(label="계산기(나열식)",command=ourour_cal)
edit_menu.add_command(label="연결열부하 DB",command=lambda : view_command1(1))
edit_menu.add_command(label="난방 HX용량 DB",command=lambda : view_command2(1))
edit_menu.add_command(label="급탕 HX용량 DB",command=lambda : view_command3(1))

center_window(868,593)
mat = False
f_num=""
ex1=0




frame1 = LabelFrame(root, text="연결열부하")
frame1.grid(row=0,column=4,rowspan=3)
frame2 = LabelFrame(root, text = "난방HX 용량")
frame2.grid(row=2,column=4,rowspan=4)
frame3 = LabelFrame(root, text = "급탕HX 용량")
frame3.grid(row=5,column=4,rowspan=4)
frame4 = LabelFrame(root, text = "세대수")
frame4.grid(row=9,column=4,rowspan=3)

f_1 =Label(frame1, text="인입관경   ")
f_1.grid(row=1,column=0,padx=10 ,pady=3)
f_2=Label(frame1, text="  PDCV 관경  ")
f_2.grid(row=2,column=0,padx=10 ,pady=3)
f_3 =Label(frame1, text="열량계 관경")
f_3.grid(row=3,column=0,padx=10 ,pady=3)

gg0= Entry(frame1,width=10,justify='right')
gg0.grid(row=0,column=0)
gg00=Label(frame1,text="Mcal/h").grid(row=0,column=1)
gg1 =Entry(frame1,width=12)
gg1.grid(row=1,column=1)
gg2 =Entry(frame1,width=12)
gg2.grid(row=2,column=1)
gg3 =Entry(frame1,width=12)
gg3.grid(row=3,column=1)


g_1 =Label(frame2, text="난방PP LPM")
g_1.grid(row=1,column=0,padx=10 ,pady=3)
g_2=Label(frame2, text="1차 난방관경")
g_2.grid(row=2,column=0,padx=10 ,pady=3)
g_3 =Label(frame2, text="2차 난방관경")
g_3.grid(row=3,column=0,padx=10 ,pady=3)
g_4 =Label(frame2, text="팽창탱크 Lit")
g_4.grid(row=4,column=0,padx=10 ,pady=3)
g_5=Label(frame2, text="난방TCV 관경")
g_5.grid(row=5,column=0,padx=10 ,pady=3)


ggg0= Entry(frame2,width=10,justify='right')
ggg0.grid(row=0,column=0)
ggg00=Label(frame2,text="Mcal/h").grid(row=0,column=1)
ggg1=Entry(frame2,width=12)
ggg1.grid(row=1,column=1)
ggg2=Entry(frame2,width=12)
ggg2.grid(row=2,column=1)
ggg3=Entry(frame2,width=12)
ggg3.grid(row=3,column=1)
ggg4=Entry(frame2,width=12)
ggg4.grid(row=4,column=1)
ggg5=Entry(frame2,width=12)
ggg5.grid(row=5,column=1)

h_1 =Label(frame3, text="급탕PP LPM")
h_1.grid(row=1,column=0,padx=10 ,pady=3)
h_2=Label(frame3, text="1차 재열관경")
h_2.grid(row=2,column=0,padx=10 ,pady=3)
h_3 =Label(frame3, text="2차 급탕관경")
h_3.grid(row=3,column=0,padx=10 ,pady=3)
h_4 =Label(frame3, text="급탕TCV 관경")
h_4.grid(row=4,column=0,padx=10 ,pady=3)

gggg0= Entry(frame3,width=10,justify='right')
gggg0.grid(row=0,column=0)
gggg00=Label(frame3,text="Mcal/h").grid(row=0,column=1)
gggg1=Entry(frame3,width=12)
gggg1.grid(row=1,column=1)
gggg2=Entry(frame3,width=12)
gggg2.grid(row=2,column=1)
gggg3=Entry(frame3,width=12)
gggg3.grid(row=3,column=1)
gggg4=Entry(frame3,width=12)
gggg4.grid(row=4,column=1)

i_1 =Label(frame4, text="_   ΔT40℃   _")
i_1.grid(row=1,column=0,padx=10 ,pady=3)
i_2=Label(frame4, text="_   ΔT50℃   _")
i_2.grid(row=2,column=0,padx=10 ,pady=3)
i_3 =Label(frame4, text="3n, ΔT40℃")
i_3.grid(row=3,column=0,padx=10 ,pady=3)

ggggg0 = Entry(frame4,width=10,justify='right')
ggggg0.grid(row=0,column=0)
ggggg00 =Label(frame4,text="세대").grid(row=0,column=1)

ggggg1=Entry(frame4,width=12)
ggggg1.grid(row=1,column=1)
ggggg2= Entry(frame4,width=12)
ggggg2.grid(row=2,column=1)
ggggg3= Entry(frame4,width=12)
ggggg3.grid(row=3,column=1)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

f2 = Text(root, width=39,height=39, font= ("NanumGothicBold","12"), borderwidth=3) 
e = Entry(root, width=30, font= ("NanumGothicBold","12"), borderwidth=14, justify='right')
f = Text(root, width=39,height=39, font= ("NanumGothicBold","12"), borderwidth=3)
e.grid(row=0, column=0, columnspan=3)
f.grid(row=0, column=5, columnspan=3, rowspan=20)

#////--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def button_click(number):
    global ex1
    myLabel21.focus() 
    if ex1==1:
        e.delete(0,END)
        e.insert(0,str(number))
        ex1=0
    else:
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))
        
# def button2_click(number):
#     global eex1
     
#     if eex1==1:
#         e2.delete(0,END)
#         e2.insert(0,str(number))
#         eex1=0
#     else:
#         current = e2.get()
#         e2.delete(0, END)
#         e2.insert(0, str(current) + str(number))

def button_press(numb):
    
    if numb.keysym == "Delete":
        current = e.get()
        e.delete(len(current)-1,len(current))

    if numb.keysym == "1" or numb.keysym == "2" or numb.keysym == "3" or numb.keysym == "4" or numb.keysym == "5" or numb.keysym == "6" or numb.keysym == "7" or numb.keysym == "8"or numb.keysym == "9" or numb.keysym == "0":
        numb=numb.char 
    else:
        return    
    global ex1
    if ex1==1:
        e.delete(0,END)
        e.insert(0,str(numb))
        ex1=0
    else:
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(numb))


root.bind('<Key>', button_press)


def button_clear():
    global f_num
    global mat
    f_num = 0
    f.delete('1.0',END)
    e.delete(0, END)



def button_our():
    global ex1
    ex1=1
    our = e.get()
    kkcal=0
    # global f_num    
    f_num =int((36 + 9*sqrt(4*int(our)-2))*0.8*60*40/1000)
    f_num2=int((36 + 9*sqrt(3*int(our)-2))*0.8*60*40/1000)
    kkcal = round(((f_num2/f_num)*100),2)
    e.delete(0,END)
    e.insert(0 , our)
    e.insert(our, str("세대→ "))
    e.insert(our,f_num)
    e.insert(f_num, str(" Mcal/hr(ΔT40℃)"))
    hh=e.get()
    f.insert(tk.INSERT,hh+"\n"+"\n")
    e.delete(0,END)
    e.insert(0,our)
    mat = True
    # print (pd1[0])
    ggggg0.delete(0,END)
    ggggg0.insert(0,our)
    ggggg1.delete(0,END)
    ggggg1.insert(0,f_num)
    ggggg1.insert(our,str(" Mcal/h"))
    ggggg2.delete(0,END)
    ggggg2.insert(0,int(f_num*5/4))
    ggggg2.insert(our,str(" Mcal/h"))
    ggggg3.delete(0,END)
    ggggg3.insert(0,kkcal)
    ggggg3.insert(our,str(" %"))
    return

def button_our2():
    global ex1
    ex1=1
    our = e.get()
    global mat
    global f_num    
    f_num =int((36 + 9*sqrt(4*int(our)-2))*0.8*60*50/1000)
    f_num1 =int((36 + 9*sqrt(4*int(our)-2))*0.8*60*40/1000)
    f_num2=int((36 + 9*sqrt(3*int(our)-2))*0.8*60*40/1000)
    kkcal = round(((f_num2/f_num1)*100),2)
    e.delete(0,END)
    e.insert(0 , our)
    e.insert(our, str("세대→ "))
    e.insert(our,f_num)
    e.insert(f_num, str(" Mcal/hr(ΔT50℃)"))
    hh=e.get()
    f.insert(tk.INSERT,hh+"\n"+"\n")
    e.delete(0,END)
    e.insert(0,our)
    ggggg0.delete(0,END)
    ggggg0.insert(0,our)
    ggggg1.delete(0,END)
    ggggg1.insert(0,int(f_num*4/5))
    ggggg1.insert(our,str(" Mcal/h"))
    ggggg2.delete(0,END)
    ggggg2.insert(0,f_num)
    ggggg2.insert(our,str(" Mcal/h"))
    ggggg3.delete(0,END)
    ggggg3.insert(0,kkcal)
    ggggg3.insert(our,str(" %"))
    mat = True
    return




def button_exe1():
    myLabel21.focus()
    global ex1
    ex1=1
    init=""
    our = e.get()

    if int(our) < 95:
       return
      
    e.delete(0,END)
    e.insert(0,str("**연결열부하**"))
    e.insert(our,our)
    e.insert(our," Mcal/hr인 경우")
    hh=e.get()
    f.insert(tk.INSERT,hh+"\n")
    

    #--------------------------------------기계실인입배관 관경별 기준표상에 95%에 육박시 관경하나 더 크게함------------
    if int(our) > 19839:
        init="300 A"
        initloc=300
    elif int(our) > int((19839-11031)*float(afccc)+11031):
        init="300 A+"
        initloc=300
        initper=float(((int(our)-11031)/(19839-11031))*100)
    elif int(our) > 11031:
        init="250 A"
        initloc=250
        initper=float(((int(our)-11031)/(19839-11031))*100)
    elif int(our) > int((11031-5326)*float(afccc)+5326):
        init="250 A+"
        initloc=250
        initper=float(((int(our)-5326)/(11031-5326))*100)
    elif int(our) > 5326:
        init="200 A"
        initloc=200
        initper=float(((int(our)-5326)/(11031-5326))*100)
    elif int(our) > int((5326-3373)*float(afccc)+3373):
        init="200 A+"
        initloc=200
        initper=float(((int(our)-3373)/(5326-3373))*100)    
    elif int(our) > 3373:
        init="150 A"
        initloc=150
        initper=float(((int(our)-3373)/(5326-3373))*100)
    elif int(our) > int((3373-1913)*float(afccc)+1913):
        init="150 A+"
        initloc=150
        initper=float(((int(our)-1913)/(3373-1913))*100)
    elif int(our) > 1913:
        init="125 A"
        initloc=125
        initper=float(((int(our)-1913)/(3373-1913))*100)
    elif int(our) > int((1913-949)*float(afccc)+949):
        init="125 A+"
        initloc=125
        initper=float(((int(our)-949)/(1913-949))*100)
    elif int(our) > 949:
        init="100 A"
        initloc=100 
        initper=float(((int(our)-949)/(1913-949))*100) 
    elif int(our) > int((949-598)*float(afccc)+598):
        init="100 A+"
        initloc=100 
        initper=float(((int(our)-598)/(949-598))*100)  
    elif int(our) > 598:
        init="80 A"
        initloc=80
        initper=float(((int(our)-598)/(949-598))*100) 
    elif int(our) > int((598-313)*float(afccc)+313):
        init="80 A+"
        initloc=80  
        initper=float(((int(our)-313)/(598-313))*100)   
    elif int(our) > 313:
        init="65 A"
        initloc=65
        initper=float(((int(our)-313)/(598-313))*100)
    elif int(our) > int((313-163)*float(afccc)+163):
        init="65 A+"
        initloc=65 
        initper=float(((int(our)-163)/(313-163))*100)   
    elif int(our) > 163:
        init="50 A"
        initloc=50
        initper=float(((int(our)-163)/(313-163))*100) 
    elif int(our) > int((163-109)*float(afccc)+109):
        init="50 A+"
        initloc=50
        initper=float(((int(our)-109)/(163-109))*100) 
    elif int(our) > 109:
        init="40 A"
        initloc=40
        initper=float(((int(our)-109)/(163-109))*100)
    elif int(our) > int((109-54)*float(afccc)+54):
        init="40 A+"
        initloc=40
        initper=float(((int(our)-54)/(109-54))*100)
    elif int(our) > 54:
        init="32 A"
        initloc=32
        initper=float(((int(our)-54)/(109-54))*100)
    elif int(our) > int((54-1)*float(afccc)+1):
        init="32 A+"
        initloc=32
        initper=float(((int(our)-1)/(54-1))*100)
    elif int(our) > 1:
        init="25 A"
        initloc=25   
        initper=float(((int(our)-1)/(54-1))*100)                    
    f_num = int((int(our)/65/sqrt(0.7))*1.167)
    e.delete(0,END)
    e.insert(0 , str("인입관경"))
    e.insert(our, str("   → "))
    e.insert(our,init)
    e.insert(our,"("+str(round(initper,2))+"%)")


    gg0.delete(0,END)
    gg0.insert(0,our)
    gg1.delete(0,END)
    gg1.insert(0,init+" ("+str(round(initper,1))+"%)")
     
    hh=e.get()
    f.insert(tk.INSERT,hh+"\n")

    pdc=""
    veloc=""
    if f_num > pd1[0]:
        pdc="300 A"
        veloc=300
    elif f_num > pd1[1]:
        pdc="250 A"
        veloc=250
    elif f_num > pd1[2]:
        pdc="200 A"
        veloc=200    
    elif f_num > pd1[3]:
        pdc="150 A"
        veloc=150
    elif f_num > pd1[4]:
        pdc="125 A"
        veloc=125
    elif f_num > pd1[5]:
        pdc="100 A"
        veloc=100    
    elif f_num > pd1[6]:
        pdc="80 A"
        veloc=80    
    elif f_num > pd1[7]:
        pdc="65 A"
        veloc=65    
    elif f_num > pd1[8]:
        pdc="50 A"
        veloc=50
    elif f_num > pd1[9]:
        pdc="40 A"
        veloc=40
    elif f_num > pd1[10]:
        pdc="32 A"
        veloc=32
    elif f_num > pd1[11]:
        pdc="25 A"
        veloc=25     
    elif f_num > 1:
        pdc="20 A"
        veloc=20 

# --입입관경보다 PDCV관경이 두단계 이상 아래일 경우, PDCV관경을 인입배관경의 두단계아래로 배관경 상승--------------------------------------------------------------------------------------------------
    if initloc == 300 and veloc < 199:
        pdc="200 A+" 
    if initloc == 250 and veloc < 149:
        pdc="150 A+" 
    if initloc == 200 and veloc < 124:
        pdc="125 A+" 
    if initloc == 150 and veloc < 99:
        pdc="100 A+" 
    if initloc == 125 and veloc < 79:
        pdc="80 A+" 
    if initloc == 100 and veloc < 64:
        pdc="65 A+" 
    if initloc == 80 and veloc < 49:
        pdc="50 A+" 
    if initloc == 65 and veloc < 39:
        pdc="40 A+" 
    if initloc == 50 and veloc < 31:
        pdc="32 A+" 
    if initloc == 40 and veloc < 24:
        pdc="25 A+" 
    if initloc == 32 and veloc < 19:
        pdc="20 A" 


# ----------------------------------------------------------------------------------------------------
    e.delete(0,END)
    e.insert(0 , str("PDCV관경"))
    e.insert(our, str(" → "))
    e.insert(our,pdc)
    e.insert(our,"("+checked1.get()+")")
    hh=e.get()
    f.insert(tk.INSERT,hh+"\n")
    
    gg0.delete(0,END)
    gg0.insert(0,our)
    gg2.delete(0,END)
    gg2.insert(0,pdc)

    velo=0
    velo=round(int(our)*4/(3.14*veloc*veloc*0.000001*3600)/65,2)
    e.delete(0,END)
    e.insert(0 , str("PDCV유속"))
    e.insert(our, str("→ "))
    e.insert(our,velo)
    e.insert(our,str("m/s"))
    e.insert(our,str("(↓6m/s권장)"))
    hh=e.get()
    f.insert(tk.INSERT,hh+"\n")

# -----------------------------------------------------------------------   

    velocv=0
    velocv=round(float((int(our)/65/sqrt(0.7))*1.167),1)
    e.delete(0,END)
    e.insert(0 , str("CV값(PDCV)"))
    # e.insert(our,"("+checked1.get()+")")
    e.insert(our, str("→ "))
    e.insert(our,velocv)
    # e.insert(our,str("m/s"))
    # e.insert(our,str("(↓6m/s권장)"))
    hh=e.get()
    f.insert(tk.INSERT,hh+"\n")

   
#--------------------------------------------------------------------------
    flow=""
    
    if int(our) > pd2[0]:
        flow="300 A"
    elif int(our) > int((pd2[0]-pd2[1])*float(afccc)+pd2[1]):
        flow="300 A+"
        flowper=float(((int(our)-pd2[1])/(pd2[0]-pd2[1]))*100)
    elif int(our) > pd2[1]:
        flow="250 A"
        flowper=float(((int(our)-pd2[1])/(pd2[0]-pd2[1]))*100)
    elif int(our) > int((pd2[1]-pd2[2])*float(afccc)+pd2[2]):
        flow="250 A+"
        flowper=float(((int(our)-pd2[2])/(pd2[1]-pd2[2]))*100)
    elif int(our) > pd2[2]:
        flow="200 A"
        flowper=float(((int(our)-pd2[2])/(pd2[1]-pd2[2]))*100)
    elif int(our) > int((pd2[2]-pd2[3])*float(afccc)+pd2[3]):
        flow="200 A+" 
        flowper=float(((int(our)-pd2[3])/(pd2[2]-pd2[3]))*100)   
    elif int(our) > pd2[3] :
        flow="150 A"
        flowper=float(((int(our)-pd2[3])/(pd2[2]-pd2[3]))*100) 
    elif int(our) > int((pd2[3]-pd2[4])*float(afccc)+pd2[4]):
        flow="150 A+" 
        flowper=float(((int(our)-pd2[4])/(pd2[3]-pd2[4]))*100) 
    elif int(our) > pd2[4] :
        flow="125 A"
        flowper=float(((int(our)-pd2[4])/(pd2[3]-pd2[4]))*100)
    elif int(our) > int((pd2[4]-pd2[5])*float(afccc)+pd2[5]):
        flow="125 A+"
        flowper=float(((int(our)-pd2[5])/(pd2[4]-pd2[5]))*100) 
    elif int(our) > pd2[5] :
        flow="100 A" 
        flowper=float(((int(our)-pd2[5])/(pd2[4]-pd2[5]))*100)   
    elif int(our) > int((pd2[5]-pd2[6])*float(afccc)+pd2[6]):
        flow="100 A+" 
        flowper=float(((int(our)-pd2[6])/(pd2[5]-pd2[6]))*100)  
    elif int(our) > pd2[6] :
        flow="80 A"  
        flowper=float(((int(our)-pd2[6])/(pd2[5]-pd2[6]))*100)  
    elif int(our) > int((pd2[6]-pd2[7])*float(afccc)+pd2[7]):
        flow="80 A+" 
        flowper=float(((int(our)-pd2[7])/(pd2[6]-pd2[7]))*100) 
    elif int(our) > pd2[7] :
        flow="65 A" 
        flowper=float(((int(our)-pd2[7])/(pd2[6]-pd2[7]))*100)   
    elif int(our) > int((pd2[7]-pd2[8])*float(afccc)+pd2[8]):
        flow="65 A+" 
        flowper=float(((int(our)-pd2[8])/(pd2[7]-pd2[8]))*100) 
    elif int(our) > pd2[8] :
        flow="50 A"
        flowper=float(((int(our)-pd2[8])/(pd2[7]-pd2[8]))*100)
    elif int(our) > int((pd2[8]-pd2[9])*float(afccc)+pd2[9]):
        flow="50 A+"
        flowper=float(((int(our)-pd2[9])/(pd2[8]-pd2[9]))*100)  
    elif int(our) > pd2[9] :
        flow="40 A"
        flowper=float(((int(our)-pd2[9])/(pd2[8]-pd2[9]))*100) 
    elif int(our) > int((pd2[9]-pd2[10])*float(afccc)+pd2[10]):
        flow="40 A+" 
        flowper=float(((int(our)-pd2[10])/(pd2[9]-pd2[10]))*100)  
    elif int(our) > pd2[10] :
        flow="32 A"
        flowper=float(((int(our)-pd2[10])/(pd2[9]-pd2[10]))*100)
    elif int(our) > int((pd2[10]-pd2[11])*float(afccc)+pd2[11]):
        flow="32 A+" 
        flowper=float(((int(our)-pd2[11])/(pd2[10]-pd2[11]))*100) 
    elif int(our) > pd2[11] :
        flow="25 A" 
        flowper=float(((int(our)-pd2[11])/(pd2[10]-pd2[11]))*100)    
    elif int(our) > int((pd2[11]-pd2[12])*float(afccc)+pd2[12]):
        flow="25 A+" 
        flowper=float(((int(our)-pd2[12])/(pd2[11]-pd2[12]))*100)  
    elif int(our) > 10:
        flow="20 A"        
    e.delete(0,END)
    e.insert(0 , str("열량계관경"))
    e.insert(our, str("→ "))
    e.insert(our,flow)
    e.insert(our,"("+checked2.get()+")")
    e.insert(our,"("+str(round(flowper,2))+"%)")  
    hh=e.get()
    f.insert(tk.INSERT,hh+"\n"+"\n")
#--------------------------------------------------------------

    # flow=""
    # if int(our) > pd2[0]:
    #     flow="300 A"
    # elif int(our) > pd2[1]:
    #     flow="250 A"
    # elif int(our) > pd2[2]:
    #     flow="200 A"    
    # elif int(our) > pd2[3]:
    #     flow="150 A"
    # elif int(our) > pd2[4]:
    #     flow="125 A"
    # elif int(our) > pd2[5]:
    #     flow="100 A"    
    # elif int(our) > pd2[6]:
    #     flow="80 A"    
    # elif int(our) > pd2[7]:
    #     flow="65 A"    
    # elif int(our) > pd2[8]:
    #     flow="50 A"
    # elif int(our) > pd2[9]:
    #     flow="40 A"
    # elif int(our) > pd2[10]:
    #     flow="32 A"
    # elif int(our) > pd2[11]:
    #     flow="25 A"    
    # elif int(our) > 10:
    #     flow="20 A"        
    # e.delete(0,END)
    # e.insert(0 , str("보정 열량계관경"))
    # e.insert(our, str("→ "))
    # e.insert(our,flow)
    # e.insert(our,"("+checked2.get()+")") 
    # hh=e.get()
    # f.insert(tk.INSERT,hh+"\n"+"\n")





#----------------------------------------------------------------








    gg0.delete(0,END)
    gg0.insert(0,our)
    gg3.delete(0,END)
    gg3.insert(0,flow+" ("+str(round(flowper,1))+"%)")
    
    e.delete(0,END)
    e.insert(our,our)
    add_command1()

    return

def button_exe2():
    global ex1
    ex1=1
    init2=""
    our = e.get()
    if int(our) < 9:
       return
    global afc
    e.delete(0,END)
    e.insert(0,str("**난방HX 용량**"))
    e.insert(our,our)
    e.insert(our," Mcal/hr인 경우")
    hh=e.get()
    f.insert(tk.INSERT,hh+"\n")


#------------------------------------------------------------------------------------------
    if int(our) > pd7[0]:
        init2="300 A"
    elif int(our) > int((pd7[0]-pd7[1])*float(afccc)+pd7[1]):
        init2="300 A+"  
        init2per=float(((int(our)-pd7[1])/(pd7[0]-pd7[1]))*100)
    elif int(our) > pd7[1]:
        init2="250 A"
        init2per=float(((int(our)-pd7[1])/(pd7[0]-pd7[1]))*100)
    elif int(our) > int((pd7[1]-pd7[2])*float(afccc)+pd7[2]):
        init2="250 A+" 
        init2per=float(((int(our)-pd7[2])/(pd7[1]-pd7[2]))*100) 
    elif int(our) > pd7[2]:
        init2="200 A" 
        init2per=float(((int(our)-pd7[2])/(pd7[1]-pd7[2]))*100)    
    elif int(our) > int((pd7[2]-pd7[3])*float(afccc)+pd7[3]):
        init2="200 A+" 
        init2per=float(((int(our)-pd7[3])/(pd7[2]-pd7[3]))*100)  
    elif int(our) > pd7[3]:
        init2="150 A"
        init2per=float(((int(our)-pd7[3])/(pd7[2]-pd7[3]))*100)
    elif int(our) > int((pd7[3]-pd7[4])*float(afccc)+pd7[4]):
        init2="150 A+"
        init2per=float(((int(our)-pd7[4])/(pd7[3]-pd7[4]))*100)
    elif int(our) > pd7[4]:
        init2="125 A"
        init2per=float(((int(our)-pd7[4])/(pd7[3]-pd7[4]))*100)
    elif int(our) > int((pd7[4]-pd7[5])*float(afccc)+pd7[5]):
        init2="125 A+"
        init2per=float(((int(our)-pd7[5])/(pd7[4]-pd7[5]))*100)
    elif int(our) > pd7[5]:
        init2="100 A"  
        init2per=float(((int(our)-pd7[5])/(pd7[4]-pd7[5]))*100)  
    elif int(our) > int((pd7[5]-pd7[6])*float(afccc)+pd7[6]):
        init2="100 A+"
        init2per=float(((int(our)-pd7[6])/(pd7[5]-pd7[6]))*100)
    elif int(our) > pd7[6]:
        init2="80 A" 
        init2per=float(((int(our)-pd7[6])/(pd7[5]-pd7[6]))*100) 
    elif int(our) > int((pd7[6]-pd7[7])*float(afccc)+pd7[7]):
        init2="80 A+"
        init2per=float(((int(our)-pd7[7])/(pd7[6]-pd7[7]))*100)  
    elif int(our) > pd7[7]:
        init2="65 A"  
        init2per=float(((int(our)-pd7[7])/(pd7[6]-pd7[7]))*100) 
    elif int(our) > int((pd7[7]-pd7[8])*float(afccc)+pd7[8]):
        init2="65 A+" 
        init2per=float(((int(our)-pd7[8])/(pd7[7]-pd7[8]))*100)   
    elif int(our) > pd7[8]:
        init2="50 A"
        init2per=float(((int(our)-pd7[8])/(pd7[7]-pd7[8]))*100)
    elif int(our) > int((pd7[8]-pd7[9])*float(afccc)+pd7[9]):
        init2="50 A+" 
        init2per=float(((int(our)-pd7[9])/(pd7[8]-pd7[9]))*100)
    elif int(our) > pd7[9]:
        init2="40 A"
        init2per=float(((int(our)-pd7[9])/(pd7[8]-pd7[9]))*100)
    elif int(our) > int((pd7[9]-pd7[10])*float(afccc)+pd7[10]):
        init2="40 A+" 
        init2per=float(((int(our)-pd7[10])/(pd7[9]-pd7[10]))*100)
    elif int(our) > pd7[10]:
        init2="32 A"
        init2per=float(((int(our)-pd7[10])/(pd7[9]-pd7[10]))*100)
    elif int(our) > int((pd7[10]-pd7[11])*float(afccc)+pd7[11]):
        init2="32 A+" 
        init2per=float(((int(our)-pd7[11])/(pd7[10]-pd7[11]))*100)
    elif int(our) > pd7[11]:
        init2="25 A" 
        init2per=float(((int(our)-pd7[11])/(pd7[10]-pd7[11]))*100)  
    elif int(our) > int((pd7[11]-pd7[12])*float(afccc)+pd7[12]):
        init2="25 A+" 
        init2per=float(((int(our)-pd7[12])/(pd7[11]-pd7[12]))*100)
    elif int(our) > pd7[12]:
        init2="20 A"
        init2per=float(((int(our)-pd7[12])/(pd7[11]-pd7[12]))*100)
    elif int(our) > int((pd7[12]-pd7[13])*float(afccc)+pd7[13]):
        init2="20 A+" 
        init2per=float(((int(our)-pd7[13])/(pd7[12]-pd7[13]))*100)
    elif int(our) > pd7[13]:
        init2="15 A"
        init2per=float(((int(our)-pd7[13])/(pd7[12]-pd7[13]))*100)
    f_tcv1 = round(((int(our)/pdddd/sqrt(0.3))*1.167),3)
    e.delete(0,END)
    e.insert(0 , str("난방1차 관경"))
    e.insert(our, str("→ "))
    e.insert(our,init2+"("+checked7.get()+"난방)")
    e.insert(our,"("+str(round(init2per,2))+"%)") 
#-------------------------------------------------------------------------------------------
    hh=e.get()
    f.insert(tk.INSERT,hh+"\n")
    
    ggg0.delete(0,END)
    ggg0.insert(0,our)
    ggg2.delete(0,END)
    ggg2.insert(0,init2+" ("+str(round(init2per,1))+"%)")
    
# ----------------------------------------------------------------------------------

    lpm=""
    lpm=round(((int(our)/pdd99)*1000/60),1)
    e.delete(0,END)
    e.insert(0 , str("난방PP 유량"))
    e.insert(our, str(" → "))
    e.insert(our,int(lpm))
    e.insert(our,str(" LPM(100%)"))
    hh=e.get()
    f.insert(tk.INSERT,hh+"\n")
    
    ggg0.delete(0,END)
    ggg0.insert(0,our)
    ggg1.delete(0,END)
    ggg1.insert(0,int(lpm))
    ggg1.insert(our,str(" lpm"))
# ----------------------------------------------------------------------------------

    expan=""
    expan=int(int(our)*30*pd8/float(afc))
    e.delete(0,END)
    e.insert(0 , str("팽창탱크"))
    e.insert(our, str("      → "))
    e.insert(our,math.ceil(int(expan)/100)*100)
    e.insert(our,str(" Liter("))
    e.insert(our,int(expan))
    e.insert(our,str("lit)"))
    e.insert(our,checked7.get())
    hh=e.get()
    f.insert(tk.INSERT,hh+"\n")
    ggg0.delete(0,END)
    ggg0.insert(0,our)
    ggg4.delete(0,END)
    ggg4.insert(0,math.ceil(int(expan)/100)*100)
    ggg4.insert(our,str("("))
    ggg4.insert(our,int(expan))
    ggg4.insert(our,str(" lit)"))

# ----------------------------------------------------------------------------------


    # tcv1=""
    # if f_tcv1 > pd3[0]:
    #     tcv1="200 A"
    # elif f_tcv1 > int((pd3[0]-pd3[1])*float(afccc)+pd3[1]):
    #     tcv1="200 A+" 
    #     tcv1per=float(((f_tcv1-pd3[1])/(pd3[0]-pd3[1]))*100) 
    # elif f_tcv1 > pd3[1]:
    #     tcv1="150 A"
    #     tcv1per=float(((f_tcv1-pd3[1])/(pd3[0]-pd3[1]))*100)
    # elif f_tcv1 > int((pd3[1]-pd3[2])*float(afccc)+pd3[2]):
    #     tcv1="150 A+"
    #     tcv1per=float(((f_tcv1-pd3[2])/(pd3[1]-pd3[2]))*100)  
    # elif f_tcv1 > pd3[2]:
    #     tcv1="125 A" 
    #     tcv1per=float(((f_tcv1-pd3[2])/(pd3[1]-pd3[2]))*100)
    # elif f_tcv1 > int((pd3[2]-pd3[3])*float(afccc)+pd3[3]):
    #     tcv1="125 A+"
    #     tcv1per=float(((f_tcv1-pd3[3])/(pd3[2]-pd3[3]))*100)     
    # elif f_tcv1 > pd3[3]:
    #     tcv1="100 A"
    #     tcv1per=float(((f_tcv1-pd3[3])/(pd3[2]-pd3[3]))*100)  
    # elif f_tcv1 > int((pd3[3]-pd3[4])*float(afccc)+pd3[4]):
    #     tcv1="100 A+"
    #     tcv1per=float(((f_tcv1-pd3[4])/(pd3[3]-pd3[4]))*100)     
    # elif f_tcv1 > pd3[4]:
    #     tcv1="80 A"
    #     tcv1per=float(((f_tcv1-pd3[4])/(pd3[3]-pd3[4]))*100) 
    # elif f_tcv1 > int((pd3[4]-pd3[5])*float(afccc)+pd3[5]):
    #     tcv1="80 A+" 
    #     tcv1per=float(((f_tcv1-pd3[5])/(pd3[4]-pd3[5]))*100) 
    # elif f_tcv1 > pd3[5]:
    #     tcv1="65 A" 
    #     tcv1per=float(((f_tcv1-pd3[5])/(pd3[4]-pd3[5]))*100) 
    # elif f_tcv1 > int((pd3[5]-pd3[6])*float(afccc)+pd3[6]):
    #     tcv1="65 A+" 
    #     tcv1per=float(((f_tcv1-pd3[6])/(pd3[5]-pd3[6]))*100)  
    # elif f_tcv1 > pd3[6]:
    #     tcv1="50 A" 
    #     tcv1per=float(((f_tcv1-pd3[6])/(pd3[5]-pd3[6]))*100)
    # elif f_tcv1 > int((pd3[6]-pd3[7])*float(afccc)+pd3[7]):
    #     tcv1="50 A+" 
    #     tcv1per=float(((f_tcv1-pd3[7])/(pd3[6]-pd3[7]))*100)   
    # elif f_tcv1 > pd3[7]:
    #     tcv1="40 A"
    #     tcv1per=float(((f_tcv1-pd3[7])/(pd3[6]-pd3[7]))*100)
    # elif f_tcv1 > int((pd3[7]-pd3[8])*float(afccc)+pd3[8]):
    #     tcv1="40 A+" 
    #     tcv1per=float(((f_tcv1-pd3[8])/(pd3[7]-pd3[8]))*100)    
    # elif f_tcv1 > pd3[8]:
    #     tcv1="32 A"
    #     tcv1per=float(((f_tcv1-pd3[8])/(pd3[7]-pd3[8]))*100)
    # elif f_tcv1 > int((pd3[8]-pd3[9])*float(afccc)+pd3[9]):
    #     tcv1="32 A+"
    #     tcv1per=float(((f_tcv1-pd3[9])/(pd3[8]-pd3[9]))*100)  
    # elif f_tcv1 > pd3[9]:
    #     tcv1="25 A"
    #     tcv1per=float(((f_tcv1-pd3[9])/(pd3[8]-pd3[9]))*100)
    # elif f_tcv1 > int((pd3[9]-pd3[10])*float(afccc)+pd3[10]):
    #     tcv1="25 A+" 
    #     tcv1per=float(((f_tcv1-pd3[10])/(pd3[9]-pd3[10]))*100) 
    # elif f_tcv1 > pd3[10]:
    #     tcv1="20 A"
    #     tcv1per=float(((f_tcv1-pd3[10])/(pd3[9]-pd3[10]))*100)
    # elif f_tcv1 > int((pd3[10]-pd3[11])*float(afccc)+pd3[11]):
    #     tcv1="20 A+" 
    #     tcv1per=float(((f_tcv1-pd3[11])/(pd3[10]-pd3[11]))*100) 
    # elif f_tcv1 > pd3[11]:
    #     tcv1="15 A" 
    #     tcv1per=float(((f_tcv1-pd3[11])/(pd3[10]-pd3[11]))*100) 

    tcv1=""
    if f_tcv1 > pd3[0]:
        tcv1="200 A"
    elif f_tcv1 > float((pd3[0]-pd3[1])*float(afccc)+pd3[1]):
        tcv1="200 A+" 
        tcv1per=float(((f_tcv1-pd3[1])/(pd3[0]-pd3[1]))*100) 
    elif f_tcv1 > pd3[1]:
        tcv1="150 A"
        tcv1per=float(((f_tcv1-pd3[1])/(pd3[0]-pd3[1]))*100)
    elif f_tcv1 > float((pd3[1]-pd3[2])*float(afccc)+pd3[2]):
        tcv1="150 A+"
        tcv1per=float(((f_tcv1-pd3[2])/(pd3[1]-pd3[2]))*100) 
    elif f_tcv1 > pd3[2]:
        tcv1="125 A" 
        tcv1per=float(((f_tcv1-pd3[2])/(pd3[1]-pd3[2]))*100) 
    elif f_tcv1 > float((pd3[2]-pd3[3])*float(afccc)+pd3[3]):
        tcv1="125 A+" 
        tcv1per=float(((f_tcv1-pd3[3])/(pd3[2]-pd3[3]))*100)    
    elif f_tcv1 > pd3[3]:
        tcv1="100 A"
        tcv1per=float(((f_tcv1-pd3[3])/(pd3[2]-pd3[3]))*100)
    elif f_tcv1 > float((pd3[3]-pd3[4])*float(afccc)+pd3[4]):
        tcv1="100 A+" 
        tcv1per=float(((f_tcv1-pd3[4])/(pd3[3]-pd3[4]))*100)
    elif f_tcv1 > pd3[4]:
        tcv1="80 A"
        tcv1per=float(((f_tcv1-pd3[4])/(pd3[3]-pd3[4]))*100)
    elif f_tcv1 > float((pd3[4]-pd3[5])*float(afccc)+pd3[5]):
        tcv1="80 A+" 
        tcv1per=float(((f_tcv1-pd3[5])/(pd3[4]-pd3[5]))*100)
    elif f_tcv1 > pd3[5]:
        tcv1="65 A" 
        tcv1per=float(((f_tcv1-pd3[5])/(pd3[4]-pd3[5]))*100)
    elif f_tcv1 > float((pd3[5]-pd3[6])*float(afccc)+pd3[6]):
        tcv1="65 A+" 
        tcv1per=float(((f_tcv1-pd3[6])/(pd3[5]-pd3[6]))*100)   
    elif f_tcv1 > pd3[6]:
        tcv1="50 A"  
        tcv1per=float(((f_tcv1-pd3[6])/(pd3[5]-pd3[6]))*100)  
    elif f_tcv1 > float((pd3[6]-pd3[7])*float(afccc)+pd3[7]):
        tcv1="50 A+" 
        tcv1per=float(((f_tcv1-pd3[7])/(pd3[6]-pd3[7]))*100)       
    elif f_tcv1 > pd3[7]:
        tcv1="40 A"
        tcv1per=float(((f_tcv1-pd3[7])/(pd3[6]-pd3[7]))*100) 
    elif f_tcv1 > float((pd3[7]-pd3[8])*float(afccc)+pd3[8]):
        tcv1="40 A+" 
        tcv1per=float(((f_tcv1-pd3[8])/(pd3[7]-pd3[8]))*100)   
    elif f_tcv1 > pd3[8]:
        tcv1="32 A"
        tcv1per=float(((f_tcv1-pd3[8])/(pd3[7]-pd3[8]))*100) 
    elif f_tcv1 > float((pd3[8]-pd3[9])*float(afccc)+pd3[9]):
        tcv1="32 A+" 
        tcv1per=float(((f_tcv1-pd3[9])/(pd3[8]-pd3[9]))*100) 
    elif f_tcv1 > pd3[9]:
        tcv1="25 A"
        tcv1per=float(((f_tcv1-pd3[9])/(pd3[8]-pd3[9]))*100)
    elif f_tcv1 > float((pd3[9]-pd3[10])*float(afccc)+pd3[10]):
        tcv1="25 A+" 
        tcv1per=float(((f_tcv1-pd3[10])/(pd3[9]-pd3[10]))*100)
    elif f_tcv1 > pd3[10]:
        tcv1="20 A"
        tcv1per=float(((f_tcv1-pd3[10])/(pd3[9]-pd3[10]))*100)
    elif f_tcv1 > float((pd3[10]-pd3[11])*float(afccc)+pd3[11]):
        tcv1="20 A+" 
        tcv1per=float(((f_tcv1-pd3[11])/(pd3[10]-pd3[11]))*100)
    elif f_tcv1 > pd3[11]:
        tcv1="15 A"   
        tcv1per=float(((f_tcv1-pd3[11])/(pd3[10]-pd3[11]))*100)     



    e.delete(0,END)
    e.insert(0 , str("난방TCV관경"))
    e.insert(our, str("→ "))
    e.insert(our,tcv1)
    e.insert(our,"("+checked3.get()+")")
    e.insert(our,"("+str(round(tcv1per,2))+"%)") 


    hh=e.get()
    f.insert(tk.INSERT,hh+"\n")

    ggg0.delete(0,END)
    ggg0.insert(0,our)
    ggg5.delete(0,END)
    ggg5.insert(0,tcv1+" ("+str(round(tcv1per,1))+"%)")

 # -----------------------------------------------------------------------   

    f_tcv11=0
    f_tcv11=round(float((int(our)/pdddd/sqrt(0.3))),1)
    e.delete(0,END)
    e.insert(0 , str("kV값(TCV)"))
    # e.insert(our,"("+checked1.get()+")")
    e.insert(our, str("→ "))
    e.insert(our,f_tcv11)
    # e.insert(our,str("m/s"))
    # e.insert(our,str("(↓6m/s권장)"))
    hh=e.get()
    f.insert(tk.INSERT,hh+"\n")

  
#--------------------------------------------------------------------------




    secon=""
    if lpm > pd4[0]:
        secon="300 A"
    elif lpm > int((pd4[0]-pd4[1])*float(afccc)+pd4[1]):
        secon="300 A+"  
        seconper=float(((lpm-pd4[1])/(pd4[0]-pd4[1]))*100)
    elif lpm > pd4[1]:
        secon="250 A"
        seconper=float(((lpm-pd4[1])/(pd4[0]-pd4[1]))*100)
    elif lpm > int((pd4[1]-pd4[2])*float(afccc)+pd4[2]):
        secon="250 A+" 
        seconper=float(((lpm-pd4[2])/(pd4[1]-pd4[2]))*100)
    elif lpm > pd4[2]:
        secon="200 A"  
        seconper=float(((lpm-pd4[2])/(pd4[1]-pd4[2]))*100)  
    elif lpm > int((pd4[2]-pd4[3])*float(afccc)+pd4[3]):
        secon="200 A+"
        seconper=float(((lpm-pd4[3])/(pd4[2]-pd4[3]))*100) 
    elif lpm > pd4[3]:
        secon="150 A"
        seconper=float(((lpm-pd4[3])/(pd4[2]-pd4[3]))*100) 
    elif lpm > int((pd4[3]-pd4[4])*float(afccc)+pd4[4]):
        secon="150 A+" 
        seconper=float(((lpm-pd4[4])/(pd4[3]-pd4[4]))*100) 
    elif lpm > pd4[4]:
        secon="125 A"
        seconper=float(((lpm-pd4[4])/(pd4[3]-pd4[4]))*100)
    elif lpm > int((pd4[4]-pd4[5])*float(afccc)+pd4[5]):
        secon="125 A+" 
        seconper=float(((lpm-pd4[5])/(pd4[4]-pd4[5]))*100)
    elif lpm > pd4[5]:
        secon="100 A" 
        seconper=float(((lpm-pd4[5])/(pd4[4]-pd4[5]))*100) 
    elif lpm > int((pd4[5]-pd4[6])*float(afccc)+pd4[6]):
        secon="100 A+" 
        seconper=float(((lpm-pd4[6])/(pd4[5]-pd4[6]))*100)  
    elif lpm > pd4[6]:
        secon="80 A"  
        seconper=float(((lpm-pd4[6])/(pd4[5]-pd4[6]))*100)   
    elif lpm > int((pd4[6]-pd4[7])*float(afccc)+pd4[7]):
        secon="80 A+"
        seconper=float(((lpm-pd4[7])/(pd4[6]-pd4[7]))*100)    
    elif lpm > pd4[7]:
        secon="65 A" 
        seconper=float(((lpm-pd4[7])/(pd4[6]-pd4[7]))*100)  
    elif lpm > int((pd4[7]-pd4[8])*float(afccc)+pd4[8]):
        secon="65 A+" 
        seconper=float(((lpm-pd4[8])/(pd4[7]-pd4[8]))*100)   
    elif lpm > pd4[8]:
        secon="50 A"
        seconper=float(((lpm-pd4[8])/(pd4[7]-pd4[8]))*100)
    elif lpm > int((pd4[8]-pd4[9])*float(afccc)+pd4[9]):
        secon="50 A+" 
        seconper=float(((lpm-pd4[9])/(pd4[8]-pd4[9]))*100)
    elif lpm > pd4[9]:
        secon="40 A"
        seconper=float(((lpm-pd4[9])/(pd4[8]-pd4[9]))*100)
    elif lpm > int((pd4[9]-pd4[10])*float(afccc)+pd4[10]):
        secon="40 A+"
        seconper=float(((lpm-pd4[10])/(pd4[9]-pd4[10]))*100) 
    elif lpm > pd4[10]:
        secon="32 A"
        seconper=float(((lpm-pd4[10])/(pd4[9]-pd4[10]))*100)
    elif lpm > int((pd4[10]-pd4[11])*float(afccc)+pd4[11]):
        secon="32 A+" 
        seconper=float(((lpm-pd4[11])/(pd4[10]-pd4[11]))*100)
    elif lpm > pd4[11]:
        secon="25 A"  
        seconper=float(((lpm-pd4[11])/(pd4[10]-pd4[11]))*100)
    elif lpm > int((pd4[11]-pd4[12])*float(afccc)+pd4[12]):
        secon="25 A+"
        seconper=float(((lpm-pd4[12])/(pd4[11]-pd4[12]))*100)  
    elif lpm > pd4[12]:
        secon="20 A"    
        seconper=float(((lpm-pd4[12])/(pd4[11]-pd4[12]))*100)        
    e.delete(0,END)
    e.insert(0 , str("난방2차 관경"))
    e.insert(our, str("→ "))
    e.insert(our,secon)
    e.insert(our,"("+checked4.get()+")")
    e.insert(our,"("+str(round(seconper,1))+"%)") 
    hh=e.get()
    f.insert(tk.INSERT,hh+"\n"+"\n")
    ggg0.delete(0,END)
    ggg0.insert(0,our)
    ggg3.delete(0,END)
    ggg3.insert(0,secon+" ("+str(round(seconper,1))+"%)")

    e.delete(0,END)
    # g.insert(0,str("난방HX 용량"))
    e.insert(our,our)
    # g.insert(our," Mcal/hr인 경우")
    add_command2()
    return




def button_exe3():
    global ex1
    ex1=1
    init3=""
    our = e.get()
    if int(our) < 20:
       return
    e.delete(0,END)
    e.insert(0,str("**급탕HX 용량**"))
    e.insert(our,our)
    e.insert(our," Mcal/hr인 경우")
    hh=e.get()
    f.insert(tk.INSERT,hh+"\n")
    
    if int(our)/40 > 433.77:
        init3="300 A"
    elif int(our)/40 > (433.77-241.33)*float(afccc)+241.33:
        init3="300 A+"
        init3per=float(((int(our)/40-241.33)/(433.77-241.33))*100)
    elif int(our)/40 > 241.33:
        init3="250 A"
        init3per=float(((int(our)/40-241.33)/(433.77-241.33))*100)
    elif int(our)/40 > (241.33-116.62)*float(afccc)+116.62:
        init3="250 A+"
        init3per=float(((int(our)/40-116.62)/(241.33-116.62))*100)
    elif int(our)/40 > 116.62:
        init3="200 A" 
        init3per=float(((int(our)/40-116.62)/(241.33-116.62))*100)   
    elif int(our)/40 > (116.62-73.89)*float(afccc)+73.89:
        init3="200 A+"
        init3per=float(((int(our)/40-73.89)/(116.62-73.89))*100)
    elif int(our)/40 > 73.89:
        init3="150 A"
        init3per=float(((int(our)/40-73.89)/(116.62-73.89))*100)
    elif int(our)/40 > (73.89-41.95)*float(afccc)+41.95:
        init3="150 A+"
        init3per=float(((int(our)/40-41.95)/(73.89-41.95))*100)
    elif int(our)/40 > 41.95:
        init3="125 A"
        init3per=float(((int(our)/40-41.95)/(73.89-41.95))*100)
    elif int(our)/40 > (41.95-20.82)*float(afccc)+20.82:
        init3="125 A+"
        init3per=float(((int(our)/40-20.82)/(41.95-20.82))*100)
    elif int(our)/40 > 20.82:
        init3="100 A"
        init3per=float(((int(our)/40-20.82)/(41.95-20.82))*100) 
    elif int(our)/40 > (20.82-13.15)*float(afccc)+13.15:
        init3="100 A+" 
        init3per=float(((int(our)/40-13.15)/(20.82-13.15))*100) 
    elif int(our)/40 > 13.15:
        init3="80 A" 
        init3per=float(((int(our)/40-13.15)/(20.82-13.15))*100) 
    elif int(our)/40 > (13.15-6.88)*float(afccc)+6.88:
        init3="80 A+"
        init3per=float(((int(our)/40-6.88)/(13.15-6.88))*100)   
    elif int(our)/40 > 6.88:
        init3="65 A" 
        init3per=float(((int(our)/40-6.88)/(13.15-6.88))*100)   
    elif int(our)/40 > (6.88-3.58)*float(afccc)+3.58:
        init3="65 A+"
        init3per=float(((int(our)/40-3.58)/(6.88-3.58))*100)     
    elif int(our)/40 > 3.58:
        init3="50 A"
        init3per=float(((int(our)/40-3.58)/(6.88-3.58))*100)
    elif int(our)/40 > (3.58-2.41)*float(afccc)+2.41:
        init3="50 A+" 
        init3per=float(((int(our)/40-2.41)/(3.58-2.41))*100)
    elif int(our)/40 > 2.41:
        init3="40 A"
        init3per=float(((int(our)/40-2.41)/(3.58-2.41))*100)
    elif int(our)/40 > (2.41-1.19)*float(afccc)+1.19:
        init3="40 A+" 
        init3per=float(((int(our)/40-1.19)/(2.41-1.19))*100)
    elif int(our)/40 > 1.19:
        init3="32 A"
        init3per=float(((int(our)/40-1.19)/(2.41-1.19))*100)
    elif int(our)/40 > (1.19-0.64)*float(afccc)+0.64:
        init3="32 A+"
        init3per=float(((int(our)/40-0.64)/(1.19-0.64))*100)
    elif int(our)/40 > 0.64:
        init3="25 A"  
        init3per=float(((int(our)/40-0.64)/(1.19-0.64))*100)
    elif int(our)/40 > (0.64-0.29)*float(afccc)+0.29:
        init3="25 A+" 
        init3per=float(((int(our)/40-0.29)/(0.64-0.29))*100) 
    elif int(our)/40 > 0.29:
        init3="20 A"
        init3per=float(((int(our)/40-0.29)/(0.64-0.29))*100) 
    elif int(our)/40 > (0.29-0.01)*float(afccc)+0.01:
        init3="20 A+" 
        init3per=float(((int(our)/40-0.01)/(0.29-0.01))*100) 
    elif int(our)/40 > 0.01 :
        init3="15 A"
        init3per=float(((int(our)/40-0.01)/(0.29-0.01))*100)
    f_tcv2 = int((int(our)/40/sqrt(0.3))*1.167)
    e.delete(0,END)
    e.insert(0 , str("1차 재열관경"))
    e.insert(our, str("→ "))
    e.insert(our,init3)
    e.insert(our,"("+str(round(init3per,2))+"%)") 
    hh=e.get()
    f.insert(tk.INSERT,hh+"\n")
    gggg0.delete(0,END)
    gggg0.insert(0,our)
    gggg2.delete(0,END)
    gggg2.insert(0,init3+" ("+str(round(init3per,1))+"%)")

    lpm2=""
    lpm2=int((int(our)/40*1000/60)*0.4)
    e.delete(0,END)
    e.insert(0 , str("급탕PP 유량"))
    e.insert(our, str(" → "))
    e.insert(our,int(lpm2))
    e.insert(our,str(" LPM(환탕량40%)"))
    hh=e.get()
    f.insert(tk.INSERT,hh+"\n")
    gggg0.delete(0,END)
    gggg0.insert(0,our)
    gggg1.delete(0,END)
    gggg1.insert(0,int(lpm2))
    gggg1.insert(our,str(" lpm"))

    tcv2=""
    if f_tcv2 > pd5[0]:
        tcv2="200 A"
    elif f_tcv2 > float((pd5[0]-pd5[1])*float(afccc)+pd5[1]):
        tcv2="200 A+" 
        tcv2per=float(((f_tcv2-pd5[1])/(pd5[0]-pd5[1]))*100) 
    elif f_tcv2 > pd5[1]:
        tcv2="150 A"
        tcv2per=float(((f_tcv2-pd5[1])/(pd5[0]-pd5[1]))*100)
    elif f_tcv2 > float((pd5[1]-pd5[2])*float(afccc)+pd5[2]):
        tcv2="150 A+"
        tcv2per=float(((f_tcv2-pd5[2])/(pd5[1]-pd5[2]))*100) 
    elif f_tcv2 > pd5[2]:
        tcv2="125 A" 
        tcv2per=float(((f_tcv2-pd5[2])/(pd5[1]-pd5[2]))*100) 
    elif f_tcv2 > float((pd5[2]-pd5[3])*float(afccc)+pd5[3]):
        tcv2="125 A+" 
        tcv2per=float(((f_tcv2-pd5[3])/(pd5[2]-pd5[3]))*100)    
    elif f_tcv2 > pd5[3]:
        tcv2="100 A"
        tcv2per=float(((f_tcv2-pd5[3])/(pd5[2]-pd5[3]))*100)
    elif f_tcv2 > float((pd5[3]-pd5[4])*float(afccc)+pd5[4]):
        tcv2="100 A+" 
        tcv2per=float(((f_tcv2-pd5[4])/(pd5[3]-pd5[4]))*100)
    elif f_tcv2 > pd5[4]:
        tcv2="80 A"
        tcv2per=float(((f_tcv2-pd5[4])/(pd5[3]-pd5[4]))*100)
    elif f_tcv2 > float((pd5[4]-pd5[5])*float(afccc)+pd5[5]):
        tcv2="80 A+" 
        tcv2per=float(((f_tcv2-pd5[5])/(pd5[4]-pd5[5]))*100)
    elif f_tcv2 > pd5[5]:
        tcv2="65 A" 
        tcv2per=float(((f_tcv2-pd5[5])/(pd5[4]-pd5[5]))*100)
    elif f_tcv2 > float((pd5[5]-pd5[6])*float(afccc)+pd5[6]):
        tcv2="65 A+" 
        tcv2per=float(((f_tcv2-pd5[6])/(pd5[5]-pd5[6]))*100)   
    elif f_tcv2 > pd5[6]:
        tcv2="50 A"  
        tcv2per=float(((f_tcv2-pd5[6])/(pd5[5]-pd5[6]))*100)  
    elif f_tcv2 > float((pd5[6]-pd5[7])*float(afccc)+pd5[7]):
        tcv2="50 A+" 
        tcv2per=float(((f_tcv2-pd5[7])/(pd5[6]-pd5[7]))*100)       
    elif f_tcv2 > pd5[7]:
        tcv2="40 A"
        tcv2per=float(((f_tcv2-pd5[7])/(pd5[6]-pd5[7]))*100) 
    elif f_tcv2 > float((pd5[7]-pd5[8])*float(afccc)+pd5[8]):
        tcv2="40 A+" 
        tcv2per=float(((f_tcv2-pd5[8])/(pd5[7]-pd5[8]))*100)   
    elif f_tcv2 > pd5[8]:
        tcv2="32 A"
        tcv2per=float(((f_tcv2-pd5[8])/(pd5[7]-pd5[8]))*100) 
    elif f_tcv2 > float((pd5[8]-pd5[9])*float(afccc)+pd5[9]):
        tcv2="32 A+" 
        tcv2per=float(((f_tcv2-pd5[9])/(pd5[8]-pd5[9]))*100) 
    elif f_tcv2 > pd5[9]:
        tcv2="25 A"
        tcv2per=float(((f_tcv2-pd5[9])/(pd5[8]-pd5[9]))*100)
    elif f_tcv2 > float((pd5[9]-pd5[10])*float(afccc)+pd5[10]):
        tcv2="25 A+" 
        tcv2per=float(((f_tcv2-pd5[10])/(pd5[9]-pd5[10]))*100)
    elif f_tcv2 > pd5[10]:
        tcv2="20 A"
        tcv2per=float(((f_tcv2-pd5[10])/(pd5[9]-pd5[10]))*100)
    elif f_tcv2 > float((pd5[10]-pd5[11])*float(afccc)+pd5[11]):
        tcv2="20 A+" 
        tcv2per=float(((f_tcv2-pd5[11])/(pd5[10]-pd5[11]))*100)
    elif f_tcv2 > pd5[11]:
        tcv2="15 A"   
        tcv2per=float(((f_tcv2-pd5[11])/(pd5[10]-pd5[11]))*100)     


    e.delete(0,END)
    e.insert(0 , str("급탕TCV관경"))
    e.insert(our, str("→ "))
    e.insert(our,tcv2)
    e.insert(our,"("+checked5.get()+")")
    e.insert(our,"("+str(round(tcv2per,2))+"%)") 

    hh=e.get()
    f.insert(tk.INSERT,hh+"\n")
    gggg0.delete(0,END)
    gggg0.insert(0,our)
    gggg4.delete(0,END)
    gggg4.insert(0,tcv2+" ("+str(round(tcv2per,1))+"%)")

 # -----------------------------------------------------------------------   

    f_tcv22=0
    f_tcv22=round(float((int(our)/40/sqrt(0.3))),1)
    e.delete(0,END)
    e.insert(0 , str("kV값(TCV)"))
    # e.insert(our,"("+checked1.get()+")")
    e.insert(our, str("→ "))
    e.insert(our,f_tcv22)
    # e.insert(our,str("m/s"))
    # e.insert(our,str("(↓6m/s권장)"))
    hh=e.get()
    f.insert(tk.INSERT,hh+"\n")

  
#--------------------------------------------------------------------------





    secon2=""
    if int(our)> pd6[0]:
        secon2="300 A"
    elif int(our) > int((pd6[0]-pd6[1])*float(afccc)+pd6[1]):
        secon2="300 A+"
        secon2per=float(((int(our)-pd6[1])/(pd6[0]-pd6[1]))*100) 
    elif int(our)> pd6[1]:
        secon2="250 A"
        secon2per=float(((int(our)-pd6[1])/(pd6[0]-pd6[1]))*100)
    elif int(our) > int((pd6[1]-pd6[2])*float(afccc)+pd6[2]):
        secon2="250 A+" 
        secon2per=float(((int(our)-pd6[2])/(pd6[1]-pd6[2]))*100)
    elif int(our)> pd6[2]:
        secon2="200 A" 
        secon2per=float(((int(our)-pd6[2])/(pd6[1]-pd6[2]))*100) 
    elif int(our) > int((pd6[2]-pd6[3])*float(afccc)+pd6[3]):
        secon2="200 A+"
        secon2per=float(((int(our)-pd6[3])/(pd6[2]-pd6[3]))*100)   
    elif int(our)> pd6[3]:
        secon2="150 A"
        secon2per=float(((int(our)-pd6[3])/(pd6[2]-pd6[3]))*100)
    elif int(our) > int((pd6[3]-pd6[4])*float(afccc)+pd6[4]):
        secon2="150 A+" 
        secon2per=float(((int(our)-pd6[4])/(pd6[3]-pd6[4]))*100)  
    elif int(our)> pd6[4]:
        secon2="125 A"
        secon2per=float(((int(our)-pd6[4])/(pd6[3]-pd6[4]))*100)
    elif int(our) > int((pd6[4]-pd6[5])*float(afccc)+pd6[5]):
        secon2="125 A+"
        secon2per=float(((int(our)-pd6[5])/(pd6[4]-pd6[5]))*100)  
    elif int(our)> pd6[5]:
        secon2="100 A" 
        secon2per=float(((int(our)-pd6[5])/(pd6[4]-pd6[5]))*100)  
    elif int(our) > int((pd6[5]-pd6[6])*float(afccc)+pd6[6]):
        secon2="100 A+" 
        secon2per=float(((int(our)-pd6[6])/(pd6[5]-pd6[6]))*100) 
    elif int(our)> pd6[6]:
        secon2="80 A" 
        secon2per=float(((int(our)-pd6[6])/(pd6[5]-pd6[6]))*100) 
    elif int(our) > int((pd6[6]-pd6[7])*float(afccc)+pd6[7]):
        secon2="80 A+"  
        secon2per=float(((int(our)-pd6[7])/(pd6[6]-pd6[7]))*100) 
    elif int(our)> pd6[7]:
        secon2="65 A" 
        secon2per=float(((int(our)-pd6[7])/(pd6[6]-pd6[7]))*100)   
    elif int(our) > int((pd6[7]-pd6[8])*float(afccc)+pd6[8]):
        secon2="65 A+"
        secon2per=float(((int(our)-pd6[8])/(pd6[7]-pd6[8]))*100)   
    elif int(our)> pd6[8]:
        secon2="50 A"
        secon2per=float(((int(our)-pd6[8])/(pd6[7]-pd6[8]))*100) 
    elif int(our) > int((pd6[8]-pd6[9])*float(afccc)+pd6[9]):
        secon2="50 A+"
        secon2per=float(((int(our)-pd6[9])/(pd6[8]-pd6[9]))*100)   
    elif int(our)> pd6[9]:
        secon2="40 A"
        secon2per=float(((int(our)-pd6[9])/(pd6[8]-pd6[9]))*100)
    elif int(our) > int((pd6[9]-pd6[10])*float(afccc)+pd6[10]):
        secon2="40 A+" 
        secon2per=float(((int(our)-pd6[10])/(pd6[9]-pd6[10]))*100)
    elif int(our)> pd6[10]:
        secon2="32 A"
        secon2per=float(((int(our)-pd6[10])/(pd6[9]-pd6[10]))*100)
    elif int(our) > int((pd6[10]-pd6[11])*float(afccc)+pd6[11]):
        secon2="32 A+"
        secon2per=float(((int(our)-pd6[11])/(pd6[10]-pd6[11]))*100) 
    elif int(our)> pd6[11]:
        secon2="25 A"  
        secon2per=float(((int(our)-pd6[11])/(pd6[10]-pd6[11]))*100) 
    elif int(our) > int((pd6[11]-pd6[12])*float(afccc)+pd6[12]):
        secon2="25 A+"  
        secon2per=float(((int(our)-pd6[12])/(pd6[11]-pd6[12]))*100)        
    e.delete(0,END)
    e.insert(0 , str("급탕2차 관경"))
    e.insert(our, str("→ "))
    e.insert(our,secon2)
    e.insert(our,"("+checked6.get()+")")
    e.insert(our,"("+str(round(secon2per,2))+"%)") 
    hh=e.get()
    f.insert(tk.INSERT,hh+"\n"+"\n")
    gggg0.delete(0,END)
    gggg0.insert(0,our)
    gggg3.delete(0,END)
    gggg3.insert(0,secon2+" ("+str(round(secon2per,1))+"%)")
    e.delete(0,END)
  
    e.insert(our,our)
    add_command3()
    return



myFont = font.Font(size=2)

button_1 = Button(root, text="1", width=11,height=4, command=lambda : button_click(1))
button_1.configure(highlightbackground="red",cursor="dotbox" ,relief="raised")
button_1.grid(row=3, column=0)
button_2 = Button(root, text="2", width=11,height=4,cursor="dotbox" ,command=lambda : button_click(2)).grid(row=3, column=1)
button_3 = Button(root, text="3", width=11,height=4,cursor="dotbox" ,command=lambda : button_click(3)).grid(row=3, column=2)
button_4 = Button(root, text="4", width=11,height=4,cursor="dotbox" ,command=lambda : button_click(4)).grid(row=2, column=0)
button_5 = Button(root, text="5", width=11,height=4,cursor="dotbox", command=lambda : button_click(5)).grid(row=2, column=1)
button_6 = Button(root, text="6", width=11,height=4 ,cursor="dotbox",command=lambda : button_click(6)).grid(row=2, column=2)
button_7 = Button(root, text="7", width=11,height=4,cursor="dotbox" ,command=lambda : button_click(7)).grid(row=1, column=0)
button_8 = Button(root, text="8", width=11,height=4,cursor="dotbox" ,command=lambda : button_click(8)).grid(row=1, column=1)
button_9 = Button(root, text="9", width=11,height=4,cursor="dotbox" ,command=lambda : button_click(9)).grid(row=1, column=2)
button_0 = Button(root, text="0", width=11,height=4,cursor="dotbox", command=lambda : button_click(0)).grid(row=4, column=1)

button_exe1 = Button(root, text="연결열부하",font= ("NanumGothicBold","9"),bg="#CEF6F5", width=11,height=2,borderwidth=3,cursor="exchange", command=button_exe1)
button_exe1.grid(row=6, column=2)  
# button_pump = Button(root,  text="난방HX 용량\n↓\n출력:난방PP ",font= ("NanumGothicBold","9"),bg="white", padx=1.1, pady=13, command= button_pump).grid(row=4,column=0,sticky = N+E+W+S)
# button_exp = Button(root, text="난방HX 용량\n↓\n 출력:팽창탱크",font= ("NanumGothicBold","9"),bg="white", padx=3.48, pady=13, command= button_exp).grid(row=4,column=2,sticky = N+E+W+S )
button_clear = Button(root,text="Clear",font= ("NanumGothicBold","9"), width=11,height=2,borderwidth=3,cursor="watch", command= button_clear).grid(row=5,column=2,padx=3,pady=2)
button_our = Button(root, text="세대수△T40℃ \n↓\n 출력:급탕HX",font= ("NanumGothicBold","9"),width=11,height=5,cursor="exchange", command= button_our).grid(row=4,column=0)
button_our2 = Button(root, text="세대수△T50℃ \n↓\n 출력:급탕HX",font= ("NanumGothicBold","9"),width=11,height=5,cursor="exchange", command= button_our2).grid(row=4,column=2,padx=3,pady=3)
#  CEF6F5   ,  F6D8CE ,   F5F6CE

button_exe2 = Button(root,text="난방 HX",font= ("NanumGothicBold","9"),bg="#F6D8CE", width=11,height=2,cursor="exchange",borderwidth=3, command= button_exe2)
button_exe2.grid(row=7,column=2)


button_exe3 = Button(root,text="급탕 HX",font= ("NanumGothicBold","9"),bg="#F5F6CE",width=11,height=2,cursor="exchange",borderwidth=3, command= button_exe3)
button_exe3.grid(row=11,column=2)

button_exe1.bind('<Button-3>', view_command1)
button_exe2.bind('<Button-3>', view_command2)
button_exe3.bind("<Button-3>", view_command3)

button_cold = Button(root,text="냉동기",font= ("NanumGothicBold","8"),bg="#CEF6F5",width=11,height=2,cursor="exchange",borderwidth=3, command= simple)
button_cold.grid(row=14,column=0)


def selected1(event):
    global pd1
    if checked1.get() == "신우" :
        pd1=[650,450,320,185,150,90,68,44,25,17,11,9]
    elif checked1.get() == "신한" :
        pd1=[590,480,327,222,146,93,58,37,23,14,9,6]
    elif checked1.get() == "삼양" :
        pd1=[100000,90000,288,200,128,72,50,32,18,12.5,8]
    elif checked1.get() == "삼손" :
        pd1=[583.5,490.1,326.7,221.7,145.8,93.3,58.3,37.3,23.3,14.5,9.3,5.8,3.7]
    elif checked1.get() == "경영" :
        pd1=[100000,90000,490.1,332.6,204.2,128.3,93.3,35,23.3,14.5,8.7,5.8]

option1 = ["신우","신한","삼양","삼손","경영"]
pd1=[650,450,320,185,150,90,68,44,25,17,11,9]
checked1=StringVar()
checked1.set(option1[0])
drop1 = OptionMenu(root, checked1,*option1, command = selected1)
drop1.config(width=7,font= ("NanumGothicBold","9"),bg="#CEF6F5",cursor="plus",borderwidth=4)
drop1.grid(row=5,column=1)
myLabel1 = Label(root, text="PDCV제조사 →").grid(row=5,column=0)


def selected2(event):
    global pd7
    global pd8
    global pdd99
    global pdddd
    if checked7.get() =="복사":
        pd7=[28195,15686,7580,4803,2726,1353,854,447,232,157,77,42,19,1]
        pd8=0.01678
        pdd99=15
        pdddd=65
    if checked7.get() =="대류":
        pd7=[26026,14479,6996,4433,2526,1249,788,413,214,144.7,71.1,38.4,17.1,1]
        pd8=0.02243*2/3
        pdd99=20
        pdddd=60
    if checked7.get() =="대류△10℃":
        pd7=[26026,14479,6996,4433,2526,1249,788,413,214,144.7,71.1,38.4,17.1,1]
        pd8=0.01421*2/3
        pdd99=10
        pdddd=60



option7 = ["복사","대류","대류△10℃"]
pd7=[28195,15686,7580,4803,2726,1353,854,447,232,157,77,42,19,1]
pd8=0.01678
pdd99 = 15
pdddd = 65
checked7=StringVar()
checked7.set(option7[0])
drop7 = OptionMenu(root, checked7, *option7, command = selected2)
drop7.config(width=7,font= ("NanumGothicBold","9"),cursor="plus",bg="#F6D8CE",borderwidth=4)
drop7.grid(row=10,column=1)
myLabel17=Label(root, text="난방방식 → ",width=10,height=1)
myLabel17.config(anchor=E)
myLabel17.grid(row=10,column=0)



def selected3(event):
    global afc
    afc = checked10.get()   

option10 = [0.85,0.84,0.83,0.82,0.81,0.80,0.79,0.78,0.77,0.76,0.75,0.74,0.73,0.72,0.71,0.70,0.60,0.59,0.58,0.57,0.56,0.55,0.54,0.53,0.52,0.51,0.50,0.49,0.48,0.47,0.46,0.45]
afc=0.8
checked10=StringVar()
checked10.set(option10[5])
drop10 = OptionMenu(root, checked10, *option10, command = selected3)
drop10.config(width=7,font=("NanumGothicBold","9"),cursor="plus",bg="#F6D8CE",borderwidth=4)
drop10.grid(row=7,column=1)
myLabel10=Label(root, text="A.F → ",anchor=W,width=10,height=1)
myLabel10.config(anchor=E)
myLabel10.grid(row=7,column=0)



#---------------------------------------------------------------------------------------------------------------------------------
def selected333(event):
    global afccc
    afccc = checked1000.get()   
   
option1000 = [0.98,0.97,0.96,0.95,0.94,0.93,0.92,0.91,0.90,0.85,0.80,0.75,0.70,0.65,0.60,0.55,0.50]
afccc=0.95
checked1000=StringVar()
checked1000.set(option1000[3])
drop1000 = OptionMenu(root, checked1000, *option1000, command = selected333)
drop1000.config(width=7,font=("NanumGothicBold","9"),cursor="plus",borderwidth=4)
drop1000.grid(row=14,column=2)
myLabel1000=Label(root, text="관경UP %→ ",anchor=W,width=11,height=2)
myLabel1000.config(anchor=E)
myLabel1000.grid(row=14,column=1)

#----------------------------------------------------------------------------------------------------------------------------------

def selected4(event):
    global pd2
    if checked2.get() == "급탕1단" :
        pd2=[32500,16250,9750,6500,4550,2925,1625,975,650,390,228,98] 
    if checked2.get() == "급1대류" :
        pd2=[30000,15000,9000,6000,4200,2700,1500,900,600,360,210,90]    
    if checked2.get() == "급탕2단" :
        pd2=[37500,18750,11250,7500,5250,3375,1875,1125,750,450,263,113]  
    if checked2.get() =="급2대류":
        pd2=[35000,17500,10500,7000,4900,3150,1750,1050,700,420,245,105]
checked2=StringVar()
option2 = ["급탕2단","급탕1단","급2대류","급1대류"]
pd2=[37500,18750,11250,7500,5250,3375,1875,1125,750,450,263,113] #연결열부하값으로 열량계 결정(급탕2단여부에 따라 다름 동일연결열부하값이라면 일반이 쬐근 더 큰 열량계 관경인듯 )

checked2=StringVar()
checked2.set(option2[0])
drop2 = OptionMenu(root, checked2,*option2, command = selected4)
drop2.config(width=7,font= ("NanumGothicBold","9"),cursor="plus",bg="#CEF6F5",borderwidth=4)
drop2.grid(row=6,column=1)
myLabel2 = Label(root, text="급탕열교환기 →")
myLabel2.grid(row=6,column=0)



def selected5(event):
    global pd3
    if checked3.get() == "SIEMENS" :
        pd3=[420.1,291.7,186.7,116.7,73.5,46.6,29.1,18.6,11.6,7.3,4.6,0.1]
    if checked3.get() == "LS사우타" :
        pd3=[408.4,291.7,186.7,116.7,73.5,46.6,29.1,18.6,11.6,7.3,4.6]
    if checked3.get() == "나라콘트롤" :
        pd3=[396.7,291.7,186.7,116.7,73.5,46.6,29.1,12,11.6,7,4.6]
    if checked3.get() == "제니스" :
        pd3=[330.2,219.3,151.7,106.1,75.8,45.5,29.1,18.6,11.6,5.8,3.8]
    if checked3.get() == "덕산메카시스" :
        pd3=[350.1,233.4,144.7,91,57.1,36.1,29.1,14,11.6,5.8,3.5]
    if checked3.get() == "에스체테" :
        pd3=[373.4,291.7,186.7,116.7,73.5,46.6,29.1,18.6,11.6,7.3,4.6]
    if checked3.get() == "디토" :
        pd3=[350.1,223.4,144.7,91,57.1,36.1,29.1,18.6,14,7.3,4.6]
    if checked3.get() == "국제콘트로닉스" :
        pd3=[314.1,199.4,124.6,79.7,62.7,39.7,24.8,15.8,9.9,6.1,3.9]
    if checked3.get() == "국제BMS" :
        pd3=[330.2,219.3,151.7,106.1,75.8,45.5,29.1,18.6,11.6,5.8,3.5]
    if checked3.get() == "오토메이션" :
        pd3=[350.1,223.4,144.7,91,57.1,36.1,22.1,14,11.6,5.8,3.5]
    if checked3.get() == "아이콘트롤스" :
        pd3=[466.8,291.7,186.7,116.7,73.5,44.4,29.1,18.6,11.6,7.3,4.6]
    if checked3.get() == "댄포스" :
        pd3=[373.4,256.7,169.2,116.7,73.5,46.6,29.1,18.6,11.6,7.3,4.6]
    if checked3.get() == "한국하니웰" :
        pd3=[420.1,291.7,186.7,116.7,73.5,46.6,29.1,18.6,11.6,7.3,4.6]        

option3 = ["SIEMENS","LS사우타","나라콘트롤","제니스","덕산메카시스","에스체테","디토","국제콘트로닉스","국제BMS","오토메이션","아이콘트롤스","댄포스","한국하니웰"]
pd3=[420.1,291.7,186.7,116.7,73.5,46.6,29.1,18.6,11.6,7.3,4.6,0.1]
checked3=StringVar()
checked3.set(option3[0])
drop3 = OptionMenu(root, checked3,*option3,command = selected5)
drop3.config(width=7,font= ("NanumGothicBold","9"),cursor="plus",bg="#F6D8CE",borderwidth=4)
drop3.grid(row=8,column=1)
myLabel3 = Label(root,width=10, text="난방TCV → ")
myLabel3.config(anchor=E)
myLabel3.grid(row=8,column=0)


def selected6(event):
    global pd4
    if checked4.get() == "STS" :
        pd4=[6834,3846,1840,1160,661.2,326.4,208.8,105.6,54.5,36.5,17.6,8.3,3.6] 
    if checked4.get() == "동관" :
        pd4=[5728,3202,1528,944.2,523.4,246.5,153.2,85.7,40.7,25.5,14.4,7.0,2.6]     
    if checked4.get() == "강관" :
        pd4=[5553,3148,1543,970.4,559.5,282.2,185.6,93.9,50.7,34,16.4,8.9,4.1] 
option4 = ["STS","동관","강관"]
pd4=[6834,3846,1840,1160,661.2,326.4,208.8,105.6,54.5,36.5,17.6,8.3,3.6]
checked4=StringVar()
checked4.set(option4[0])
drop4 = OptionMenu(root, checked4,*option4, command = selected6)
drop4.config(width=7,font= ("NanumGothicBold","9"),cursor="plus",bg="#F6D8CE",borderwidth=4)
drop4.grid(row=9,column=1,pady=5)
myLabel4 = Label(root,width=10, text="2차재질 → ")
myLabel4.config(anchor=E)
myLabel4.grid(row=9,column=0)


def selected7(event):
    global pd5
    if checked5.get() == "SIEMENS" :
        pd5=[420.1,291.7,186.7,116.7,73.5,46.6,29.1,18.6,11.6,7.3,4.6,0.1]
    if checked5.get() == "LS사우타" :
        pd5=[408.4,291.7,186.7,116.7,73.5,46.6,29.1,18.6,11.6,7.3,4.6]
    if checked5.get() == "나라콘트롤" :
        pd5=[396.7,291.7,186.7,116.7,73.5,46.6,29.1,12,11.6,7,4.6]
    if checked5.get() == "제니스" :
        pd5=[330.2,219.3,151.7,106.1,75.8,45.5,29.1,18.6,11.6,5.8,3.8]
    if checked5.get() == "덕산메카시스" :
        pd5=[350.1,233.4,144.7,91,57.1,36.1,29.1,14,11.6,5.8,3.5]
    if checked5.get() == "에스체테" :
        pd5=[373.4,291.7,186.7,116.7,73.5,46.6,29.1,18.6,11.6,7.3,4.6]
    if checked5.get() == "디토" :
        pd5=[350.1,223.4,144.7,91,57.1,36.1,29.1,18.6,14,7.3,4.6]
    if checked5.get() == "국제콘트로닉스" :
        pd5=[314.1,199.4,124.6,79.7,62.7,39.7,24.8,15.8,9.9,6.1,3.9]
    if checked5.get() == "국제BMS" :
        pd5=[330.2,219.3,151.7,106.1,75.8,45.5,29.1,18.6,11.6,5.8,3.5]
    if checked5.get() == "오토메이션" :
        pd5=[350.1,223.4,144.7,91,57.1,36.1,22.1,14,11.6,5.8,3.5]
    if checked5.get() == "아이콘트롤스" :
        pd5=[466.8,291.7,186.7,116.7,73.5,44.4,29.1,18.6,11.6,7.3,4.6]
    if checked5.get() == "댄포스" :
        pd5=[373.4,256.7,169.2,116.7,73.5,46.6,29.1,18.6,11.6,7.3,4.6]
    if checked5.get() == "한국하니웰" :
        pd5=[420.1,291.7,186.7,116.7,73.5,46.6,29.1,18.6,11.6,7.3,4.6]        

option5 = ["SIEMENS","LS사우타","나라콘트롤","제니스","덕산메카시스","에스체테","디토","국제콘트로닉스","국제BMS","오토메이션","아이콘트롤스","댄포스","한국하니웰"]
pd5=[420.1,291.7,186.7,116.7,73.5,46.6,29.1,18.6,11.6,7.3,4.6,0.1]
checked5=StringVar()
checked5.set(option5[0])
drop5 = OptionMenu(root, checked5,*option5, command = selected7)
drop5.config(width=7,font= ("NanumGothicBold","9"),cursor="plus",bg="#F5F6CE",borderwidth=4)
drop5.grid(row=12,column=1)
myLabel5 = Label(root,width=10, text="급탕TCV → ")
myLabel5.config(anchor=E)
myLabel5.grid(row=12,column=0)

def selected8(event):
    global pd6
    if checked6.get() == "STS(한난)" :
        pd6=[16402,9232,4416,2784,1587,783.4,501.1,253.5,130.3,87.5,42.1,19.8,8.7]
    if checked6.get() == "동관(한난)" :
        pd6=[13749,7685,3669,2266,1256,591.5,367.7,205.7,97.8,61.1,34.6,16.8,6.2]     
    if checked6.get() == "STS" :
        pd6=[16402,9232,4416,2784,1587,783.4,501.1,253.5,130.8,87.5,42.1,19.8,8.7]
    if checked6.get() == "동관" :
        pd6=[13749,7685,3669,2266,1256,591.5,367.7,205.7,97.8,61.1,34.6,16.8,6.2]               
        
option6 = ["STS(한난)","동관(한난)","STS","동관"]
pd6=[16402,9232,4416,2784,1587,783.4,501.1,253.5,130.8,87.5,42.1,19.8,8.7]
checked6=StringVar()
checked6.set(option6[2])
drop6 = OptionMenu(root, checked6,*option6, command = selected8)
drop6.config(width=7,font= ("NanumGothicBold","9"),cursor="plus",bg="#F5F6CE",borderwidth=4)
drop6.grid(row=11,column=1)
myLabe6 = Label(root,width=10, text="2차재질 →").grid(row=11,column=0)

pre1=Entry(root,width=11 )
pre1.grid(row=13,column=0)
pre2=Entry(root,width=11 )
pre2.grid(row=13,column=1)
pre3=Button(root,width=11,height=1,text="예열관경",relief="ridge",command=lambda : preheat(7))
pre3.grid(row=13,column=2)
pre1.insert(0,"난방HX용량")
pre2.insert(0,"예열+재열HX")
pre4= Entry(root, width=10,justify="left")
pre4.grid(row=13,column=4,sticky=W)

pre6=Label(root,text="(비고→)").grid(row=12,column=2,sticky=E)
pre5=Entry(root,width=10,justify="left")
pre5.grid(row=12,column=4,sticky=W)



def preheat(heat):
    global ex1
    ex1=1
    prehe=""
    ourpre=pre1.get()
    our=pre2.get() 
    prehe=int(our)/40+int(ourpre)/65

    secon3=""
    if prehe> 433.77:
        secon3="300 A"
    elif prehe> 241.33:
        secon3="250 A"
    elif prehe> 116.62:
        secon3="200 A"    
    elif prehe> 73.89:
        secon3="150 A"
    elif prehe> 41.95:
        secon3="125 A"
    elif prehe> 20.82:
        secon3="100 A"    
    elif prehe> 13.15:
        secon3="80 A"    
    elif prehe> 6.88:
        secon3="65 A"    
    elif prehe> 3.58:
        secon3="50 A"
    elif prehe> 2.41:
        secon3="40 A"
    elif prehe> 1.19:
        secon3="32 A"
    elif prehe> 0.64:
        secon3="25 A"
    elif prehe> 0.29:
        secon3="20 A"               
    e.delete(0,END)
    e.insert(0 , str("1차 예열관경"))
    e.insert(our, str("→ "))
    e.insert(our,secon3+"\n"+"(난방:"+pre1.get()+"Mcal/h, 급탕:"+pre2.get()+"Mcal/h)")
    hh=e.get()
    f.insert(tk.INSERT,hh+"\n"+"\n")
    print(prehe)
    e.delete(0,END)
    # i.insert(0,str("급탕HX 용량"))
    e.insert(our,our)
    pre1.delete(0,END)
    pre2.delete(0,END)
    pre1.insert(0,"난방HX용량")
    pre2.insert(0,"예열+재열HX")
    pre4.delete(0,END)
    pre4.insert(0,secon3)
    # f.grid_forget()
    # i.insert(our," Mcal/hr인 경우")

# mycan=Canvas(root,width=200,height=2)
# mycan.grid(row=11,column=0,columnspan=3)

myLabel21 = Label(root, text='''1. KDHC의 경우 PDCV관경 결정식에서 (△P = Network 최대차압 - 0.7bar) 이므로 Cv값 자체가 작고  
                             인입관경의 1/2 보다 한단계 작은 관경이상으로 결정하며 소음등을 방지하기 위해 6m/s이하의 유속을 권장               
                            2. 2차 난방배관 관경 결정시 2차난방배관 재질 3가지(STS,동관,강관)에 따라 다른 테이블을 적용하였음                           
                            3. 1차 예열관경을 보기 위해서는, 제일 아래줄에 있는 2개의 enntry에 숫자를 직접 입력하고 "예열관경" 버튼을 실행   
                            4. PDCV유량계수 :  Cv=Q/(√∆P)×1.167  = ((연결열부하/∆T)/√∆P)×1.167  ,  ∆T=65℃ ,  ∆P=0.7 로 적용한 상태임         
                            5. 난방TCV유량계수 :  Cv=Q/(√∆P)×1.167  = ((난방HX용량/∆T)/√∆P)×1.167  ,  ∆T=65℃ , ∆P=0.3 로 적용한 상태임      
                            6. 급탕TCV유량계수 :  Cv=Q/(√∆P)×1.167  = ((급탕HX용량/∆T)/√∆P)×1.167  ,  ∆T=40℃ , ∆P=0.3 로 적용한 상태임      
                            7. 급탕열교환기 용량 결정식 (36+9√(4N-2))×0.8×60×∆T ,  N:세대수 , ∆T=40℃ or 50℃                                                
                            8. TCV제조사가 13개나 입력되어 있지만, 대부분 default값인 SIEMENS 것이 현장에 설치됨 (PDCV는 5개사 중 3개사 혼재함)
                            9. 밀폐식 팽창탱크 용량 산출에서 A.F(유효팽창계수)값이 한난지침에 15층 기준 0.43~0.56이고 기계실인 경우 1.5~2배 용량
                               으로 팽창탱크 용량을 결정, 현재 압축기 부착형 & 팽창기수분리기 카달로그 상에 A.F가 0.8 정도로 기계실에 설치함  
                               A.F = 1-(Pi+1.0332)/(Pf+1.0332)  Pf=Pi+Pmax(통상Pi는 팽창탱크 최소운전압력이고 Pf는 최고운전압력으로 봄)
                            10. 급탕2차 재질선택시 한난과  GS파워가 관경 선택기준?값이 다른데 이유가 무엇인지 현재 모름   
                            11. 대수평균온도차 관련하여, 설계시 Q(열교환기 용량) = K(총괄전열계수) x A(전열면적) x LMTD(대수평균온도차) 임     
                            12. database 관련 : 연결열부하/난방HX/급탕HX 3개에 대해 3개의 데이터베이스가 자동생성됨...비고 란에 입력시 같이 데이터로
                                들어감...비고란에 검토중인 건물명을 넣는 것을 추천.(해당 버튼에서 우클릭해도 데이터베이스 실행됨) 
                            13. 팽창탱크 용량선정 관련하여 : 복사시 Mcal당 30리터, 대류시 Mcal당 20리터로 함, 냉난방겸용 대류시(FCU등) 델타티10도임(대류10)                                                                   
                            Copyright © simsangb@gspower.co.kr ALL RIGHTS RESERVED.
                            14. 현재 TCV를 제외한 모든 관경에 대하여 한단계 아래의 관경과의 차이에서 95%에 육박시 한관경 큰것으로 변환을 하고 "+"표기를 추가함
                                PDCV의 경우는 인입관경보다 두단계 아래의 관경까지만 가능하도록 하고 "+"표기를 추가함    

                                                                                                                                                            ''')
myLabel21.configure(anchor=W)                                                                                                                                                            
myLabel21.grid(row=0,column=8,rowspan=40)
root.mainloop()
