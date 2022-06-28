import tkinter as tk

label_font_style = ("Arial",40, "bold")
small_font_style = ("Arial",16)
Light_gray = "#F5F5F5"
digit_font = ("Arial", 24, "bold")
default_font =("Arial", 20)
off_white = "#F8FAFF"
white="#FFFFFF"
light_blue="#CCEDFF"
lable_color = "#25265E"


class calculator:

    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")
        self.total_expression =""
        self.current_expression =""
        self.display_frame=self.create_display_frame()
        self.total_label,self.labels = self.create_display_labels()
        self.digits = {
            7:(1,1),8:(1,2),9:(1,3),4:(2,1),5:(2,2),
            6:(2,3),1:(3,1),2:(3,2),3:(3,3),
            0:(4,2),".":(4,1)
        }

        self.operations ={"/": "\u00F7", "*": "\u00D7","-": "-","+": "+" }
        self.buttons_frame=self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0,weight=1)
        for x in range(1,5):
            self.buttons_frame.columnconfigure(x,weight=1)

        
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_button()
        self.bind_keys()

    def bind_keys(self):
        self.window.bind("<Return>",lambda event: self.evaluate()) 
        for key in self.digits:
            self.window.bind(str(key), lambda event,digit=key:self.add_to_expression(digit))   

        for key in self.operations:
            self.window.bind(key, lambda event, op=key:self.append_operator(op))    
        
    def create_special_button(self):
        self.create_clear_button()
        self.create_equal_button()
        self.create_square_button()
        self.create_squareroot_button()
            
    def create_display_labels(self):
        total_labels = tk.Label(self.display_frame, text=self.total_expression , anchor=tk.E,fg=lable_color,bg=Light_gray,padx=24,font=small_font_style)
        total_labels.pack(expand=True,fill="both")



        labels = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E,fg=lable_color,bg=Light_gray,padx=24,font=label_font_style)
        labels.pack(expand=True,fill="both")

        return total_labels,labels

    def clean(self):
            self.current_expression=" "
            self.total_expression=" "
            self.update_total_label()
            self.update_label()
    
    def evaluate(self):
         self.total_expression += self.current_expression
         self.update_total_label()
         
         self.current_expression =str(eval(self.total_expression))

         self.total_expression= " "
         self.update_label()


    def create_display_frame(self):
          frame =tk.Frame(self.window,height=221,bg=Light_gray) 
          frame.pack(expand=True,fill="both")  
          return frame   

    def add_to_expression(self,value1):
        self.current_expression += str(value1)
        self.update_label()


    def create_digit_buttons(self):

        for digit,value in self.digits.items():

             button=tk.Button(self.buttons_frame, text=str(digit),bg=white,fg=lable_color,font=digit_font,borderwidth=0,command=lambda x=digit : self.add_to_expression(x))
             button.grid(row=value[0],column=value[1],sticky=tk.NSEW)

    def append_operator(self,operator):
          self.current_expression += operator
          self.total_expression += self.current_expression
          self.current_expression = " "
          self.update_total_label()
          self.update_label()



    def create_operator_buttons(self):
        i=0
        for op,sym in self.operations.items():
            button=tk.Button(self.buttons_frame,text=sym,bg=off_white,fg=lable_color,font=default_font,borderwidth=0,command=lambda x=op:self.append_operator(x))
            button.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1

    def create_clear_button(self):
         
         button=tk.Button(self.buttons_frame,text="C",bg=off_white,fg=lable_color,font=default_font,borderwidth=0,command=lambda:self.clean())
         button.grid(row=0,column=1,sticky=tk.NSEW)

    def square(self):
         self.current_expression = str((eval(f"{self.current_expression}**2")))
         self.update_label()

    def create_square_button(self):
         
         button=tk.Button(self.buttons_frame,text="x\u00b2",bg=off_white,fg=lable_color,font=default_font,borderwidth=0,command=lambda:self.square())
         button.grid(row=0,column=2,sticky=tk.NSEW)  

    def squareroot(self):
         self.current_expression = str((eval(f"{self.current_expression}**0.5")))
         self.update_label()

    def create_squareroot_button(self):
         
         button=tk.Button(self.buttons_frame,text="\u221ax",bg=off_white,fg=lable_color,font=default_font,borderwidth=0,command=lambda:self.squareroot())
         button.grid(row=0,column=3,sticky=tk.NSEW) 


    def create_equal_button(self):
         
         button=tk.Button(self.buttons_frame,text="=",bg=light_blue,fg=lable_color,font=default_font,borderwidth=0,command=lambda:self.evaluate())
         button.grid(row=4,column=3,sticky=tk.NSEW , columnspan=2)




    def create_buttons_frame(self):
          frame =tk.Frame(self.window)
          frame.pack(expand=True,fill="both")
          return frame
    
    def update_total_label(self):
        expression = self.total_expression
        for op,sym in self.operations.items():
            expression=expression.replace(op,f"{sym}")
        self.total_label.config(text=expression)

    def update_label(self):
        self.labels.config(text=self.current_expression[:11])




    def run(self):
        self.window.mainloop()    



if __name__ == "__main__":
     
     calc=calculator()
     calc.run()




  