import datetime
PLOT_STYLE_RES: dict[str, list[bool] | int | str | float] = {
    "font": 'Times New Roman',
    "title_size": 20,
    "label_size": 16,
    "internal_fontsize":16,
    "label_weight": 'bold',
    "line_width": 0.75,
    "border": [False, False, True, True],
}
RES_MARKERS = [
        'k--',
        'r-.',
        'g:',
        'b--',
        'm-',
        'c:',
        '-'
        ]
color = {
        "light" : "white",
        "dark" : "#121212"
        }

alpha = {
        "light" : 0.5,
        "dark" : 0.2
        }
contrast = {
        "light" : "black",
        "dark" : "#E0E0E0"
        }

current_hour = datetime.datetime.now().hour

if 6 <= current_hour < 18:
    mode = "light"
else:
    mode = "dark"

palettes = {
    'light': {
        'continuity': 'royalblue',
        'x': 'darkorange',
        'y': 'forestgreen',
        'k': 'crimson',
        'omega': 'darkviolet',
        'energy': 'saddlebrown'  # Replaced teal
    },
    'dark': {
        'continuity': 'skyblue',
        'x': 'sandybrown',
        'y': 'mediumaquamarine',
        'k': 'lightcoral',
        'omega': 'orchid',
        'energy': 'peru'          # Replaced turquoise
    }
}

# mode = "dark"
