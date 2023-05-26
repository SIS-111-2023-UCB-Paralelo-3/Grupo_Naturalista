import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import font
from tkinter import messagebox
import random

palabras = ['Cedro', 'Lapacho', 'Quina', 'Jacarandá', 'Algarrobo', 'JUCUWILD']

filas = 20
columnas = 20

letras = [[''] * columnas for _ in range(filas)]
botones = [[None] * columnas for _ in range(filas)]
seleccionados = []

def generar_sopa_de_letras():
    for i in range(filas):
        for j in range(columnas):
            letras[i][j] = random.choice('abcdefghijklmnopqrstuvwxyz')

def mostrar_sopa_de_letras():
    for i in range(filas):
        for j in range(columnas):
            boton = tk.Button(ventana, text=letras[i][j], width=2, relief='solid', state=tk.NORMAL, font=('Arial', 12, 'bold'), bg='#BDFCC9', fg='black')
            boton.grid(row=i, column=j, padx=1, pady=1)
            boton.bind('<Button-1>', lambda event, fila=i, columna=j: seleccionar_letra(fila, columna))
            botones[i][j] = boton

def seleccionar_letra(fila, columna):
    if botones[fila][columna]['state'] == tk.NORMAL:
        if len(seleccionados) > 0:
            ultima_fila, ultima_columna = seleccionados[-1]
            if abs(fila - ultima_fila) > 1 or abs(columna - ultima_columna) > 1:
                limpiar_seleccion()
        seleccionados.append((fila, columna))
        botones[fila][columna].config(bg='yellow')
    else:
        seleccionados.remove((fila, columna))
        botones[fila][columna].config(bg='#BDFCC9')

def verificar_palabras():
    encontradas = []
    for palabra in palabras:
        for direccion in [(0, 1), (1, 0), (1, 1), (1, -1)]:
            dx, dy = direccion
            if buscar_palabra(palabra, dx, dy):
                encontradas.append(palabra)
                break
    resaltar_palabras(encontradas)

def buscar_palabra(palabra, dx, dy):
    for i, j in seleccionados:
        fila, columna = i, j
        for letra in palabra:
            if not (0 <= fila < filas and 0 <= columna < columnas and letras[fila][columna] == letra):
                return False
            fila += dx
            columna += dy
        return True
    return False

def resaltar_palabras(palabras_encontradas):
    for i, j in seleccionados:
        botones[i][j].config(bg='#BDFCC9')
    for palabra in palabras_encontradas:
        for i, j in seleccionados:
            botones[i][j].config(bg='green')
        seleccionados.clear()

def limpiar_seleccion():
    for i, j in seleccionados:
        botones[i][j].config(bg='#BDFCC9')
    seleccionados.clear()

def mostrar_palabras():
    palabras_label.config(text="Palabras a encontrar:\n" + ", ".join(palabras), font=('Arial', 14, 'bold'), fg='black')

def reiniciar_sopa_de_letras():
    generar_sopa_de_letras()
    for i in range(filas):
        for j in range(columnas):
            botones[i][j].config(text=letras[i][j], state=tk.NORMAL, bg='#BDFCC9')
    limpiar_seleccion()

ventana = tk.Tk()
ventana.title('Sopa de Letras')
ventana.config(bg='#BDFCC9')

generar_sopa_de_letras()

mostrar_sopa_de_letras()

palabras_label = tk.Label(ventana, justify=tk.LEFT, anchor='w', bg='#BDFCC9')
palabras_label.grid(row=filas+1, columnspan=columnas)
mostrar_palabras()

verificar_boton = tk.Button(ventana, text='Verificar', command=verificar_palabras, font=('Arial', 14, 'bold'), bg='#BDFCC9', fg='black', relief='solid')
verificar_boton.grid(row=filas+2, columnspan=columnas)

reiniciar_boton = tk.Button(ventana, text='Jugar de Nuevo', command=reiniciar_sopa_de_letras, font=('Arial', 14, 'bold'), bg='#BDFCC9', fg='black', relief='solid')
reiniciar_boton.grid(row=filas+3, columnspan=columnas)

for i in range(filas):
    ventana.grid_rowconfigure(i, weight=1)
for j in range(columnas):
    ventana.grid_columnconfigure(j, weight=1)


ventana.mainloop()


