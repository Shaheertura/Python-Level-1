#----------------------------------------------------Import libs and Modules---------------------------------
try:                                                                                                        #
    from random import randint                                                                              #
    import sys                                                                                              #
    from tkinter import *                                                                                   #
    import tkinter.messagebox                                                                               #
    from tkinter import ttk                                                                                 #
except:                                                                                                     #
    print("[!]Your Python Coudnt Import these Modules\nPython Either needs TO be REINSALLED OR REPAIRED[!]")#
#-----------------------------------------------------------------------------------------------------------#    
def banner():
    banner1 = """
  ___        _   _                _   _           _   _             
 / _ \      | | | |                 | | (_)         | | (_)            
/ /_\ \_   _| |_| |__   ___ _ __ | |_ _  ___ __ _| |_ _  ___  _ __  
|  _  | | | | __| '_ \ / _ \ '_ \| __| |/ __/ _` | __| |/ _ \| '_ \ 
| | | | |_| | |_| | | |  __/ | | | |_| | (_| (_| | |_| | (_) | | | |
\_| |_/\__,_|\__|_| |_|\___|_| |_|\__|_|\___\__,_|\__|_|\___/|_| |_|
                                                                    
                                                                    
 _____           _                                                  
/  ___|         | |                                                 
\ `--. _   _ ___| |_ ___ _ __ ___                                   
 `--. \ | | / __| __/ _ \ '_ ` _ \                                  
/\__/ / |_| \__ \ ||  __/ | | | | |                                 
\____/ \__, |___/\__\___|_| |_| |_|                                 
        __/ |                                                       
       |___/                                                        
                   
                   
                                    
"""
    banner2= """
 █████╗ ██╗   ██╗████████╗██╗  ██╗███████╗███╗   ██╗████████╗██╗ ██████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗██║   ██║╚══██╔══╝██║  ██║██╔════╝████╗  ██║╚══██╔══╝██║██╔════╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
███████║██║   ██║   ██║   ███████║█████╗  ██╔██╗ ██║   ██║   ██║██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║
██╔══██║██║   ██║   ██║   ██╔══██║██╔══╝  ██║╚██╗██║   ██║   ██║██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
██║  ██║╚██████╔╝   ██║   ██║  ██║███████╗██║ ╚████║   ██║   ██║╚██████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                                               
███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗                                                          
██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║                                                          
███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║                                                          
╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║                                                          
███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║                                                          
╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝                                                          
                                                                                                               
                             
                                                                    
                                                                                                                                                                        
                                                  """
    banner3 = """
    #                                                                                  
   # #   #    # ##### #    # ###### #    # ##### #  ####    ##   ##### #  ####  #    # 
  #   #  #    #   #   #    # #      ##   #   #   # #    #  #  #    #   # #    # ##   # 
 #     # #    #   #   ###### #####  # #  #   #   # #      #    #   #   # #    # # #  # 
 ####### #    #   #   #    # #      #  # #   #   # #      ######   #   # #    # #  # # 
 #     # #    #   #   #    # #      #   ##   #   # #    # #    #   #   # #    # #   ## 
 #     #  ####    #   #    # ###### #    #   #   #  ####  #    #   #   #  ####  #    # 
                                                                                       
  #####                                                                                
 #     # #   #  ####  ##### ###### #    #                                              
 #        # #  #        #   #      ##  ##                                              
  #####    #    ####    #   #####  # ## #                                              
       #   #        #   #   #      #    #                                              
 #     #   #   #    #   #   #      #    #                                              
  #####    #    ####    #   ###### #    #                                              
                                                                                       
                                                  
                                                       
                                                                                                                                   
"""
    banners = [banner1,banner2,banner3]
    print(banners[randint(0,2)])
banner()
#-------------------------------------Main-----------------------------------
reglist = {
    "admin" : "admin",
    "User123" : "secret"
}

def main():
    root = Tk()
    app = SalesLogin(root)

