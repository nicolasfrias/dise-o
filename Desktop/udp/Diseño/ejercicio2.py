
#busqueda binaria que aparecia en la diapositiva
def binary_search(A, key):
    pos = -1
    inicio = 0
    fin = len(A) -1
    while inicio <= fin:
        mid = inicio + (fin-inicio)//2
        if A[mid] < key:
            inicio = mid+1
        elif A[mid] > key:
            fin = mid-1
        else:
            pos = mid
            break
    return pos



def threesum(arr):
    solucion=[] 
    arr.sort() 
    for i in range(0,len(arr)-2):
        for j in range(i+1,len(arr)-1):
            suma=arr[i]+arr[j]
            temp=binary_search(arr,-suma)            
            if temp!=-1:
                trio=[]
                trio.append(arr[i])
                trio.append(arr[j])
                trio.append(arr[temp])
                solucion.append(trio)
    print (solucion)

def test():
    A=[]
    a=-10
    for x in range(0,50):
        A.append(a)
        a+=1

    
    
    threesum(A)
    #print(A[ass])

test()



