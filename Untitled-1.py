def fun(n):
    k=n
    if n==0:
        return
    print(k-n)
    fun(n-1)
fun(5)