import tkinter
import tkinter.messagebox
class FiveChessWindows:

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('Five Chess')
        self.window.geometry('600x500')
        self.top = tkinter.Frame(self.window,width = 400,height = 50,bg = 'whitesmoke',borderwidth = 1)
        self.chess = tkinter.Frame(self.window,width = 400,height = 400,bg = 'white',borderwidth = 1)
        self.buttons = tkinter.Frame(self.window,width = 200,height = 500,bg = 'lightgray',borderwidth = 1)
        self.bottom = tkinter.Frame(self.window,width = 400,height = 50,bg = 'whitesmoke',borderwidth = 1)
        self.top.place(x = 0, y = 0)
        self.chess.place(x = 0, y = 50)
        self.buttons.place(x = 400, y = 0)
        self.bottom.place(x = 0, y = 450)
        self.canvas = tkinter.Canvas(self.chess, width = 381, height = 381, bg = 'white', highlightthickness = 1)
        self.canvas.place(x = 10, y = 10)
        self.startChess = False
        self.color = 1
        self.chessarray = [[0 for j in range(19)] for i in range(19)]
        self.start = tkinter.Button(self.buttons, text = 'Start', width = 10, command = self.startFun)
        self.start.place(x = 70, y = 100)
        self.replay = tkinter.Button(self.buttons, text = 'Replay', width = 10, command = self.startFun)
        self.replay.place(x = 70, y = 200)
        self.canvas.bind("<Button-1>", self.events)
        self.window.mainloop()

    def startFun(self):
        self.startChess = True
        self.color = 1
        self.canvas.delete("all")
        self.chessarray = [[0 for j in range(19)] for i in range(19)]
        for line in range(19):
            self.canvas.create_line(line * 20 + 11, 11, line * 20 + 11, 371)
            self.canvas.create_line(11, line * 20 + 11, 371, line * 20 + 11)
    def checkChess(self,cx,cy):
        if cx >= 0 and cx < 19 and cy >= 0 and cy <19 and self.chessarray[cx][cy] == - self.color:
            return True
        else:
            return False
    def checkWin(self,x,y):
        flag1,flag2,flag3,flag4,win = 0,0,0,0,0
        for i in range(1,5):
            if self.checkChess(x + i,y):
                flag1 += 1
            else:
                break
        for i in range(1, 5):
            if self.checkChess(x - i,y):
                flag1 += 1
            else:
                break
        for i in range(1, 5):
            if self.checkChess(x,y + i):
                flag2 += 1
            else:
                break
        for i in range(1, 5):
            if self.checkChess(x,y - i):
               flag2 += 1
            else:
               break
        for i in range(1, 5):
            if self.checkChess(x + i,y + i):
               flag3 += 1
            else:
               break
        for i in range(1, 5):
            if self.checkChess(x - i,y - i):
               flag3 += 1
            else:
               break
        for i in range(1, 5):
            if self.checkChess(x + i,y - i):
               flag4 += 1
            else:
               break
        for i in range(1, 5):
            if self.checkChess(x - i,y + i):
               flag4 += 1
            else:
               break
        if flag1 > 3 or flag2 > 3 or flag3 > 3 or flag4 > 3:
            win = 1
        return win

    def setPiece(self,x,y):
        def drawCircle(self, x, y, r, **kwargs):
            return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)
        if self.chessarray[x][y] == 0 and x < 20 and y < 20 and x >= 0 and y >= 0:
            self.chessarray[x][y] = self.color
            if self.color == 1:
               drawCircle(self.canvas, x * 20 + 11, y * 20 + 11, 10, fill = 'black')
               self.changeColor()
            else:
               drawCircle(self.canvas, x * 20 + 11, y * 20 + 11, 10, fill = 'white')
               self.changeColor()
        else:
           tkinter.messagebox.showinfo("messagebox", "Can not be here")

    def changeColor(self):
        self.color = - self.color

    def events(self,evt):
        if self.startChess:
           mouse_x = evt.x
           mouse_y = evt.y
           chessx = (mouse_x - 1) // 20
           chessy = (mouse_y - 1) // 20
           self.setPiece(chessx,chessy)
           if self.checkWin(chessx,chessy) == 1:
              if self.color == 1:
                 tkinter.messagebox.showinfo("message", "Congratulations black win!")
                 self.startChess = False
              else:
                 tkinter.messagebox.showinfo("message", "Congratulations white win!")
                 self.startChess = False
        else:
            tkinter.messagebox.showinfo("message", "Please click start or replay the game")

i = FiveChessWindows()
