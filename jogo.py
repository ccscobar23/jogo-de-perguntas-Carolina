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
        
#3 pergunta
cantor = input("Quem escreveu a música 'Oceano'?")

if cantor == "Djavan" or cantor == "djavan":
    print("Exatamente, a resposta está correta!")
else:
        print("Não foi dessa vez!")
        
#4 pergunta
cidade = input("De qual cidade é a banda Charlie Brown Jr?")

if cidade == "Santos" or cidade == "santos":
    print("Parabéns, você está indo muito bem!")
else:
        print("Não foi dessa vez!")
