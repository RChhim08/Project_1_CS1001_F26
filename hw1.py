"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data


#Part 1: vowel_count
# TODO: Purpose: The function counts how many vowels are inside of a string
# TODO: Input(s): The input is called "text" which is a string
# TODO: Output: The function returns the int count, which is an accumlator that counts how many vowels are in text
def vowel_count(text: str) -> int: 
    vowel = "aeiouAEIOU" 
    count = 0
    for char in text:
        if char in vowel:
            count += 1
    return count 

# Part 2: short_lists
# TODO: Purpose: The function looks for lists with the length of 2 and returns every list that has the length of 2
# TODO: Input(s): The input is a nest list that the function will look through
# TODO: Output: The function returns final which is another nested list that will contain each list from items that has a length of 2
def short_lists(items: list[list[int]]) -> list[list[int]]:
    final = []
    for i in items:
        if len(i) == 2:
            final.append(i)
    return final


    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 2: implement short_lists")


# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: The function returns a list where lists that have a length of 2 are ascending in order while everything remains untouched from the original list.
    # TODO: Input(s): The parameter items is a nested list that will contain int values
    # TODO: Output: The function will return a nested list with ints, untouched besides of lists that have length of 2 which will be an ascending order. 
    final = []
    for i in items:
        if len(i) == 2:
            copy = i[:] #prevents mutating the original nested list (I don't know if I needed the orignal list to stay the same or not...better safe than sorry)
            if copy[0] > copy[1]: 
                temp = copy[1]
                copy[1] = copy[0]
                copy[0] = temp
            final.append(copy)
        else:
            final.append(i)
    return final 





    # TODO: Replace this exception with your implementation.
    #raise NotImplementedError("Part 3: implement ascending_pairs")


# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    # TODO: Purpose: The function will sum up first and second and return an object representing the sum in dollars and cents seperatly
    # TODO: Input(s): First and second are objects that have the attribute of dollars and cents.
    # TODO: Output: The function will return an object with new attributes created from the attributes from the objects of first and second.
    newCent = first.cents + second.cents
    newDollar = first.dollars + second.dollars
    if newCent >= 100:
        while newCent >= 100:
            newCent -= 100
            newDollar += 1 
    return data.Price(newDollar, newCent)
    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 4: implement add_prices")


# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    # TODO: Purpose: The function will return the area of the given rectangle object throughs simple multiplication 
    # TODO: Input(s): The rectangle object is an object that will be passed through the function in which I will use its attributes to compute its area.
    # TODO: Output: The function will return a float that will represent the rectangles area
    height = rectangle.top_left.y  - rectangle.bottom_right.y
    width = rectangle.bottom_right.x - rectangle.top_left.x
    area = height * width
    return area
    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 5: implement rectangle_area")


# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # TODO: Purpose: The function will find every book made by an author 
    # TODO: Input(s): Author is a string that will be used to find what books match with it.
    # TODO: Output: explain what the function returns.
    final = []
    for book in books:
        if author in book.authors:
            final.append(book)
    return final
    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 6: implement books_by_author")


# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # TODO: Purpose: The function finds a circle that can enclose the rectangle perfectly based on the rectangles attributes
    # TODO: Input(s): The rectangles parameter is an object that has attributes relating to the rectangles coordinates, top left and bottom right
    # TODO: Output: The function returns an object that represents the circle that can encole the rectangle
    y_center = (rectangle.top_left.y + rectangle.bottom_right.y)/2
    x_center = (rectangle.top_left.x + rectangle.bottom_right.x)/2
    center = data.Point(x_center, y_center)
    dy = center.y - rectangle.top_left.y
    dx = center.x - rectangle.top_left.x
    radius = (dx ** 2 + dy ** 2) ** 0.5
    return data.Circle(center, radius)
    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 7: implement circle_bound")


# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # TODO: Purpose: Find the average pay across employees but return a list of names that are being paid below this minimum.
    # TODO: Input(s): The parameters is the object Employee that has the attributes name which is a string and pay_rate which is an int
    # TODO: Output: The function returns a list of strings which are the names of the employees whos pay is stricly below the average
    if employees == []:
        return []
    count = 0
    name_list = []
    avg_pay = 0
    for name in employees:
        count += 1
        avg_pay += name.pay_rate
    avg_pay = avg_pay/count
    for name in employees:
        if name.pay_rate < avg_pay:
            name_list.append(name.name) 
    return name_list

    # TODO: Replace this exception with your implementation.
    raise NotImplementedError("Part 8: implement below_pay_average")
