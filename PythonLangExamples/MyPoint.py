class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def printAll(self):
        print(self.x, self.y)
        
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
        