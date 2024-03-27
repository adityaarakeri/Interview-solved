class ArrayList:
    def __init__(self, nums) -> None:
        self.nums = nums

    def __iter__(self):
        self.pos = 0
        return self
    def __next__(self):
        if (self.pos < len(self.nums)):
            self.pos += 1
            return self.nums[self.pos - 1]
        else:
            raise StopIteration

array_obj = ArrayList([1,2,3])

it = iter(array_obj)
print(next(it)) # 1
print(next(it)) # 2
print(next(it)) # 3
print(next(it)) # stopIteration exception
