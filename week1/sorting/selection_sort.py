class Solution: 
    def select(self, arr, i):
        # code here 
        pass
    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1):
            min = i
            for j in range(i+1,n):
                if arr[min] > arr[j]:
                    arr[min],arr[j] = arr[j],arr[min]
                    


