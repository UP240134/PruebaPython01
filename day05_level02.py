#Ejercicio 2
ages = ["19","22","19","24","20","25","26","24", "25","24"]
print("Edades =", ages)
Vmax = max(ages)
print("Edad maxima", Vmax)
Vmin = min(ages)
print("Edad minima" , Vmin)
ages_ord = ["19","19","20","22","24","24","24","25","25","26"]
print("Edades ordenadas" , ages_ord)
Suma = 26+19
Res = Suma/2
print("La media de edad es: ",Res.__trunc__() )
Suma2= (19 + 19 + 20 + 22 + 24 + 24 + 24 + 25 + 25 + 26)
Prom= (Suma2/10) 
print("Promedio de los datos es: ",Prom)
ages_int = [int(age) for age in ages]
range_ages = max(ages_int) - min(ages_int)
print("Rango de edades:", range_ages)
min_diff = abs(min(ages_int) - Prom)
max_diff = abs(max(ages_int) - Prom)
print("abs(min - promedio):", min_diff)
print("abs(max - promedio):", max_diff)

# Suponiendo que tienes una lista llamada countries
countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan']

# Encontrar el/los país(es) del medio
mid = len(countries) // 2
if len(countries) % 2 == 0:
    middle_countries = countries[mid-1:mid+1]
else:
    middle_countries = [countries[mid]]

print("País(es) del medio:", middle_countries)
countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan']

n = len(countries)
mid = n // 2
if n % 2 == 0:
    first_half = countries[:mid]
    second_half = countries[mid:]
else:
    first_half = countries[:mid+1]
    second_half = countries[mid+1:]

print("Primera mitad:", first_half)
print("Segunda mitad:", second_half)
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

first, second, third, *scandic_countries = countries

print("First country:", first)
print("Second country:", second)
print("Third country:", third)
print("Scandic countries:", scandic_countries)