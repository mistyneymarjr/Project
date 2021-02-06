from tkinter import *  #this module is used to export gui packets
import time

root=Tk()
root.title("Random Password Generator")
root.geometry("400x200")

Resultstring=""
result=0


def initial():                  #to create the initial pos and store in it result
    temp_res=time.time_ns() 
    global result
    result=temp_res




def rand(mod):                      #sudo random generator
    multiplier=1664599               
    adder=10139042289
    m=2**32
    global result
    result=(result*multiplier+adder)%m
    res=result%mod
    return res






def Randompassword():
    global Resultstring
    list_of_length=[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
    l_string="abcdefghijklmnopqrstuvwxyz"
    r_string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s_string="@!#$%^&*{[]}><\|."
    digit="0123456789"
    string="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@!#$%^&*{[]}><\|."
    Result_string=[]
    lalpha=0
    ralpha=0
    digits=0
    schar=0
    initial()
    l=rand(21)
    initial()
    r1=rand(26)
    r2=rand(26)
    r3=rand(10)
    r4=rand(17)
    r5=rand(26)
    r6=rand(26)
    Result_string.append(l_string[r1])
    Result_string.append(r_string[r2])
    Result_string.append(s_string[r4])
    
    for i in range(3,list_of_length[l]-3):
        c1=rand(53)                             #assigning rand 53 mixtures
        Result_string.append(string[c1])        #append in result_string whatever c1 will point

    Result_string.append(digit[r3])
    Result_string.append(l_string[r6])
    Result_string.append(r_string[r5])
    length=len(Result_string)
    
    for k in range(0,len(Result_string)):
        Resultstring+=str(Result_string[k])         #the list is getting converted to string
    label=Label(root,text="{}".format(Resultstring),fg="black")
    label.grid(row=47,column=239)
  

    




        
def Display_password(String):
   entry.delete(0,'end')                
   entry.insert(0,String)
   global Resultstring
   Resultstring=""



    
entry=Entry(root,width=60,borderwidth=5)
entry.grid(row=35,column=239)
b1=Button(root,text="Generate",borderwidth=5,width=20,bg="grey",command=Randompassword)
b1.grid(row=195,column=239)    
b2=Button(root,text="Copy",borderwidth=3,width=20,bg="grey",command=lambda:Display_password(Resultstring)) 
b2.grid(row=245,column=239)

root.mainloop()













