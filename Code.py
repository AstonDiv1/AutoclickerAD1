import time
import threading
from pynput import keyboard
from pynput.mouse import Button, Controller
import tkinter as tk
from tkinter import ttk

class AutoClicker:
    def __init__(self, button, interval=0.1):
        # Initialize the controller for keyboard or mouse based on the button type
        self.controller = keyboard.Controller() if isinstance(button, keyboard.Key) else Controller()
        self.button = button
        self.active = False
        self.thread = None
        self.interval = interval

    def start_autoclicker(self):
        # Start the autoclicker by setting it as active and creating a new thread
        self.active = True
        self.thread = threading.Thread(target=self._autoclick)
        self.thread.start()

    def stop_autoclicker(self):
        # Stop the autoclicker by setting it as inactive and joining the thread
        self.active = False
        if self.thread is not None:
            self.thread.join()

    def _autoclick(self):
        # The main loop for the autoclicker, continuously clicking at the specified interval
        while self.active:
            self.controller.press(self.button)
            self.controller.release(self.button)
            time.sleep(self.interval)

def on_press(key):
    # Toggle the autoclicker on or off when the activation key is pressed
    if key == activation_key:
        toggle_clicker()

def toggle_clicker():
    # Toggle the state of the autoclicker between active and inactive
    if current_clicker.active:
        current_clicker.stop_autoclicker()
    else:
        current_clicker.start_autoclicker()

def set_interval(interval):
    # Set the interval for the autoclicker clicks
    current_clicker.interval = interval

def set_clicker_button(button):
    # Set the button to be clicked by the autoclicker
    global current_clicker
    current_clicker.stop_autoclicker()
    current_clicker = AutoClicker(button, current_clicker.interval)

def set_activation_key(new_key):
    # Set the key that activates or deactivates the autoclicker
    global activation_key
    activation_key = new_key

# Initial configuration
activation_key = keyboard.Key.f1
current_clicker = AutoClicker(Button.left)

# Texts for different languages
texts = {
    'en': {
        'title': "AutoClicker Settings",
        'select_speed': "Select Speed",
        'select_click_type': "Select Click Type",
        'select_activation_key': "Select Activation Key",
        'low': "Low",
        'normal': "Normal",
        'high': "High",
        'manual': "Manual",
        'manual_input': "Enter interval (seconds):",
        'left_click': "Left Click",
        'right_click': "Right Click",
        'middle_click': "Middle Click",
        'space': "Space",
        'enter': "Enter",
        'delete': "Delete",
        'footer': "Created by AstonDiv1"
    },
    'fr': {
        'title': "Paramètres de l'AutoClicker",
        'select_speed': "Sélectionner la Vitesse",
        'select_click_type': "Sélectionner le Type de Clic",
        'select_activation_key': "Sélectionner la Touche d'Activation",
        'low': "Faible",
        'normal': "Normal",
        'high': "Élevé",
        'manual': "Manuel",
        'manual_input': "Entrer l'intervalle (secondes) :",
        'left_click': "Clic Gauche",
        'right_click': "Clic Droit",
        'middle_click': "Clic Molette",
        'space': "Espace",
        'enter': "Entrée",
        'delete': "Suppr",
        'footer': "Créé par AstonDiv1"
    },
    'es': {
        'title': "Configuración de AutoClicker",
        'select_speed': "Seleccionar Velocidad",
        'select_click_type': "Seleccionar Tipo de Clic",
        'select_activation_key': "Seleccionar Tecla de Activación",
        'low': "Baja",
        'normal': "Normal",
        'high': "Alta",
        'manual': "Manual",
        'manual_input': "Ingrese el intervalo (segundos):",
        'left_click': "Clic Izquierdo",
        'right_click': "Clic Derecho",
        'middle_click': "Clic Medio",
        'space': "Espacio",
        'enter': "Entrar",
        'delete': "Eliminar",
        'footer': "Creado por AstonDiv1"
    },
    'de': {
        'title': "AutoClicker Einstellungen",
        'select_speed': "Geschwindigkeit auswählen",
        'select_click_type': "Klick-Typ auswählen",
        'select_activation_key': "Aktivierungstaste auswählen",
        'low': "Niedrig",
        'normal': "Normal",
        'high': "Hoch",
        'manual': "Manuell",
        'manual_input': "Intervall eingeben (Sekunden):",
        'left_click': "Linksklick",
        'right_click': "Rechtsklick",
        'middle_click': "Mittelklick",
        'space': "Leertaste",
        'enter': "Eingabetaste",
        'delete': "Löschen",
        'footer': "Erstellt von AstonDiv1"
    }
}

current_language = 'en'

def change_language(language):
    # Change the language of the UI
    global current_language
    current_language = language
    refresh_ui()

