import inflect

p=inflect.engine()
names=[]

while True:
    try:
        name=input("Name: ")
        names.append(name)

    except EOFError:
        break


formated_name=p.join(names)
print(f"Adieu, adieu, to {formated_name}")
    

