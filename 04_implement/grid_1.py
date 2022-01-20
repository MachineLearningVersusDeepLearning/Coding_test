##########
# problem 
##########
##########
# input
##########
# 5
# RRRUDD

##########
# output 
##########
# 3 4   


class __grid_problem(): 
    def __init__(self):
        print("grid problem start")
        self.__main()
        
    def __main(self):
        print(" grid size : ")
        _grid_size = int(input())
        print ("your grid size is {}".format(_grid_size))
        
        print(" directions : ")
        _directions = str(input().split())    
        print(" your directions are {}".format(_directions))
        
        _x,_y = 1,1        
        
        for _d in _directions :
            ########### up down left right labeling #########
            if _d == 'u' :
                _x-=1
            elif _d =='d':
                _x+=1
            elif _d =='l':
                _y-=1
            elif _d =='r':
                _y+=1
                
            ############ threshold #########
            if _x <1 :
                _x =1
            elif _x > _grid_size:
                _x = _grid_size 
                
            if _y <1 :
                _y =1
            elif _y > _grid_size:
                _y = _grid_size             
                
        print (" final goal is : {} {}".format(_x,_y))
            
            
        
        
        
if __name__ == "__main__":
    __grid_problem()