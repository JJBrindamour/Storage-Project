from typing import List, Tuple
import pickle

class Item:
    def __init__(self):
        pass

class Ref:
    def __init__(self, ref: Tuple(str, Item), mutable: bool = True):
        '''
        Initializes the Ref Class with a all of it's re
        '''
        
        pass

class Group:
    def __init__(self):
        pass

class Store:
    @classmethod
    def load(cls, file):
        pickle.load(open(file, 'rb'))

    def __init__(self, groups: List[Group] = [], refs: List[Ref] =[], items: List[Item] = [], name: str = "Name"):     
        self.groups = groups
        self.refs = refs
        self.items = items

    def __repr__(self):
        return " ".join(self.groups)

    def save(self, file):
        pickle.dump(self, open(file, "wb"))

db = Store(groups=[1,2,3,4,5,6,7,8,9])
db.save('out.store')
fromSaveDb = Store.load('out.store')
print(fromSaveDb)
