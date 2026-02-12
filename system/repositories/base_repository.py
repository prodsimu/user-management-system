from database.database import Database


class BaseRepository:

    def __init__(self, database: Database, collection_name: str):
            self.database = database
            self.collection = getattr(database, collection_name)


#  CREATE

    def add(self, item):
        self.collection.append(item)


    def get_next_id(self):
        if not self.collection:
            return 1
        
        last_id = self.collection[-1].id
        return last_id + 1


# READ

    def get_all(self):
        return self.collection


    def get_by_id(self, item_id: int):
        for item in self.collection:
            if item.id == item_id:
                return item
            
        return None


    def get_by_field(self, field: str, value):
        for item in self.collection:

            attr_value = getattr(item, field, None)

            if attr_value == value:
                return item
            
        return None


    def exists_by_id(self, item_id: int):
        return any(item.id == item_id for item in self.collection)


    def exists_by_field(self, field: str, value):
        for item in self.collection:

            attr_value = getattr(item, field, None)

            if attr_value == value:
                return True
            
        return False


    def count(self):
        return len(self.collection)


# UPDATE

    def update_by_id(self, item_id: int, new_data: dict):
        for item in self.collection:
            if item.id == item_id:

                for key, value in new_data.items():

                    if key == "id":
                        continue

                    if hasattr(item, key):
                        setattr(item, key, value)

                return True

        return False


# DELETE

    def delete(self, item_id: int):
        for i, item in enumerate(self.collection):
            if item.id == item_id:
                self.collection.pop(i)
                return True
            
        return False
