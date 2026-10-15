

import customtkinter as ctk

# Configuración inicial del tema
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Base de datos en memoria
db = {
    1: {"Modelo": "Accord", "Año": 2008},
    2: {"Modelo": "Rav-4", "Año": 2024}
}


class AppAutomoviles(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestión de Automóviles")
        self.geometry("680 x 520")
        self.resizable(False, False)

        # Panel Izquierdo: Formularios
        self.frame_inputs = ctk.CTkFrame(self, width=280)
        self.frame_inputs.pack(side="left", fill="y", padx=15, pady=15)

        self.lbl_title = ctk.CTkLabel(
            self.frame_inputs, text="Datos del Automóvil", font=("Arial", 16, "bold")
        )
        self.lbl_title.pack(pady=(15, 10))

        self.entry_id = ctk.CTkEntry(self.frame_inputs, placeholder_text="ID (número)")
        self.entry_id.pack(pady=8, padx=15, fill="x")

        self.entry_modelo = ctk.CTkEntry(self.frame_inputs, placeholder_text="Modelo")
        self.entry_modelo.pack(pady=8, padx=15, fill="x")

        self.entry_anio = ctk.CTkEntry(self.frame_inputs, placeholder_text="Año")
        self.entry_anio.pack(pady=8, padx=15, fill="x")

        # Botones de Operaciones
        self.btn_agregar = ctk.CTkButton(
            self.frame_inputs, text="Agregar", command=self.agregar
        )
        self.btn_agregar.pack(pady=5, padx=15, fill="x")

        self.btn_buscar = ctk.CTkButton(
            self.frame_inputs, text="Buscar por ID", command=self.leer
        )
        self.btn_buscar.pack(pady=5, padx=15, fill="x")

        self.btn_actualizar = ctk.CTkButton(
            self.frame_inputs, text="Actualizar", command=self.actualizar
        )
        self.btn_actualizar.pack(pady=5, padx=15, fill="x")

        self.btn_eliminar = ctk.CTkButton(
            self.frame_inputs,
            text="Eliminar",
            fg_color="#D32F2F",
            hover_color="#9A0007",
            command=self.eliminar,
        )
        self.btn_eliminar.pack(pady=5, padx=15, fill="x")

        self.btn_limpiar = ctk.CTkButton(
            self.frame_inputs,
            text="Limpiar Campos",
            fg_color="gray",
            hover_color="#555555",
            command=self.limpiar_campos,
        )
        self.btn_limpiar.pack(pady=(5, 15), padx=15, fill="x")

        # Panel Derecho: Visualización
        self.frame_display = ctk.CTkFrame(self)
        self.frame_display.pack(side="right", fill="both", expand=True, padx=(0, 15), pady=15)

        self.lbl_lista = ctk.CTkLabel(
            self.frame_display, text="Base de Datos", font=("Arial", 16, "bold")
        )
        self.lbl_lista.pack(pady=(15, 5))

        self.txt_output = ctk.CTkTextbox(self.frame_display, width=340, height=360)
        self.txt_output.pack(pady=5, padx=15, fill="both", expand=True)

        self.lbl_status = ctk.CTkLabel(
            self.frame_display, text="Listo", font=("Arial", 11), text_color="gray"
        )
        self.lbl_status.pack(pady=(5, 10))

        # Carga inicial
        self.listar()

    def mostrar_mensaje(self, mensaje, error=False):
        color = "#FF5252" if error else "#66BB6A"
        self.lbl_status.configure(text=mensaje, text_color=color)

    def limpiar_campos(self):
        self.entry_id.delete(0, "end")
        self.entry_modelo.delete(0, "end")
        self.entry_anio.delete(0, "end")

    def listar(self):
        self.txt_output.configure(state="normal")
        self.txt_output.delete("1.0", "end")

        if not db:
            self.txt_output.insert("end", "La base de datos está vacía.\n")
        else:
            for id_auto, datos in db.items():
                registro = f"ID: {id_auto} | Modelo: {datos['Modelo']} | Año: {datos['Año']}\n"
                self.txt_output.insert("end", registro)

        self.txt_output.configure(state="disabled")

    def agregar(self):
        try:
            id_usuario = int(self.entry_id.get())
            modelo = self.entry_modelo.get().strip()
            anio = int(self.entry_anio.get())

            if not modelo:
                self.mostrar_mensaje("El campo 'Modelo' no puede estar vacío.", error=True)
                return

            if id_usuario in db:
                self.mostrar_mensaje(f"El ID {id_usuario} ya existe.", error=True)
            else:
                db[id_usuario] = {"Modelo": modelo, "Año": anio}
                self.mostrar_mensaje("Automóvil agregado correctamente.")
                self.limpiar_campos()
                self.listar()
        except ValueError:
            self.mostrar_mensaje("ID y Año deben ser enteros válidos.", error=True)

    def leer(self):
        try:
            clave = int(self.entry_id.get())
            if clave in db:
                datos = db[clave]
                self.entry_modelo.delete(0, "end")
                self.entry_modelo.insert(0, datos["Modelo"])

                self.entry_anio.delete(0, "end")
                self.entry_anio.insert(0, str(datos["Año"]))

                self.mostrar_mensaje(f"Automóvil con ID {clave} encontrado.")
            else:
                self.mostrar_mensaje(f"El ID {clave} no existe.", error=True)
        except ValueError:
            self.mostrar_mensaje("Ingrese un número de ID válido para buscar.", error=True)

    def actualizar(self):
        try:
            id_usuario = int(self.entry_id.get())
            if id_usuario in db:
                modelo = self.entry_modelo.get().strip() or db[id_usuario]["Modelo"]
                anio_input = self.entry_anio.get().strip()
                anio = int(anio_input) if anio_input else db[id_usuario]["Año"]

                db[id_usuario] = {"Modelo": modelo, "Año": anio}
                self.mostrar_mensaje("Registro actualizado correctamente.")
                self.limpiar_campos()
                self.listar()
            else:
                self.mostrar_mensaje(f"El ID {id_usuario} no existe.", error=True)
        except ValueError:
            self.mostrar_mensaje("El año debe ser un número entero válido.", error=True)

    def eliminar(self):
        try:
            id_usuario = int(self.entry_id.get())
            if id_usuario in db:
                del db[id_usuario]
                self.mostrar_mensaje("Registro eliminado correctamente.")
                self.limpiar_campos()
                self.listar()
            else:
                self.mostrar_mensaje(f"El ID {id_usuario} no existe.", error=True)
        except ValueError:
            self.mostrar_mensaje("Ingrese un ID válido para eliminar.", error=True)


if __name__ == "__main__":
    app = AppAutomoviles()
    app.mainloop()