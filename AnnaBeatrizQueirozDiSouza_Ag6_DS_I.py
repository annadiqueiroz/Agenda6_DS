valor_compra = float(input("Digite o valor total da compra: ")) #float para permitir valores decimais

if valor_compra < 200: 
    print(f"Você recebeu um desconto de 5%! Seu valor com desconto é de {valor_compra - valor_compra*0.05}") #pega o valor total e subtrai do valor com desconto
elif valor_compra >=200 and valor_compra <300: #indentado para estar dentro do bloco
    print(f"Você recebeu um desconto de 10%! Seu valor com desconto é de {valor_compra - valor_compra*0.10}")
else: #se for maior que 300
    print(f"Você recebeu um desconto de 15%! Seu valor com desconto é de {valor_compra - valor_compra*0.15}")