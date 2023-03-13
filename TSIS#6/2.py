x = "dscwecdssnoanjknUINXAanQXUIANkauxnNXSJac"
sum_upper_letter = 0
sum_lower_letter = 0
for i in x:
    if i.islower():
        sum_lower_letter += 1
    elif i.isupper():
        sum_upper_letter += 1
print("There is {} lower letters".format(sum_lower_letter))

print("There is {} upper letters".format(sum_upper_letter))
