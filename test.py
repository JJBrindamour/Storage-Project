import pickle

class Data:
    @classmethod
    def load(cls, file):
        return pickle.load(open(file, 'rb'))
    
    def __init__(self, *data):
        self.data = list(data)
    
    def __repr__(self):
        return " ".join(map(lambda data: str(data), self.data))
    
    def save(self, file):
        pickle.dump(self, open(file, "wb"))

data = Data(1,2,3,4,5,6,7,8,9)
data.save('out.store')
fromSave = Data.load('out.store')
print(fromSave)
