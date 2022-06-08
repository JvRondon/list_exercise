list = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 12, 3, 3, -52]

greatervalue = list[0]
smallervalue = list[0]
pairlist = []
negativesum = 0
average  = 0

print('Greaters: ' + str(greatervalue))
for index in range(0, len(list)):
    #greatervalue
    if (greatervalue < list[index]):
        greatervalue = list[index]

print('--------------------------------------------------------------------------------------')
print('Smallers:' + str(smallervalue))

# smallervalue
if (smallervalue > list[index]):
    smallervalue = list[index]

print(smallervalue)
print('--------------------------------------------------------------------------------------')
print('Pair: ' + str(pairlist))

# Pair numbers
if (list[index] % 2 == 0):
    pairlist.append(list[index])

print(pairlist)
print('--------------------------------------------------------------------------------------')
print('Sum of the negatives: ' + str(negativesum))

# Sum of the negatives
if (list[index] < 0):
    negativesum = negativesum + list[index]

    # avarage
    average  = +average  + list[index]
average  = average  / len(list)

print('--------------------------------------------------------------------------------------')
print('Average: ' + str(average ))
