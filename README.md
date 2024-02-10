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

**<<SET 4>>**

ZADANIE 4.2
Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, które zwracają pełny string przez return. Funkcje nie powinny pytać użytkownika o dane, tylko korzystać z argumentów.

ZADANIE 4.3
Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.

ZADANIE 4.4
Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.

ZADANIE 4.5
Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie. Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.

ZADANIE 4.6
Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która może zawierać zagnieżdżone podsekwencje.

ZADANIE 4.7
Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości. Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji. Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

**<<SET 5>>**

Stworzyć plik fracs.py i zapisać w nim funkcje do działań na ułamkach. Ułamek będzie reprezentowany przez listę dwóch liczb całkowitych [licznik, mianownik]. Napisać kod testujący moduł fracs.

**<< SET 6>>**

W pliku fracsv2.py zdefiniować klasę Frac wraz z potrzebnymi metodami. Ułamek jest reprezentowany przez parę liczb całkowitych. Napisać kod testujący moduł fracs.

**<< SET 7>>**

W pliku rectangles.py zdefiniować klasę Rectangle wraz z potrzebnymi metodami. Wykorzystać wyjątek ValueError do obsługi błędów. Napisać kod testujący moduł rectangles.

Stworzyć następujące iteratory nieskończone:
(a) zwracający 0, 1, 0, 1, 0, 1, ...,
(b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W")
(c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... .

**<< SET 8>>**

Wzbogacić klasę Rectangle o nowe funkcjonalności.
Stworzyć metodę klasy o nazwie 'from_points', która pozwoli utworzyć prostokąt z listy lub krotki zawierającej dwa punkty, lewy dolny i prawy górny.
Za pomocą dekoratora @property dodać atrybuty wirtualne zwracające liczbę (współrzędną): top, left, bottom, right, width, height. Dodać atrybuty wirtualne zwracające Point: topleft, bottomleft, topright, bottomright. Można rozważyć zamianę metody center() na atrybut wirtualny.
W osobnym pliku przygotować testy klasy Rectangle w formacie dla modułu 'pytest'.

**<< SET 9>>**

Zaimplementować prostą grę o topieniu padającego śniegu. Przy górnej krawędzi ekranu pojawiają się losowo płatki śniegu, które spadają w dół ruchem jednostajnym. Zadaniem gracza jest topienie płatków śniegu przez klikanie na nie myszą. Celem gry jest niedopuszczenie, aby jakiś płatek śniegu dotarł do dolnej krawędzi ekranu.
Można rozważyć wariant gry, w którym tworzą się zaspy śniegu, a gra kończy się, gdy zaspa urośnie do górnej krawędzi ekranu.

**<< SET 10>>**

Napisać program z GUI, który symuluje rzut kostką sześcienną. Program powinien mieć przycisk uruchamiający rzut kostką i etykietę wyświetlającą wynik.

**<< SET 11>>**

Do klasy DoubleList dopisać nowe metody.

**<<SET 12>>**

Poprawić implementację tablicową stosu tak, aby korzystała z wyjątków w przypadku pojawienia się błędu. Metoda pop() ma zgłaszać błąd w przypadku pustego stosu. Metoda push() ma zgłaszać błąd w przypadku przepełnienia stosu. Napisać kod testujący stos.

Stworzyć ADT w postaci kolejki losowej, z której elementy będą pobierane w losowej kolejności. Zadbać o to, aby każda operacja była wykonywana w stałym czasie, niezależnie od liczby elementów w kolejce.

**<<Final Project>>**

Znalezienie i zwizualizowanie cykli Hamiltona na grafie.