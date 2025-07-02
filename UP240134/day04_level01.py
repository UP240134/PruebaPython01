C1 = "Treinta "
C2 = "días "
C3 = "de "
C4 = "Python"
Cad_Com = C1 + C2 + C3 + C4
print(Cad_Com)

E1 = "Codificacion "
E2 = "para "
E3 = "todos"
Emp_com = E1+E2+E3
print(Emp_com)
print(len(Emp_com))
print(Emp_com.upper())
print(Emp_com.lower())
print(Emp_com.capitalize())
print(Emp_com.title())
print(Emp_com.swapcase())
Word = Emp_com.split()
SWord = "".join("Codificacion")
print(SWord)
print("Codificacion"in Emp_com)
print(Emp_com.find("Codificacion "))
print(Emp_com.index("Codificacion "))
Cad2 = "Coding For All"
New_cad = Cad2.replace("Coding","All")
F1 = "Python for Everyone"
F1mod = F1.replace("Everyone","All")
print(F1mod)
F2 = "Coding for All"
Div_spa = F2.split()
print(Div_spa)
Empresas= "Facebook, Google , Microsoft, Apple , IBM, Oracle, Amazon"
divido = Empresas.split(",")
print(divido)
print(F2[0])
ult=len(F2)-1
print(ult)
print(F2[ult])
print(F2[10])
P1= "Python for Everyone".split()
ac1 = "".join([p[0] for p in P1])
print(ac1)
P2= "Coding for All".split()
ac2= "".join([p[0] for p in P2])
print(ac2)
print(F2.index("C"))
print(F2.index("f"))
F3="Coding for all People"
print(F3.rfind("l"))
F3 = "No se puede terminar una oración con because porque es una conjunción"
Bcause= F3.find("because")
print(Bcause)
F4="No se puede terminar una oración con because porque es una conjunción"
Pcause = F4.rindex("because")
print(Pcause)
F5 = "No se puede terminar una oración con because porque es una conjunción"
Rcause = F5.replace("because","")
print(Rcause)
F6 = "No se puede terminar una oración con because porque es una conjunción"
Fcause= F6.find("because")
print(Fcause)
T1="Coding for All"
Rt = T1.startswith ("Coding")
print(Rt)
T2="Coding for All"
Rt2= T2.endswith("Coding")
print(Rt2)
T3= "Coding for All"
Rts=T3.strip()
print(f"Resultado de"[T3.endswith("coding")])
texto = "  Coding For All  "
res = texto.strip()
print(f'Resultado sin espacios: "{res}"')
variables = ["variable1", "1variable", "variable_1", "variable-1", "Variable", "_variable"]
for var in variables:
    print(f'{var}: {var.isidentifier()}')

       
    print("30DaysOfPython:", "30DaysOfPython".isidentifier())           # False
    print("thirteen_days_of_python:", "thirteen_days_of_python".isidentifier())  # True
    
  
    bibliotecas = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
    unidas = ' # '.join(bibliotecas)
    print(unidas)  
    

    oracion1 = "30DaysOfPython"
    oracion2 = "hola mundo"
    print(f"{oracion1}\n{oracion2}")