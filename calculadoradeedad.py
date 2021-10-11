import datetime #biblioteca de fecha y hora actual
import tkinter as tk
from PIL import Image,ImageTk #biblioteca que trabaj con imagenes

window=tk.Tk()
window.geometry("480x480")#tamaño de la ventana
window.title(" ¿Que edad tienes? ")#nombre del cuadro
name = tk.Label(text = "NOMBRE")#cuatro etiquetas para colocar en cuadriculas
name.grid(column=0,row=1)#cuadricula
year = tk.Label(text = "AÑO NACIMIENTO")
year.grid(column=0,row=2)
month = tk.Label(text = "MES")
month.grid(column=0,row=3)
date = tk.Label(text = "DIA")
date.grid(column=0,row=4)
nameEntry = tk.Entry()#entrada de usuario para corresponderse a las cuadriculas
nameEntry.grid(column=1,row=1)
yearEntry = tk.Entry()
yearEntry.grid(column=1,row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1,row=3)
dateEntry = tk.Entry()
dateEntry.grid(column=1,row=4)

def getInput():#funcion para obtener las entradas del usuario
    name=nameEntry.get()
    dulzura = Person(name,datetime.date(int(yearEntry.get()),int(monthEntry.get()),int(dateEntry.get())))
    textArea = tk.Text(master=window,height=10,width=25)
    textArea.grid(column=1,row=6)
    answer = "{dulzura}, tu tienes {age} años".format(dulzura=name, age=dulzura.age())
    textArea.insert(tk.END,answer)
    
button=tk.Button(window,text="CALCULAR EDAD",command=getInput,bg="pink")
button.grid(column=1,row=5)
    
class Person:#clase para definir edad del usaurio restandola con la fecha de hoy
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age

image=Image.open('banderines.png')#incorporacion de imagenes
image.thumbnail((300,300),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
label_image=tk.Label(image=photo)
label_image.grid(column=1,row=0)

window.mainloop()
