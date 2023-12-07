import PySimpleGUI as sG
from zip_extractor import extract_archive

sG.theme('Black')

label1 = sG.Text("Select archive: ")
input1 = sG.Input()
choose_button1 = sG.FileBrowse("Choose a file", key="archive")

label2 = sG.Text("Select folder: ")
input2 = sG.Input()
choose_button2 = sG.FolderBrowse("choose a folder", key="folder")

extract_button = sG.Button("Extract")
output_label = sG.Text(key="output", text_color="green")

window = sG.Window("Archive Extractor", layout=[[label1, input1, choose_button1],
                                                [label2, input2, choose_button2],
                                                [extract_button, output_label]])

while True:
    event, values = window.read()
    extract_archive(values["archive"], values["folder"])
    window["output"].update(value="Extraction Completed!")
    break

window.close()
