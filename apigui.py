from tkinter import *
import requests
root=Tk()
temp=StringVar()
te=Entry(root,textvariable=temp,font="Lucida 10 ",fg="blue")
te.grid(row=40,column=4,pady=2)
mintemp=StringVar()
mte=Entry(root,textvariable=mintemp,font="Lucida 10 ",fg="blue")
mte.grid(row=42,column=4,pady=2)
maxtemp=StringVar()
mate=Entry(root,textvariable=maxtemp,font="Lucida 10 ",fg="blue")
mate.grid(row=44,column=4,pady=2)
ftemp=StringVar()
fte=Entry(root,textvariable=ftemp,font="Lucida 10 ",fg="blue")
fte.grid(row=46,column=4,pady=2)
win=StringVar()
wind=Entry(root,textvariable=win,font="Lucida 10 ",fg="blue")
wind.grid(row=40,column=10,pady=2)
wins=StringVar()
winds=Entry(root,textvariable=wins,font="Lucida 10 ",fg="blue")
winds.grid(row=42,column=10,pady=2)
hum=StringVar()
humi=Entry(root,textvariable=hum,font="Lucida 10 ",fg="blue")
humi.grid(row=44,column=10,pady=2)
er=StringVar()
ero=Entry(root,textvariable=er,font="Algerian 20 ",fg="red")
ero.grid(row=50,columnspan=17,pady=50,padx=30)
def home():
        temp.set("NULL")
        te.update()
        mintemp.set("NULL")
        mte.update()
        maxtemp.set("NULL")
        mate.update()
        ftemp.set("NULL")
        fte.update()
        win.set("NULL")
        wind.update()
        wins.set("NULL")
        winds.update()
        hum.set("NULL")
        humi.update()
        er.set("Enter correct city to searched")
        ero.update()
def delhi():
        try:
                r=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=168bb3b4c288d8e44b5cd09ab01e4bc4")
                json_object=r.json();
                temp_k=float(json_object['main']['temp'])
                C=(temp_k-273.15)
                mtemp_k=float(json_object['main']['temp_min'])
                mc=(mtemp_k-273.15)
                matemp_k=float(json_object['main']['temp_max'])
                mac=(matemp_k-273.15)
                ftempk=float(json_object['main']['feels_like'])
                fteC=(ftempk-273.15)
                windd=float(json_object['wind']['deg'])
                windss=float(json_object['wind']['speed'])
                wind_s=3.6*windss
                Humm=float(json_object['main']['humidity'])
                temp.set(C)
                te.update()
                mintemp.set(mc)
                mte.update()
                maxtemp.set(mac)
                mate.update()
                ftemp.set(fteC)
                fte.update()
                win.set(windd)
                wind.update()
                wins.set(wind_s)
                winds.update()
                hum.set(Humm)
                humi.update()
        except Exception as e:
                er.set("Your city is not find")
                ero.update()
def chica():
        try:
                r=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Chicago&appid=168bb3b4c288d8e44b5cd09ab01e4bc4")
                json_object=r.json();
                temp_k=float(json_object['main']['temp'])
                C=(temp_k-273.15)
                mtemp_k=float(json_object['main']['temp_min'])
                mc=(mtemp_k-273.15)
                matemp_k=float(json_object['main']['temp_max'])
                mac=(matemp_k-273.15)
                ftempk=float(json_object['main']['feels_like'])
                fteC=(ftempk-273.15)
                windd=float(json_object['wind']['deg'])
                windss=float(json_object['wind']['speed'])
                wind_s=3.6*windss
                Humm=float(json_object['main']['humidity'])
                temp.set(C)
                te.update()
                mintemp.set(mc)
                mte.update()
                maxtemp.set(mac)
                mate.update()
                ftemp.set(fteC)
                fte.update()
                win.set(windd)
                wind.update()
                wins.set(wind_s)
                winds.update()
                hum.set(Humm)
                humi.update()
        except Exception as e:
                er.set("Your city is not find")
                ero.update()
