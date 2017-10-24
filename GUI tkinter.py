from tkinter import Tk, BOTH, LEFT, RAISED, X, Y, TOP
from tkinter.ttk import Frame #container for others widgets
from tkinter.ttk import Button, Style, Label, Entry
from PIL import Image, ImageTk



class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        self.style=Style()
        #self.style.theme_use("default")
        #self.style.configure("TFrame",background="#256")

        self.master.title("Fifa Tournament Creator")
        self.pack(fill=BOTH,expand=3)

        frame=Frame(self,relief=RAISED,borderwidth=1)
        frame.pack(fill=BOTH,expand=True)

        logo=Image.open("fifa-logo.jpg")
        logotk=ImageTk.PhotoImage(logo)
        label1=Label(self,image=logotk)
        label1.image=logotk #tutaj zatrzymujemy referencje do obiektu, konieczne bez tego nic nie wyswietlimy
        label1.place(x=0,y=0)


        addPlayerButton=Button(self,text="Dodaj zawodnika",command=self.addPlayerLabel)
        addPlayerButton.pack(side=LEFT,expand=True)
        showListButton=Button(self,text="Lista zawodników")
        showListButton.pack(side=LEFT,expand=True)
        deletePlayerButton=Button(self,text="Usuń zawodnika",command=self.delPlayerLabel)
        deletePlayerButton.pack(side=LEFT,expand=True)
        checkTableButton=Button(self,text="Pokaż tabele")
        checkTableButton.pack(side=LEFT,expand=True)
        startTournamentButton=Button(self,text="Rozpocznij turniej")
        startTournamentButton.pack(side=LEFT,expand=True)
        quitButton=Button(self,text="Zamknij",command=self.master.quit)
        quitButton.pack(side=LEFT,expand=True)


        self.centerWindow()

    def centerWindow(self):
        width=550
        height=400
        screen_width=self.master.winfo_screenwidth()
        screen_height=self.master.winfo_screenheight()

        ww=(screen_width-width)/2
        wh=(screen_height-height)/2

        self.master.geometry('%dx%d+%d+%d' % (width,height,ww,wh))

    def addPlayerLabel(self):

        frame1=Frame()
        frame1.pack(fill=X)

        frame2=Frame()
        frame2.pack(fill=X)

        lbl1=Label(frame1,text="Imie",width=10)
        lbl1.pack(side=LEFT)

        Entry1=Entry(frame1)
        Entry1.pack(fill=X)

        lbl2=Label(frame2,text="Zespół",width=10)
        lbl2.pack(side=LEFT)

        Entry2=Entry(frame2)
        Entry2.pack(fill=X)

        confirmButton=Button(self.master,text="Zatwierdź")
        confirmButton.pack()

    def delPlayerLabel(self):

        frame1=Frame(self)
        frame1.pack(fill=X)

        lbl1=Label(frame1,text="ID",width=10)
        lbl1.pack(side=LEFT,fill=X)

        Entry1=Entry(frame1)
        Entry1.pack(fill=X)

def main():
    root=Tk()
    app=Example()
    root.mainloop()

main()