class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.root = tk.Tk()
        self.root.title("Tres en Raya - Selva")
        self.root.configure(bg='#003300')  
        
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.root, text="", width=10, height=5,
                                   command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col, padx=5, pady=5)
                button.configure(bg='#00FF00', fg='#FFFFFF')  
                button_row.append(button)
            self.buttons.append(button_row)
        
        self.restart_button = tk.Button(self.root, text="Volver a Jugar", command=self.restart_game)
        self.restart_button.grid(row=3, columnspan=3, pady=10)
        self.restart_button.configure(bg='#00FF00', fg='#FFFFFF')  
    
    def make_move(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(row, col):
                messagebox.showinfo("¡Fin del juego!", f"Ganador: {self.current_player}")
                self.end_game()
            elif self.check_draw():
                messagebox.showinfo("¡Fin del juego!", "¡Empate!")
                self.end_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self, row, col):
        player = self.current_player
        if self.board[row][0] == self.board[row][1] == self.board[row][2] == player:
            return True
        
        if self.board[0][col] == self.board[1][col] == self.board[2][col] == player:
            return True
        
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] == player) or \
           (self.board[0][2] == self.board[1][1] == self.board[2][0] == player):
            return True
        return False
    
    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == '':
                    return False
        return True
    
    def restart_game(self):
        self.current_player = "X"
        self.board = [['' for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for button in row:
                button.config(text="")
                button.config(state=tk.NORMAL)
        self.root.destroy()  
    
    def end_game(self):
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)
        self.restart_button.config(state=tk.NORMAL)
    
    def start(self):
        self.root.mainloop()

def open_game_window():
    game = TicTacToe()
    game.start()

def show_options():
    game_window = tk.Toplevel(root)
    game_window.title("Opciones")
    game_window.configure(bg='#FFFFFF')


def show_game_screen():
    game_window = tk.Toplevel(ventana)
    game_window.geometry("1350x1000")

    color_frame = tk.Frame(game_window, width=20, height=200, bg="olive drab")
    color_frame.pack()

    text_label = tk.Label(color_frame, text="Veremos estos dos juegos que nos ayudaran a divertirnos mientras aprendemos,\ndonde encontraremos palabras que sean importantes lugares de Tarija\n", font=("MV boli", 15), fg="white", bg="green")
    text_label.pack(padx=300, pady=10)
    
    color_frame = tk.Frame(game_window, width=20, height=200, bg="olive drab")
    color_frame.pack()

    text_label = tk.Label(color_frame, text="ESTOS SERAN NUESTROS DOS JUEGOS\n _SOPA DE LETRAS: te divertiras buscando palabras de nuestra region chapaca tarijeña \n _TRES EN RAYA: desafia a tus amigos y juega este juego para divertirte", font=("MV boli", 15), fg="white", bg="green")
    text_label.pack(padx=280, pady=10)
    
    color_frame = tk.Frame(game_window, width=20, height=200, bg="olive drab")
    color_frame.pack()

    text_label = tk.Label(color_frame, text="A continuacion tendras dos opciones, escoge del cual mas sea tu gusto", font=("MV boli", 15), fg="white", bg="green")
    text_label.pack(padx=335, pady=10)



    image_frame = tk.Frame(game_window, width=400, height=600, bg="white")
    image_frame.pack()

    image_path = "Logo.png"
    image = tk.PhotoImage(file=image_path)
    resized_image = image.subsample(1,3)  

    image_label = tk.Label(image_frame, image=resized_image, bg="white")
    image_label.image = resized_image
    image_label.pack(pady=20)

    scenic_route_button = tk.Button(game_window, text="TRES EN RAYA", font=("MV boli", 20), bg="olive drab", command=open_game_window)
    scenic_route_button.pack(side=tk.LEFT, padx=50, pady=20)
    
    sopa_letras_button = tk.Button(game_window, text="SOPA DE LETRAS", font=("MV boli", 20), bg="olive drab", command=show_options)
    sopa_letras_button.pack(side=tk.LEFT, padx=50, pady=20)

def show_options():
    options_window = tk.Toplevel(ventana)
    options_window.geometry("800x600")
    options_window.title("Opciones")

    def show_image(image_path):
        image_window = tk.Toplevel(options_window)
        image_window.geometry("1150x600")
        image_window.title("Imagen")
        
        image = Image.open(image_path)
        image = image.resize((1150, 600), Image.ANTIALIAS)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 100)  
        
        if image_path == "Tariquia.jpeg":
            draw.text((50, 50), "TARIQUIA", fill=(255, 255, 255), font=font)
        elif image_path == "SAMA.jpeg":
            draw.text((40, 40), "CORDILLERA DE \n SAMA", fill=(255, 255, 255), font=font)  
        elif image_path == "Corbalan.jpeg":
            draw.text((30, 30), "RESERVA EL \nCORBALAN", fill=(255, 255, 255), font=font)  
        elif image_path == "Aguarague.jpg":
            draw.text((30, 30), "P.N. SERRANÍA,\n DEL AGUARAGÜE", fill=(255, 255, 255), font=font)  
        elif image_path == "Alarachi.jpeg":
            draw.text((30, 30), "RESERVA NATURAL\n ALARACHI", fill=(255, 255, 255), font=font)  
        elif image_path == "Nicolas.jpg":
            draw.text((30, 30), "ÁREA PROTEGIDA \nSAN NICOLÁS", fill=(255, 255, 255), font=font)  
        
        photo = ImageTk.PhotoImage(image)

        image_label = tk.Label(image_window, image=photo)
        image_label.pack()

        image_window.mainloop()

    option_button1 = tk.Button(options_window, text="Reserva Natural de Tariquía", font=("MV boli", 20), bg="GREEN", command=lambda: show_image("Tariquia.jpeg"))
    option_button1.pack(pady=20)

    option_button2 = tk.Button(options_window, text="Cordillera de Sama", font=("MV boli", 20), bg="GREEN", command=lambda: show_image("SAMA.jpeg"))
    option_button2.pack(pady=20)

    option_button3 = tk.Button(options_window, text="Reserva Natural El Corbalan", font=("MV boli", 20), bg="GREEN", command=lambda: show_image("Corbalan.jpeg"))
    option_button3.pack(pady=20)

    option_button4 = tk.Button(options_window, text="Parque Nacional Serranía del Aguaragüe", font=("MV boli", 20), bg="GREEN", command=lambda: show_image("Aguarague.jpg"))
    option_button4.pack(pady=20)

    option_button5 = tk.Button(options_window, text="Reserva Natural Alarachi", font=("MV boli", 20), bg="GREEN", command=lambda: show_image("Alarachi.jpeg"))
    option_button5.pack(pady=20)

    option_button6 = tk.Button(options_window, text="Área Protegida Municipal San Nicolás", font=("MV boli", 20), bg="GREEN", command=lambda: show_image("Nicolas.jpg"))
    option_button6.pack(pady=20)

