def factorial(num):
    if num>=0:
        fact = 1
        for i in range(1,num+1):
           fact = fact * i
        return fact
    else:
        return 'No existe el factorial de un numero negativo'
