from os import listdir
from color_square import color_square

colors = open("/Users/mark/Documents/Processing/People/colors.txt").readlines()
colors = [c.strip() for c in colors]

dir = "/Users/mark/Documents/Processing/People/complete-photos/"
folders = listdir(dir)

folders = [f for f in folders if not f[0]=="."]

squares = []
total = 0

i = 0
j = 0

for f in folders:

    if f=="affiliated-faculty": continue

    photo_dir = dir+f
    photos = listdir(photo_dir)
    photos = [p for p in photos if not p[:5]=="blank" and not p[0]=="."]
    
    for photo in photos:

        print total, photo_dir+"/"+photo
        squares.append(color_square(photo_dir+"/"+photo,0,0,120,160,i,j))
        total += 1

        j +=  1
        if j>4: 
            j = 0
            i += 1  
mm1 = 100.0
mm2 = 1000.0
mm3 = 1000.0
mm4 = 100.0
vals = [i/mm1 for i in range(int(mm1)+1)] + [1]*10 +\
       [i/mm2 + 1 for i in range(int(mm2)+1)]+ [2]*10 +\
       [i/mm3 + 2 for i in range(int(mm3)+1)] + [3]*10 +\
       [i/mm4 + 3 for i in range(int(mm4)+1)]

v = 0

def setup():
    
    fullScreen(P3D)
    background(51)
    ortho() 
    #size(3840, 940, P3D)

def draw():
    
    global v
    
    background(51)
    translate(width/2.0, height/2.0)
    
    c = 0
    i = 0
    j = 0
    
    if v<len(vals)-1: v += 1
    
    for c in range(len(squares)):
        
        squares[c].update(vals[v])
        squares[c].render(i,j,colors[c])
        
        j +=  1
        if j>4: 
            j = 0
            i += 1