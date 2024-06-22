from time import time


class Fibonacci:
    def calcola_funzione(self, n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.calcola_funzione(n-1) + self.calcola_funzione(n-2)

if __name__=='__main__':
    fib= Fibonacci()
    N=20
    start_time= time()
    elemento= fib.calcola_funzione(N)
    end_time= time()
    print(f"L'elemento {N} della sequenza è {fib.calcola_funzione(6)}")
    print(f"Elapsed time: {end_time-start_time}")