##
#Author:Dylan Garrett
#Date:11/9/2016
#Description: The program works like a game of mine sweeper, without the game it prints a key to the mine sweeper game
##
import random
#Mine Module
class Mines:

    def __init__(self,mine="*", row=7, columns=7):
        '''int_mines initalizes all the global variables and also calls the init_grid method arg: mine, row, columns'''
        
        self.mine_charater = mine
        self.number_of_rows=row
        self.number_of_columns=columns
        self.list_of_lists = []
        self.helper()
        
    def helper(self):
        '''init_grid creates rows containing "-" which then is appened to our main list name list_of_lists'''
         
        for j in range(self.number_of_columns):
            row_insert=[]
            
            for i in range (self.number_of_rows):
                row_insert.append("-")
            self.list_of_lists.append(row_insert)
        
        
        
        
        
    def set_mines(self,num_mines):
        '''Set mines makes sure that the number of mines does not exceed the amount of spaces on the board'''
        
        
        if num_mines > (self.number_of_rows*self.number_of_columns):
            print("Error") 
            number_of_mines=0
            print(self.number_of_mines)
            
        else:
            self.number_of_mines = num_mines
            
        
        
    def place_mines(self):
        '''place_mines starts a loop that is determined by the number of mines and then scans the specific list and a specific element within the list and changes the charater to a mine '''
        
        
        while self.number_of_mines > 0:
            mine_y = random.randrange(0,self.number_of_rows -1)
            mine_x = random.randrange(0, self.number_of_columns -1)
            if self.list_of_lists[mine_y][mine_x] !=self.mine_charater:
                self.list_of_lists[mine_y][mine_x] = self.mine_charater
                self.number_of_mines = self.number_of_mines -1
            
            
            
    def __str__(self):
        '''prints the list_of_lists'''
        list_string = ""
        print("The grid with mines is:")
        for i in range(len(self.list_of_lists)):
        
            
            for j  in range(len(self.list_of_lists[i])):
                list_string= list_string + self.list_of_lists[i][j]
            list_string = list_string + "\n"
            
        return(list_string)
    
        
    
        
    
#init_mines()
#set_mines(9)
#str_mines()