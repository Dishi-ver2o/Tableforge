# backend/utils.py
def validate_columns(columns):
    valid_types = {"INTEGER", "TEXT", "REAL", "BLOB"}
    cols = []
    for line in columns:
        if ":" not in line:
            raise ValueError(f"Invalid column format: '{line}' (use name:TYPE)")
        name, dtype = line.split(":")
        name = name.strip()
        dtype = dtype.strip().upper()
        if dtype not in valid_types:
            raise ValueError(f"Invalid type '{dtype}' for column '{name}'")
        cols.append((name, dtype))
    return cols