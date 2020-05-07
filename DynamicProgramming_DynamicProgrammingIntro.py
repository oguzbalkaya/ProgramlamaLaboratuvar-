def fib(n):
#Bu fonksiyonda daha önce hesaplanan bir fib sayısı farklı bir fib sayısını hesaplamada kullanılacağı zaman tekrar hesaplanıyor.Karmaşıklığı O(2^n)
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def fastFib(n,memo={}):
#Bu fonksiyonda daha önce hesaplanan fib sayıları kaydedilerek tekrar hesaplanmaz.Karmaşıklığı O(n)
    if n==0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1,memo)+fastFib(n-2,memo)
        memo[n]=result
        return result
print(fib(5))
print(fib(5))
