from sqlalchemy import create_engine
import urllib


def get_sql_server_engine(server: str, database: str):
    connection_string = (
        "Driver={ODBC Driver 17 for SQL Server};"
        f"Server={server};"
        f"Database={database};"
        "Trusted_Connection=yes;"
    )

    params = urllib.parse.quote_plus(connection_string)
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
    return engine
