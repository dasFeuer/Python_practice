a = int(input("Enter the number between 4 to 9: ")) 
if ( a < 4 or a  >  9):
    print("Number Exceuted")
else:
    raise ValueError("Value should be between 4 and 9")
