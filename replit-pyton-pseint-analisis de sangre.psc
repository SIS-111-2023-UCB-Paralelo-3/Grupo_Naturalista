#alumno 1 alan poquechoque
def sumatoria (LDLcolesterol,HDLcolesterol,VLDLcolesterol):
    sumatoria=LDLcolesterol+HDLcolesterol+VLDLcolesterol
if sumatoria<200:
	return "Su nivel de colesterol es, "+str(sumatoria)+ " ,es decir,optimo"
else:
if sumatoria>200 and sumatoria<240:
	return"Su nivel esta sobre el limite optimo y el alto"
else:
	sumatoria>240
	return" Su nivel de colesterol es muy alto"
def LDLcolesterol1(LDLcolesterol):
if LDLcolesterol<100:
	return"LDLcolesterol es optimo"
else:
if LDLcolesterol>100 and LDLcolesterol<129:
	return "Su LDLcolesterol esta sobre el limite"
else:
if LDLcolesterol>130 and LDLcolesterol <189:
	return " Su LDLcolesterol es alto"
else:
if LDLcolesterol>190:
	return "Su LDLcolesterol es muy alto"
def HDLcolesterol1 (HDLcolesterol):
if HDLcolesterol>40 and HDLcolesterol<60:
	return "HDLcolesterol es optimo"
else:
if  HDLcolesterol>60:
	return "HDLcolesterol  es beneficioso"
def VLDLcolesterol1 (VLDLcolesterol):      
if VLDLcolesterol>2 and VLDLcolesterol<30:
	return "VLDLcolesterol es Optimo"
else:
if VLDLcolesterol>30:
	return "VLDLcolesterol es perjudicial" 
	
    
	print("Ingrese sus datos de colesterol")
	LDLcolesterol=float(input("Ingrese sus datos LDLcolesterol"))
	HDLcolesterol=float(input("Ingrese sus datos de nivel de HDLcolesterol"))
	VLDLcolesterol=float(input("Ingrese sus datos de nivel VLDLcolesterol"))
	print (LDLcolesterol1(LDLcolesterol))
	print (HDLcolesterol1(HDLcolesterol))
	print (VLDLcolesterol1(VLDLcolesterol))
	print (sumatoria(LDLcolesterol,HDLcolesterol,VLDLcolesterol))
	#alumno2 matias medrano
	#se equivoco pero mañana lo arregla
	HDL_Colesterol=int(input("por favor ingrese su HDL-Colesterol medido: "))
	LDL_Colesterol=int(input("por favor ingrese su LDL-Colesterol: "))
	VLDL_Colesterol=int(input("por favor ingrese su VLDL-Colesterol: "))
if HDL_Colesterol>40 and HDL_Colesterol<60:
    resultado="Optimo"
elif HDL_Colesterol>60:
    resultado="Alto pero Benificioso"
else:
    resultado="Bajo"
	print("HDL-Colesterol :" + resultado)
	
if LDL_Colesterol<100:
    resultado="Optimo"
elif LDL_Colesterol>100 and LDL_Colesterol<129:
    resultado="Sobre el limite de optimo"
elif LDL_Colesterol>129 and LDL_Colesterol<189:
    resultado="Alto"
elif LDL_Colesterol>=190:
    resultado=" Muy Alto"
	print("LDL-Colesterol :" + resultado)
	
if VLDL_Colesterol>2 and VLDL_Colesterol<30:
    resultado="optimo"
elif VLDL_Colesterol>30:
    resultado="Perjudicial"
	print("VLDL-Colesterol :" + resultado)
	colesterolTotal=HDL_Colesterol+LDL_Colesterol+VLDL_Colesterol
	print("Coresterol Total: ", colesterolTotal , "mg/dl")
	print("                         ElMedraPa")
	
	#para alumno3 tito palacios
		#Alumno3
		#Valores sobre la apolipoproteina
		import alumno 1
		import alumno 2
		import alumno 3
	def apolipoproteinaA_I1(apolipoproteinaA_I):
    if apolipoproteinaA_I == 130:
        return"su nivel de apolipoproteinaA_I es optimo"
    else:
	if apolipoproteinaA_I > 130:
		return"su nivel de apolipoproteinaA_I es beneficioso"
	def apolipoproteinaB1(apolipoproteinaB):
    if apolipoproteinaB < 90:
        return"su nivel de apolipoproteinaB es optimo"
    else:
	if apolipoproteinaB > 90 and apolipoproteinaB < 115:
		return"su nivel de apolipoproteinaB esta sobre el limite optimo"
	else:
	if apolipoproteinaB > 115 and apolipoproteinaB < 140:
		return"su nivel de apiloproteinaB es alto"
	else:
	if apolipoproteinaB > 140:
		return"su nivel de apiloproteinaB es muy alto"
		print("ingrese sus valores de apolipoproteina")
		apolipoproteinaA_I=float(input("Ingrese sus datos de apolipoproteinaA_I"))
		apolipoproteinaB=float(input("Ingrese sus datos de apolipoproteinaB"))
		print(apolipoproteinaA_I1(apolipoproteinaA_I))
		print(apolipoproteinaB1(apolipoproteinaB))

