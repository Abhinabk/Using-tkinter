from tkinter import *
import requests
from tkinter import font
#ce2f3b332e97e2d8d036683294ccacd3
#api.openweathermap.org/data/2.5/forecast?q={city name},{state}&appid={your api key}
root = Tk()
HEIGHT = 700
WIDTH = 800
def wether_res(weather):
    try:
        name = (weather['name'])
        country = (weather['sys']['country'])
        tempr = (weather['main']['temp'])
        condition = (weather['weather'][0]['description'])
        final = f"Name = {name} \n Country = {country} \n Temprature =  {tempr}°C \n Condition = {condition}  "
    except:
        final = f"Sorry no data"
    return final


def getWet(city):
    key = 'ce2f3b332e97e2d8d036683294ccacd3'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    parms = {'APPID':key,'q':city,'units':'metric'}
    response = requests.get(url,params=parms)
    weather = response.json()
    label['text'] = wether_res(weather)


canvas = Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

background_image = PhotoImage(file="/Users/abhinabkrishnatraya/Desktop/py/tkin/landscape.png")
bacground_lable = Label(root,image=background_image)
bacground_lable.place(relwidth=1,relheight=1)


frame = Frame(root,bg='#B8F0FF',bd=2)
frame.place(relx=0.5,rely=0.1,relwidth =0.75,relheight=0.1,anchor="n")

entry=Entry(frame,font =40)
entry.place(relwidth=0.65,relheight=1)

button = Button(frame,text="Get weather",font = ('Ariel',15),command=lambda:getWet(entry.get()))
button.place(relx=0.7,relheight=1,relwidth=0.3)

low_frame = Frame(root,bg='#B8F0FF',bd=10)
low_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label = Label(low_frame,font = ('Bagdad',20))
label.place(relwidth=1,relheight=1)
# print(font.families())
root.mainloop()