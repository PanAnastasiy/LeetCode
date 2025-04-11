class MapSum:

    def __init__(self):
        self.dct = {}

    def insert(self, key: str, val: int) -> None:
        self.dct[key] = val

    def sum(self, prefix: str) -> int:
        counter = 0
        for key in self.dct.keys():
            if key.startswith(prefix):
                counter += self.dct.get(key)
        return counter

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)