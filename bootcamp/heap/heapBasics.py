class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        self.upHeap(arr, n, i)
        self.downHeap(arr, n, i)
        
       
        # code here
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for i in range(n):
            self.upHeap(arr,n,i)
        # code here
    
    # #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr,n)
        while (n > 0):
            self.remove(arr, n, 0)
            n -= 1
        
        arr.reverse()
        
        # while (n > 0):
        #     self.buildHeap(arr, n)
        #     arr[0], arr[n-1] = arr[n-1], self.getMin(arr)
        #     n -= 1
        # arr.reverse()
            
            # arr[i] = self.getMin(arr)
            # self.heapify(arr,i,n)
        # self.buildHeap(arr,n)
        # for i in range(n//2 - 1, -1, -1):
        #     self.upheap(i,arr)
 
    # # One by one extract elements
       
    #     for i in range(n-1, 0, -1):
    #         mini = self.getMin(arr)
    #         temp = self;  
    #         arr[0] = arr[i];  
    #         arr[i] = temp;  
          
    #         self.heapify(arr,i,0)
            # self.upheap(i,arr)
           
 
        #code here
        
        
        
    #Helper functions
    def leftChild(self,i):
        return (2 * i) +1
    def rightChild(self,i):
        return (2 * i) + 2
    def parent(self,i):
        return (i - 1)//2
    
    
    #functions
    
    def insert(self,arr, n, element):
        arr[n] = element
        self.upHeap(arr,n+1,n)
        
        
    def remove(self,arr,n,i):
       arr[i], arr[n-1] = arr[n-1], arr[i]
       self.heapify(arr, n-1, i)
        
        
    def getMin(self,arr):
        if len(arr):
            return arr[0]
        # for i in range(1,len(arr)):
        #     if arr[i] < mini:
        #         mini = arr[i]
        #         # self.getMin(arr[i:])
        # return mini
        
    def upHeap(self, arr, n, i):
        p = self.parent(i)
        if (i > 0 and arr[i] < arr[p]):
            arr[p], arr[i] = arr[i], arr[p]
            self.upHeap(arr, n, p)
    
    def downHeap(self,arr,n,i):
        minI = self.leftChild(i)
        
        if (minI >= n):
            return
        
        right = self.rightChild(i)
        
        if (right < n and arr[minI] > arr[right]):
            minI = right
        
        if (i < n and arr[i] > arr[minI]):
            arr[i], arr[minI] = arr[minI],arr[i]
            i = minI
            self.downHeap(arr, n, i)           
                
  