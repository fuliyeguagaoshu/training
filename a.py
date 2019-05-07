#!/usr/bin/env python3



import sys

def calculate(income):
    value =income*0.835-5000
    if value<=0:
        result = 0
    elif value <=3000:
        result = value*0.03
    elif value<=12000:
        result = value*0.1-210
    elif value<=25000:
        result = value*0.2-1410
    elif value<=35000:
        result = value*0.25-2660
    elif value<=55000:
        result = value*0.3-4410
    elif value<=80000:
        result = value*0.35-7160
    else:
        result = value*0.45-15160
    income_final = income*0.835-result
    return income_final







if __name__ == '__main__':
 #   id_income = {}
    if len(sys.argv)<=1:
        print('Parameter Error')
        sys.exit()
    for arg in sys.argv[1:]:
        arg_split = arg.split(':')
        if len(arg_split)!=2:
            print('Parameter Error')
            sys.exit()
        try:
            income = int (arg_split[1])
        except:
            print('Parameter Error')
            sys.exit()
        income_final = calculate(income)
        print('{}:{:.2f}'.format(arg_split[0],income_final))
'''     id_income[arg_split[0]] = income_final
     for key, value in id_income.items():
        print('{}:{:.2f}'.format(key,value))'''


