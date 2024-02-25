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
        i = len(vals) - 1
        while i >= 0:
            if vals[i][0] <= timestamp:
                ans = vals[i][1]
                break
            i -= 1 
        return ans
            
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
