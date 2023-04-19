#Torneo_Relampago
import random


equipos = ['IngenieriaEnSistemas', 'IngenieriaMecatronica', 'Medicina', 'IngenieriaCivil', 'IngenieriaBiomedica', 'IngenieriaComercial', 'Arquitectura', 'Derecho']


partidos = []
while len(equipos) >= 2:
    equipo1, equipo2 = random.sample(equipos, 2)
    partidos.append((equipo1, equipo2))
    equipos.remove(equipo1)
    equipos.remove(equipo2)
	
	
	print("Cuartos de final:")
for partido in partidos:
    print(partido[0], "vs", partido[1])
	
	
	ganadoresCuartosDeFinal = [random.choice(partido) for partido in partidos]
	print("\nEquipos que pasaron a semifinales:", ganadoresCuartosDeFinal)
	
	
	semifinales = []
while len(ganadoresCuartosDeFinal) >= 2:
    equipo1, equipo2 = random.sample(ganadoresCuartosDeFinal, 2)
    semifinales.append((equipo1, equipo2))
    ganadoresCuartosDeFinal.remove(equipo1)
    ganadoresCuartosDeFinal.remove(equipo2)
	
	
	print("\nSemifinales:")
for partido in semifinales:
    print(partido[0], "vs", partido[1])
	
	
	ganadoresSemifinales = [random.choice(partido) for partido in semifinales]
	print("\nEquipos que pasaron a la final:", ganadoresSemifinales)
	
	
	print("\nFinal:")
	print(ganadoresSemifinales[0], "vs", ganadoresSemifinales[1])
	
	
	ganadorFinal = random.choice(ganadoresSemifinales)
	print("\nGanador del torneo:", ganadorFinal)
	
	
	perdedoresSemifinales = [partido for partido in semifinales if partido not in ((ganadoresSemifinales[0], ganadoresSemifinales[1]),)]
	print("\nEquipos que jugaron para tercer lugar:", [x[0] for x in perdedoresSemifinales])
	
	
	print("\nPartido por tercer lugar:")
	print(perdedoresSemifinales[0][0], "vs", perdedoresSemifinales[1][0])
	
	
	ganadorTercerLugar = random.choice([perdedoresSemifinales[0][0], perdedoresSemifinales[1][0]])
	print("\nGanador del tercer lugar:", ganadorTercerLugar)
