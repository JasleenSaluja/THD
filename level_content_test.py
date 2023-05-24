from pickle import load

file = r'C:\mp\THD-3\levels\level_1_2023_05_23_11_28_46.game'

with open(file, 'rb') as f:
    canvas_data = load(f)

print(canvas_data)