from Tkinter import *


cipher = [["H", "E", "R", ">", "p", "l", "^", "V", "P", "k", "|", "1", "L", "T", "G", "2", "d"],
                   ['N', 'p', '+', 'B', '!', '?', 'O', '%', 'D', 'W', 'Y', '.', '<', '*', 'K', 'f', '@'],
                   ['B', 'y', ':', 'c', 'M', '+', 'U', 'Z', 'G', 'W', '!', '@', 'L', '?', 'z', 'H', 'J'],
                   ['S', 'p', 'p', '7', '^', 'l', '8', '*', 'V', '3', 'p', 'O', '+', '+', 'R', 'K', '2'],
                   ['_', '9', 'M', '+', 'z', 't', 'j', 'd', '|', '5', 'F', 'P', '+', '&', '4', 'k', '/'],
                   ['p', '8', 'R', '^', 'F', 'l', 'O', '-', '*', 'd', 'C', 'k', 'F', '>', '2', 'D', '!'],
                   ['?', '5', '+', 'K', 'q', '%', ';', '2', 'U', 'c', 'X', 'G', 'V', '.', 'z', 'L', '|'],
                   ['!', 'G', '2', 'J', 'f', 'j', '?', 'O', '+', '_', 'N', 'Y', 'z', '+', '@', 'L', '9'],
                   ['d', '<', 'M', '+', 'b', '+', 'Z', 'R', '2', 'F', 'B', 'c', 'y', 'A', '6', '4', 'K'],
                   ['-', 'z', 'l', 'U', 'V', '+', '^', 'J', '+', 'O', 'p', '7', '<', 'F', 'B', 'y', '-'],
                   ['U', '+', 'R', '/', '5', 't', 'E', '|', 'D', 'Y', 'B', 'p', 'b', 'T', 'M', 'K', 'O'],
                   ['2', '<', 'c', 'l', 'R', 'J', '|', '*', '5', 'T', '4', 'M', '.', '+', '&', 'B', 'F'],
                   ['z', '6', '9', 'S', 'y', '?', '+', 'N', '|', '5', 'F', 'B', 'c', '!', ';', '8', 'R'],
                   ['l', 'G', 'F', 'N', '^', 'f', '5', '2', '4', 'b', '.', 'c', 'V', '4', 't', '+', '+'],
                   ['y', 'B', 'X', '1', '*', ':', '4', '9', 'C', 'E', '>', 'V', 'U', 'Z', '5', '-', '+'],
                   ['|', 'c', '.', '3', 'z', 'B', 'K', '!', 'O', 'p', '^', '.', 'f', 'M', 'q', 'G', '2'],
                   ['R', 'c', 'T', '+', 'L', '1', '6', 'C', '<', '+', 'F', 'l', 'W', 'B', '|', '@', 'L'],
                   ['+', '+', '@', 'W', 'C', 'z', 'W', 'c', 'P', 'O', 'S', 'H', 'T', '/', '!', '@', 'p'],
                   ['|', 'F', 'k', 'd', 'W', '<', '7', 't', 'B', '_', 'Y', 'O', 'B', '*', '-', 'C', 'c'],
                   ['>', 'M', 'D', 'H', 'N', 'p', 'k', 'S', 'z', 'Z', 'O', '8', 'A', '|', 'K', ';', '+']]


class Application(Frame):


    def __init__(self, master):
        Frame.__init__(self,master, background="azure4")
        self.grid(column=20,row=25)
        self.create_widgets()

    def create_widgets(self):
        self.place(relx=0.5, rely=0.45, anchor=CENTER)

        """Lable"""
        self.logo = Label(self, text="uZ SCRAMBLE",font=("z340",56,"bold"),fg="Black",  bg="azure4")
        self.logo.grid(row =0, column = 0, columnspan = 19, pady=(70,10))

        self.text = Text(self, bg="seashell3",highlightbackground="black",bd=0, width="34", height="20", font=("courier", 30))
        self.text.grid(row=3, column=2, columnspan = 17, rowspan = 20, sticky="nw", padx=(5,0), pady=(5,0))




