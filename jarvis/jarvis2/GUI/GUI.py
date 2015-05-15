import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.lights_on = tk.Button(self)
        self.lights_on["text"] = "On"
        self.lights_on["command"] = self.on_press
        self.lights_off = tk.Button(self)
        self.lights_off["text"] = "Off"
        self.lights_off["bg"] = "blue"
        self.lights_off["command"] = self.off_press
        self.lights_on.pack(side="top")
        self.lights_off.pack(side="right")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

    def off_press(self):
        print("BOOP")

    def on_press(self):
        print("ON")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
