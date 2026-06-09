import random, os, json, time

selection = ""

if not os.path.exists('listThing.json'):
    with open("listThing.json", "w") as f:
        f.write('[]')
    
with open('listThing.json', 'r') as f:
    listThing = json.load(f)

def ls():
    if len(listThing) == 0:
        print("No items. Type n to add a new item.")
    else:
        print("#\tID\tname")
        for i in range(len(listThing)):
            if listThing[i]["isPrime"]:
                isPrimeSign = "*"
            else:
                isPrimeSign = ""
            print(f"{i+1} {isPrimeSign}\t{listThing[i]["order"]}\t{listThing[i]["name"]}")
        print("* Prime items")

def add():
    name = ""
    isPrimeInput = -1
    isPrime = False
    isPrimeSign = ""
    orderId = random.randint(0, 500)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Add New Item")
    print("─────────────────────────────")
    name = input("Type the name of item: ")
    while isPrimeInput != 0 and isPrimeInput != 1:
        isPrimeInput = int(input("Is it Prime? Type 0 for No, 1 for Yes. "))
        if isPrimeInput == 0:
            isPrime = False
        elif isPrimeInput == 1:
            isPrime = True
    listThing.append({"name": name, "order": orderId, "isPrime": isPrime})
    with open('listThing.json', 'w+') as f:
        f.write(json.dumps(listThing))
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Add New Item")
    print("─────────────────────────────")
    print(f"Added {name} (ID: {orderId})")
    time.sleep(1.5)
        
def delete():
    selectDelete = 0
    while selectDelete < 1 or selectDelete > len(listThing):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Delete an Item")
        print("─────────────────────────────")
        ls()
        selectDelete = int(input("\nSelect one to delete: "))
    nameDelete = listThing[selectDelete-1]["name"]
    idDelete = listThing[selectDelete-1]["order"]
    del listThing[selectDelete-1]
    with open('listThing.json', 'w+') as f:
        f.write(json.dumps(listThing))
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Delete an Item")
    print("─────────────────────────────")
    print(f"Deleted {nameDelete} (ID: {idDelete})")
    time.sleep(1.5)
        
def ship():
    global listThing
    os.system('cls' if os.name == 'nt' else 'clear')
    listThing = sorted(listThing, key=lambda x: x['isPrime'], reverse=True)
    print("Shipping Simulator")
    print("─────────────────────────────")
    ls()
    print()
    for i in range(len(listThing)):
        print(f"Shipping {i+1}. {listThing[i]["name"]} (ID: {listThing[i]["order"]})")
        time.sleep(5)
    
while selection.lower() != "q":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Project Amazonita")
    print("─────────────────────────────")
    ls()
    if len(listThing) > 0:
        print("\nn: New Item\t d: Delete an Item\ts: Shipping Simulator\tq: Quit")
    selection = input("\n>>> ")
    if selection.lower() == "n":
        add()
    if selection.lower() == "d":
        delete()
    if selection.lower() == "s":
        ship()
