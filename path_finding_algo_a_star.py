import pygame as pg
from math import sqrt
from queue import PriorityQueue
WIDTH=765
root=pg.display.set_mode((WIDTH,WIDTH))
pg.display.set_caption("Path finding Algo -A*")

#color for further use
BLUE=(0,191,255)
PARR_GREEN=(0, 255 ,127)
BLACK_BLUE=(0, 0, 255)
BLACK=(0, 0 ,0)
RED=(255, 0, 0)
LIME_GREEN=(50, 205 ,50)
GOLD=(255, 215 ,0)
WHITE=(255, 255, 255)
GREY=(128, 128, 128)

class Node:
    """
    each node denotes a square in the grid,
    each square denotes a sqaure in a graph
    """
    def __init__(self,row,column,width,total_no_rows):
        self.row=row
        self.column=column
        self.x=row*width
        self.y=column*width
        self.width=width
        self.color=WHITE
        self.neighbors=[]
        self.total_no_rows=total_no_rows
        
    def get_position(self):
        return self.row,self.column
    
    def make_closed(self):
        self.color=BLUE
        
    def make_open(self):
        self.color=BLACK_BLUE
        
    def make_barrier(self):
        self.color=BLACK
        
    def make_start(self):
        self.color=PARR_GREEN
        
    def make_end(self):
        self.color=RED
    
    def is_closed(self):
        """checks if the node is already visited"""
        return self.color==BLUE
    
    def is_open(self):
        """checks if the node is still not visited"""
        return self.color==BLACK_BLUE
    
    def is_barrier(self):
        """checks if the node is a barrier"""
        return self.color==BLACK
    
    def is_start(self):
        """checks if the node is the start node"""
        return self.color==PARR_GREEN
    
    def is_end(self):
        """checks if the node is the end node"""
        return self.color==RED
    
    def reset(self):
        """resets the node to unvisited"""
        self.color=WHITE
        
    def make_path(self):
        self.color=GOLD
    
    def draw(self,root):
        x1=self.x
        y1=self.y
        x2=self.width
        y2=self.width
        pg.draw.rect(root,self.color,(x1,y1,x2,y2))
    
    def find_neighbors(self,grid):
        self.neighburs=[]
        if self.row<self.total_no_rows-1 and not grid[self.row+1][self.column].is_barrier():
            self.neighbors.append(grid[self.row+1][self.column])
        if self.row>0 and not grid[self.row-1][self.column].is_barrier():
            self.neighbors.append(grid[self.row-1][self.column])
        if self.column<self.total_no_rows-1 and not grid[self.row][self.column +1].is_barrier():
            self.neighbors.append(grid[self.row][self.column +1])
        if self.column>0 and not grid[self.row][self.column-1].is_barrier():
            self.neighbors.append(grid[self.row][self.column-1])
    
    def __lt__(self,other):
        return False
        
#distance function or h(n) function
        
def h(node1,node2):
    x1,y1=node1
    x2,y2=node2
    return (abs(x1-x2)+abs(y1-y2))

def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()
    
#ma in algo
def a_star_algo(draw,grid,start,end):
    count=0
    open_set=PriorityQueue()
    open_set.put((0,count,start))
    came_from={}
    g_score={node:float("inf") for row in grid for node in row}
    g_score[start]=0
    f_score={node:float("inf") for row in grid for node in row}
    f_score[start]=h(start.get_position(),end.get_position())
    
    open_set_hash={start}
    
    while not open_set.empty():
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pygame.quit()
        current = open_set.get()[2]
        open_set_hash.remove(current)
        
        if current==end:
            reconstruct_path(came_from,end,draw)
            end.make_end()
            return True
        
        for neighbor in current.neighbors:
            temp_g_score=g_score[current]+1
            
            if temp_g_score<g_score[neighbor]:
                came_from[neighbor]=current
                g_score[neighbor]=temp_g_score
                f_score[neighbor]=temp_g_score+h(neighbor.get_position(),end.get_position())
                if neighbor not in open_set_hash:
                    count+=1
                    open_set.put((f_score[neighbor],count,neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        draw()
        
        if current!=start:
            current.make_closed()
    
    return False
    
    
    
    
def make_grid(rows,width):
    #rows=columns as each node is represented as a square
    grid=[]
    gap=width//rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node=Node(i,j,gap,rows)
            grid[i].append(node)
    return grid

def draw_grid(root,rows,width):
    gap=width//rows
    for i in range(rows):
        pg.draw.line(root,GREY,(0,i*gap),(width,i*gap))
        for j in range(rows):
            pg.draw.line(root,GREY,(j*gap,0),(j*gap,width))
            
def draw(root,grid,rows,width):
    """first make the screen white and then draw each sqare individually.
    """
    root.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(root)
            
    draw_grid(root,rows,width)
    pg.display.update()
    
def get_current_position_click(position,rows,width):
    gap=width//rows
    x,y=position
    
    row=x//gap
    column=y//gap
    
    return row,column

def main(root,width):
    ROWS=45
    grid=make_grid(ROWS,width)
    
    start=None
    end=None
    
    run=True
    started=False
    
    while run:
        draw(root,grid,ROWS,width)
        for event in pg.event.get():
            if event.type==pg.QUIT:
                run=False
                
            if started:
                continue
            if pg.mouse.get_pressed()[0]:
                position=pg.mouse.get_pos()
                row,column=get_current_position_click(position,ROWS,width)
                node=grid[row][column]
                if not start:
                    start=node
                    start.make_start()
                    
                elif not end:
                    end=node
                    end.make_end()
                    
                elif node !=end and node !=start:
                    node.make_barrier()
                    
            elif pg.mouse.get_pressed()[2]:
                position=pg.mouse.get_pos()
                row,column=get_current_position_click(position,ROWS,width)
                node=grid[row][column]
                node.reset()
                if node==start:
                    start=None
                elif node==end:
                    end=None
                    
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.find_neighbors(grid)
                    a_star_algo(lambda:draw(root,grid,ROWS,width),grid,start,end)
                
                if event.key==pg.K_ESCAPE:
                    start=None
                    end=None
                    grid=make_grid(ROWS,width)
    pg.quit()

main(root,WIDTH)