class TimeMap:

    def __init__(self):
        self.kvs = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kvs:
            self.kvs[key] = []
        self.kvs[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kvs:
            return ""
        vals = self.kvs[key]
        ans = ""
        l, r = 0, len(vals) - 1
        while l <= r:
            m = (l + r)//2
            if vals[m][0] <= timestamp:
                ans = vals[m][1]
                l = m + 1 
            else:
                r = m - 1
        return ans
            
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
