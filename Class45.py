import hashlib
import zlib
from Crypto.Hash import *
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('1200x600')
root.config(bg='orange')
n = StringVar()
v = StringVar()

lbl = Label(root,text="Hash Calculator",font=('arial',80,'bold')
            ,fg='white',bg='orange')
lbl.place(x=200,y=0)
first = ttk.Combobox(root, width = 27, textvariable = n)
first.place(x=600,y=200)

entry= Entry(root,font=('arial',20,'bold'),width=12)
entry.place(x=400,y=200)



first['values'] =        (' MD5', 
                          ' MD4',
                          ' MD2',
                          ' SHA1',
                          ' SHA224',
                          ' SHA256',
                          ' SHA384',
                          ' SHA512',
                          ' Adler 32')

def calc():
    f = first.get()
    
    if f == " MD5":
        f1 = entry.get()
        
        hash_object = hashlib.md5(f1.encode())
        hash = hash_object.hexdigest()
        print("MD5:",hash)
    elif f == " MD4":
        f2 = entry.get()
        hashObject = hashlib.new('md4', f2.encode('utf-8'))
        digest = hashObject.hexdigest()
        print("MD4:",digest)
    elif f == " MD2":
        f3 = entry.get()
        hashObject = MD2.new()
        hashObject.update(f3.encode('utf-8'))
        digest = hashObject.hexdigest()
        print("MD2:",digest)
    elif f == " SHA1":
        f4 = entry.get()
        encoded=f4.encode()
        result = hashlib.sha1(encoded)
        print("SHA1:",result.hexdigest())
    elif f == " SHA224":
        f5 = entry.get()
        encoded=f5.encode()
        result = hashlib.sha224(encoded)
        print("SHA224:",result.hexdigest())
    elif f == " SHA256":
        f6 = entry.get()
        encoded=f6.encode()
        result = hashlib.sha256(encoded)
        print("SHA256:",result.hexdigest())
    elif f ==" SHA384":
        f7 = entry.get()
        encoded=f7.encode()
        reuslt = hashlib.sha256(encoded)
        print("SHA384:",reuslt.hexdigest())
    elif f ==" SHA512":
        f8 = entry.get()
        encoded=f8.encode()
        result = hashlib.sha512(encoded)
        print("SHA512:",result.hexdigest())
    elif f ==" Adler 32":
        f9=entry.get()
        encoded = f9.encode()
        result = zlib.adler32(encoded)
        print("ADLER32:",result)
    
    
        

hashbtn = Button(root,text="Convert",bg='orange',fg='white',width=20,font=('arial',20,'bold'),command=calc)
hashbtn.place(x=500,y=300)
root.mainloop()
