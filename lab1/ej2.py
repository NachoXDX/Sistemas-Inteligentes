import random

def main():
    
    num = random.sample(range(10,300),241)
    l1 = num[0:(len(num)//2)]
    l2 = num[(len(num)//2):]
    print(l1)
    print(l2)    
    if len(l1) + len(l2) == len(num) and  0<= abs(len(l1) - len(l2)) <= 1:
        print("Exito")
    else:
        print("fallo")

if __name__ == "__main__":
    main()




# 0 1 2 3 4 5 6 7 8 9
#[1,2,3,4,5,6,7,8,9,10] -> len 10
# list[0:5] -> [1,2,3,4,5] 
# list[5:] -> [6,7,8,9,10]