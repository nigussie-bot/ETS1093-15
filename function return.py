#define function 
def area(l, w):
    # Calculate the area of the rectangle
    a = l * w
    
    return a  # Return the calculated area

# Get user input for length and width
length = int(input('Enter length of rectangle: '))
width = int(input('Enter width of rectangle: '))

result=area(length, width)

# Print the result
print("Area of rectangle is: " + str(result))