def refresh_ui():
    # Refresh the UI elements to reflect the selected language
    window.title(texts[current_language]['title'])
    speed_frame.config(text=texts[current_language]['select_speed'])
    click_frame.config(text=texts[current_language]['select_click_type'])
    key_frame.config(text=texts[current_language]['select_activation_key'])
    manual_label.config(text=texts[current_language]['manual_input'])
    
    # Update speed options
    for widget in speed_frame.winfo_children():
        widget.destroy()
    for speed in ["low", "normal", "high", "manual"]:
        ttk.Radiobutton(speed_frame, text=texts[current_language][speed], variable=speed_var, value=speed.capitalize(), command=update_speed).pack(anchor="w")
    manual_frame.pack(padx=10, pady=10, fill="x")

    # Update click type options
    for widget in click_frame.winfo_children():
        widget.destroy()
    for click in ["left_click", "right_click", "middle_click", "space", "enter", "delete"]:
        ttk.Radiobutton(click_frame, text=texts[current_language][click], variable=click_var, value=texts[current_language][click], command=update_clicker).pack(anchor="w")

    # Update activation key options
    for widget in key_frame.winfo_children():
        widget.destroy()
    for key in ["F1", "F2", "F3", "F4"]:
        ttk.Radiobutton(key_frame, text=key, variable=activation_key_var, value=key, command=update_activation_key).pack(anchor="w")

    # Update footer
    footer.config(text=texts[current_language]['footer'])

def update_speed():
    # Update the autoclicker speed based on the selected option
    speed = speed_var.get()
    interval = 1.0  # Default to normal speed
    if speed == "Low":
        interval = 0.5
    elif speed == "High":
        interval = 0.01
    elif speed == "Manual":
        try:
            interval = float(manual_entry.get())
        except ValueError:
            interval = 0.1
    set_interval(interval)

def update_clicker():
    # Update the button to be clicked by the autoclicker
    button = click_var.get()
    if button == texts[current_language]["left_click"]:
        set_clicker_button(Button.left)
    elif button == texts[current_language]["right_click"]:
        set_clicker_button(Button.right)
    elif button == texts[current_language]["middle_click"]:
        set_clicker_button(Button.middle)
    elif button == texts[current_language]["space"]:
        set_clicker_button(keyboard.Key.space)
    elif button == texts[current_language]["enter"]:
        set_clicker_button(keyboard.Key.enter)
    elif button == texts[current_language]["delete"]:
        set_clicker_button(keyboard.Key.delete)

def update_activation_key():
    # Update the activation key for the autoclicker
    new_key = activation_key_var.get()
    if new_key == "F1":
        set_activation_key(keyboard.Key.f1)
    elif new_key == "F2":
        set_activation_key(keyboard.Key.f2)
    elif new_key == "F3":
        set_activation_key(keyboard.Key.f3)
    elif new_key == "F4":
        set_activation_key(keyboard.Key.f4)

def create_interface():
    # Create the main interface for the autoclicker settings
    global window, speed_frame, click_frame, key_frame, manual_frame, manual_label, manual_entry, speed_var, click_var, activation_key_var, footer

    window = tk.Tk()
    window.title(texts[current_language]['title'])
    window.geometry("350x570")

    # Speed settings
    speed_frame = ttk.LabelFrame(window, text=texts[current_language]['select_speed'])
    speed_frame.pack(padx=10, pady=10, fill="x")

    speed_var = tk.StringVar(value="Normal")
    for speed in ["low", "normal", "high", "manual"]:
        ttk.Radiobutton(speed_frame, text=texts[current_language][speed], variable=speed_var, value=speed.capitalize(), command=update_speed).pack(anchor="w")
    
    # Manual interval input
    manual_frame = ttk.Frame(window)
    manual_label = ttk.Label(manual_frame, text=texts[current_language]['manual_input'])
    manual_label.pack(side="left", padx=5)
    manual_entry = ttk.Entry(manual_frame)
    manual_entry.pack(side="left", padx=5)
    manual_entry.insert(0, "0.1")

    manual_frame.pack(padx=10, pady=10, fill="x")

    # Click type settings
    click_frame = ttk.LabelFrame(window, text=texts[current_language]['select_click_type'])
    click_frame.pack(padx=10, pady=10, fill="x")

    click_var = tk.StringVar(value=texts[current_language]['left_click'])
    for click in ["left_click", "right_click", "middle_click", "space", "enter", "delete"]:
        ttk.Radiobutton(click_frame, text=texts[current_language][click], variable=click_var, value=texts[current_language][click], command=update_clicker).pack(anchor="w")

    # Activation key settings
    key_frame = ttk.LabelFrame(window, text=texts[current_language]['select_activation_key'])
    key_frame.pack(padx=10, pady=10, fill="x")

    activation_key_var = tk.StringVar(value="F1")
    for key in ["F1", "F2", "F3", "F4"]:
        ttk.Radiobutton(key_frame, text=key, variable=activation_key_var, value=key, command=update_activation_key).pack(anchor="w")

    # Language buttons
    lang_frame = ttk.LabelFrame(window, text="Languages")
    lang_frame.pack(padx=10, pady=10, fill="x")

    tk.Button(lang_frame, text="English", command=lambda: change_language('en')).pack(side="left", padx=5, pady=5)
    tk.Button(lang_frame, text="Français", command=lambda: change_language('fr')).pack(side="left", padx=5, pady=5)
    tk.Button(lang_frame, text="Español", command=lambda: change_language('es')).pack(side="left", padx=5, pady=5)
    tk.Button(lang_frame, text="Deutsch", command=lambda: change_language('de')).pack(side="left", padx=5, pady=5)

    # Footer with creator information
    footer = ttk.Label(window, text=texts[current_language]['footer'], font=('Arial', 10, 'italic'))
    footer.pack(side="bottom", pady=10)

    window.mainloop()

# Start the interface in a separate thread to not block the key listener
interface_thread = threading.Thread(target=create_interface)
interface_thread.start()

# Listen to all key press events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
