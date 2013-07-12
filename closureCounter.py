class Counter(object):
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        print self.count,
        return self

    def reset(self):
        self.count = 0
        print "[reset]",
        return self

