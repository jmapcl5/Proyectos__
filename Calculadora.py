import tkinter as tk

import tkinter.ttk as ttk
class Calculadora:
    def __init__(self,master):
        self.master = master
        self.master.title("Calculadora")
        self.master.geometry("310x280+100+100") #100 izq 100 arriba
        self.master.resizable(1, 1)
        self.master.iconbitmap("icon_calc.ico") #coloca iconos
        self.master.config(bg="#000000")

        
        frm=tk.Frame(self.master, bg="#FFE668")
        frm.pack(padx=10,pady=10)

        self.var_num=tk.StringVar() # este objeto instanciara un string y lo mostraremos en la pantalla
        self.var_num.set("0") # esto pondra 0 en la pantalla por defecto como las calculadoras
        self.first_num=0
        self.var_op=None 
        self.solved=False
        #widgets 
        self.entDisplay =tk.Entry(frm, width=15,font='"Digital-7 Mono" 20 bold',bd=3,textvariable=self.var_num,justify=tk.RIGHT,bg="#E6FFD9") #bd es para  borde, justify pone el texto en una posicion
        self.btn0=tk.Button(frm,text="0",width=4,font="Arial 16",bg="#FFF77B",command=lambda:self.add_num_display("0"))
        self.btn1=tk.Button(frm,text="1",width=4,font="Arial 16",bg="#FFF77B",command=lambda:self.add_num_display("1"))
        self.btn2=tk.Button(frm,text="2",width=4,font="Arial 16",bg="#FFF77B",command=lambda:self.add_num_display("2"))
        self.btn3=tk.Button(frm,text="3",width=4,font="Arial 16",bg="#FFF77B",command=lambda:self.add_num_display("3"))
        self.btn4=tk.Button(frm,text="4",width=4,font="Arial 16",bg="#FFF77B",command=lambda:self.add_num_display("4"))
        self.btn5=tk.Button(frm,text="5",width=4,font="Arial 16",bg="#FFF77B",command=lambda:self.add_num_display("5"))
        self.btn6=tk.Button(frm,text="6",width=4,font="Arial 16",bg="#FFF77B",command=lambda:self.add_num_display("6"))
        self.btn7=tk.Button(frm,text="7",width=4,font="Arial 16",bg="#FFF77B",command=lambda:self.add_num_display("7"))
        self.btn8=tk.Button(frm,text="8",width=4,font="Arial 16",bg="#FFF77B",command=lambda:self.add_num_display("8"))
        self.btn9=tk.Button(frm,text="9",width=4,font="Arial 16",bg="#FFF77B",command=lambda:self.add_num_display("9"))
        self.btnPoint=tk.Button(frm,text=".",width=4,font="Arial 16",bg="#FFF77B",command=lambda:self.add_num_display("."))
        self.btnEqual=tk.Button(frm,text="=",width=4,font="Arial 16",bg="#FFF561",command=self.solve )
        self.btAdd=tk.Button(frm,text="+",width=4,font="Arial 16",bg="#FFF561",command=lambda:self.set_operation("+"))
        self.btnSub=tk.Button(frm,text="-",width=4,font="Arial 16",bg="#FFF561",command=lambda:self.set_operation("-"))
        self.btnMul=tk.Button(frm,text="x",width=4,font="Arial 16",bg="#FFF561",command=lambda:self.set_operation("x"))
        self.btnDiv=tk.Button(frm,text="/",width=4,font="Arial 16",bg="#FFF561",command=lambda:self.set_operation("/"))
        self.btnDel=tk.Button(frm,text="Del",width=4,font="Arial 16",bg="#FDC056",command=self.clear_display)
        
        self.entDisplay.grid(row=0,column=1,columnspan=3,padx=5,pady=5) #columnspan=a, es para extender desde la column en un ancho de a columnas
        self.btn0.grid(row=4,column=0,padx=5,pady=5)
        self.btn1.grid(row=3,column=0,padx=5,pady=5)
        self.btn2.grid(row=3,column=1,padx=5,pady=5)
        self.btn3.grid(row=3,column=2,padx=5,pady=5)
        self.btn4.grid(row=2,column=0,padx=5,pady=5)
        self.btn5.grid(row=2,column=1,padx=5,pady=5)
        self.btn6.grid(row=2,column=2,padx=5,pady=5)
        self.btn7.grid(row=1,column=0,padx=5,pady=5)    
        self.btn8.grid(row=1,column=1,padx=5,pady=5)      
        self.btn9.grid(row=1,column=2,padx=5,pady=5)
        self.btnPoint.grid(row=4,column=1,padx=5,pady=5)
        self.btnEqual.grid(row=4,column=2,padx=5,pady=5)
        self.btAdd.grid(row=1,column=3,padx=5,pady=5)
        self.btnSub.grid(row=2,column=3,padx=5,pady=5)
        self.btnMul.grid(row=4,column=3,padx=5,pady=5)
        self.btnDiv.grid(row=3,column=3,padx=5,pady=5)
        self.btnDel.grid(row=0,column=0,padx=5,pady=5)
    
    def add_num_display(self,num):
        if self.solved:
            self.clear_display()
            self.solved = False
        if self.var_num.get()=="0" or self.var_num.get()=="Error":
            self.var_num.set("")
        if num=="." and self.var_num.get()=="":
            self.var_num.set("0.")
        if len(self.var_num.get())<12:
            if num=="." and self.var_num.get().count(".") > 0:
                return None
            self.var_num.set(self.var_num.get() + num)
    def set_operation(self, op):
        if self.var_op==None:
            self.var_op=op
            self.first_num=float(self.var_num.get())
            self.clear_display()

    
    def solve(self):
        if self.var_op=="+":
            result=self.first_num + float(self.var_num.get())
        elif self.var_op=="-":
            result=self.first_num - float(self.var_num.get())
        elif self.var_op=="x":
            result=self.first_num * float(self.var_num.get())
        elif self.var_op=="/":
            try:
                result=self.first_num / float(self.var_num.get())
            except ZeroDivisionError: 
                result="Error"
        self.var_op=None
        self.var_num.set(str(result)[:12])
        self.solved=True
    
    def clear_display(self):
        self.var_num.set("0")
def main():
    root=tk.Tk()
    app=Calculadora(root)
    root.mainloop()

#python calculadora.py (__name__:"__main__")
#import calculator (__name__:"calculatora.py")
if __name__ == "__main__":
    main() 