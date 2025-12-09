def оkruzhnost(r):
    a = 2 * 3.14 * int(r)   
    return a

def krug(r):
    b = 3.14 * int(r)**2   
    return b

def main():
    r = input('Введите радиус круга в сантиметрах')
    print('Длина окружности в сантиметрах',оkruzhnost(r),)    
    print('Площадь круга в сантиметрах квадратных',krug(r))      
if __name__ == '__main__':
    main()
