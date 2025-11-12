#colocar título e descrever o jogo
print("JOGO DE PERGUNTAS")

print("O jogo será trabalhado na forma de utilizar dados externos, para desenvolver respostas e novas perguntas usando a ideia de input.")

#pensar em um tema
nome = input("qual é seu nome?")
print("oii", nome,"! Hoje vamos fazer um quiz sobre música! Vamos começar?")

#primeira pergunta
maiorbanda = input("Qual é considerada a maior banda de todos os tempos?")

if maiorbanda == "Beatles" or maiorbanda == "beatles" or maiorbanda == "The Beatles" or maiorbanda =="the beatles":
    print("Parabéns,",nome,", você acertou!")

else:
        print("Não foi dessa vez!")

#2 pergunta
banda = input("De qual banda é a música 'Tempo Perdido'?")

if banda == "Legião Urbana" or banda == "legião urbana" or banda == "Legiao Urbana" or banda == "legiao urbana":
    print("Ótimo, você acertou!")
else:
        print("Não foi dessa vez!")
