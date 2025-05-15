#List comprehension

#Syntax : [expression for item in iterable if condition]

#Create a list of squares from 1 to 10
squares = [i**2 for i in range(1,11)]
print(squares)  #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Get even numbers from 1 to 20
even_nums = [i for i in range(1,21) if i%2==0]
print(even_nums) #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#Convert all strings to upper case
langs = ["python","c","java","c++","html"]
uppercase = [i.upper() for i in langs]
print(uppercase) #['PYTHON', 'C', 'JAVA', 'C++', 'HTML']

#Extract digits from a string
text = "ab17hdg8768jbk"
digits = [char for char in text if char.isdigit()]
print(digits) #['1', '7', '8', '7', '6', '8']

#Numbers not divisible by 3 from 1 to 10
notdivby_3 = [i for i in range(1,11) if i%3!=0]
print(notdivby_3) #[1, 2, 4, 5, 7, 8, 10]

#Dictionary comprehension
#Syntax -> {key_expression:value_expression for item in range if condition}

#Square of numbers as a values
sq_nums = {num:num**2 for num in range(1,6)}
print(sq_nums) #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#Mapping words to their lengths
words = ["apple","mango","jackfruit","pineapple"]
word_len = {word:len(word) for word in words}
print(word_len) #{'apple': 5, 'mango': 5, 'jackfruit': 9, 'pineapple': 9}

#Filtering even numbers
evens_dict = {num:num for num in range(1,11) if num%2==0}
print(evens_dict) #{2: 2, 4: 4, 6: 6, 8: 8, 10: 10}

#Create dictionary from two lists
keys = [1,2,3]
values = ["one","two","three"]
res = {k:v for k,v in zip(keys,values)}
print(res) #{1: 'one', 2: 'two', 3: 'three'}

#Convert values to upper_case
data = {"f_name":"sravani","l_name":"Rayapureddy"}
upper_dict = {k:v.upper() for k,v in data.items()}
print(upper_dict) #{'f_name': 'SRAVANI', 'l_name': 'RAYAPUREDDY'}

#Set comprehension
#Syntax -> {expression for item in iterable if condition}

#Unique squares
nums = {2,8,10,2,7,1,9,10}
unq_squares = {num**2 for num in nums}
print(unq_squares) #{64, 1, 4, 100, 81, 49}

#Unique vowels
sentence = "Python language"
unq_vowels = {char for char in sentence if char in "aeiou"}
print(unq_vowels) #{'u', 'a', 'o', 'e'}

#Square of odd numbers
odd_squares = {num**2 for num in range(1,11) if num%2!=0}
print(odd_squares) #{1, 9, 81, 49, 25}

#Unique characters in a list
words = ["apple","banana"]
chars = {char for word in words for char in word}
print(chars) #{'a', 'l', 'n', 'b', 'p', 'e'}

#Generator comprehension
#Syntax -> (expression for item in iterable if condition)

#Generator for squares
squares = (num**2 for num in range(1,6))
print(list(squares)) #[1, 4, 9, 16, 25]

#Capitalised names
names = ["john","jane"]
cap_names = (name.capitalize() for name in names)
print(list(cap_names))





