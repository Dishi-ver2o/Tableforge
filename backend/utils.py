# backend/utils.py
def validate_columns(columns):
    valid_types = {"INTEGER", "TEXT", "REAL", "BLOB"}
    cols = []
    if isinstance(columns, str):
        lines = columns.strip().split("\n")
    else:
        lines = columns  
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if ":" not in line:
            raise ValueError(f"Invalid column format: '{line}' (use name:TYPE)")
        name, dtype = line.split(":", 1)
        name = name.strip()
        dtype = dtype.strip().upper()
        if not name.isidentifier():
            raise ValueError(f"Invalid column name: '{name}'")
        if dtype not in valid_types:
            raise ValueError(f"Invalid type '{dtype}' for column '{name}'")
        cols.append((name, dtype))
    return cols