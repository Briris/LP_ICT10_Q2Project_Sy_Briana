from js import document

# Path information
paths = {
    "btn_victory": ("Victory Road", "Victory Road is the classic path where you challenge Gym Leaders in order to become a champion."),
    "btn_legends": ("Path of Legends", "Path of Legends takes you on an adventure to discover and bond with Titan Pokémon."),
    "btn_starfall": ("Starfall Street", "Starfall Street allows you to challenge Team Star bases and uncover their secrets.")
}

def show_path_info(event):
    """Display path information as a paragraph"""
    if event.target.id in paths:
        title, content = paths[event.target.id]
        document.getElementById("pathTitle").textContent = title
        document.getElementById("pathContent").textContent = content
        document.getElementById("pathInfo").style.display = "block"
