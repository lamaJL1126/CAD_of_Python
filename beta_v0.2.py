import ezdxf

points_list = []

commads_code = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "All": 8,
    "Command_Code_Start------------": 9,
    "stop": 10,
    "search": 11,
    "clear": 12,
    "Command_Code_End--------------": 13,
}

def search_command(search_object_number):
    return points_list[search_object_number]

def clear_commad(clear_object):
    if input("Clear (Y/N): ").strip().upper() == "Y":
        if clear_object == 8:
            points_list.clear()
        else:
            points_list[clear_object] = None
    else:
        print("Operation canceled.")

def commads(number):
    if number == 11:    # search
        search_object = input("What point do you need to search : ")
        search_object_number = commads_code.get(search_object, None)
        
        if search_object_number is None:
            print("Point not found.")
        elif search_object_number == 8:
            print("All points: ")
            for i, point in enumerate(points_list):
                if point is not None:
                    print(f"Point {i}: {point}")
        else:
            if points_list[search_object_number] is not None:
                print(f"{search_object} = {points_list[search_object_number]}")
            else:
                print(f"{search_object} has not been set.")

    elif number == 12:  # clear
        clear_object = input("What point do you need to clear (or All): ")
        clear_object_number = commads_code.get(clear_object, None)
        
        if clear_object_number is not None:
            clear_commad(clear_object_number)
            print(f"Cleared {clear_object}")
        else:
            print("Invalid point code.")

while True:
    print("""
           _ - D - _
      A_ -     .     - _     
      |- _     .         - _ 
      |    - _ .         _ - C
      |        - _   _ -     |
      |        .   B         |
      |        .   |         |
      |    _ - H - |         |
      |_ -         | - _     |
      E- _         |     - _ |
           - _     |     _ - G
               - _ | _ -     
                   F
    """)

    commad_code_input = input("/")

    number = commads_code.get(commad_code_input, None)
    if number is None:
        print("Invalid command code.")
        continue

    if number <= 7:
        try:
            x = int(input(f"Point {commad_code_input} x = "))
            y = int(input(f"Point {commad_code_input} y = "))
            z = int(input(f"Point {commad_code_input} z = "))
        except ValueError:
            print("You need to input integers.")
            continue
        points_list.insert(number, (x, y, z))

    elif number == 10:
        break
    elif 9 < number < 13:
        commads(number)