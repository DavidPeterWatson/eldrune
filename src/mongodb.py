from pymongo import MongoClient
from typing import Dict, List, Optional, Union
import json

class MongoDBHandler:
    def __init__(self, database_name: str, collection_name: str, host: str = 'localhost', port: int = 27017):
        try:
            self.client = MongoClient(host, port)
            self.db = self.client[database_name]
            self.collection = self.db[collection_name]
        except Exception as e:
            raise ConnectionError(f"Failed to connect to MongoDB: {str(e)}")

    def insert_one(self, data: Dict) -> str:
        try:
            result = self.collection.insert_one(data)
            return str(result.inserted_id)
        except Exception as e:
            raise Exception(f"Failed to insert document: {str(e)}")

    def insert_many(self, data: List[Dict]) -> List[str]:
        try:
            result = self.collection.insert_many(data)
            return [str(id) for id in result.inserted_ids]
        except Exception as e:
            raise Exception(f"Failed to insert documents: {str(e)}")

    def find_one(self, query: Dict) -> Optional[Dict]:
        try:
            result = self.collection.find_one(query)
            if result:
                result['_id'] = str(result['_id'])
            return result
        except Exception as e:
            raise Exception(f"Failed to find document: {str(e)}")

    def find_many(self, query: Dict = None, limit: int = None) -> List[Dict]:
        try:
            cursor = self.collection.find(query or {})
            if limit:
                cursor = cursor.limit(limit)
            
            results = []
            for doc in cursor:
                doc['_id'] = str(doc['_id'])
                results.append(doc)
            return results
        except Exception as e:
            raise Exception(f"Failed to find documents: {str(e)}")

    def update_one(self, query: Dict, update_data: Dict, upsert: bool = False) -> bool:
        try:
            result = self.collection.update_one(
                query,
                {'$set': update_data},
                upsert=upsert
            )
            return result.modified_count > 0 or (upsert and result.upserted_id is not None)
        except Exception as e:
            raise Exception(f"Failed to update document: {str(e)}")

    def update_many(self, query: Dict, update_data: Dict) -> int:
        try:
            result = self.collection.update_many(
                query,
                {'$set': update_data}
            )
            return result.modified_count
        except Exception as e:
            raise Exception(f"Failed to update documents: {str(e)}")

    def delete_one(self, query: Dict) -> bool:
        try:
            result = self.collection.delete_one(query)
            return result.deleted_count > 0
        except Exception as e:
            raise Exception(f"Failed to delete document: {str(e)}")

    def delete_many(self, query: Dict) -> int:
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            raise Exception(f"Failed to delete documents: {str(e)}")

    def close(self):
        self.client.close()