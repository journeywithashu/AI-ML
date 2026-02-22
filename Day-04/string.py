word1 = "I Love"
word2 = "python"
sentence = word1 + " " + word2


#concatenate
print(sentence)

#Slicing

word = "I study from itself"

print(word[5:])

#String formatting

a = 5
b = 10
sum = a + b
print("sum is {}".format(sum))

#normal formating
print("language is {}".format("python"))
print("sum of {} & {} is {}".format(a, b, sum))

#index based formatting
print("sum of {1} & {0} is {2}".format(a, b, sum ))

#value based formatting
print("value of vars {a} & {b}".format(a = 5, b = 10))

#f- string

print(f"sum of {a} & {b} is {a + b}")