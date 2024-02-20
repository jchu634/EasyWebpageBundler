import uvicorn
from fastapiserver import app
from config import Settings

import webview
import sys
import threading

import webview.menu as wm

import platform

backendPort = 6789
host = "0.0.0.0"

def server():
    uvicorn.run(app, port=backendPort, host=host)

def change_active_window_content():
    active_window = webview.active_window()
    if active_window:
        pass
        # Load HTML from String
        # active_window.load_html()
    
        # Load URL from String
        # active_window.load_url()

def open_file_dialog():
    active_window = webview.active_window()
    active_window.create_file_dialog(webview.SAVE_DIALOG, directory='/', save_filename='test.file')

def open_print_dialog():
    active_window = webview.active_window()
    active_window.create_file_dialog(webview.SAVE_DIALOG, directory='/', save_filename='test.file')


if __name__ == "__main__":
    t = threading.Thread(target=server)
    t.daemon = True
    t.start()
    
    webview.create_window(Settings.APPNAME, f"http://localhost:{backendPort}")
    menu_items = [
        wm.Menu(
            'Navigation Menu',
            [
                wm.MenuAction('Change Active Window Content', change_active_window_content),
                wm.MenuSeparator(),
                wm.MenuAction('Save As', open_file_dialog),
            ],
        ),
    ]

    match platform.system():
        case "Windows":
            webview.start(menu=menu_items)
        case "Linux":
            webview.start(menu=menu_items, gui='gtk', private_mode=False)
        
    sys.exit()