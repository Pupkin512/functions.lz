def even(chislo):
    if chislo % 2 == 0:
        print('Чётное число')
    else: 
        print('Не чётное число')
def main():
    chislo = int(input('Введите число'))
    even(chislo)
    
if __name__ == '__main__':
    main()
