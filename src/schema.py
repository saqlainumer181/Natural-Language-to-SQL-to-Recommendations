import sqlite3
import json


DB_PATH = './db/chinook.db'  # Path to the Chinook SQLite database


class Schema():
    def __init__(self):
        self.db_path = DB_PATH

    def extract_schema(self, db_path):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        
        schema = {}
        
        # Get all table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        for table in tables:
            table_name = table[0]
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            
            schema[table_name] = []
            for col in columns:
                column_info = {
                    'column_id': col[0],
                    'name': col[1],
                    'type': col[2],
                    'notnull': bool(col[3]),
                    'default_value': col[4],
                    'primary_key': bool(col[5])
                }
                schema[table_name].append(column_info)
        
        cursor.close()
        connection.close()
        
        return schema

    def create_metadata(self, schema):
        metadata = {
            "database_name": "chincook",
            "tables": schema
        }
        return json.dumps(metadata, indent=4)

    def get_schema(self):
        
        try:
            schema = self.extract_schema(self.db_path)
            metadata_doc = self.create_metadata(schema)
            
            print("Metadata extraction complete.")
            return metadata_doc
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None

