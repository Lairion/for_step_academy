from json import load
from tkinter import Tk, ttk
from connector import TuyaConnector
from setting import DEVICE_FOLDER

class MainWindow:
    
    connector = TuyaConnector()
    
    def __init__(self, file):
        self.root = Tk()
        self.root.title(file.stem)
        self.device = load(open(file))
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()
        self.label = ttk.Label(self.root, text="Choose action")
        self.label.grid(column=0, row=0)
        self.cmb = ttk.Combobox(
            self.root, text="Run", values=list(self.device["commands"].keys())
        )
        self.cmb.grid(column=0, row=1)
        self.btn = ttk.Button(self.root, text="Run", command=self.run)
        self.btn.grid(column=0, row=2)
        
    def open(self):
        self.root.mainloop()
        
    def run(self):
        self.connector.make_device_command(
            self.device["id"], self.device["commands"][self.cmb.get()]
        )
        
def run_tuya():
    device_file= DEVICE_FOLDER.joinpath("kettle.json")
    if not device_file.is_file():
        print(f"{device_file} not exist")
        return False
    MainWindow(device_file)
    