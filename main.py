

from src.schema import Schema


def main():
    # Create a schema
    schema = Schema()
    table_schema = schema.get_schema()
    print("type: ", type(table_schema))
    print(table_schema)


if __name__ == "__main__":
    main()
