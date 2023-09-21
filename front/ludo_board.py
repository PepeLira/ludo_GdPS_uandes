import tkinter as tk
from .ui.player_panel import PlayerPanel
import random
from collections import Counter
from backend.game_flow import GameFlow


class LudoBoard:
    def __init__(self, root, n_of_players=4):
        self.root = root
        self.root.title("Ludo Board")
        self.n_of_players = n_of_players
        self.current_player = None
        self.states = ["n_of_players", "player_order", "roll_dice", "move_token", "end"]
        self.current_state = self.states[0]

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        self.ref_width = int(screen_width // 1.8)
        self.player_panel_width = self.ref_width//4
        self.cell_width = self.ref_width//8//6
        self.finish_cell_width = self.ref_width//8

        self.root.resizable(False, False)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.glory_paths = []
        self.common_path = []
        self.start_cells = []
        self.player_panels = []

        # Create squares in the first three columns
        self.draw_board()

        # Create information text and button in the fourth column
        self.create_info_column()

        # for i in range(len(self.common_path)):
        #     label = tk.Label(self.common_path[i], text=str(i), bg="lightblue", font=("Helvetica", 20))
        #     label.place(relx=0.5, rely=0.5, anchor="center")
        # for glory_path in self.glory_paths:
        #     for i in range(len(glory_path)):
        #         label = tk.Label(glory_path[i], text=str(i), bg="lightblue", font=("Helvetica", 20))
        #         label.place(relx=0.5, rely=0.5, anchor="center")

    def clear_board(self, player_panel):
        for prev_cell in player_panel.common_tokens:
            for widget in prev_cell.winfo_children():
                widget.destroy()
        player_panel.common_tokens = []

    def clear_glory_paths(self, player_panel):
        for prev_cell in player_panel.glory_path:
            for widget in prev_cell.winfo_children():
                widget.destroy()
    
    def draw_common_path_tokens(self, token_sells, player_panel):
        number_counts = Counter(token_sells)
        counts = [(number, count) for number, count in number_counts.items()]

        for i, count in counts:
            i = i-1 
            if i > 0:
                sell = self.common_path[i]
                player_panel.draw_player_token(sell, count)

    def draw_glory_path_tokens(self, token_sells, player_panel):
        number_counts = Counter(token_sells)
        counts = [(number, count) for number, count in number_counts.items()]

        for i, count in counts:
            i = i-1 
            if i > 0:
                sell = player_panel.glory_path[i]
                player_panel.draw_player_token(sell, count)

    def draw_player_panels(self):
        colors = ["red", "lightgreen", "lightblue", "orange"]
        for i in range(self.n_of_players):
            self.player_panels.append(PlayerPanel(self.root, 
                                                colors[i],
                                                self.glory_paths[i],
                                                self.start_cells[i],
                                                self.player_bases[i],
                                                self.common_path,
                                                self.player_panel_width,
                                                self.cell_width))
        self.sim_game_flow = GameFlow(self.n_of_players)

        # self.player_panels[1].draw_player_token(self.player_panels[1].glory_path[2], 2)
        # self.player_panels[1].draw_base_tokens(2)
        # self.draw_winner_tokens(self.player_panels, [1,2,1,3])

    def draw_board(self):
        self.player_bases = []
        self.player_paths = []
        player_paths = []
        for row in range(3):
            for col in range(3):
                if [row, col] in [[0, 0], [2, 0], [0, 2], [2, 2]]: #Corners 
                    panel = tk.Frame(self.root, bg="white", width=self.ref_width//4, height=self.ref_width//4)
                    self.player_bases.append(panel)
                    self.define_cells(col, row, panel)
                elif [row, col] in [[0, 1], [2, 1]]:
                    frame_width = self.ref_width//8
                    frame_height = self.ref_width//4 
                    path = tk.Frame(self.root, bg="white", width=frame_width, height=frame_height)
                    player_paths.append(path)
                    self.define_cells(col, row, path)
                    if [row, col] == [0, 1]:
                        orientation = 'vp'
                    else:
                        orientation = 'vn'
                    common_path_cells, glory_path_cells, start_cell = self.add_board_path(path, orientation, frame_width, frame_height)
                    self.start_cells.append(start_cell + len(self.common_path))
                    self.common_path += common_path_cells
                    self.glory_paths.append(glory_path_cells)

                elif ([row, col] in [[1, 0], [1, 2]]):
                    frame_width = self.ref_width//4
                    frame_height = self.ref_width//8
                    path = tk.Frame(self.root, bg="white", width=frame_width, height=frame_height)
                    player_paths.append(path)
                    self.define_cells(col, row, path)
                    if [row, col] == [1, 0]:
                        orientation = 'hp'
                    else:
                        orientation = 'hn'
                    common_path_cells, glory_path_cells, start_cell = self.add_board_path(path, orientation, frame_width, frame_height)
                    self.start_cells.append(start_cell + len(self.common_path))
                    self.common_path += common_path_cells
                    self.glory_paths.append(glory_path_cells)
                else:
                    frame = tk.Frame(self.root, bg="white", width=self.ref_width//8, height=self.ref_width//8)
                    self.finish_cell = frame
                    self.define_cells(col, row, frame)
        
        self.glory_paths = [self.glory_paths[1], self.glory_paths[0], self.glory_paths[3], self.glory_paths[2]]
        self.start_cells = [8, 21, 47, 34]
        self.common_path = self.common_path[13:26] + self.common_path[0:13] + self.common_path[26:39] + self.common_path[39:52]


    def add_board_path(self, frame, orientation, width, height):
        cells = []
        glory_path = [6, 7, 8, 9, 10, 11]
        common_path = [17, 16, 15, 14, 13, 12, 6, 0, 1, 2, 3, 4, 5]
        glory_path_cells = []
        common_path_cells = []
        if "h" in orientation:
            rows = 3
            cols = 6
            size = width/6
            h_index = range(rows)
            if orientation == 'hp':
                h_index = range(rows)
                v_index = range(cols)
            else:
                h_index = range(rows-1, -1, -1)
                v_index = range(cols-1, -1, -1)
            
            for row in h_index:
                for col in v_index:
                    cell = tk.Frame(frame, bg="#f0f0f0", width=size, height=size)
                    cells.append(cell)
                    cell.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
        elif "v" in orientation:
            rows = 6
            cols = 3
            size = height/6
            if orientation == 'vp':
                v_index = range(rows)
                h_index = range(cols-1, -1, -1)
            else:
                v_index = range(rows-1, -1, -1)
                h_index = range(cols)
            
            for col in h_index:
                for row in v_index:
                    cell = tk.Frame(frame, bg="#f0f0f0", width=size, height=size)
                    cells.append(cell)
                    cell.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
        for i in glory_path:
            glory_path_cells.append(cells[i])
        for i in common_path:
            common_path_cells.append(cells[i])
        
        start_cell = 8

        return common_path_cells, glory_path_cells, start_cell

    def define_cells(self, col, row, frame, weight=1):
        frame.grid(row=row, column=col, sticky="nsew")
        # Make the cells expand when the window is resized
        self.root.grid_columnconfigure(col, weight=weight)
        self.root.grid_rowconfigure(row, weight=weight)

    def draw_winner_tokens(self, n_of_tokens):
        players = self.player_panels
        # Destroy all child widgets inside the frame
        for widget in self.finish_cell.winfo_children():
            widget.destroy()
        
        frame_width = self.finish_cell_width

        if len(players) == 3:
            token_cords = [[1, 1, n_of_tokens[0]], [1, 2, n_of_tokens[1]], [2, 1, n_of_tokens[2]]]
        elif len(players) == 2:
            token_cords = [[1, 1, n_of_tokens[0]], [1, 2, n_of_tokens[1]]]
        elif len(players) == 1:
            token_cords = [[1, 1, n_of_tokens[0]]]
        else:
            token_cords = [[1, 1, n_of_tokens[0]], [1, 2, n_of_tokens[1]], [2, 1, n_of_tokens[2]], [2, 2, n_of_tokens[3]]]

        # Create a canvas inside the frame
        canvas = tk.Canvas(self.finish_cell, bg="white", width=frame_width, height=frame_width)
        canvas.pack(expand=True, fill="both")

        # Calculate the coordinates and size for four circles
        circle_radius = frame_width // 8
        distance_between_circles = frame_width // 4

        # Draw four circles aligned to the center of the frame
        for i in range(len(token_cords)):
            row = token_cords[i][0]
            col = token_cords[i][1]
            n_of_tokens = token_cords[i][2]

            delta = frame_width/8
            x1 = col * distance_between_circles + circle_radius - delta
            y1 = row * distance_between_circles + circle_radius - delta
            x2 = x1 + 2 * circle_radius
            y2 = y1 + 2 * circle_radius
            canvas.create_oval(x1, y1, x2, y2, fill=players[i].color, outline="white", width=3)

            text = str(n_of_tokens)
            canvas.create_text(col * distance_between_circles + delta, 
                                row * distance_between_circles + delta, 
                                text=text, 
                                font=("Helvetica", 12, "bold"))

    def create_info_column(self):
        self.info_label = tk.Label(self.root, text="Ingrese el número de jugadores:")
        self.info_label.grid(row=0, column=3, padx=5, pady=5, sticky="nsew")

        self.info_text = tk.Text(self.root, height=5, width=20)
        self.info_text.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

        self.action_button = tk.Button(self.root, text="Enviar", command=self.handle_button_click)
        self.action_button.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

    def handle_button_click(self):
        if self.current_state == self.states[0]: # Numero de jugadores
            # Get the player number from the text area
            player_number = self.info_text.get("1.0", "end-1c")  # Retrieve the text excluding the trailing newline character

            # Check if the input is a valid player number
            if 1 <= int(player_number) <= 4:
                self.n_of_players = int(player_number)
                self.display_message(f"Juego de {player_number} jugadores")
            else:
                self.display_message("Invalid input. Please enter a valid player number.")
            self.draw_player_panels()
            self.current_state = self.states[1]
        elif self.current_state == self.states[1]: # Quien empieza
            self.display_message("Quien empieza?")
            winner, message = self.get_highest_player(list(range(len(self.player_panels))))
            # Calculate the new order of players
            new_order = [(winner + i) % len(self.player_panels) for i in range(len(self.player_panels))]

            # Rearrange the 'self.player_panels' list based on the new order
            # self.player_panels = [self.player_panels[i] for i in new_order]
            self.display_message(message)

            self.current_state = self.states[2]
    
        elif self.current_state == self.states[2]: # Tirar dado
            self.board_state = self.sim_game_flow.game_board_states.pop(0)
            self.display_message(f"El jugador {self.board_state['current_player']} sacó {self.board_state['dice']}")
            self.current_state = self.states[3]
        elif self.current_state == self.states[3]: # Mover ficha
            for i in range(len(self.player_panels)):
                player_panel = self.player_panels[i]
                self.clear_glory_paths(player_panel)
                self.clear_board(player_panel)
                player_panel.draw_base_tokens(self.board_state["base_tokens"][i])
                self.draw_common_path_tokens(self.board_state["common_path"][i], player_panel)
                self.draw_glory_path_tokens(self.board_state["glory_paths"][i], player_panel)
            self.draw_winner_tokens(self.board_state["winner_tokens"])
            if self.board_state["winner"]:
                self.current_state = self.states[4]
            else:
                self.current_state = self.states[2]
        
        elif self.current_state == self.states[4]: # Fin del juego
            self.display_message(f"El juego ha terminado \n El ganador es el jugador {self.board_state['current_player']}")

    def get_highest_player(self, player_panels):
        while True:
            message = ''
            player_numbers = []
            for player in player_panels:
                number = random.randint(1, 6)
                player_numbers.append((player, number))

            # Sort the player numbers in descending order by their rolled numbers
            player_numbers.sort(key=lambda x: x[1], reverse=True)

            # Check for ties by comparing the highest number with the second highest
            if len(player_numbers) > 1 and player_numbers[0][1] == player_numbers[1][1]:
                # It's a tie; remove the tied players and roll the dice again
                tied_players = [player_numbers[0][0], player_numbers[1][0]]
                player_panels = [player for player in player_panels if player not in tied_players]
                continue
            else:
                # Return the player with the highest number
                for x in player_numbers:
                    message += f"Jugador {x[0]+1} sacó {x[1]}\n"
                message += f"Jugador {player_numbers[0][0]+1} empieza"
                return player_numbers[0][0], message

    def display_message(self, message):
        # Display a message in the information text area
        self.info_label.config(text=message)

if __name__ == "__main__":
    root = tk.Tk()
    my_gui = LudoBoard(root)
    root.mainloop()
