
import pygame
import heapq
import math
import sys
from pygame.locals import*


class Map:

    #khoi tao 
    def __init__(self):
        self.A=[]
        self.petrol=0
        self.M=0

    #doc file de lay du lieu
    def ReadFile(self):

        filepath= 'map.txt'
        
        with open(filepath) as fp:
            self.petrol= int(fp.readline().splitlines()[0])
            self.M= int(fp.readline().splitlines()[0])
            for i in range(0,self.M+1):
                st=fp.readline()
                temp=[]
                for j in range(0,len(st)):
                    if(st[j]=='\n'):
                        break
                    if(st[j]==' '):
                        continue
                    temp.append(int(st[j]))
                    if (len(temp)<self.M-1):
                        continue
                if (len(temp)==self.M):    
                    self.A.append(temp)
            fp.close()

class SearchDFS:

    #ham khoi tao
    def __init__(self,A,M,N):
        self.A=A
        self.M=M #ma tran M*M
        self.N=N #so lit xang ban dau
        self.came_from={}#luu duong di
        self.visited=[]#luu cac diem da di qua
        self.success=False
    
    #ham kiem tra diem nay co con nam trong do thi khong
    def in_bounds(self, pos):
        x, y  = pos
        if (x>=self.M or x<0 or y>=self.M or y<0):
            return False
        return True
        
    #ham kiem tra diem nay co the di qua hay khong (khong la tuong va chua dc mo)
    def passable(self, pos):
        # neu diem nay khong phai la tuong
        x,y=pos[0], pos[1]
        if (self.in_bounds(pos)==False):
            return False

        if (self.A[x][y] != 0 and self.visited[x][y] == False):
            return True
        return False
        
    #ham tra ra nhung diem lan can co the di den
    def neighbors(self, pos):
        #danh sach vi tri co the di qua
        x,y = pos[0], pos[1]
        neighbors = [(x,y-1),(x-1,y),(x+1,y),(x,y+1)]
        valid_neighbors = []

        for i in range(0,len(neighbors)):
            #neu diem nay van con nam trong map và có thể dii, tức không phải là tường
            if (self.passable(neighbors[i])==True):
                valid_neighbors.append(neighbors[i])
        #tra ra danh sach cac vi tri hop le
        return valid_neighbors

    #ham luu vet duong di
    def trace_path(self, start, goal):
        
        curr = goal
        path = []
        while curr != start:
            path.append(curr)
            curr = self.came_from[curr]
        path.append(start)
        path.reverse()
        return path

    #tim kiem DFS
    def DFS(self,start, goal):
        x,y=start
        petrol=self.N
        stack=[(petrol,start)]

        #tao ra list danh dau tat ca cac diem di qua
        for i in range(0,A.M):
            temp=[]
            for j in range(0,A.M):
                temp.append(False)
            self.visited.append(temp)
     
        while len(stack)>0:
            curr_petrol, curr_node=stack.pop()
            x,y=curr_node
            self.visited[x][y]=True 
            
            for i in self.neighbors(curr_node):
                x,y=i
                if (i==goal and curr_petrol-1>=0):
                    self.came_from[goal]=curr_node
                    self.visited[x][y]=True
                    self.success =True
                    return
                elif (curr_petrol-1==0 and self.A[x][y]!=2):#het xang ma tai diem dang dung khong phai la cay xang
                    self.visited[x][y]=True
                    continue
                else:
                    if (self.A[x][y]==2):
                        curr_petrol=petrol
                        stack.append((curr_petrol,i))
                        self.came_from[i]=curr_node
                        
                    else:
                        stack.append((curr_petrol-1,i))
                        self.came_from[i]=curr_node
                    self.visited[x][y]=True  
        self.success= False  

