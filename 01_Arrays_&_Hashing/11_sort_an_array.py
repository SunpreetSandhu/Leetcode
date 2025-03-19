class Solution(object):
   def sortArray(self, nums):
       """
       :type nums: List[int]
       :rtype: List[int]
       """
       def merge(arr, L,M,R):
           left = arr[L:M+1]
           right = arr[M+1:R+1]
           i = L
           j = k = 0


           while j<len(left) and k<len(right):
               if left[j]<=right[k]:
                   arr[i] = left[j]
                   j+=1
               else:
                   arr[i] = right[k]
                   k+=1
               i+=1
           while j<len(left):
               arr[i] = left[j]
               j+=1
               i+=1
           while k<len(right):
               arr[i] = right[k]
               k+=1
               i+=1
           return arr
       def mergeSort(arr, l, r):
           if l == r:
               return arr
           m = (l+r)//2
           mergeSort(arr, l, m)
           mergeSort(arr, m+1, r)
           merge(arr,l,m,r)
           return arr
       return mergeSort(nums, 0, len(nums)-1)
