distancia= float(input("Qual a diatância que se pretende percorrer em km?"))
velocidade= float(input("Qual a velocidade média?"))

tempo_viagem= (distancia / velocidade)

print(f"O tempo da viagem foi de {tempo_viagem:.1f} horas")