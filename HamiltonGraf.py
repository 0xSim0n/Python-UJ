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

    # Tworzenie dużego okręgu
    # canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline="black")

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
    # If the vertex is adjacent to
    # the vertex of the previously
    # added vertex
    if graph[path[pos - 1]][v] == 0:
        return False

    # If the vertex has already
    # been included in the path
    for i in range(pos):
        if path[i] == v:
            return False

    # Both the above conditions are
    # not true, return true
    return True


# To check if there exists
# at least 1 hamiltonian cycle
hasCycle = False


# Function to find all possible
# hamiltonian cycles
def hamCycle(graph):
    global hasCycle

    # Initially value of boolean
    # flag is false
    hasCycle = False

    # Store the resultant path
    path = []
    path.append(0)

    # Keeps the track of the
    # visited vertices
    visited = [False] * (len(graph))

    for i in range(len(visited)):
        visited[i] = False

    visited[0] = True

    # Function call to find all
    # hamiltonian cycles
    FindHamCycle(graph, 1, path, visited)

    if hasCycle:
        print("No Hamiltonian Cycle possible ")
        return


# Recursive function to find all
# hamiltonian cycles
def FindHamCycle(graph, pos, path, visited):
    # If all vertices are included
    # in Hamiltonian Cycle
    cycle = []
    if pos == len(graph):

        # If there is an edge
        # from the last vertex to
        # the source vertex
        if graph[path[-1]][path[0]] != 0:

            # Include source vertex
            # into the path and
            # print the path
            path.append(0)
            for i in range(len(path)):
                cycle.append(path[i])
            cycles.append(cycle)
            # Remove the source
            # vertex added
            path.pop()

            # Update the hasCycle
            # as true
            hasCycle = True
        return

    # Try different vertices
    # as the next vertex
    for v in range(len(graph)):

        # Check if this vertex can
        # be added to Cycle
        if isSafe(v, graph, path, pos) and not visited[v]:
            path.append(v)
            visited[v] = True

            # Recur to construct
            # rest of the path
            FindHamCycle(graph, pos + 1, path, visited)

            # Remove current vertex
            # from path and process
            # other vertices
            visited[v] = False
            path.pop()

def draw_Hamilton(x):  # x numer cyklu hamiltona
    for i in range(len(cycles[x]) - 1):
        if len(cycles) != 0:
            start_x, start_y = circle_centers[cycles[x][i]]
            end_x, end_y = circle_centers[cycles[x][i+1]]
            canvas.create_line(start_x, start_y, end_x, end_y, fill="red", width=4)


adj = [
    [ 0, 1, 1, 0, 0, 1 ],
    [ 1, 0, 1, 0, 1, 1 ],
    [ 1, 1, 0, 1, 0, 0 ],
    [ 0, 0, 1, 0, 1, 0 ],
    [ 0, 1, 0, 1, 0, 1 ],
    [ 1, 1, 0, 0, 1, 0 ],
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

hamCycle(adj)


def on_button_click():
    click_count_var.set((click_count_var.get() + 1) % len(cycles))
    draw_Hamilton((click_count_var.get() + 1) % len(cycles))

click_count_var = tk.IntVar()
click_count_var.set(0)

button = tk.Button(root, text="Hamilton Cycle ", command=on_button_click)
button.pack()

label = tk.Label(root, textvariable=click_count_var)
label.pack()


root.mainloop()
