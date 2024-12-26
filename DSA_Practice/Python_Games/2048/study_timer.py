import tkinter


class study_timer:
    def __init__(self, master):
        self.master = master
        self.mainframe = tkinter.Frame(self.master, bg='white')
        self.mainframe.pack(fill = tkinter.BOTH, expand=True)

        self.build_grid()
        self.build_banner()

    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=0)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=0)

    def build_banner(self):
        banner = tkinter.Label(
            self.mainframe,
            bg='black',
            text='TIMER',
            fg='white',
            font=('Ravie Regular', 30)
        )
        banner.grid(
            row=0, column=0,
            stick='ew',
            padx=10, pady=10
        )

if __name__ == "__main__":
    root = tkinter.Tk()
    ss = study_timer(root)
    root.mainloop()