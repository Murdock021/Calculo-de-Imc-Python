nome = str (input("Qual seu Nome ? "))
sobrenome = str (input("Qual seu Sobrenome ?"))

print("Oi",nome,sobrenome, "Vamos iniciar o seu teste de IMC...")


peso = float(input("Qual o seu peso (em Kg):"))
altura = float(input("Qual é a sua altura(em metros): "))

imc = peso / (altura ** 2)

print (nome,sobrenome,"o seu IMC é {:.1f}".format(imc))

if imc <18.5:
    print(nome,sobrenome,"Você está abaixo do peso ideal")
elif 18.5 <=imc<24.9:
    print(nome,sobrenome,"Você está no peso normal")
elif 24.9<=imc<29.9:
    print(nome,sobrenome,"Você está acima do peso ideal")
else:
    print(nome,sobrenome,"Você tem obesidade grau I")