# COLUMN GUI
        '''Lables'''
        self.a = Label(self, text="0",font=(16), bg="azure4").grid(row=1, column=2, sticky="W",padx= (15,0))
        self.b = Label(self, text="1",font=(16), bg="azure4").grid(row=1, column=3, sticky="W",padx= (0,0))
        self.c = Label(self, text="2",font=(16), bg="azure4").grid(row=1, column=4, sticky="W",padx= (0,0))
        self.d = Label(self, text="3",font=(16), bg="azure4").grid(row=1, column=5, sticky="W",padx= (0,0))
        self.e = Label(self, text="4",font=(16), bg="azure4").grid(row=1, column=6, sticky="W",padx= (0,0))
        self.f = Label(self, text="5",font=(16), bg="azure4").grid(row=1,column=7, sticky="W",padx= (0,0))
        self.g = Label(self, text="6",font=(16), bg="azure4").grid(row=1, column=8, sticky="W",padx= (0,0))
        self.h = Label(self, text="7",font=(16), bg="azure4").grid(row=1, column=9, sticky="W",padx= (0,0))
        self.i = Label(self, text="8",font=(16), bg="azure4").grid(row=1, column=10, sticky="W",padx= (0,0))
        self.j = Label(self, text="9",font=(16), bg="azure4").grid(row=1,column=11, sticky="W",padx= (0,0))
        self.k = Label(self, text="10",font=(16), bg="azure4").grid(row=1, column=12, sticky="W",padx= (0,0))
        self.l = Label(self, text="11",font=(16), bg="azure4").grid(row=1, column=13, sticky="W",padx= (0,0))
        self.m = Label(self, text="12",font=(16), bg="azure4").grid(row=1, column=14, sticky="W",padx= (0,0))
        self.n = Label(self, text="13",font=(16), bg="azure4").grid(row=1, column=15, sticky="W",padx= (0,0))
        self.o = Label(self, text="14",font=(16), bg="azure4").grid(row=1, column=16, sticky="W",padx= (0,0))
        self.p = Label(self, text="15",font=(16), bg="azure4").grid(row=1, column=17, sticky="W",padx= (0,0))
        self.q = Label(self, text="16",font=(16), bg="azure4").grid(row=1, column=18, sticky="W",padx= (0,10))

        '''Column Data entry'''
        self.ea = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.eb = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.ec = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.ed = Entry(self, bg="seashell3",highlightbackground="black", bd=0, width="2")
        self.et = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.ef = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.eg = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.eh = Entry(self, bg="seashell3",highlightbackground="black", bd=0, width="2")
        self.ei = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.ej = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.ek = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.el = Entry(self, bg="seashell3",highlightbackground="black", bd=0, width="2")
        self.em = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.en = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.eo = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.ep = Entry(self, bg="seashell3",highlightbackground="black", bd=0, width="2")
        self.eq = Entry(self, bg="seashell3",highlightbackground="black", bd=0, width="2")

        self.ea.grid(row=2, column=2, padx= (10,3), sticky="W")
        self.eb.grid(row=2, column=3, padx= (0,3), sticky="W")
        self.ec.grid(row=2, column=4, padx= (0,3), sticky="W")
        self.ed.grid(row=2, column=5, padx= (0,3), sticky="W")
        self.et.grid(row=2, column=6, padx= (0,3), sticky="W")
        self.ef.grid(row=2, column=7, padx= (0,3), sticky="W")
        self.eg.grid(row=2, column=8, padx= (0,3), sticky="W")
        self.eh.grid(row=2, column=9, padx= (0,3), sticky="W")
        self.ei.grid(row=2, column=10, padx= (0,3), sticky="W")
        self.ej.grid(row=2, column=11, padx= (0,3), sticky="W")
        self.ek.grid(row=2, column=12, padx= (0,3),sticky="W")
        self.el.grid(row=2, column=13, padx= (0,3), sticky="W")
        self.em.grid(row=2, column=14, padx= (0,3), sticky="W")
        self.en.grid(row=2, column=15, padx= (0,3), sticky="W")
        self.eo.grid(row=2, column=16, padx= (0,3), sticky="W")
        self.ep.grid(row=2, column=17, padx= (0,3), sticky="W")
        self.eq.grid(row=2, column=18, padx= (0,3), sticky="W")

        self.ea.insert(END, '0')
        self.eb.insert(END, '1')
        self.ec.insert(END, '2')
        self.ed.insert(END, '3')
        self.et.insert(END, '4')
        self.ef.insert(END, '5')
        self.eg.insert(END, '6')
        self.eh.insert(END, '7')
        self.ei.insert(END, '8')
        self.ej.insert(END, '9')
        self.ek.insert(END, '10')
        self.el.insert(END, '11')
        self.em.insert(END, '12')
        self.en.insert(END, '13')
        self.eo.insert(END, '14')
        self.ep.insert(END, '15')
        self.eq.insert(END, '16')
        
        

