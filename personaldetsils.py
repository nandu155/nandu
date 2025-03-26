def get_person_detail():
    name = input("enter your name:")
    address = input("enter your address:")
    email = input("enter your email:")
    phone = input("enter your phone number:")
    return name,address,email,phone

def print_person_details(name,address,email,phone):
    print(f"\n---Personal Details---")
    print(f"Name:{name}")
    print(f"Address:{address}")
    print(f"Email:{email}")
    print(f"Phone Number:{phone}")

name,address,email,phone = get_person_detail()

print_person_details(name,address,email,phone)
