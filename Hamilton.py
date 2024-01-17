import tkinter as tk
import math


def create_circles_on_circle(x, y, z):

    # Rozmiary okna
    window_width = canvas.winfo_reqwidth()
    window_height = canvas.winfo_reqheight()

    # Współrzędne środka dużego okręgu
    center_x = window_width // 2
    center_y = window_height // 2

    # Promień dużego okręgu
    radius = x

    # Liczba mniejszych kół
    num_circles = y

    # Tworzenie mniejszych kół na dużym okręgu
    for i in range(num_circles):
        angle = i * (360 / num_circles)  # Kąt w stopniach
        angle_rad = math.radians(angle)  # Konwersja kąta na radiany

        # Obliczanie współrzędnych środka mniejszego koła w oparciu o współrzędne biegunowe
        circle_center_x = center_x + radius * math.cos(angle_rad)
        circle_center_y = center_y + radius * math.sin(angle_rad)

        # Promień mniejszego koła
        circle_radius = 25

        # Tworzenie mniejszego koła i dodanie mu odpowiedniego numeru
        canvas.create_oval(circle_center_x - circle_radius, circle_center_y - circle_radius,
                            circle_center_x + circle_radius, circle_center_y + circle_radius, fill="blue")

        canvas.create_text(circle_center_x, circle_center_y, text=str(i), fill="white", font=("Arial", 24, "bold"))

        circle_centers.append((circle_center_x, circle_center_y))

    # Tworzenie połączeń
    for i in range(len(z)):
        for j in range(len(z[i])):
            if z[i][j] == 1:
                start_x, start_y = circle_centers[i]
                end_x, end_y = circle_centers[j]
                canvas.create_line(start_x, start_y, end_x, end_y, fill="black", width=1)


def isSafe(v, graph, path, pos):
    if graph[path[pos - 1]][v] == 0:
        return False

    for i in range(pos):
        if path[i] == v:
            return False

    return True


def hamCycle(graph):

    path = []
    path.append(0)

    visited = [False] * (len(graph))

    for i in range(len(visited)):
        visited[i] = False

    visited[0] = True

    FindHamCycle(graph, 1, path, visited)

def FindHamCycle(graph, pos, path, visited):
    cycle = []
    if pos == len(graph):
        if graph[path[-1]][path[0]] != 0:
            path.append(0)
            for i in range(len(path)):
                cycle.append(path[i])
            cycles.append(cycle)
            path.pop()
        return
    for v in range(len(graph)):
        if isSafe(v, graph, path, pos) and not visited[v]:
            path.append(v)
            visited[v] = True
            FindHamCycle(graph, pos + 1, path, visited)
            visited[v] = False
            path.pop()


# Rysowanie odnalezionego cyklu Hamiltona
def draw_Hamilton(x):    # x numer cyklu hamiltona
    for i in range(len(cycles[x]) - 1):
        if len(cycles) != 0:
            start_x, start_y = circle_centers[cycles[x][i]]
            end_x, end_y = circle_centers[cycles[x][i+1]]
            canvas.create_line(start_x, start_y, end_x, end_y, fill="red", width=4, tags = "lane")

# Usunięcie obecnie zaznaczonego cyklu
def delet_previous():
    canvas.delete("lane")

# Funkcja do zmiany wyświetlanych cykli
def on_button_click():
    if len(cycles) != 0:
        click_count_var.set((click_count_var.get() + 1) % len(cycles))
        delet_previous()
        draw_Hamilton((click_count_var.get() + 1) % len(cycles))

def has_cycle():
    if len(cycles) == 0:
        print("Can't find Hamilton cycle")
    else:
        print(cycles)

# Input
adj = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0]
]

circle_centers =[]
cycles = []
number_of_circles = len(adj)

# Tworzenie głównego okna
root = tk.Tk()
root.title("Hamilton cycle")
root.geometry("500x500")
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Tworzenie okręgów
create_circles_on_circle(150, number_of_circles, adj)

# Odnalezenie cykli Hamiltona
hamCycle(adj)
has_cycle()

# Przełączanie pomiędzy cyklami
click_count_var = tk.IntVar()
click_count_var.set(0)

button = tk.Button(root, text=" Next ", command=on_button_click, width=6, height=2, font=("Arial", 16, "bold"), bg="yellow")
button.pack()

label = tk.Label(root, text = " Ilość cykli Hamiltona: " + str(len(cycles)), font=("Arial", 16, "bold"))
label.place(x=0, y=0)

root.mainloop()