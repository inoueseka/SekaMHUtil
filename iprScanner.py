# Scan through IPR files in same path for a specified keyword. (Set to "Assets" by default)

from pathlib import Path
import re

SEARCH_STRING = "Assets"

for file_path in Path(".").rglob("*.ipr"):  
    with file_path.open("rb") as file:  # Open file in binary mode
        # Read the file
        contents = file.read().decode(errors="ignore")  # Decode binary content to string
        
        if SEARCH_STRING in contents:
            print(file_path)
            matches = re.findall(f'({SEARCH_STRING}.{{1,100}})', contents) # Find all occurrences of the search string following "Assets" up to specified bytes

            # Alternatively, to find all occurrences of the search string preceding "Assets" up to specified bytes
                # matches = re.findall(f'.{{1,100}}{SEARCH_STRING}.{{0,100}}', contents)
            
            for match in matches:
                print(match)

input("Press Enter to exit...")
