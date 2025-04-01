cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = int(input("Há quantos anos você fuma? "))

minutos_por_cigarro = 10  
minutos_por_dia = cigarros_por_dia * minutos_por_cigarro  
total_minutos = minutos_por_dia * (anos_fumando * 365)  
total_dias = total_minutos / (24 * 60)


print(f"Você perdeu aproximadamente {total_dias:.2f} dias de vida devido ao fumo.")