# ROW GUI

        self.aa = Label(self, text="0",font=(16), bg="azure4").grid(row=3, column=0, sticky="N",pady= (15,0))
        self.bb = Label(self, text="1",font=(16), bg="azure4").grid(row=4, column=0, sticky="N",pady= (8,0))
        self.cc = Label(self, text="2",font=(16), bg="azure4").grid(row=5, column=0, sticky="N",pady= (8,0))
        self.dd = Label(self, text="3",font=(16), bg="azure4").grid(row=6, column=0, sticky="N",pady= (8,0))
        self.ee = Label(self, text="4",font=(16), bg="azure4").grid(row=7, column=0, sticky="N",pady= (8,0))
        self.ff = Label(self, text="5",font=(16), bg="azure4").grid(row=8,column=0, sticky="N",pady= (8,0))
        self.gg = Label(self, text="6",font=(16), bg="azure4").grid(row=9, column=0, sticky="N",pady= (8,0))
        self.hh = Label(self, text="7",font=(16), bg="azure4").grid(row=10, column=0, sticky="N",pady= (8,0))
        self.ii = Label(self, text="8",font=(16), bg="azure4").grid(row=11, column=0, sticky="N",pady= (8,0))
        self.jj = Label(self, text="9",font=(16), bg="azure4").grid(row=12,column=0, sticky="N",pady= (8,0))
        self.kk = Label(self, text="10",font=(16), bg="azure4").grid(row=13, column=0, sticky="N",pady= (8,0))
        self.ll = Label(self, text="11",font=(16), bg="azure4").grid(row=14, column=0, sticky="N",pady= (8,0))
        self.mm = Label(self, text="12",font=(16), bg="azure4").grid(row=15, column=0, sticky="N",pady= (8,0))
        self.nn = Label(self, text="13",font=(16), bg="azure4").grid(row=16, column=0, sticky="N",pady= (8,0))
        self.oo = Label(self, text="14",font=(16), bg="azure4").grid(row=17, column=0, sticky="N",pady= (8,0))
        self.pp = Label(self, text="15",font=(16), bg="azure4").grid(row=18, column=0, sticky="N",pady= (8,0))
        self.qq = Label(self, text="16",font=(16), bg="azure4").grid(row=19, column=0, sticky="N",pady= (8,0))
        self.rr = Label(self, text="17",font=(16), bg="azure4").grid(row=20, column=0, sticky="N",pady= (8,0))
        self.ss = Label(self, text="18",font=(16), bg="azure4").grid(row=21, column=0, sticky="N",pady= (8,0))
        self.tt = Label(self, text="19",font=(16), bg="azure4").grid(row=22, column=0, sticky="N",pady= (8,0))

        '''RoW Data entry'''
        self.ra = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.rb = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.rc = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.rd = Entry(self, bg="seashell3",highlightbackground="black", bd=0, width="2")
        self.re = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.rf = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.rg = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.rh = Entry(self, bg="seashell3",highlightbackground="black", bd=0, width="2")
        self.ri = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.rj = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.rk = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.rl = Entry(self, bg="seashell3",highlightbackground="black", bd=0, width="2")
        self.rm = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.rn = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.ro = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.rp = Entry(self, bg="seashell3",highlightbackground="black", bd=0, width="2")
        self.rq = Entry(self, bg="seashell3",highlightbackground="black", bd=0, width="2")
        self.rr = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="2")
        self.rs = Entry(self, bg="seashell3",highlightbackground="black", bd=0, width="2")
        self.rt = Entry(self, bg="seashell3",highlightbackground="black", bd=0, width="2")

        self.ra.grid(row=3, column=1, pady= (10,1),sticky="S")
        self.rb.grid(row=4, column=1, pady= (6,0), sticky="S")
        self.rc.grid(row=5, column=1, pady= (6,0), sticky="S")
        self.rd.grid(row=6, column=1, pady= (6,0), sticky="S")
        self.re.grid(row=7, column=1, pady= (6,0), sticky="S")
        self.rf.grid(row=8, column=1, pady= (6,0), sticky="S")
        self.rg.grid(row=9, column=1, pady= (6,0), sticky="S")
        self.rh.grid(row=10, column=1, pady= (6,0), sticky="S")
        self.ri.grid(row=11, column=1, pady= (6,0), sticky="S")
        self.rj.grid(row=12, column=1, pady= (6,0), sticky="S")
        self.rk.grid(row=13, column=1, pady= (6,0), sticky="S")
        self.rl.grid(row=14, column=1, pady= (6,0), sticky="S")
        self.rm.grid(row=15, column=1, pady= (6,0), sticky="S")
        self.rn.grid(row=16, column=1, pady= (6,0), sticky="S")
        self.ro.grid(row=17, column=1, pady= (6,0), sticky="S")
        self.rp.grid(row=18, column=1, pady= (6,0), sticky="S")
        self.rq.grid(row=19, column=1, pady= (6,0), sticky="S")
        self.rr.grid(row=20, column=1, pady= (6,0), sticky="S")
        self.rs.grid(row=21, column=1, pady= (6,0), sticky="S")
        self.rt.grid(row=22, column=1, pady= (6,6), sticky="S")

        self.ra.insert(END, '0')
        self.rb.insert(END, '1')
        self.rc.insert(END, '2')
        self.rd.insert(END, '3')
        self.re.insert(END, '4')
        self.rf.insert(END, '5')
        self.rg.insert(END, '6')
        self.rh.insert(END, '7')
        self.ri.insert(END, '8')
        self.rj.insert(END, '9')
        self.rk.insert(END, '10')
        self.rl.insert(END, '11')
        self.rm.insert(END, '12')
        self.rn.insert(END, '13')
        self.ro.insert(END, '14')
        self.rp.insert(END, '15')
        self.rq.insert(END, '16')
        self.rr.insert(END, '17')
        self.rs.insert(END, '18')
        self.rt.insert(END, '19')

        
        '''button'''
        self.started = Button(self, text="JUMBLE", command=self.start_test, width="15", height ="1")
        self.started.config(highlightbackground="azure4", font=("z340",20,"bold"))
        self.started.grid(row=23, columnspan = 19, pady=(15,0))


        '''solution'''
        self.ascii = Label(self, text="ASCII",font=("Z340",36,"bold"),fg="Black",  bg="azure4")
        self.ascii.grid(row =5, column = 20, columnspan = 1, pady=(0,0))
        
        self.sol = Text(self, bg="seashell3",highlightbackground="black",bd=0, width="17", height="20", font=("Courier"))
        self.sol.grid(row=1, column=20, rowspan = 19, padx= (20,16), pady=(0,0))

        self.name = Entry(self, bg="seashell3",highlightbackground="black",bd=0, width="17",  font=("Courier"))
        self.name.grid(row=16, column=20, pady= (0,1),sticky="S")

        self.namefile = Label(self, text="NAME ASCII",font=("Z340",24,"bold"),  bg="azure4").grid(row=15, column=20, sticky="S",pady= (0,0))

        self.save = Button(self, text="SAVE ASCII", command=self.save, width="10")
        self.save.grid(column = 20,row=17, columnspan = 19, pady=(0,0))
        self.save.config( highlightbackground="azure4", font=("z340",16,"bold"))

        self.cred = Label(self, text="PROGRAM BY: BIZu",font=("Z340",20,"bold"), bg="azure4").grid(row=23, column=20, columnspan=3,pady= (15,0))

        
        '''add text to cipher board'''
        for row in cipher:
            self.text.insert(END, str(row).replace("[","").replace("]","").replace(",","").replace("'","")+"\n")




    def start_test(self):
        self.sol.delete(1.0, END)
        self.text.delete(1.0, END)

        
        c1= int(self.ea.get())
        c2= int(self.eb.get())
        c3= int(self.ec.get())
        c4= int(self.ed.get())
        c5= int(self.et.get())
        c6= int(self.ef.get())
        c7= int(self.eg.get())
        c8= int(self.eh.get())
        c9= int(self.ei.get())
        c10= int(self.ej.get())
        c11= int(self.ek.get())
        c12= int(self.el.get())
        c13= int(self.em.get())
        c14= int(self.en.get())
        c15= int(self.eo.get())
        c16= int(self.ep.get())
        c17= int(self.eq.get())

        r1= int(self.ra.get())
        r2= int(self.rb.get())
        r3= int(self.rc.get())
        r4= int(self.rd.get())
        r5= int(self.re.get())
        r6= int(self.rf.get())
        r7= int(self.rg.get())
        r8= int(self.rh.get())
        r9= int(self.ri.get())
        r10= int(self.rj.get())
        r11= int(self.rk.get())
        r12= int(self.rl.get())
        r13= int(self.rm.get())
        r14= int(self.rn.get())
        r15= int(self.ro.get())
        r16= int(self.rp.get())
        r17= int(self.rq.get())
        r18= int(self.rr.get())
        r19= int(self.rs.get())
        r20= int(self.rt.get())

        
        """Reorder text code"""
        movecol =  [[x[c1], x[c2], x[c3], x[c4], x[c5], x[c6], x[c7], x[c8], x[c9], x[c10], x[c11], x[c12], x[c13], x[c14], x[c15], x[c16], x[c17]] for x in cipher]

        roword = [r1, r2, r3, r4, r5, r6, r7, r8, r9,r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20]

        moverow = [movecol[i] for i in roword]

            
        '''Code to output text to txt and on screen'''
        for row in moverow:
            self.sol.insert(END, str(row).replace("[","").replace("]","").replace(",","").replace("'","").replace(" ","")+"\n")
            self.text.insert(END, str(row).replace("[","").replace("]","").replace(",","").replace("'","")+"\n")
 

        
    def save(self):
        cat= "ciphers/" + str(self.name.get()) +".txt"

        
        c1= int(self.ea.get())
        c2= int(self.eb.get())
        c3= int(self.ec.get())
        c4= int(self.ed.get())
        c5= int(self.et.get())
        c6= int(self.ef.get())
        c7= int(self.eg.get())
        c8= int(self.eh.get())
        c9= int(self.ei.get())
        c10= int(self.ej.get())
        c11= int(self.ek.get())
        c12= int(self.el.get())
        c13= int(self.em.get())
        c14= int(self.en.get())
        c15= int(self.eo.get())
        c16= int(self.ep.get())
        c17= int(self.eq.get())

        r1= int(self.ra.get())
        r2= int(self.rb.get())
        r3= int(self.rc.get())
        r4= int(self.rd.get())
        r5= int(self.re.get())
        r6= int(self.rf.get())
        r7= int(self.rg.get())
        r8= int(self.rh.get())
        r9= int(self.ri.get())
        r10= int(self.rj.get())
        r11= int(self.rk.get())
        r12= int(self.rl.get())
        r13= int(self.rm.get())
        r14= int(self.rn.get())
        r15= int(self.ro.get())
        r16= int(self.rp.get())
        r17= int(self.rq.get())
        r18= int(self.rr.get())
        r19= int(self.rs.get())
        r20= int(self.rt.get())

        
        """Reorder text code"""
        movecol =  [[x[c1], x[c2], x[c3], x[c4], x[c5], x[c6], x[c7], x[c8], x[c9], x[c10], x[c11], x[c12], x[c13], x[c14], x[c15], x[c16], x[c17]] for x in cipher]

        roword = [r1, r2, r3, r4, r5, r6, r7, r8, r9,r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20]

        moverow = [movecol[i] for i in roword]

        """txt file code to create multiple txt files"""

        f= open(cat,"w+")

            
        '''Code to output text to txt file'''
        for row in moverow:
            f.write(str(row).replace("[","").replace("]","").replace(",","").replace("'","").replace(" ","")+"\n")

        

# Root Commands
root = Tk()
root.title("Z-Scramble")
app = Application(root)
root.geometry("900x1030+300+300")
root.configure(background='azure4')

root.mainloop()