class SearchBFS:

    #ham khoi tao
    def __init__(self,A,M,N):
        self.A=A
        self.M=M #ma tran M*M
        self.N=N #so lit xang ban dau
        self.came_from={}#luu duong di
        self.visited=[]#luu cac diem da di qua
        self.success=False

    #ham kiem tra diem nay co con nam trong do thi khong
    def in_bounds(self, pos):
        x, y  = pos
    
        # check if pos (x,y) is in maze matrix
        if (x>=self.M or x<0 or y>=self.M or y<0):
            return False
        return True
        
    #ham kiem tra diem nay co the di qua hay khong (khong la tuong va chua dc mo)
    def passable(self, pos):
        # if pos is NOT the one of position in walls
        x,y=pos[0], pos[1]
        if (self.in_bounds(pos)==False):
            return False

        if (self.A[x][y] != 0 and self.visited[x][y] == False):
            return True
        return False
        
    #ham tra ra nhung diem lan can co the di den
    def neighbors(self, pos):
        # Return a list of positions are neighbors of pos
        x,y = pos[0], pos[1]
        neighbors = [(x,y-1),(x+1,y),(x-1,y),(x,y+1)]
        valid_neighbors = []

        for i in range(0,len(neighbors)):
            #neu diem nay van con nam trong map và có thể dii, tức không phải là tường
            if (self.passable(neighbors[i])==True):
                valid_neighbors.append(neighbors[i])
        return valid_neighbors

    #ham luu vet duong di
    def trace_path(self, start, goal):
        curr = goal
        path = []
        while curr != start:
            path.append(curr)
            curr = self.came_from[curr]
        path.append(start)
        path.reverse()
        return path

    #tim kiem DFS
    def BFS(self,start, goal):
        x,y=start
        petrol=self.N
        queue=[(petrol,start)]

        #tao ra list danh dau tat ca cac diem di qua
        for i in range(0,A.M):
            temp=[]
            for j in range(0,A.M):
                temp.append(False)
            self.visited.append(temp)

        while (len(queue)>0):
            curr_petrol, curr_node=queue.pop(0)
            x,y=curr_node
            self.visited[x][y]=True

            for i in self.neighbors(curr_node):
                x,y=i
                if (i==goal and curr_petrol-1>=0):
                    self.came_from[goal]=curr_node
                    self.visited[x][y]=True
                    self.success= True
                    return
                elif (curr_petrol-1==0 and self.A[x][y]!=2):#het xang ma tai diem dang dung khong phai la cay xang
                    self.visited[x][y]=True
                else:
                    if (self.A[x][y]==2):
                        curr_petrol=petrol
                        queue.append((curr_petrol,i))
                        self.came_from[i]=curr_node
                    else:
                        queue.append((curr_petrol-1,i))
                        self.came_from[i]=curr_node
                    self.visited[x][y]=True   

        self.success= False

class SearchUCS:

    #ham khoi tao
    def __init__(self,A,M,N):
        self.A=A
        self.M=M #ma tran M*M
        self.N=N #so lit xang ban dau
        self.came_from={}#luu duong di
        self.visited=[]#luu cac diem da di qua
        self.success=False
    #ham kiem tra diem nay co con nam trong do thi khong
    def in_bounds(self, pos):
        x, y  = pos
        if (x>=self.M or x<0 or y>=self.M or y<0):
            return False
        return True
        
    #ham kiem tra diem nay co the di qua hay khong (khong la tuong va chua dc mo)
    def passable(self, pos):
        x,y=pos[0], pos[1]
        if (self.in_bounds(pos)==False):
            return False

        if (self.A[x][y] != 0 and self.visited[x][y] ==False):
            return True
        return False

    #ham tra ra nhung diem lan can co the di den
    def neighbors(self, pos):
        x,y = pos[0], pos[1]
        neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        valid_neighbors = []    

        for i in range(0,len(neighbors)):
            #neu diem nay van con nam trong map và có thể dii, tức không phải là tường
            if (self.passable(neighbors[i])==True):
                valid_neighbors.append(neighbors[i])
        return valid_neighbors

    #ham luu vet duong di
    def trace_path(self, start, goal):
        curr = goal
        path = []
        while curr != start:
            path.append(curr)
            curr = self.came_from[curr]
        path.append(start)
        path.reverse()
        return path

    #tim kiem UCS
    def UCS(self,start,goal):
        pqueue=[]#hang doi uu tien
        petrol=self.N
        heapq.heappush(pqueue,(0,petrol,start))
        
        cost_so_far={start: 0}#chi phi den hien tai 
        
        #tao ra list danh dau tat ca cac diem di qua
        for i in range(0,A.M):
            temp=[]
            for j in range(0,A.M):
                temp.append(False)
            self.visited.append(temp)

        while len(pqueue)>0:
            curr=heapq.heappop(pqueue)#lay ra phan tu nao co ch phi be nhat trong hang doi
            curr_cost, curr_petrol,curr_node=curr#gan gia ti moi cho node hien tai
            x,y=curr_node
            self.visited[x][y]=True
            for next_node in self.neighbors(curr_node):
                x,y=next_node
                new_cost = curr_cost+1#chi phi la nhu nhau
                if next_node==goal and curr_petrol-1>=0:#kiem tra co phai node dich hay chua
                    self.came_from[goal]=curr_node
                    self.visited[x][y]=True
                    self.success= True#thoát hàm
                    return
                if next_node not in cost_so_far or new_cost<cost_so_far[next_node]:#node nay chi phi nho hon 
                    if (curr_petrol-1==0 and self.A[x][y]!=2):#neu di den node nay vua het xang ma con o day ko phai la tram xang
                        self.visited[x][y]=True
                    else:#con xang
                        if (self.A[x][y]==2):#gap tram xang
                            curr_petrol=petrol
                            heapq.heappush(pqueue,(new_cost,curr_petrol,next_node))
                            self.came_from[next_node]=curr_node
                            cost_so_far[next_node]=new_cost#cap nhat chi phi cho node moi them vao
                        else:#1 diem co the di
                            heapq.heappush(pqueue,(new_cost,curr_petrol-1,next_node))
                            self.came_from[next_node]=curr_node
                            cost_so_far[next_node]=new_cost#cap nhat chi phi cho node moi them vao  
                        self.visited[x][y]=True
        
        self.success= False

