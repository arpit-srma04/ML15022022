import tkinter as tkn
app=tkn.Tk()
app.title('calculator')
app.geometry('400x400')


tkn.Label(app,text='a',textvariable='a',font=('',25)).place(x=0,y=0)
tkn.Label(app,text='b',textvariable='b',font=('',25)).place(x=200,y=0)
tkn.Label(app,text='Ans',textvariable='res',font=('',25)).place(x=80,y=200)


a=tkn.Variable(app)
tkn.Entry(app,textvariable=a).place(x=50,y=15)
b=tkn.Variable(app)
tkn.Entry(app,textvariable=b).place(x=250,y=15)
res=tkn.Variable(app)
tkn.Entry(app,textvariable=res).place(x=150,y=210)


def calculator(op):
    res.set(eval(a.get()+op+b.get()))
    
    
tkn.Button(app,text='+',font=('',20),command=lambda:calculator('+')).place(x=0,y=50)
tkn.Button(app,text='-',font=('',20),command=lambda:calculator('-')).place(x=50,y=50)
tkn.Button(app,text='x',font=('',20),command=lambda:calculator('*')).place(x=100,y=50)
tkn.Button(app,text='/',font=('',20),command=lambda:calculator('/')).place(x=150,y=50)


app.mainloop()
