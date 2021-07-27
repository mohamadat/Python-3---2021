from tkinter import *
# from window import openlink
import webbrowser
def openlink():
    the_url_text = entry.get()
    print('Opend link...')
    # url = 'https://www.youtube.com'
    # https://www.google.com
    webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
    webbrowser.get('chrome').open(url)

window = Tk()

window.title('My Browser')

entry = Entry(window, width=20).pack()


button = Button(text='Lets Go', command=openlink).pack()


#In the end loop
window.mainloop()
