import tkinter as tk
import random

# -----------------------
# SETTINGS
# -----------------------

WIDTH = 1200
HEIGHT = 700
BLOCK_SIZE = 40

# -----------------------
# WINDOW
# -----------------------

root = tk.Tk()
root.title("Mini Minecraft")

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="skyblue"
)
canvas.pack()

# -----------------------
# PLAYER
# -----------------------

player_x = 0
player_y = 8

camera_x = 0
camera_y = 0

# -----------------------
# BLOCKS
# -----------------------

colors = {
    "grass": "#4CAF50",
    "dirt": "#8B4513",
    "stone": "#808080",
    "sand": "#F4E19C",
    "water": "#2196F3",
    "wood": "#795548",
    "leaves": "#2E7D32",
    "coal": "#222222",
    "iron": "#B0BEC5",
    "gold": "#FFD700",
    "diamond": "#00E5FF",
    "lava": "#FF5722",
    "brick": "#B71C1C",
    "snow": "#FFFFFF",
    "glass": "#BBDEFB"
}

selected_block = "grass"

# -----------------------
# WORLD
# -----------------------

world = {}

# terrain
for x in range(-150, 150):

    ground = random.randint(10, 14)

    for y in range(ground, 30):

        if y == ground:
            world[(x, y)] = "grass"

        elif y < ground + 3:
            world[(x, y)] = "dirt"

        else:
            world[(x, y)] = "stone"

# ores
for x in range(-150, 150):

    for y in range(15, 30):

        r = random.random()

        if r < 0.03:
            world[(x, y)] = "coal"

        elif r < 0.05:
            world[(x, y)] = "iron"

        elif r < 0.06:
            world[(x, y)] = "gold"

        elif r < 0.065:
            world[(x, y)] = "diamond"

# trees
for x in range(-120, 120, 10):

    ground_y = None

    for y in range(0, 30):

        if world.get((x, y)) == "grass":
            ground_y = y
            break

    if ground_y:

        for h in range(1, 5):
            world[(x, ground_y - h)] = "wood"

        for lx in range(x - 2, x + 3):
            for ly in range(ground_y - 6, ground_y - 2):
                world[(lx, ly)] = "leaves"

# lake
for x in range(-30, -10):
    for y in range(12, 16):
        world[(x, y)] = "water"

# lava pool
for x in range(30, 45):
    for y in range(20, 24):
        world[(x, y)] = "lava"

# -----------------------
# DRAW
# -----------------------

def draw():

    canvas.delete("all")

    start_x = camera_x // BLOCK_SIZE - 2
    end_x = start_x + WIDTH // BLOCK_SIZE + 5

    start_y = camera_y // BLOCK_SIZE - 2
    end_y = start_y + HEIGHT // BLOCK_SIZE + 5

    for x in range(start_x, end_x):

        for y in range(start_y, end_y):

            if (x, y) in world:

                block = world[(x, y)]

                sx = x * BLOCK_SIZE - camera_x
                sy = y * BLOCK_SIZE - camera_y

                canvas.create_rectangle(
                    sx,
                    sy,
                    sx + BLOCK_SIZE,
                    sy + BLOCK_SIZE,
                    fill=colors[block],
                    outline="black"
                )

    # player

    px = player_x * BLOCK_SIZE - camera_x
    py = player_y * BLOCK_SIZE - camera_y

    canvas.create_rectangle(
        px,
        py,
        px + 30,
        py + 50,
        fill="red"
    )

    # UI

    canvas.create_rectangle(
        5,
        5,
        WIDTH - 5,
        50,
        fill="white"
    )

    canvas.create_text(
        WIDTH // 2,
        25,
        text=(
            "WASD Move | Left Click Place | Right Click Break | "
            "1 Grass 2 Dirt 3 Stone 4 Sand 5 Water "
            "6 Wood 7 Leaves 8 Iron 9 Diamond 0 Lava"
        ),
        font=("Arial", 11)
    )

    canvas.create_text(
        120,
        65,
        text=f"Selected Block: {selected_block}",
        font=("Arial", 14, "bold")
    )

# -----------------------
# CAMERA
# -----------------------

def update_camera():

    global camera_x
    global camera_y

    camera_x = player_x * BLOCK_SIZE - WIDTH // 2
    camera_y = player_y * BLOCK_SIZE - HEIGHT // 2

# -----------------------
# KEYS
# -----------------------

def key(event):

    global player_x
    global player_y
    global selected_block

    if event.keysym.lower() == "a":
        player_x -= 1

    elif event.keysym.lower() == "d":
        player_x += 1

    elif event.keysym.lower() == "w":
        player_y -= 1

    elif event.keysym.lower() == "s":
        player_y += 1

    elif event.char == "1":
        selected_block = "grass"

    elif event.char == "2":
        selected_block = "dirt"

    elif event.char == "3":
        selected_block = "stone"

    elif event.char == "4":
        selected_block = "sand"

    elif event.char == "5":
        selected_block = "water"

    elif event.char == "6":
        selected_block = "wood"

    elif event.char == "7":
        selected_block = "leaves"

    elif event.char == "8":
        selected_block = "iron"

    elif event.char == "9":
        selected_block = "diamond"

    elif event.char == "0":
        selected_block = "lava"

    update_camera()
    draw()

# -----------------------
# MOUSE
# -----------------------

def left_click(event):

    world_x = (event.x + camera_x) // BLOCK_SIZE
    world_y = (event.y + camera_y) // BLOCK_SIZE

    world[(world_x, world_y)] = selected_block

    draw()

def right_click(event):

    world_x = (event.x + camera_x) // BLOCK_SIZE
    world_y = (event.y + camera_y) // BLOCK_SIZE

    if (world_x, world_y) in world:
        del world[(world_x, world_y)]

    draw()

# -----------------------
# EVENTS
# -----------------------

root.bind("<Key>", key)

canvas.bind("<Button-1>", left_click)
canvas.bind("<Button-3>", right_click)

# -----------------------
# START
# -----------------------

update_camera()
draw()

root.mainloop()
