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
    
    def getTableData(self, tableName:str):
        cur = self.getCursor()
        cur.execute(f"SELECT * FROM {tableName};")
        
        return cur.fetchall()
    
    def createTable(self, tableName:str, values:dict[str,str]):
        valueList = [f"{valueName} {valueProperties}" for valueName, valueProperties in values.items()]
        valueStr = ','.join(valueList)
        
        return self.instance.execute(f"CREATE TABLE IF NOT EXISTS {tableName} ({valueStr})")
        
    def writeTable(self, tableName:str, values:dict[str,str]):
        query = f"INSERT INTO {tableName}({"'"+"\', \'".join(values.keys())+"'"}) VALUES({"'"+"\', \'".join(values.values())+"'"});"
        return self.instance.execute(query)
        
    def updateTable(self, tableName:str, values:dict[str,str], condition:str):
        valueList = [f"{key}='{value}'" for key,value in values.items()]
        query = f"UPDATE {tableName} SET {", ".join(valueList)} WHERE {condition};"
        return self.instance.execute(query)
    