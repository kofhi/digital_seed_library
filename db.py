import pandas as pd
import urllib
from pathlib import Path
from sqlalchemy import create_engine

# returns engine with microsoft access dialect
def access_engine(access_db):
    # connection string
    cnnstr = (
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
        r"DBQ=" + access_db
    )
    cnnurl = f"access+pyodbc:///?odbc_connect={urllib.parse.quote_plus(cnnstr)}"
    acc_engine = create_engine(cnnurl)
    return acc_engine

# creates connection to database file
def create_access_engine():
    db_path = Path("/digital_seed_library/cnuw_digital_seed_library_db.accdb")
    engine = access_engine(db_path)
    return engine

print(Path("/digital_seed_library/cnuw_digital_seed_library_db.accdb"))

# SEED CHARACTERISTICS DATAFRAMES
# SEED TYPES
def get_seed_types():
    sql = '''SELECT SeedType
            FROM tblSeedType'''
    
    # creates datafame, stores result set in a variable
    df_seed_types = pd.read_sql(sql, create_access_engine())

    return df_seed_types