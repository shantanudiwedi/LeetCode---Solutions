class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        total=0 
        sum_window = sum(arr[0:k])
        if sum_window/float(k) >=threshold:
            total+=1 
        for i in range (k,len(arr)):
            sum_window+= arr[i]-arr[i-k]
            if sum_window/float(k) >= threshold:
                total+=1
        return total 