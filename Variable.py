from typing import Self

class Variable():
    counter: int = 0
    varList = []
    def __init__(self, name:str, displayName:str, category:str, executeFunc, row:int = None) -> None:
        self.name: str = name
        self.displayName: str = displayName
        self.category: bool = category
        self.execFunc = executeFunc
        self.row = row
        
        Variable.counter += 1
        Variable.varList.append(self)

    @classmethod
    def varibaleCount(cls) -> int:
        return cls.counter
    
    @classmethod
    def variableList(cls):
        return cls.varList
    
    @classmethod
    def getObjectByDisplayName(cls, name: str) -> Self:
        for obj in cls.varList:
            if(name == obj.displayName):
                return obj
        return None
    @classmethod
    def getObjectByName(cls, name:str) -> Self:
        for obj in cls.varList:
            if(name == obj.name):
                return obj
        return None
            
    def execute(self, message, query = False, *args):
        return self.execFunc(message, query, *args)
    
    def isCategory(self) -> bool:
        return self.category == "main"
    
