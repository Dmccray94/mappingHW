# question 1

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

actual_places =list(filter(lambda place: place.strip(), places))

print(actual_places)

# question 2
author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

sorted_authors = sorted(author, key=lambda authors: authors.split(" ")[-1].lower())

print(sorted_authors)

# question 3

# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

f_places = list(map(lambda temp: (temp[0], (9/5)*temp[-1] + 32), places))

print(f_places)

# question 4

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
    
for n in range(0,6):
    print(f"Iteration {n}: {fibonacci(n)}")