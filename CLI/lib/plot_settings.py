import datetime

RES_STYLE: dict[str, list[bool] | int | str | float] = {
    "font": 'Times New Roman',
    "title_size": 18,
    "label_size": 18,
    "internal_fontsize": 14,
    "label_weight": 'bold',
    "line_width": 1.8,
    "tick_width": 1.8,
    "border": [True, True, True, True],
    "grid": "off",
    "marker_size": 4
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
        'x-velocity': 'darkorange',
        'y-velocity': 'forestgreen',
        'k': 'crimson',
        'omega': 'darkviolet',
        'energy': 'saddlebrown'  # Replaced teal
    },
    'dark': {
        'continuity': 'skyblue',
        'x-velocity': 'sandybrown',
        'y-velocity': 'mediumaquamarine',
        'k': 'lightcoral',
        'omega': 'orchid',
        'energy': 'peru'          # Replaced turquoise
    }
}

# mode = "dark"