def cana():
        try:
                r=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Canada&appid=168bb3b4c288d8e44b5cd09ab01e4bc4")
                json_object=r.json();
                temp_k=float(json_object['main']['temp'])
                C=(temp_k-273.15)
                mtemp_k=float(json_object['main']['temp_min'])
                mc=(mtemp_k-273.15)
                matemp_k=float(json_object['main']['temp_max'])
                mac=(matemp_k-273.15)
                ftempk=float(json_object['main']['feels_like'])
                fteC=(ftempk-273.15)
                windd=float(json_object['wind']['deg'])
                windss=float(json_object['wind']['speed'])
                wind_s=3.6*windss
                Humm=float(json_object['main']['humidity'])
                temp.set(C)
                te.update()
                mintemp.set(mc)
                mte.update()
                maxtemp.set(mac)
                mate.update()
                ftemp.set(fteC)
                fte.update()
                win.set(windd)
                wind.update()
                wins.set(wind_s)
                winds.update()
                hum.set(Humm)
                humi.update()
        except Exception as e:
                er.set("Your city is not find")
                ero.update()
def weather():
        try:
                r=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={s1.get()}&appid=168bb3b4c288d8e44b5cd09ab01e4bc4")
                json_object=r.json();
                temp_k=float(json_object['main']['temp'])
                C=(temp_k-273.15)
                mtemp_k=float(json_object['main']['temp_min'])
                mc=(mtemp_k-273.15)
                matemp_k=float(json_object['main']['temp_max'])
                mac=(matemp_k-273.15)
                ftempk=float(json_object['main']['feels_like'])
                fteC=(ftempk-273.15)
                windd=float(json_object['wind']['deg'])
                windss=float(json_object['wind']['speed'])
                wind_s=3.6*windss
                Humm=float(json_object['main']['humidity'])
                temp.set(C)
                te.update()
                mintemp.set(mc)
                mte.update()
                maxtemp.set(mac)
                mate.update()
                ftemp.set(fteC)
                fte.update()
                win.set(windd)
                wind.update()
                wins.set(wind_s)
                winds.update()
                hum.set(Humm)
                humi.update()
        except Exception as e:
                er.set("Your city is not find")
                ero.update()
root.geometry("1920x1080")
root.title("Weather")
root.wm_iconbitmap("1779940.ico")
Label(root,text="Weather-x",font="Algerian 25 bold",fg="brown").grid(row=1,column=2,padx=10)
Button(root,text="Search",command=weather,font="Arial 12 ",fg="red").grid(row=1,column=11,padx=11)
s1=StringVar()
mymenu=Menu(root)
m1=Menu(mymenu,tearoff=0)
m1.add_command(label="Delhi",command=delhi,font="lucida 15")
m1.add_command(label="Chicago",command=chica,font="lucida 15")
m1.add_separator()
m1.add_command(label="Canada",command=cana,font="lucida 15")
root.config(menu=mymenu,)
mymenu.add_cascade(label="Check here",menu=m1,font="Algerian 30 bold")
# canv=Canvas(root)
# canv.grid(rowspan=3,columnspan=3)
# canv.create_rectangle(10,0,20,60,width=2,outline="blue")
Entry(root,textvariable=s1,font="Arial 15 ").grid(row=1,column=10,padx=12)
Label(root,text="pricing",font="Arial 12 ").grid(row=1,column=9,padx=12)
Button(root,text="Home",font="Arial 12 ",command=home).grid(row=1,column=7,padx=12)
Label(root,text="Weather for city",font="lucida 25 bold",pady=30).grid(row=20,columnspan=35,pady=20)
f2=Frame(root,padx=20).grid(row=6,column=5)
l1=Label(root,text="Temparatue",font="Lucida 25 bold",fg="blue",pady=15).grid(row=30,column=3,padx=35)
Label(root,text="Wind Properties",font="Lucida 25 bold",fg="blue",pady=15).grid(row=30,column=9,padx=35)
Label(root,text="Temparature :-",font="Arial 14").grid(row=40,column=3)
Label(root,text="Min Temparature :-",font="Arial 14").grid(row=42,column=3)
Label(root,text="Max Temparature :-",font="Arial 14").grid(row=44,column=3)
Label(root,text="Fells Like:-",font="Arial 14").grid(row=46,column=3)
Label(root,text="Wind Degree :-",font="Arial 14").grid(row=40,column=9)
Label(root,text="Wind speed :-",font="Arial 14").grid(row=42,column=9)
Label(root,text="Humidity:-",font="Arial 14").grid(row=44,column=9)
Label(root,text="* All temparature unit are in degreee celcius",fg="red",font="Arial 10").grid(row=80,columnspan=5)
Label(root,text="* wind speed in km/hr",fg="red",font="Arial 10").grid(row=82,columnspan=4)
Label(root,text="* Humidity is %",fg="red",font="Arial 10").grid(row=84,columnspan=4)
Button(root,text="Exit",font="Algerian 25 bold ",bg="red",fg="green",command=root.destroy).grid(row=90,columnspan=15)
root.mainloop()