##### Problem #######
import math

    ########### problem ###########
    #### minimum of the number of coin #########
    ### my coin - 500/100/50 #########


class __change_money():
    def __init__(self):
        print("start")
        #self.__test_solution()
        self.__test_optimization()

    
    def __test_solution(self):
        ######### 1. input - all money #########
        print("Write total money :")
        _total_money = int(input())

        ######### 2. Calculate change each other ######
        _500_n = math.floor(_total_money / 500)
        _500_n_remain = _total_money % 500
        print("500 won : " ,_500_n)
        
        
        _100_n = math.floor(_500_n_remain / 100)
        _100_n_remain = _500_n_remain % 100
        print("100 won : " ,_100_n)

        _50_n = math.floor(_100_n_remain / 50)
        _50_n_remain = _100_n_remain % 50
        print("50 won : " ,_50_n)
        
        _10_n = math.floor(_50_n_remain / 10)
        _10_n_remain = _50_n_remain % 10
        print("10 won : " ,_10_n)

        
    def __test_optimization(self):
        ######### 1. input - all money #########
        print("Write total money :")
        _total_money = int(input())
        
        ######### 2. change money ############
        _changes = [500,100,50,10]
        
        ######### 3. Calculate change each other ######
        for _change in _changes :
            _change_n = math.floor(_total_money / _change)
            _total_money = _total_money % _change
            print(_change," won : " ,_change_n)
        
        
        
if __name__ == "__main__":
    _test = __change_money()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    