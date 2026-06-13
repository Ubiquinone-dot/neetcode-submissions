class TimeMap:

    def __init__(self):
        self.data={}
    
    def getidx(self, arr, timestamp, add=False):
        # return the index that the timestamp would 
        # have in the sorted array
        l, r = 0, len(arr)-1
        while r >= l:
            m = (l+r)//2
            if arr[m][0] == timestamp:
                return m if not add else m+1
            elif arr[m][0] < timestamp:
                l = m + 1
            else:
                r = m - 1
        return l

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = [(timestamp, value)]
            return
        arr = self.data[key]
        if len(arr) == 1:
            if arr[0][0] > timestamp:
                arr = [(timestamp, value)] + arr
            else:
                arr = arr + [(timestamp, value)] 
        else:
            m = self.getidx(arr, timestamp)
            arr = arr[:m+1] + [(timestamp, value)] + arr[1+m:]
        self.data[key] = arr

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        arr = self.data[key]
        if len(arr) == 1:
            if arr[0][0] > timestamp:
                return ""
            else:
                return arr[0][-1]

        idx = self.getidx(arr, timestamp, add=True)
        if idx == 0:
            return ""
        return arr[idx-1][-1]
