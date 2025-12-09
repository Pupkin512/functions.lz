import math
def prime(a):
    b = 0
    n = int(math.sqrt(a) + 1)
    if a <= 1:
        print('Число не простое и не составное') 
    else:
        for i in range(2, n): 
            if a % i == 0:
                b = 1
            else:
                b = 0
        if b == 0 :
                print('Число простое')
        else:
                print('Число составное')
def main():
     a = int(input('Введите число'))
     prime(a)       
     
if __name__ == '__main__':
    main()
