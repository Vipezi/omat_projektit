#! /usr/bin/python3

def ask_link():
    link = input("what will be the link name, link name should start with link_ : ")
    if link.startswith('link_'):
        return link
    else:
        return False

def ask_shape():
    shape = input("""What shape you want to use:
                      1 = Solid sphere
                      2 = Solid cuboid
                      3 = Solid cylinder """)

    if shape == "1":
        return "Solid sphere"
    elif shape == "2":
       return "Solid cuboid"
    elif shape == "3":
        return "Solid cylinder"
    else:
        return False

def ask_value(metric):
    value = input(f"now give, {metric} as decimal number: ")
    try:
        float(value)
        #pass
    except ValueError:
        print("Not a valid answer, try again.")
        ask_value(metric)
    
    return value

def repeat():
    beginning_of_the_end = input("Do you want to quit, then answer yes if you want to continue answer no: ")
    if beginning_of_the_end == "no":
        main()
    elif beginning_of_the_end == "yes":
        pass
    else:
        print("Not a valid answer, try again.")
        repeat()

def add_values_to_list(value):
    values.append(value)


#links = []
#shapes = []
#masses = []
#radiuses = []

values = []
def main():
    
    program = True
    while program:
        link = ask_link()
        if link == False:
            print("Not a valid answer, try again.")
            ask_link()
        else:
            #links.append(link)
            pass


        shape = ask_shape()
        if shape == False:
            print("Not a valid answer, try again.")
            ask_shape()
        else:
            #shapes.append(shape)
            pass

        if shape == "Solid sphere":
            print(f"you choosed {shape}, give: mass, radius")
            mass = ask_value("mass")
            add_values_to_list(mass)
            radius = ask_value("radius")
            add_values_to_list(radius)
        elif shape == "Solid cuboid":
            print(f"you choosed {shape}, give: width, height, depth and mass")
            width = ask_value("width")
            add_values_to_list(width)
            height = ask_value("height")
            add_values_to_list(height)
            depth = ask_value("radius")
            add_values_to_list(depth)
            mass = ask_value("mass")
            add_values_to_list(mass)
        else:
            print(f"you choosed {shape}, give: radius, height and mass")
            radius = ask_value("radius")
            add_values_to_list(radius)
            height = ask_value("height")
            add_values_to_list(height)
            mass = ask_value("mass")
            add_values_to_list(mass)
            
        repeat()

        filename = input("give a filename where to save, use .xml ending for filename: ")
        try:
            filename.endswith('.xml')
            pass
        except NameError:
            print("Not a right file type!")
        with open(filename, 'w') as f:
            for str in values: 
                f.write(str)
            break
        

main()