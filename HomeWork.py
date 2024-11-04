# Python exercises (TUESDAY)

# Ex 1 ( Creating a list )
fruits = ("Apple", "Mango", "Grapes", "Straberry", "Peach")
print(fruits) 


# Ex 2 ( Accesing elements )
colors = ['red', 'blue', 'green', 'yellow', 'purple']
print(colors[0], colors[2], colors[-1])


# Ex 3 ( Modifying a list )
numbers = [10,20,30,40,50]
numbers[1] = 25
numbers.append(60)
print(numbers)


# Ex 4 ( List Slicing )
names = ['Alice', 'Bob', 'Charlie', 'Davud', 'Emma']
subset = names[:3]
print(subset)


# Ex 5 ( Looping through a list )
numbers = list(range(1,11))
print("Squares of Numbers 1-10:")
for number in numbers:
    print(number ** 2)


# Ex 6 ( List Methods : Append / Extend )
shopping_cart = []
shopping_cart.append('milk')
shopping_cart.append('bread')
shopping_cart.append('eggs')
shopping_cart.extend(['butter', 'cheese'])
print(shopping_cart)


# Ex 7 ( Finding Min , Max in a list )
numbers = [45, 22, 88, 56, 92, 33]
print("Max Number: ", max(numbers))
print("Min Number: ", min(numbers))


# Ex 8 ( Counting Occurnaces )
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
print("Count of 'a': ", letters.count('a'))


# Ex 9 ( List Comprehension )
squares_of_even = [x ** 2 for x in range(11) if x % 2 ==0 ]
print(squares_of_even)


# Ex 10 ( Removing Duplicates )
nums = [1, 2, 3, 4, 5, 6, 7]
unique_nums = list(set(nums))
print(unique_nums)
