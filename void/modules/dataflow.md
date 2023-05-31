<h1 align=center>How Data Flows Through The Program</h1>

<!-- TODO: Add Public/Private -->

- `modules/imports.py`: `FileImporter`: obj
    - Input: `configs/congigs.py`
        - ROOT_DIR: str
        - LOAD_DIR: str
        - ATTHLETES: list[str]
        - SHEET_NAME: str
- `modules/stat_types.py`: `StatTypes`: list[obj]
    - Uses: `modules/stat_object`: `Stat`: obj 
        - prev_stat: str
        - full_stat: str
        - type: str
        - direction: str
        - position: str
        - prefixes: str
        - stat: str
        - suffixes: list[str]
        - is_attempt: bool
- `modules/converter.py`: `Converter`: obj
        