class SearchAStar:
    
    #ham khoi tao
    def __init__(self,A,M,N):
        self.A=A
        self.M=M #ma tran M*M
        self.N=N #so lit xang ban dau
        self.came_from={}#luu duong di
        self.visited=[]#luu cac diem da di qua
        self.success=False
    #ham kiem tra diem nay co con nam trong do thi khong
    def in_bounds(self, pos):
        x, y  = pos
        if (x>=self.M or x<0 or y>=self.M or y<0):
            return False
        return True
        
    #ham kiem tra diem nay co the di qua hay khong (khong la tuong va chua dc mo)
    def passable(self, pos):
        x,y=pos[0], pos[1]
        if (self.in_bounds(pos)==False):
            return False

        if (self.A[x][y] != 0 and self.visited[x][y] ==False):
            return True
        return False

    #ham tra ra nhung diem lan can co the di den
    def neighbors(self, pos):
        x,y = pos[0], pos[1]
        neighbors = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        valid_neighbors = []    

        for i in range(0,len(neighbors)):
            #neu diem nay van con nam trong map và có thể dii, tức không phải là tường
            if (self.passable(neighbors[i])==True):
                valid_neighbors.append(neighbors[i])
        return valid_neighbors

    #ham luu vet duong di
    def trace_path(self, start, goal):
        curr = goal
        path = []
        while curr != start:
            path.append(curr)
            curr = self.came_from[curr]
        path.append(start)
        path.reverse()
        return path

    #ham tinh heristic
    def heuristic(self, p1, p2, heu_type="Manhanttan"):
        if heu_type == "Manhanttan":
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        elif heu_type == "Euclidean":
            return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        
        return sys.maxsize # return maximun number
    
    #tim kiem A*
    def AStar (self,start, goal):
        pqueue=[]#hang doi uu tien
        petrol=self.N
        h=self.heuristic(start,goal)
        g=0
        f=h+g
        heapq.heappush(pqueue,(f,petrol,start))
        
        cost_so_far={start: f}#chi phi den hien tai 
        
        #tao ra list danh dau tat ca cac diem di qua
        for i in range(0,A.M):
            temp=[]
            for j in range(0,A.M):
                temp.append(False)
            self.visited.append(temp)

        while len(pqueue)>0:
            curr=heapq.heappop(pqueue)#lay ra phan tu nao co ch phi be nhat trong hang doi
            curr_cost, curr_petrol,curr_node=curr#gan gia ti moi cho node hien tai
            x,y=curr_node
            self.visited[x][y]=True
           
            for next_node in self.neighbors(curr_node):
                x,y=next_node
                h_new = self.heuristic(next_node,goal)
                g_new = curr_cost+1 
                f_new = h_new + g_new
                if next_node==goal and curr_petrol-1>=0:#kiem tra co phai node dich hay chua
                    self.came_from[goal]=curr_node
                    self.visited[x][y]=True
                    self.success= True#thoát hàm
                    return
                if next_node not in cost_so_far or f_new < cost_so_far[next_node]:#node nay chi phi nho hon 
                    if (curr_petrol-1==0 and self.A[x][y]!=2):#neu di den node nay vua het xang ma con o day ko phai la tram xang
                        self.visited[x][y]=True
                    else:#con xang
                        if (self.A[x][y]==2):#gap tram xang
                            curr_petrol=petrol
                            heapq.heappush(pqueue,(f_new,curr_petrol,next_node))
                            self.came_from[next_node]=curr_node
                            cost_so_far[next_node]=f_new#cap nhat chi phi cho node moi them vao
                        else:#1 diem co the di
                            heapq.heappush(pqueue,(f_new,curr_petrol-1,next_node))
                            self.came_from[next_node]=curr_node
                            cost_so_far[next_node]=f_new#cap nhat chi phi cho node moi them vao  
                        self.visited[x][y]=True
        print("khong tim thay duong di")
        self.success= False