class SalesLogin():
    def __init__(self,master):
        self.master = master
        self.master.title("Authentacation System")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="cadet blue")
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, text="Sales Managemnt Login System", font=('arial',60,'bold'),
                              bg='cadet blue', fg="Cornsilk")
        self.lblTitle.grid(row=0, column=0, columnspan=2,pady=20)

        #--------------------------------Frame--------------------------------
        self.LoginFrame1 = LabelFrame(self.frame, width=1350,height=300
                                      ,text="Login",font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=40)
        self.LoginFrame1.grid(row=1,column=0)

        self.LoginFrame2 = LabelFrame(self.frame, width=1000,height=200
                              ,text="Log",font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=40)


        self.LoginFrame2.grid(row=2,column=0)


        #---------------------------------------------------------------------
        self.lblUsername = Label(self.LoginFrame1,text="Username",font=('arial',30,'bold'),bd=22,
                                 bg='cadet blue', fg='Cornsilk')
        self.lblUsername.grid(row=0, column=0)

        self.txtUsername = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=7,textvariable=self.Username,
                                 width=33)
        self.txtUsername.grid(row=0,column=1)

        self.lblPassword = Label(self.LoginFrame1,text="Password",font=('arial',30,'bold'),bd=22,
                                 bg='cadet blue', fg='Cornsilk')
        self.lblPassword.grid(row=1,column=0)

        self.txtPassword = Entry(self.LoginFrame1,font=('aria',30,'bold'),bd=7,textvariable=self.Password,
                                 width=33)
        self.txtPassword.grid(row=1,column=1, columnspan=2,pady=30)

        #---------------------------------------------------------------------
        self.btnLogin = Button(self.LoginFrame2, text='Login',width=15,font=('arial',30,'bold'),
                               bg='cadet BLUE', fg='Cornsilk',command=self.Login_System)
        self.btnLogin.grid(row=3,column=0, pady=20,padx=8)

        self.btnReg = Button(self.LoginFrame2, text='Register',width=15,font=('arial',30,'bold'),
                               bg='cadet blue', fg='Cornsilk',command=self.Registration_window)
        self.btnReg.grid(row=4,column=1, pady=3, padx=8)

        self.btnReset = Button(self.LoginFrame2, text='Reset',width=15,font=('arial',30,'bold'),
                               bg='cadet blue', fg='Cornsilk',command=self.iReset)
        self.btnReset.grid(row=3,column=1, pady=20, padx=8)

        self.btnExit = Button(self.LoginFrame2, text='Exit', width=15,font=('arial',30,'bold'),
                              bg='cadet blue', fg='Cornsilk',command=self.iExit)
        self.btnExit.grid(row=3, column=2, pady=20, padx=8)
        
        #---------------------------------------------------------------------


    def Login_System(self):
        user = (self.Username.get())
        pas = (self.Password.get())
        if user in reglist.keys():
            if pas in reglist.values():
                print("Logged In")
                self.Login_window()
        else:
            tkinter.messagebox.askyesno("Sales Managment Login System", "Invalid Login Details")
            self.Username.set("")
            self.Password.set("")

    def iReset(self):
        self.Username.set("")
        self.Password.set("")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Sales Login Systems", "Confirm if you want to Exit")
        if self.iExit > 0:
            self.master.destroy()
            return

    def Login_window(self):
        self.SaleWindow = Toplevel(self.master)
        self.app = SalesManagement(self.SaleWindow)

    def Registration_window(self):
        self.RegistrationWindow = Toplevel(self.master)
        self.app = Registration(self.RegistrationWindow)

        
        
        

class SalesManagement():
    def __init__(self,master):
        self.master = master
        self.master.title("Sales Management Login System")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="cadet blue")
        self.frame.pack()

class Registration():
    def __init__(self,master):
        self.master = master
        self.master.title("Registration System")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="cadet blue")
        self.frame.pack()

        self.lblTitle = Label(self.frame, text="Registration System", font=('arial',60,'bold'),
                              bg='cadet blue', fg="Cornsilk")
        self.lblTitle.grid(row=0, column=0, columnspan=2,pady=20)


        
        
        #--------------------Frame--------------------------------------------------------------------------------
        self.LoginFrame1 = LabelFrame(self.frame, width=1350,height=300
                                      ,text="Login",font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=40)
        self.LoginFrame1.grid(row=1,column=0)

        self.LoginFrame2 = LabelFrame(self.frame, width=1000,height=200
                                      ,text="Log",font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=40)

        self.LoginFrame2.grid(row=2,column=0)
        #---------------------------------------------------------------------------------------------------------
        self.lblUsername = Label(self.LoginFrame1,text="Username",font=('arial',30,'bold'),bd=22,
                                 bg='cadet blue', fg='Cornsilk')
        self.lblUsername.grid(row=0, column=0)

        self.txtUsername = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=7,
                                 width=33)
        self.txtUsername.grid(row=0,column=1)

        self.lblPassword = Label(self.LoginFrame1,text="Password",font=('arial',30,'bold'),bd=22,
                                 bg='cadet blue', fg='Cornsilk')
        self.lblPassword.grid(row=1,column=0)

        self.txtPassword = Entry(self.LoginFrame1,font=('aria',30,'bold'),bd=7,
                                 width=33)
        self.txtPassword.grid(row=1,column=1, columnspan=2,pady=30)
        #---------------------------------------------------------------------------------------------------------
        self.btnReg = Button(self.LoginFrame2, text='Register',width=15,font=('arial',30,'bold'),
                               bg='cadet BLUE', fg='Cornsilk',command=self.iDone)
        self.btnReg.grid(row=3,column=0, pady=20,padx=8)
        #---------------------------------------------------------------------------------------------------------
    def iDone(self):
        ruser = self.txtUsername.get()
        rpas = self.txtPassword.get()

        reglist[ruser] = rpas

        print(reglist)


        
        


        

if __name__ == '__main__':
    main()








