from graphics import *

from math import *

from time import *
global x1
x1 = 50
global y1
y1 = 40


#draw a circle for player and return r,c
def PlayerGetMouse(table,win):   #has modefied it's OK
    a = win.getMouse()
    tx = (a.x-x1+25)/50
    ty = (a.y-y1+25)/50
    r0 = ty+1
    c0 = tx+1
    
    while r0 >15 or c0 >15 or r0 <1 or c0 <1 or table[r0][c0] !=0 :
        a = win.getMouse()
        tx = (a.x-x1+25)/50
        ty = (a.y-y1+25)/50
        r0 = ty+1
        c0 = tx+1

    
    x0 = x1+tx*50
    y0 = y1+ty*50
    c = Circle(Point(x0,y0),20)
    c.setFill("White")
    c.draw(win)
    
    return r0,c0

def ComputerCreateCircle(win,r,c):
    x0 = x1+50*(c-1)
    y0 = y1+50*(r-1)
    c = Circle(Point(x0,y0),20)
    c.draw(win)
    c.setFill("Black")
    for i in range(2):
        sleep(0.2)
        c.undraw()
        sleep(0.1)
        c.draw(win)
   
    

def check(table):      #check if gameover false means over
    for r in range(1,16):
        for c in range(1,16):
            if table[r][c] == 0:
                continue
            if checkiflink0(table,r,c,table[r][c]) >= 5 or checkiflink1(table,r,c,table[r][c]) >= 5 or checkiflink2(table,r,c,table[r][c]) >= 5 or checkiflink3(table,r,c,table[r][c]) >= 5:
                return False
    return True



def iflink0(table,r,c,n):   #find how many chess links in horizon, n means 1(computer) or 2(player) and return the values
    j = c
    count = 0
    blank_one = 0  #numbers of the blank
    blank_two = 0
    while j >= 1 :
        if table[r][j] == n:
            count = count+1
        elif  table[r][j] == 0:
            blank_one = 1
            break
        else:
            break
        j = j-1
        
    j = c+1
    
    while j <= 15 :
        if table[r][j] == n:
            count = count + 1
        elif  table[r][j] == 0:
            blank_two = 1
            break
        else:
            break
            
        j = j+1
        
    return count,blank_one,blank_two
    
def iflink1(table,r,c,n):    #find vertical
    i = r
    count = 0
    blank_one = 0
    blank_two = 0
    
    while i>=1 :
        if table[i][c] == n:
            count = count+1
        elif  table[i][c] == 0:
            blank_one = 1
            break
        else:
            break
        
        i = i-1
        
    i = r+1
    
    while i<=15 :
        if table[i][c] == n:
            count = count + 1
        elif  table[i][c] == 0:
            blank_two = 1
            break
        else:
            break
           
        i = i+1
        
    return count,blank_one,blank_two

def iflink2(table,r,c,n): # find 45 angle
    i = r
    j = c
    count = 0
    blank_one = 0
    blank_two = 0
    
    while i>=1 and j<=15 :
        if table[i][j] == n:
            count = count + 1
        elif  table[i][j] == 0:
            blank_one = blank_one+1
            break
        else:
            break
            
        i = i-1
        j = j+1
        
    i = r+1
    j = c-1
    
    while i<=15 and j>=1 :
        if table[i][j] == n:
            count = count+1
        elif  table[i][j] == 0:
            blank_two = 1
            break
        else:
            break
            
        i = i+1
        j = j-1
        
    return count,blank_one,blank_two

def iflink3(table,r,c,n):  #if link 135 angle
    count = 0
    i = r
    j = c
    blank_one = 0
    blank_two = 0
    
    while i>=1 and j >=1 :
        if table[i][j] == n:
            count = count+1
        elif  table[i][j] == 0:
            blank_one = 1
            break
        else:
            break
        i = i-1
        j = j-1
        
    i = r+1
    j = c+1
    
    while i<=15 and j <=15 :
        if table[i][j] == n:
            count = count+1
        elif  table[i][j] == 0:
            blank_two = 1
            break
        else:
            break
            
        i = i+1
        j = j+1
        
    return count,blank_one,blank_two


def checkiflink0(table,r,c,n):   #find how many chess links in horizon, n means 1(computer) or 2(player) and don't need to calculate the blank
    j = c
    count = 0
    while j >= 1:
        if table[r][j] == n:
            count = count+1
        else:
            break
        j = j-1
    j = c+1
    while j <= 15:
        if table[r][j] == n:
            count = count + 1
        else:
            break
            
        j = j+1
    return count
    
def checkiflink1(table,r,c,n):    #find vertical
    i = r
    count = 0
    while i>=1:
        if table[i][c] == n:
            count = count+1
        else:
            break
        
        i = i-1
    i = r+1
    while i<=15:
        if table[i][c] == n:
            count = count + 1
        else:
            break
           
        i = i+1
    return count

def checkiflink2(table,r,c,n): # find 45 angle
    i = r
    j = c
    count = 0
    while i>=1 and j<=15:
        if table[i][j] == n:
            count = count + 1
        else:
            break
            
        i = i-1
        j = j+1
    i = r+1
    j = c-1
    while i<=15 and j>=1:
        if table[i][j] == n:
            count = count+1
        else:
            break
            
        i = i+1
        j = j-1
    return count

