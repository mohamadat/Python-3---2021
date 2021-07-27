from tkinter import *
# from window import openlink
import webbrowser

window = Tk()

window.title('My Browser')


window.geometry('500x300+200+200')

def button_action():
    openlink()
    entry.delete(0, END)

def openlink():

    the_url_text = x.get()
    print('Opend link...')
    # url = 'https://www.youtube.com'
    # https://www.google.com
    webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
    webbrowser.get('chrome').open(the_url_text)

x = StringVar()

entry = Entry(window,textvar = x).pack()
button = Button(text='Lets Go', command=button_action).pack()

window.mainloop()
