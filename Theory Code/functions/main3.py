# keyword argumets -> doesnt care about order, preceed by an identifier

def hello(greeting, title, first, last):
    print(f"{greeting}, {title}.{first} {last}")

hello(greeting="Hello", first="Marius", last="Covali", title="Mr")

print("1", "2", "3", "4", "5", sep="-")

def get_phone(country_code, area_code, first, last):
    return f"{country_code} - {area_code} - {first} - {last}"

phone_num = get_phone(country_code=373, area_code=780, first=36, last=553)

print(phone_num)