# dinh nghia mau
white = (255,255,255)
brown = (105, 61, 0)
black = (0,0,0)
yellow=(245, 221, 66)
blue=(179, 213, 230)

# dat chieu dai va chieu rong cho moi o
width= 50
height = 50

# dat chieu dai va chieu rong cho moi o
widthButton= 70
heightButton = 50
 
# dat khoang cach giua cac o
margin = 5
# dat khoang cach giua cac o
marginButton = 7
 
#tao ra mot matran, la ban do dc doc tu file
A=Map()
A.ReadFile()
grid = A.A

textButton=["DFS","BFS","UCS","A*"]
searchDFS=SearchDFS(A.A, A.M, A.petrol)
searchBFS=SearchBFS(A.A, A.M, A.petrol)
searchUCS=SearchUCS(A.A, A.M, A.petrol)
searchAStar=SearchAStar(A.A, A.M, A.petrol)

pygame.init()
 
#dat chieu dai va chieu rong cua man hinh hien thi
WINDOW_SIZE = [560, 680]
screen = pygame.display.set_mode(WINDOW_SIZE)
font=pygame.font.SysFont('Arial',27) 
#tieu de cua man hinh
pygame.display.set_caption("Search")
 
# Loop until the user clicks the close button.
done = False
flat=-1

#duong dan hinh anh xe
image_motor=pygame.image.load('motorbike.png')
image_motor=pygame.transform.scale(image_motor,(50,50))

image_petrol=pygame.image.load('petrol.png')
image_petrol=pygame.transform.scale(image_petrol,(50,50))

image_flag=pygame.image.load('flag.png')
image_flag=pygame.transform.scale(image_flag,(40,40))

