import tkinter as tk

class PlayerPanel:
    def __init__(self, root, color, glory_path, start_cell, player_base, common_path, ref_width, cell_size):
        self.root = root
        self.color = color
        self.glory_path = glory_path
        self.start_cell = start_cell
        self.end_cell = start_cell - 3
        self.player_base = player_base
        self.common_path = common_path
        self.ref_width = ref_width
        self.cell_size = cell_size
        self.common_tokens = []
        self.colorize_cells()
        self.draw_base_tokens()

    def set_order(self, order):
        self.order = order

    def colorize_cells(self):
        self.player_base.configure(bg=self.color)
        for i in range(len(self.glory_path)):
            if i > 0:
                self.glory_path[i].configure(bg=self.color)
        self.common_path[self.start_cell].configure(bg=self.color)
    
    def draw_base_tokens(self, n_of_tokens=4):
        # Destroy all child widgets inside the frame
        for widget in self.player_base.winfo_children():
            widget.destroy()
        
        frame_width = self.ref_width

        if n_of_tokens == 3:
            token_cords = [[1, 1], [1, 2], [2, 1]]
        elif n_of_tokens == 2:
            token_cords = [[1, 1], [1, 2]]
        elif n_of_tokens == 1:
            token_cords = [[1, 1]]
        else:
            token_cords = [[1, 1], [1, 2], [2, 1], [2, 2]]
        if n_of_tokens > 0:
            # Create a canvas inside the frame
            canvas = tk.Canvas(self.player_base, bg=self.color, width=frame_width, height=frame_width)
            canvas.pack(expand=True, fill="both")

            # Calculate the coordinates and size for four circles
            circle_radius = frame_width // 16
            distance_between_circles = frame_width // 4

            # Draw four circles aligned to the center of the frame
            for row in range(2):
                for col in range(2):
                    if [row + 1, col + 1] in token_cords:
                        delta = frame_width/4
                        x1 = col * distance_between_circles + circle_radius + delta
                        y1 = row * distance_between_circles + circle_radius + delta
                        x2 = x1 + 2 * circle_radius
                        y2 = y1 + 2 * circle_radius
                        canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline="white", width=3)
        
    def draw_player_token(self, cell, n_of_tokens):
        self.common_tokens.append(cell)
        frame_width = self.cell_size
        
        frame_middle = frame_width // 1.2
        token_size = frame_width // 1.2  # Adjusted to center the token
        delta = frame_width / 5

        canvas = tk.Canvas(cell, bg="#f0f0f0", width=frame_width, height=frame_width)
        canvas.pack(expand=True, fill="both")

        # Create the oval
        canvas.create_oval(frame_middle + token_size + delta,
                            frame_middle - token_size + delta,
                            frame_middle - token_size + delta,
                            frame_middle + token_size + delta,
                            fill=self.color,
                            outline="white",
                            width=3)

        # Add a number inside the circle
        text = str(n_of_tokens)
        canvas.create_text(frame_middle + delta, frame_middle + delta, text=text, font=("Helvetica", 12, "bold"))
