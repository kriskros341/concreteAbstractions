def make_interval(lower, upper):
    return Interval(lower, upper)

class Interval():
    def __init__(self, lower, upper):
        self.upper = upper
        self.lower = lower
        self.middle = (lower+upper)/2

    def upper_endpoint(self):
        return self.upper
    
    def right_half(self):
        return Interval(self.middle, self.upper)

    def __str__(self):
        return f"[{self.lower}, {self.upper}]"

inter = make_interval(3,7)
print(inter.right_half().right_half().right_half().right_half().middle) #  LOL
