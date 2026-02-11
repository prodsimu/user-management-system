from database.database import Database


class BaseRepository:
    
    def __init__(self, database: Database, collection_name: str):
        self.database = database
        self.collection = getattr(database, collection_name)


    def add(self, item):
        self.collection.append(item)


    def get_all(self):
        return self.collection


    def get_next_id(self):
        if not self.collection:
            return 1
        
        last_id = self.collection[-1].id
        return last_id + 1


    def get_by_id(self, item_id: int):
        for item in self.collection:
            if item.id == item_id:
                return item
            
        return None


    def delete(self, item_id: int):
        for i, item in enumerate(self.collection):
            if item.id == item_id:
                self.collection.pop(i)
                return True
            
        return False
