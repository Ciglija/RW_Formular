import os
import shutil
import re
import sys

print("Pokrenuta skripta za filtriranje PDF fajlova")

try:
    source_folder = os.path.abspath(os.path.join(os.getcwd(), "./input"))
    destination_folder = os.path.abspath(os.path.join(os.getcwd(), "./output"))

    print(f"Source folder: {source_folder}")
    print(f"Destination folder: {destination_folder}")

    if not os.path.exists(source_folder):
        print("Source folder NE postoji!")
        sys.exit(1)

    os.makedirs(destination_folder, exist_ok=True)

    pattern = re.compile(r"^[a-zA-Z]{2}\d{7}\.pdf$", re.IGNORECASE)
    print(f"Regex pattern: {pattern.pattern}")

    files = os.listdir(source_folder)

    def clean_filename(name):
        return re.sub(r"[^\w.]", "", name)

    moved = skipped = 0
    for filename in files:
        original_path = os.path.join(source_folder, filename)

        if not os.path.isfile(original_path):
            print(f"Preskacem (nije fajl): {filename}")
            continue

        cleaned_name = clean_filename(filename)

        if pattern.match(cleaned_name):
            dst = os.path.join(destination_folder, cleaned_name)
            if os.path.exists(dst):
                print(f"Preskacem (vec postoji): {cleaned_name}")
                skipped += 1
                continue
            shutil.move(original_path, dst)
            print(f"Premestio: {filename} -> {cleaned_name}")
            moved += 1
        else:
            print(f"Preskacem (los format): {filename}")
            skipped += 1

    print(f"\nRezultat: Premesteno {moved}, Preskoceno {skipped}")

except Exception as e:
    print(f"Greska: {e}")