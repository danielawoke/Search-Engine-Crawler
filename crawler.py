total = 100 
from bs4 import BeautifulSoup
import requests
from tkinter import *
from tkinter import ttk
import tkinter as tk
link = "https://www.programiz.com/python-programming/methods/list/remove"
def sss():
	print(entry.get())
	global link
	link = entry.get()
rot = tk.Tk()
var = tk.StringVar()
entry = tk.Entry(rot, width=50)
entry.pack()
btn = Button(rot, text ='Copy and paste the starting URL you wish to use, click the button, then close the window', command=sss)
btn.pack()
var = StringVar()
label = Label(rot,text='Please be patient. 100 links are being found. This may take a minute or two', relief=RAISED)
label2 = Label(rot,text='This project is fundamentally useuless, at best it is what you make of it')
label4 = Label(rot,text='However, getting to see the ties between polarizingly diffrent websites, and the unconvering hidden suprise websites makes this a pretty entertaining toy for what its worth')
label3 = Label(rot,text='If you are a skilled programmer, I made the crawler.py script easy to edit for the "total" value, which is the number of links found')
var.set("Please be patient. 100 links are being found. This may take a minute or two")
label.pack()
label2.pack()
label4.pack()
label3.pack()
rot.mainloop()
print(link)
root = Tk()
AllLinks = []
frm = ttk.Frame(root, padding=0)
root.geometry("700x700")
Lb = Listbox(root)
def crawlerFoundation(url, static):
		vgm_url = url
		html_text = requests.get(vgm_url).text
		soup = BeautifulSoup(html_text, 'html.parser')
		subLinks = []
		for link in soup.find_all('a'):
			subLinks.append(link.get('href'))
		x = 0
		while(x<len(subLinks)):
			while subLinks[x] == None:
				del subLinks[x]
				if(x==len(subLinks)):
					break
			if x<len(subLinks):
				if subLinks[x][0:1] != 'h':
					del subLinks[x]
				else:
					x = x+1
		indexMajor = 0
		indexMinor = 0
		while(indexMinor<len(subLinks)):
			while(indexMajor<len(AllLinks)):
				if(subLinks[indexMinor] == AllLinks[indexMajor]):
					del subLinks[indexMinor]
					indexMinor = indexMinor-1
					break
				indexMajor = indexMajor+1
			indexMinor = indexMinor+1
		x = 0
		while(x<len(subLinks)):
			AllLinks.append(subLinks[x])
			if(len(AllLinks)>total):
				break			
			Lb.insert(static ,subLinks[x])
			print(subLinks[x])
			crawlerFoundation(subLinks[x],static+1)
			x = x+1
while(len(AllLinks)<=total):
	crawlerFoundation(link,0)
Lb.pack(padx=0,pady=0,fill=BOTH, expand=True)
root.mainloop()
print(AllLinks)
# python Desktop\crawler.py
