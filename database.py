import sqlite3

class Database:
    def __init__(self, db_path:str) -> None:
        
        self.instance = sqlite3.connect(db_path)
        self.path = db_path
    
    def getCursor(self):
        return self.instance.cursor()
    
    def commitChanges(self):
        return self.instance.commit()
    
    def close(self):
        return self.instance.close()
    
    def getTableData(self, tableName:str, condition:str = None):
        cur = self.getCursor()
        query = f"SELECT * FROM {tableName}"
        if condition: query = f"SELECT * FROM {tableName} WHERE {condition};"
        cur.execute(query)
        
        return cur.fetchall()
    
    def createTable(self, tableName:str, values:dict[str,str]):
        valueList = [f"{valueName} {valueProperties}" for valueName, valueProperties in values.items()]
        valueStr = ','.join(valueList)
        
        return self.instance.execute(f"CREATE TABLE IF NOT EXISTS {tableName} ({valueStr})")
    
    @staticmethod
    def formatValues(values):
        lst = []
        for value in values:
            if str(value) == value:
                lst.append(f"'{value}'")
            else: lst.append(str(value))
            
        return lst
    
    def writeTable(self, tableName:str, values:dict[str,str]):
        valueList = self.formatValues(values.values())
        query = f"INSERT INTO {tableName}({", ".join(values.keys())}) VALUES({', '.join(valueList)});"
        return self.instance.execute(query)
        
    def updateTable(self, tableName:str, values:dict[str,str], condition:str):
        valueList = [f"{key}='{value}'" for key,value in values.items()]
        query = f"UPDATE {tableName} SET {", ".join(valueList)} WHERE {condition};"
        return self.instance.execute(query)
    