texto = 'R$13,89em2x R$6,95sem juros'


frase =[]
for i in texto:
    if i != 'e':
        frase.append(i)
    else:
        break

listToStr = ''.join(map(str, frase))
print(listToStr)


"""------------------------------"""


prices = ['R$38em6x R$6,97', 'R$39,99em6x R$6,67sem juros', 'R$89,99em12x R$7,50sem juros', 'R$98em12x R$8,17sem juros',
 'R$99em12x R$8,25sem juros', 'R$100em12x R$9,50', 'R$100em12x R$9,50', 'R$100em12x R$8,33sem juros', 'R$139em12x R$13,20',
 'R$180em12x R$17,10', 'R$200em12x R$19', 'R$200em12x R$16,67sem juros', 'R$247,90em12x R$20,66sem juros', 'R$260em12x R$21,67sem juros',
 'R$279,90em12x R$23,33sem juros', 'R$280em12x R$26,60', 'R$280em12x R$23,33sem juros', 'R$298em12x R$28,31', 'R$300em12x R$28,50', 'R$309em12x R$29,35',
 'R$320em12x R$30,40', 'R$380em12x R$31,67sem juros', 'R$85em12x R$7,08sem juros', 'R$175em12x R$16,91', 'R$225em12x R$21,37', 'R$249,90em12x R$24,15',
 'R$250em12x R$23,75', 'R$250em12x R$20,83sem juros', 'R$250em12x R$23,75', 'R$250em12x R$23,75', 'R$250em12x R$24,16', 'R$250em12x R$24,16',
 'R$260em12x R$24,70', 'R$270em12x R$22,50sem juros', 'R$280em12x R$23,33sem juros', 'R$280em12x R$27,05', 'R$330em12x R$27,50sem juros', 'R$10em2x R$5,25',
 'R$12em2x R$6,30', 'R$13em2x R$6,82', 'R$13em2x R$6,82', 'R$13,90em2x R$6,95sem juros', 'R$13,90em2x R$6,95sem juros', 'R$15,99em3x R$5,33sem juros',
 'R$17,90em3x R$6,35', 'R$17,99em3x R$6sem juros', 'R$18em3x R$6,39', 'R$19,90em3x R$6,63sem juros', 'R$19,90em3x R$6,63sem juros', 'R$19,90em3x R$6,63sem juros']
print(len(prices))

p1 = []
for i in prices:
    newPrices = []
    for a in i:
        if a != 'e':
            newPrices.append(a)
        else:
            break
    p1.append(newPrices)
    

prices =[]
for i in p1:
    listToStr = ''.join(map(str, i))
    prices.append(listToStr)

print(prices)
print(len(prices))
