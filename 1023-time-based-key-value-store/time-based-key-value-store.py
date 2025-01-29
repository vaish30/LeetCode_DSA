class TimeMap:
    def __init__(self):
        self.book = {}

    def set(self,key,value,timestamp):
        if key not in self.book:
            self.book[key] = []

        self.book[key].append([value,timestamp])

    def get(self, key, timestamp):
        result = ''
        values = self.book.get(key, [])

        l, r = 0, len(values) - 1

        while l<=r:

            m = (l+r)//2

            if values[m][1]<=timestamp:
                result = values[m][0]
                l=m+1

            else:
                r = m-1
        return result