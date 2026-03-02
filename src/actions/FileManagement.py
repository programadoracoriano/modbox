import flet as ft
import os
import zipfile
import shutil


class FileManagement:
    def __init__(self, page: ft.Page, storage_path, on_success):
        self.page = page
        self.storage_path = storage_path
        self.on_success = on_success
        self.file_picker = ft.FilePicker()
        self.page.overlay.append(self.file_picker)

    def pick_file(self):
        self.file_picker.pick_files(
            allow_multiple=False,
            allowed_extensions=["zip", "rar", "7z"],
            dialog_title="Seleciona o Mod para Instalar"
        )

    def handle_file_result(self, e: ft.FilePickerResultEvent):
        if e.files:
            file_path = e.files[0].path
            mod_name = e.files[0].name.replace(".zip", "").replace(".7z", "")

            # 1. Criar pasta de destino no teu Storage
            destination = os.path.join(self.storage_path, mod_name)
            if not os.path.exists(destination):
                os.makedirs(destination)

            # 2. Extrair (Exemplo simples com ZIP)
            # Para 7z precisarias de: pip install py7zr
            try:
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(destination)

                # 3. Notificar o SQLite e a UI
                self.on_success(mod_name, destination)
                self.page.snack_bar = ft.SnackBar(ft.Text(f"Mod {mod_name} extraído com sucesso!"))
                self.page.snack_bar.open = True
                self.page.update()

            except Exception as ex:
                print(f"Erro ao extrair: {ex}")