def siguiente():
    ventana2 = tk.Toplevel(ventana)
    ventana2.title("JUCUWILD")
    ventana2.geometry("1350x1000")
    ventana2.configure(bg="darkgreen")

    color_frame = tk.Frame(ventana2, width=200, height=200, bg="darkgreen")
    color_frame.pack()

    text_label = tk.Label(color_frame, text="BIENVENIDO A JUCUWILD", font=("ALGERIAN", 80), fg="white", bg="green")
    text_label.pack(padx=75, pady=70)

    color_frame = tk.Frame(ventana2, width=20, height=200, bg="darkgreen")
    color_frame.pack()

    text_label = tk.Label(color_frame, text="En esta área de la aplicación veremos distintos tipos de reservas y floras\nque harán un hermoso recorrido de lo que es Tarija y aprenderemos jugando unos minijuegos", font=("MV boli", 15), fg="white", bg="black")
    text_label.pack(padx=20, pady=10)
    
    color_frame = tk.Frame(ventana2, width=20, height=200, bg="white")
    color_frame.pack()


    text_label = tk.Label(color_frame, text="A continuación tendrás dos opciones:\nUna te llevará a conocer el departamento de Tarija en su bella naturaleza.\nLa otra te llevará a poder jugar unos minijuegos con personajes de animales de Tarija que te guiarán por tu camino del juego y te apoyarán.", font=("MV boli", 15), fg="white", bg="black")
    text_label.pack(padx=1, pady=20)
    
    text_label = tk.Label(color_frame, text="GRACIAS POR VER NUESTRA APLICACION, ESPERAMOS QUE LA HAYA DISFRUTADO.", font=("MV boli", 15), fg="white", bg="black")
    text_label.pack(padx=1, pady=1)


    color_frame = tk.Frame(ventana2, width=20, height=100, bg="darkgreen")
    color_frame.pack()

    scenic_route_button = tk.Button(ventana2, text="          CONOCER          ", font=("MV boli", 20), bg="olive drab", command=show_options)
    scenic_route_button.pack(side=tk.LEFT, padx=10, pady=1)

    hiking_trail_button = tk.Button(ventana2, text="           JUGAR           ", font=("MV boli", 20), bg="olive drab", command=show_game_screen)
    hiking_trail_button.pack(side=tk.RIGHT, padx=10, pady=1)

ventana = tk.Tk()
ventana.title("MI APLICACION PARA CONOCER ¨JUCUWILD¨")
ventana.geometry("1350x1000")
ventana.configure(bg="darkgreen")

fuente = font.Font(family="MV Boli")

etiqueta_texto = tk.Label(ventana, text="¡Pulse el botón siguiente para conocer más de nosotros!", font=fuente, bg="green", fg="white")
etiqueta_texto.pack()

imagen = Image.open("Logo.png")
imagen = imagen.resize((1900,600))
imagen = ImageTk.PhotoImage(imagen)

etiqueta_imagen = tk.Label(ventana, image=imagen)
etiqueta_imagen.pack()

boton_siguiente = tk.Button(ventana, text="Siguiente", font=fuente, command=siguiente)
boton_siguiente.pack()

ventana.mainloop()