# -------- Main Program Loop -----------
while not done:
    gridButton=[0,0,0,0]
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #click chuot de lay vi tri
            pos = pygame.mouse.get_pos()
            # lay toa do cua nut duoc chon
            index = pos[0] // (widthButton*2 + marginButton) 
            
            if (index==0):
                gridButton[index] = 1 
                searchDFS.DFS((0,0),(A.M-1,A.M-1))
                grid=searchDFS.A
                flat=0
            elif (index==1):
                gridButton[index] = 1
                searchBFS.BFS((0,0),(A.M-1,A.M-1))
                grid=searchBFS.A
                flat=1
            elif (index==2):
                gridButton[index] = 1
                searchUCS.UCS((0,0),(A.M-1,A.M-1))
                grid=searchUCS.A
                flat=2
            elif (index==3):
                gridButton[index] = 1
                searchAStar.AStar((0,0),(A.M-1,A.M-1))
                grid=searchAStar.A
                flat=3
 
    # dat background cho man hinh
    screen.fill(black)
    
    # ve ban do
    if (flat == -1):
        for row in range(A.M):
            for column in range(A.M):
                color=white
                if grid[row][column] == 0:
                    color = brown
                
                pygame.draw.rect(screen,
                                 color,
                                 [(margin + width) * column + margin,
                                  (margin + height) * row + margin,
                                  width,
                                  height])

                if grid[row][column]==2:
                    screen.blit(image_petrol,((margin + width) * column + margin,
                                  (margin + height) * row + margin))
                    
                  
        #dat icon cho vi tri bat dau va vi tri ket thuc
        screen.blit(image_motor,(5,5))
        screen.blit(image_flag,((margin + width) * (A.M-1) + margin+3,(margin + height) * (A.M-1) + margin))
    
    #DFS
    elif (flat==0):
        for row in range(A.M):
            for column in range(A.M):
                color=white
                if grid[row][column] == 0:
                    color = brown
                elif searchDFS.visited[row][column] == True:
                    color = blue
                pygame.draw.rect(screen,
                                 color,
                                 [(margin + width) * column + margin,
                                  (margin + height) * row + margin,
                                  width,
                                  height])

                if grid[row][column]==2:
                    screen.blit(image_petrol,((margin + width) * column + margin,
                                  (margin + height) * row + margin))
                    
                  
        #dat icon cho vi tri bat dau va vi tri ket thuc
        screen.blit(image_motor,(5,5))
        screen.blit(image_flag,((margin + width) * (A.M-1) + margin+3,(margin + height) * (A.M-1) + margin))

        #mo ta duong di da danh dau
        if (searchDFS.success==True):
            dem=0
            path= searchDFS.trace_path((0,0),(A.M-1, A.M-1))
            while dem<len(path):
                x,y=path[dem]
                screen.blit(image_motor, ((margin + width) * y + margin,(margin + height) * x + margin))
                dem+=1   

        
    #BFS
    elif (flat==1):
        for row in range(A.M):
            for column in range(A.M):
                color=white
                if grid[row][column] == 0:
                    color = brown
                elif searchBFS.visited[row][column] == True:
                    color = blue
                pygame.draw.rect(screen,
                                 color,
                                 [(margin + width) * column + margin,
                                  (margin + height) * row + margin,
                                  width,
                                  height])

                if grid[row][column]==2:
                    screen.blit(image_petrol,((margin + width) * column + margin,
                                  (margin + height) * row + margin))
                    
                  
        #dat icon cho vi tri bat dau va vi tri ket thuc
        screen.blit(image_motor,(5,5))
        screen.blit(image_flag,((margin + width) * (A.M-1) + margin+3,(margin + height) * (A.M-1) + margin))

        #mo ta duong di da danh dau
        if (searchBFS.success==True):
            dem=0
            path= searchBFS.trace_path((0,0),(A.M-1, A.M-1)) 
            while dem<len(path):
                x,y=path[dem]
                screen.blit(image_motor, ((margin + width) * y + margin,(margin + height) * x + margin))
                dem+=1
    
    #UCS
    elif (flat==2):
        for row in range(A.M):
            for column in range(A.M):
                color=white
                if grid[row][column] == 0:
                    color = brown
                elif searchUCS.visited[row][column] == True:
                    color = blue
                pygame.draw.rect(screen,
                                 color,
                                 [(margin + width) * column + margin,
                                  (margin + height) * row + margin,
                                  width,
                                  height])

                if grid[row][column]==2:
                    screen.blit(image_petrol,((margin + width) * column + margin,
                                  (margin + height) * row + margin))
                    
        #dat icon cho vi tri bat dau va vi tri ket thuc
        screen.blit(image_motor,(5,5))
        screen.blit(image_flag,((margin + width) * (A.M-1) + margin+3,(margin + height) * (A.M-1) + margin))

        #mo ta duong di da danh dau
        if (searchUCS.success==True):   
            dem=0
            path= searchUCS.trace_path((0,0),(A.M-1, A.M-1)) 
            while dem<len(path):
                x,y=path[dem]
                screen.blit(image_motor, ((margin + width) * y + margin,(margin + height) * x + margin))
                dem+=1

    #A*
    elif (flat==3):
        for row in range(A.M):
            for column in range(A.M):
                color=white
                if grid[row][column] == 0:
                    color = brown
                elif searchAStar.visited[row][column] == True:
                    color = blue
                pygame.draw.rect(screen,
                                 color,
                                 [(margin + width) * column + margin,
                                  (margin + height) * row + margin,
                                  width,
                                  height])

                if grid[row][column]==2:
                    screen.blit(image_petrol,((margin + width) * column + margin,
                                  (margin + height) * row + margin))
                    
        #dat icon cho vi tri bat dau va vi tri ket thuc
        screen.blit(image_motor,(5,5))
        screen.blit(image_flag,((margin + width) * (A.M-1) + margin+3,(margin + height) * (A.M-1) + margin))

        #mo ta duong di da danh dau
        if (searchAStar.success==True):
            dem=0
            path= searchAStar.trace_path((0,0),(A.M-1, A.M-1)) 
            while dem<len(path):
                x,y=path[dem]
                screen.blit(image_motor, ((margin + width) * y + margin,(margin + height) * x + margin))
                dem+=1
    
    #cac nut bam chon kieu search
    for i in range (4):
        color=yellow
        pygame.draw.rect(screen,color,[(marginButton + widthButton) * i*2 + marginButton,(heightButton+  marginButton)*A.M + marginButton,widthButton,
                              heightButton])
            
        screen.blit(font.render(textButton[i],True,(0,0,0)),((marginButton + widthButton) * i*2 + marginButton +12
        ,(heightButton+  marginButton)*A.M + marginButton+10))
 
    # tiep tuc va cap nhat lai man hinh
    pygame.display.flip()
    
pygame.quit()






