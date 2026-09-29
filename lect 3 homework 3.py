num = int(input("enter a number: "))

is_positive = num > 0
print ("is_positive: ", is_positive)

is_negative = num < 0
print ("is_negative: ", is_negative)

is_zero = num == 0
print ("is_zero: ", is_zero)

is_even = (num % 2 == 0)
print ("is_even: ", is_even)

if is_positive:
    sign = "positive"
elif is_negative:
    sign = "negative"
else:
    sign = "zero"
    print ("The number is: ", sign)

