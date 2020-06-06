vegetarian = input('Is anyone in your party a vegetarian?: ')
if vegetarian == 'yes':    
    vegan = input('Is anyone in your party a vegan?: ')
    if vegan == 'yes':
        gluten_free = input('Is anyone in your party gluten-free?: ')
        if gluten_free == 'yes':
            print('Here are your restaurant choices:')
            print("Corner's Cafe")
            print("The Chef's Kitchen")
            print('Main Street Pizza Company')
            print("Mama's Fine Italian")
    
        else:
            print('Here are your restaurant choices:')
            print("Joe's Gourmet Burgers")
            print("Mama's Fine Italian")
    else:
        gluten_free = input('Is anyone in your party gluten-free?: ')
        print('Here are your restaurant choices:')
        print("Joe's Gourmet Burgers")
        print('Main Street Pizza Company')
        print("Mama's Fine Italian")       
            
else:
    print('Here are your restaurant choices:')
    print("Joe's Gourmet Burgers")
        
        
