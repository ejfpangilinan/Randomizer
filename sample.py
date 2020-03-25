from tkinter import *
import random



class Randomizer:

	def __init__(self):
		self.root=Tk()
		self.root.geometry('200x350')
		self.root.title('SomeApp')
		self.root.resizable(0,0)
		self.canvas = Canvas(self.root, width=200, height=350, bg='lightblue')
		self.img= PhotoImage(file='ico.png')
		self.img.subsample(1,1)
		self.imgLabel= Label(self.canvas,image=self.img, anchor=N).place(x=38,y=20)
		self.signButton= Button(self.canvas, text='ROLL', command=self.roll).place(x=68,y=200)
		self.canvas.pack()
		self.root.mainloop()

	def roll(self):
		self.img.configure(file='3.png')



if __name__=='__main__':Randomizer()

