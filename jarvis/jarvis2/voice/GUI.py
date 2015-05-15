import tkinter as tk
import wolfy as w

def donothing():
    print("merp")

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        ##MENU
        self.menubar = tk.Menu(root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=donothing)
        self.filemenu.add_command(label="Open", command=donothing)
        self.filemenu.add_command(label="Save", command=donothing)
        self.filemenu.add_command(label="Save as...", command=donothing)
        self.filemenu.add_command(label="Close", command=donothing)

        self.filemenu.add_separator()

        self.filemenu.add_command(label="Exit", command=root.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Help Index", command=donothing)
        self.helpmenu.add_command(label="About...", command=donothing)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        
        self.queryframe = tk.LabelFrame(self,text="Ask Wolfy!", padx=5,pady=5)
        ##|| Contained inside queryframe
        self.title = tk.Label(self.queryframe, text = "Enter Query")
        self.title.pack(side="left")

        self.entry = tk.Entry(self.queryframe, bd = 5)
        self.entry.pack(side='left',padx=5)
        
        self.go = tk.Button(self.queryframe, text="Go",command=self.getText)
        self.go.pack(side="left")
        ##||
        self.queryframe.pack(side='top',padx=10,pady=10)
        
        self.scbr = tk.Scrollbar(self)
        self.scbr.pack(side='right',fill='y')
        self.res = tk.Text(self,state='normal',wrap='word',yscrollcommand=self.scbr.set)
        self.res.pack(anchor='s', side="bottom",padx=10,pady=10)
        self.scbr.config(command = self.res.yview)

    def getText(self):
        text = self.entry.get()
        self.res.insert('insert',"\n--------------------------------------\nQuery: ")
        text= text + '\n'
        self.res.insert('insert',text)
        res = w.returnWolfy(text)
        self.res.insert('insert',res)
        self.res.insert('insert',"\n")

root = tk.Tk()
app = Application(master=root)
root.config(menu=app.menubar)
app.mainloop()
