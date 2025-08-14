import os
import random
import string


print("🔧 Pokrenuta skripta za generisanje test PDF-ova...")
output_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "../in1"))
os.makedirs(output_folder, exist_ok=True)
print(output_folder)

def write_fake_pdf(path):
    with open(path, "wb") as f:
        f.write(b"%PDF-1.4\n%Fake PDF\n")

def generate_valid_name():
    letters = ''.join(random.choices(string.ascii_letters, k=2))
    numbers = ''.join(random.choices(string.digits, k=7))
    return f"{letters}{numbers}.pdf"

def generate_partial_name():
    base = generate_valid_name().replace(".pdf", "")
    change_type = random.choice(["missing_digit", "extra_letter", "wrong_order", "bad_extension"])
    if change_type == "missing_digit":
        base = base[:8]  # skrati
    elif change_type == "extra_letter":
        base = base[:2] + random.choice(string.ascii_letters) + base[2:]  # ubaci još jedno slovo
    elif change_type == "wrong_order":
        base = ''.join(random.sample(base, len(base)))  # izmešaj
    elif change_type == "bad_extension":
        return base + ".txt"
    return base + ".pdf"

# 3. Netačni: nasumični karakteri
def generate_invalid_name():
    chars = string.ascii_letters + string.digits + " _-@#$%"
    name = ''.join(random.choices(chars, k=random.randint(5, 15)))
    return name + ".pdf"

# Generiši fajlove
for i in range(165):
    fname = generate_valid_name()
    write_fake_pdf(os.path.join(output_folder, fname))

for i in range(165):
    fname = generate_partial_name()
    write_fake_pdf(os.path.join(output_folder, fname))

for i in range(170):
    fname = generate_invalid_name()
    write_fake_pdf(os.path.join(output_folder, fname))

print("✅ Generisano 500 test PDF fajlova u folderu:", output_folder)
