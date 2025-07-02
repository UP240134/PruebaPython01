#Dia 5 - Nivel 1
empty_list = []
my_list = [10, 20, 30, 40, 50, 60, 70]
print("Longitud de my_list:", len(my_list))
first_item = my_list[0]
middle_item = my_list[len(my_list)//2]
last_item = my_list[-1]
print("Primer elemento:", first_item)
print("Elemento del medio:", middle_item)
print("Último elemento:", last_item)
mixed_data_types = ["José", 30, 1.75, "Soltero", "Calle Falsa 123"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print("IT Companies:", it_companies)
print("Número de empresas:", len(it_companies))
print("Primera empresa:", it_companies[0])
print("Empresa del medio:", it_companies[len(it_companies)//2])
print("Última empresa:", it_companies[-1])
it_companies[1] = "Alphabet"
print("Lista modificada:", it_companies)
it_companies.append("Tesla")
print("Lista después de agregar:", it_companies)
it_companies.insert(len(it_companies)//2, "Twitter")
print("Lista después de insertar en el medio:", it_companies)
for i in range(len(it_companies)):
    if it_companies[i] != "IBM":
        it_companies[i] = it_companies[i].upper()
print("Lista en mayúsculas (IBM excluido):", it_companies)
joined = '#;  '.join(it_companies)
print("Unidas con '#;  ':", joined)
empresa = "GOOGLE"
print(f"{empresa} existe en la lista:", empresa in it_companies)
it_companies.sort()
print("Lista ordenada:", it_companies)
it_companies.reverse()
print("Lista en orden descendente:", it_companies)
print("Primeras 3 empresas:", it_companies[:3])
print("Últimas 3 empresas:", it_companies[-3:])
mid = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    middle_companies = it_companies[mid-1:mid+1]
else:
    middle_companies = [it_companies[mid]]
print("Empresa(s) del medio:", middle_companies)
it_companies.pop(0)
print("Después de eliminar la primera empresa:", it_companies)
mid = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    del it_companies[mid-1:mid+1]
else:
    del it_companies[mid]
print("Después de eliminar la(s) empresa(s) del medio:", it_companies)
it_companies.pop()
print("Después de eliminar la última empresa:", it_companies)
it_companies.clear()
print("Lista vacía:", it_companies)
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')
print(full_stack)