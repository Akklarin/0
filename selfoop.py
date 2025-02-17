class clasname:
    def __init__(self):
        self.text = 'bukvy'

    def add(self, x):
        self.text += x

    def mult(self, x):
        self.text *= x

s = clasname()
s.add('123')    # self is implicitly passed in
s.mult(2)         # self is implicitly passed in
print(s.text)
