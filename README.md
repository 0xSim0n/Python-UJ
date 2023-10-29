# Phyton-UJ

**<<SET 2>>**

ZADANIE 2.10
Mamy dany napis wielowierszowy line. Podać sposób obliczenia liczby wyrazów w napisie. Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline).

ZADANIE 2.11
Podać sposób wyświetlania napisu word tak, aby jego znaki były rozdzielone znakiem podkreślenia.

ZADANIE 2.12
Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line. Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.

ZADANIE 2.13
Znaleźć łączną długość wyrazów w napisie line.

ZADANIE 2.14
Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line.

ZADANIE 2.15
Na liście L znajdują się liczby całkowite dodatnie. Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.

ZADANIE 2.16
W tekście znajdującym się w zmiennej line zamienić ciąg znaków "GvR" na "Guido van Rossum".

ZADANIE 2.17
Posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości.

ZADANIE 2.18
Znaleźć liczbę cyfr zero w dużej liczbie całkowitej.

ZADANIE 2.19
Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. Chcemy zbudować napis z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024.

**<<SET 3>>**

ZADANIE 3.1
Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?
a) x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
b) for i in "axby": if ord(i) < 100: print (i)
c) for i in "axby": print (ord(i) if ord(i) < 100 else i)

ZADANIE 3.2
Co jest złego w kodzie:
a) L = [3, 5, 4] ; L = L.sort()
b) x, y = 1, 2, 3
c) X = 1, 2, 3 ; X[1] = 4
d) X = [1, 2, 3] ; X[3] = 4
e) X = "abc" ; X.append("d")
f) L = list(map(pow, range(8)))

ZADANIE 3.3
Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3.

ZADANIE 3.4
Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący x oraz trzecią potęgę x. Zatrzymanie programu następuje po wpisaniu z klawiatury stop. Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.

ZADANIE 3.5
Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo obsłużyć liczby składające się z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). Należy zbudować pełny string, a potem go wypisać.

ZADANIE 3.6
Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string, a potem go wypisać.

ZADANIE 3.8
Dla dwóch sekwencji liczb lub znaków znaleźć: (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń), (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).

ZADANIE 3.9
Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby. Znaleźć listę zawierającą sumy liczb z tych sekwencji. Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18].

ZADANIE 3.10
Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na liczby arabskie (podać kilka sposobów tworzenia takiego słownika).
