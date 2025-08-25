# school Mark Sheet
from tkinter import *
from tkinter.messagebox import askokcancel


def get_data():
    name=student_name.get()
    if name.strip() == "":
        askokcancel(title="Error", message="Please enter student name.")
        return
    
    if cse_marks.get().strip() == "" or stt_marks.get().strip() == "" or math_marks.get().strip() == "":
        askokcancel(title="Error", message="Please enter marks for all subjects.")
        return
    
    try:
        cse=float(cse_marks.get())
        stt=float(stt_marks.get())
        math=float(math_marks.get())

    except ValueError:
        askokcancel(title="Error", message="Marks must be numbers only!")
        return
    
    if not (0 <= cse <= 100 and 0 <= stt <= 100 and 0 <= math <= 100):
        askokcancel(title="Error", message="Marks must be between 0 and 100.")
        return
    
    total=cse+stt+math
    per=(total/300)*100
    grade=''
    if per >= 80:
      grade = 'A+'
    elif per >= 70:
      grade = 'A'
    elif per >= 60:
      grade = 'B'
    elif per >= 50:
      grade = 'C'
    elif per >= 40:
      grade = 'D'
    else:
      grade = 'Fail'

    show_result(name,total,per,grade)  
    student_name.set("")
    cse_marks.set("")
    stt_marks.set("")
    math_marks.set("")  

def show_result(name,total,per,grade):
    print_data=f'''
    name : {name}
    total marks : {total}
    percentage : {per:.2f}%
    grade : {grade}
    '''
    askokcancel(title='ML School',message=print_data)

#start
win=Tk()
win.title('ML School')
win.config(bg='yellow')
win.geometry('600x500')
win.resizable(False,False)
#-----------------------------------
# titel name
school_name=Label(win,text='ML School',
                  font=('Times New Roman',40,'bold'),bg='yellow')
school_name.place(x=100,y=20,height=40,width=400)
#-------------------------------------------
#variable declear
student_name=StringVar()
cse_marks=StringVar()
stt_marks=StringVar()
math_marks=StringVar()
#student name entry
st_name=Label(win,text='Student name',
              font=('Times New Roman',25,'bold'),bg='yellow')
st_name.place(x=10,y=100,height=40,width=200)

st_name_entry=Entry(win,font=('Times New Roman',25,'bold'),
                    textvariable=student_name)
st_name_entry.place(x=230,y=100,height=40,width=250)
#--------------------------------------------------------------
#student marks titel
sub_name=Label(win,text='Subject Marks',
                  font=('Times New Roman',25,'bold'),bg='yellow')
sub_name.place(x=100,y=160,height=40,width=400)
#---------------------------------------
#subjec number entry
cse_name=Label(win,text='CSE',
              font=('Times New Roman',25,'bold'),bg='yellow')
cse_name.place(x=10,y=220,height=40,width=200)

cse_name_entry=Entry(win,font=('Times New Roman',25,'bold'),
                     textvariable=cse_marks)
cse_name_entry.place(x=230,y=220,height=40,width=250)

stt_name=Label(win,text='STT',
              font=('Times New Roman',25,'bold'),bg='yellow')
stt_name.place(x=10,y=280,height=40,width=200)

stt_name_entry=Entry(win,font=('Times New Roman',25,'bold'),textvariable=stt_marks)
stt_name_entry.place(x=230,y=280,height=40,width=250)

math_name=Label(win,text='MATH',
              font=('Times New Roman',25,'bold'),bg='yellow')
math_name.place(x=10,y=340,height=40,width=200)

math_name_entry=Entry(win,font=('Times New Roman',25,'bold'),textvariable=math_marks)
math_name_entry.place(x=230,y=340,height=40,width=250)
#----------------------------------------------------
#button
button=Button(win,text='Done',
              font=('Times New Roman',20,'bold'),command=get_data)
button.place(x=180,y=400,height=30,width=200)


win.mainloop()