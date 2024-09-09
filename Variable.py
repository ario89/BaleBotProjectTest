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
        return [var for var in cls.varList]
    
    @classmethod
    def getObj(cls, name: str):
        for obj in cls.varList:
            if(name == obj.displayName):
                return obj
        return None
            
    def execute(self, message, query = False):
        return self.execFunc(message, query)
    
    def isCategory(self):
        return self.category == "main"
    
