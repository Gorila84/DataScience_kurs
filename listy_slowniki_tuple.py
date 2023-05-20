# Zadanie 1¶
# Biorąc pod uwagę ciąg o nieparzystej długości większej niż 7, zwróć łańcuch złożony z trzech środkowych znaków danego ciągu: Przypadek 1: str1 = "Datatypes" Oczekiwany wynik: aty Przypadek 2: str2 = "FullStack" Oczekiwany wynik: lSt

str1 = "Datatypes"
middle = int(len(str1) / 2)
print(middle)

4
str1[middle-1:middle+2]
str1[middle-1:middle+2]
'aty'
str2 = "FullStack"
middle = int(len(str2) / 2)
print(middle)
str2[middle-1:middle+2]
4
'lSt'
# Zadanie2
# Biorąc pod uwagę 2 ciągi, s1 i s2, utwórz nowy ciąg, dodając s2 w środku s1 Dane: s1 = "FullStack" s2 = "Python" Oczekiwany wynik: FullPythonStack

middle = int(len(str1) / 2)
s1 = "FullStack"
s2 = "Python"
middle = int(len(str1) / 2)
print(s1[:middle] + s2 + s1[middle:])
# FullPythonStack
# Zadanie 3
# Biorąc pod uwagę 2 ciągi, s1 i s2 zwróć nowy ciąg złożony z pierwszego, środkowego i ostatniego znaku każdego ciągu wejściowego Dane: s1 = "America" s2 = "Japan" Oczekiwany wynik: AJrpan

s1 = "America"
s2 = "Japan"

middle_s1 = int(len(s1) / 2)
middle_s2 = int(len(s2) / 2)
first = s1[0] + s2[0]
middle = s1[middle_s1] + s2[middle_s2]
end = s1[-1] + s2[-1]

print(first + middle + end)
#
# Zadanie 4
# Pytanie do ćwiczenia Odwróć podany ciąg Dane: str1 = "Python" Oczekiwany wynik: nohtyP

print(str1[::-1])
str1 = "Python"

print(str1[::-1])
'nohtyP'
tuple1 = (10, 20, 30, 40, 50)
print(tuple1[::-1])
(50, 40, 30, 20, 10)
# Zadanie 4
# Ćwiczenie — dostęp do wartości 20 z krotki Dana krotka jest krotką zagnieżdżoną. Napisz program w Pythonie, który wypisze wartość 20. Dane: tuple1 = ("Pomarańczowy", [10, 20, 30], (5, 15, 25))

1
tuple1 = ("Pomarańczowy", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])
20
# Zadanie 5
# Poniżej znajdują się dwie listy. Napisz program w Pythonie konwertujący je na słownik w taki sposób, że pozycja z listy 1 jest kluczem, a pozycja z listy 2 jest wartością keys = ['Dziesieć', 'Dwadzieścia', 'Trzydzieści'] values = [10, 20, 30] 2:16 Oczekiwany wynik: {'Dziesieć': 10, 'Dwadzieścia': 20, 'Trzydzieści': 30}
#
# dict_final
keys = ['Dziesieć', 'Dwadzieścia', 'Trzydzieści']
values = [10, 20, 30]

result = zip(keys, values)

dict_final = dict(result)
print(dict_final)
{'Dziesieć': 10, 'Dwadzieścia': 20, 'Trzydzieści': 30}

# Zadanie 6
# Ćwiczenie — dodaj listę elementów do zbioru Mając listę Pythona, napisz program, który doda wszystkie jej elementy do danego zbioru.
#
# sample_set
sample_set = {"Żółty", "Pomarańczowy", "Czarny"}
sample_list = ["Niebieski", "Zielony", "Czerwony"]

sample_set.update(sample_list)
print(sample_set)
{'Żółty', 'Czarny', 'Niebieski', 'Pomarańczowy', 'Zielony', 'Czerwony'}