def checkiflink3(table,r,c,n):  #if link 135 angle
    count = 0
    i = r
    j = c
    while i>=1 and j >=1:
        if table[i][j] == n:
            count = count+1
        else:
            break
        i = i-1
        j = j-1
    i = r+1
    j = c+1
    while i<=15 and j <=15:
        if table[i][j] == n:
            count = count+1
        else:
            break
            
        i = i+1
        j = j+1
    return count


def calculate(table,r,c,n):  #calculate the values
    chessnumber_one,blank1_one,blank2_one=iflink0(table,r,c,n)
    chessnumber_two,blank1_two,blank2_two=iflink1(table,r,c,n)
    chessnumber_three,blank1_three,blank2_three=iflink2(table,r,c,n)
    chessnumber_four,blank1_four,blank2_four=iflink3(table,r,c,n)
    value1=getValue(chessnumber_one,blank1_one,blank2_one)
    value2=getValue(chessnumber_two,blank1_two,blank2_two)
    value3=getValue(chessnumber_three,blank1_three,blank2_three)
    value4=getValue(chessnumber_four,blank1_four,blank2_four)

    value = value1+value2+value3+value4   #modefy sth
    return value
    

def getValue(chessnumber,blank1,blank2):
    value = 0
    if chessnumber == 2:
        if blank1+blank2 == 0:
            value = 3
        elif (blank1 == 0 and blank2 !=0) or (blank1 != 0 and blank2 ==0):
            value = 5
        else:
            value = 200
    if chessnumber == 3:
        if blank1+blank2==0:
            value = 50
        elif ( blank1 == 0 and blank2 != 0 ) or (blank1!=0 and blank2 == 0):
            value = 100
        else:
            value = 720
    if chessnumber == 4:
        if blank1+blank2 == 0:
            value = 500
        elif (blank1 == 0 and blank2 !=0) or (blank1 != 0 and blank2 ==0):
            value = 720
        else:
            value = 4320
    if chessnumber == 5:
        value = 50000

    return value
        
class tree:
    def __init__(self,r,c,n):
        self.r=r
        self.c=c
        self.children = []
        self.CP = n
    def getR(self):
        return self.r
    def getC(self):
        return self.c
    def getChildren(self):
        return self.children
    def add(self,tree):
        self.children.append(tree)
    def addValue(self,value):
        self.value = value
    def getValue(self):
        return self.value
    def addDepth(self,depth):
        self.depth = depth
    def getDepth(self):
        return self.depth
    def getCP(self):
        return self.CP
    def deleteTree(self):
        self.children = []

    


    


def createTree(table,root,t):   
    if t >=3:
        return
    s = 0
    for i in range(1,16):
        for j in range(1,16):
            if table[i][j] == 0:
                if t%2 != 0:
                    table[i][j]=1
                    root.add(tree(i,j,1))
                else:
                    table[i][j] = 2
                    root.add(tree(i,j,2))
                value = calculate(table,i,j,t)
        
                root.getChildren()[s].addValue(value)
                
               

                
                createTree(list(table),root.getChildren()[s],t+1)
                s=s+1
                table[i][j]=0
              
                
def searchBest(root):
    record = root
    recordValue = -100000
   
    for i in root.getChildren():
        a = []
        for j in i.getChildren():
            a.append(j.getValue())
            
        a.sort()
        i.addValue(i.getValue()-a[-1])
        
    for i in root.getChildren():
        #print i.getValue()
        if i.getValue()>recordValue:
            #print "YES",i.getValue()
            record = i
            recordValue = i.getValue()
    #print record.getValue()
    return record

        
def createWinLose(win,whowin):
    re = Rectangle(Point(300,290),Point(500,490))
    re.draw(win)
    re.setFill("Blue")
    if whowin == 1:
        t = Text(Point(400,390),"You Lose")
        t.draw(win)
        t.setSize(30)
    else:
        t = Text(Point(400,390),"You Win")
        t.draw(win)
        t.setSize(30)
    return re,t
            

def main():
    global x1
    global y1
    
    table = [[0 for c in range(16)]for r in range(16)]  #record the position
    
    win = GraphWin("Five Chess",800,780)
    r = Rectangle(Point(x1,y1),Point(x1+700,y1+700))
    r.draw(win)
    r.setFill("Yellow")
    t = 0
    for i in range(15):
        Line(Point(x1,y1+t),Point(x1+700,y1+t)).draw(win)
        t = t+50
    t = 0
    for i in range(15):
        Line(Point(x1+t,y1),Point(x1+t,y1+700)).draw(win)
        t = t+50
    cp=2                 #cp=1 means computer , 2 means player
    ComputerCreateCircle(win,8,8)
    table[8][8]=1
    whowin = 0

    while True:
        if cp == 2:
            r,c = PlayerGetMouse(table,win)
            table[r][c]=2
            cp = 1
            if check(table) == False:
                whowin = 2
                
        else:
            root = tree(0,0,0)
            createTree(table,root,1)
            t= searchBest(root)
            table[t.getR()][t.getC()] = 1
            ComputerCreateCircle(win,t.getR(),t.getC())
            cp = 2
            root.deleteTree()
            if check(table) == False:
                whowin = 1
                
            
        if whowin != 0:
            re,words = createWinLose(win,whowin)
            win.getMouse()
            re.undraw()
            words.undraw()
            break
        
      
    win.getMouse()
    win.close()
main()
