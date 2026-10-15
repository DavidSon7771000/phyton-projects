import customtkinter as ctk
from tkinter import messagebox

# Configuración del tema visual
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

# ==========================================
# ESTRUCTURA DE DATOS BASE
# ==========================================
servicios = {
    1: ("Corte de Cabello Tradicional", 200.00),
    2: ("Arreglo / Delineado de Barba", 150.00),
    3: ("Combo Imperial (Corte + Barba)", 300.00),
    4: ("Tinte / Camuflaje de Canas", 400.00),
    5: ("Limpieza Facial y Mascarilla", 180.00)
}

productos = {
    "Cera de Peinado": 120.00,
    "Minoxidil Tónico": 350.00,
    "Gel Extra Firme": 80.00,
    "Espuma de Afeitar": 110.00,
    "Shampoo Anticaída": 160.00
}

barberos = ["Carlos (Master)", "Alex (Senior)", "Mateo (Junior)"]

# ==========================================
# LÓGICA DE NEGOCIO
# ==========================================
def gestionarSeleccion(opcion, serviciosElegidos):
    if opcion in (1, 2):
        if 3 in serviciosElegidos:
            serviciosElegidos.remove(3)
        if opcion not in serviciosElegidos:
            serviciosElegidos.append(opcion)

    elif opcion == 3:
        serviciosElegidos = [s for s in serviciosElegidos if s not in (1, 2)]
        if 3 not in serviciosElegidos:
            serviciosElegidos.append(3)

    elif opcion in (4, 5):
        if opcion not in serviciosElegidos:
            serviciosElegidos.append(opcion)

    # REGLA AUTOMÁTICA: Si seleccionó 1 Y 2 por separado, se convierten en Combo 3
    if 1 in serviciosElegidos and 2 in serviciosElegidos:
        serviciosElegidos.remove(1)
        serviciosElegidos.remove(2)
        serviciosElegidos.append(3)

    return serviciosElegidos

# ==========================================
# INTERFAZ GRÁFICA MODERNA
# ==========================================
class POSBarberiaApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("BARBERÍA EL PELÓN - SISTEMA DE CAJA DE COBRO")
        self.geometry("1150x750")
        self.configure(fg_color="#121212")

        # Variables de estado
        self.serviciosElegidos = []
        self.productosElegidos = {}
        self.metodoPagoVar = ctk.StringVar(value="Efectivo")

        self.build_ui()

    def build_ui(self):
        # 1. HEADER SUPERIOR
        header = ctk.CTkFrame(self, fg_color="#1E1E1E", corner_radius=0, height=70)
        header.pack(fill="x", side="top")

        lbl_title = ctk.CTkLabel(
            header, 
            text="💈 BARBERÍA EL PELÓN", 
            font=ctk.CTkFont(family="Segoe UI", size=22, weight="bold"),
            text_color="#D4AF37"
        )
        lbl_title.pack(side="left", padx=25, pady=15)

        lbl_subtitle = ctk.CTkLabel(
            header, 
            text="Gestión de Caja & Punto de Venta", 
            font=ctk.CTkFont(family="Segoe UI", size=13),
            text_color="#888888"
        )
        lbl_subtitle.pack(side="left", pady=15)

        # 2. PANEL PRINCIPAL
        main_panel = ctk.CTkFrame(self, fg_color="#121212")
        main_panel.pack(fill="both", expand=True, padx=20, pady=20)

        # COLUMNA IZQUIERDA (Catálogos)
        left_col = ctk.CTkFrame(main_panel, fg_color="transparent")
        left_col.pack(side="left", fill="both", expand=True, padx=(0, 15))

        # Sección Datos de Atención
        info_card = ctk.CTkFrame(left_col, fg_color="#1E1E1E", corner_radius=12)
        info_card.pack(fill="x", pady=(0, 15), ipadx=10, ipady=10)

        ctk.CTkLabel(info_card, text="DATOS DE ATENCIÓN", font=ctk.CTkFont(size=11, weight="bold"), text_color="#D4AF37").pack(anchor="w", padx=15, pady=(5, 10))

        grid_info = ctk.CTkFrame(info_card, fg_color="transparent")
        grid_info.pack(fill="x", padx=10)

        ctk.CTkLabel(grid_info, text="Cliente:", text_color="#CCCCCC").grid(row=0, column=0, padx=10, sticky="w")
        self.ent_cliente = ctk.CTkEntry(grid_info, placeholder_text="Nombre del cliente", width=200, fg_color="#2B2B2B", border_color="#3A3A3A")
        self.ent_cliente.insert(0, "Pedro Gómez")
        self.ent_cliente.grid(row=0, column=1, padx=10)

        ctk.CTkLabel(grid_info, text="Atendió:", text_color="#CCCCCC").grid(row=0, column=2, padx=10, sticky="w")
        self.cb_barbero = ctk.CTkOptionMenu(grid_info, values=barberos, fg_color="#2B2B2B", button_color="#3A3A3A", button_hover_color="#D4AF37", dropdown_fg_color="#1E1E1E")
        self.cb_barbero.grid(row=0, column=3, padx=10)

        # Sección Servicios
        serv_card = ctk.CTkFrame(left_col, fg_color="#1E1E1E", corner_radius=12)
        serv_card.pack(fill="x", pady=(0, 15), ipadx=10, ipady=10)

        ctk.CTkLabel(serv_card, text="CATÁLOGO DE SERVICIOS", font=ctk.CTkFont(size=11, weight="bold"), text_color="#D4AF37").pack(anchor="w", padx=15, pady=(5, 10))

        for sId, (nombre, precio) in servicios.items():
            btn = ctk.CTkButton(
                serv_card,
                text=f"{nombre}  —  ${precio:.2f}",
                font=ctk.CTkFont(size=13, weight="bold"),
                fg_color="#2B2B2B",
                hover_color="#D4AF37",
                text_color="#FFFFFF",
                anchor="w",
                height=40,
                corner_radius=8,
                command=lambda id=sId: self.agregar_servicio(id)
            )
            btn.pack(fill="x", padx=15, pady=4)

        # Sección Productos (Venta Cruzada)
        prod_card = ctk.CTkFrame(left_col, fg_color="#1E1E1E", corner_radius=12)
        prod_card.pack(fill="x", ipadx=10, ipady=10)

        ctk.CTkLabel(prod_card, text="VENTA CRUZADA / PRODUCTOS", font=ctk.CTkFont(size=11, weight="bold"), text_color="#D4AF37").pack(anchor="w", padx=15, pady=(5, 10))

        grid_prod = ctk.CTkFrame(prod_card, fg_color="transparent")
        grid_prod.pack(fill="x", padx=10)

        r, c = 0, 0
        for p_nombre, p_precio in productos.items():
            btn_p = ctk.CTkButton(
                grid_prod,
                text=f"+ {p_nombre}\n${p_precio:.2f}",
                font=ctk.CTkFont(size=11),
                fg_color="#1A2E22",
                hover_color="#00E676",
                text_color="#00E676",
                height=45,
                corner_radius=8,
                command=lambda name=p_nombre: self.agregar_producto(name)
            )
            btn_p.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
            grid_prod.columnconfigure(c, weight=1)
            c += 1
            if c > 2:
                c = 0
                r += 1

        # COLUMNA DERECHA (Resumen y Pago)
        right_col = ctk.CTkFrame(main_panel, fg_color="#1E1E1E", corner_radius=12, width=380)
        right_col.pack(side="right", fill="both")

        ctk.CTkLabel(right_col, text="RESUMEN DE CUENTA", font=ctk.CTkFont(size=14, weight="bold"), text_color="#D4AF37").pack(pady=(15, 10))

        # Visor de Ticket
        self.txt_ticket = ctk.CTkTextbox(right_col, fg_color="#121212", text_color="#00FF66", font=ctk.CTkFont(family="Consolas", size=12), corner_radius=8, height=200)
        self.txt_ticket.pack(fill="x", padx=15, pady=5)

        # Métodos de Pago
        pago_card = ctk.CTkFrame(right_col, fg_color="#2B2B2B", corner_radius=10)
        pago_card.pack(fill="x", padx=15, pady=10, ipadx=5, ipady=5)

        ctk.CTkLabel(pago_card, text="Método de Pago", font=ctk.CTkFont(size=11, weight="bold"), text_color="#FFFFFF").pack(anchor="w", padx=10, pady=2)

        opts_frame = ctk.CTkFrame(pago_card, fg_color="transparent")
        opts_frame.pack(fill="x", padx=5)

        for modo in [("Efectivo 💵", "Efectivo"), ("Tarjeta 💳", "Tarjeta"), ("Transf. 📱", "Transferencia")]:
            rb = ctk.CTkRadioButton(
                opts_frame, 
                text=modo[0], 
                value=modo[1], 
                variable=self.metodoPagoVar,
                fg_color="#D4AF37", 
                hover_color="#D4AF37",
                command=self.toggle_metodo_pago
            )
            rb.pack(side="left", expand=True, pady=5)

        # Entrada de Efectivo y Cambio
        self.frame_efectivo = ctk.CTkFrame(right_col, fg_color="transparent")
        self.frame_efectivo.pack(fill="x", padx=15, pady=5)

        ctk.CTkLabel(self.frame_efectivo, text="Paga con $:", text_color="#FFFFFF").pack(side="left")
        self.ent_pago = ctk.CTkEntry(self.frame_efectivo, width=90, fg_color="#121212", border_color="#00E676", text_color="#00E676", font=ctk.CTkFont(weight="bold"))
        self.ent_pago.pack(side="left", padx=10)
        self.ent_pago.bind("<KeyRelease>", lambda e: self.calcular_cambio_live())

        self.lbl_cambio = ctk.CTkLabel(self.frame_efectivo, text="Cambio: $0.00", text_color="#D4AF37", font=ctk.CTkFont(weight="bold"))
        self.lbl_cambio.pack(side="right")

        # Totales y Comisiones
        self.lbl_total = ctk.CTkLabel(right_col, text="TOTAL: $0.00", font=ctk.CTkFont(size=20, weight="bold"), text_color="#FFFFFF")
        self.lbl_total.pack(pady=(10, 2))

        self.lbl_comision = ctk.CTkLabel(right_col, text="Comisión Barbero (40%): $0.00", font=ctk.CTkFont(size=11), text_color="#888888")
        self.lbl_comision.pack(pady=(0, 10))

        # Botones Finales
        btn_cobrar = ctk.CTkButton(
            right_col, 
            text="FINALIZAR COBRO 🛠️", 
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#D4AF37", 
            hover_color="#B38F2D", 
            text_color="#000000",
            height=45,
            corner_radius=10,
            command=self.procesar_cobro
        )
        btn_cobrar.pack(fill="x", padx=15, pady=5)

        btn_limpiar = ctk.CTkButton(
            right_col, 
            text="Limpiar Ticket", 
            font=ctk.CTkFont(size=11),
            fg_color="#2B2B2B", 
            hover_color="#3A3A3A", 
            text_color="#FFFFFF",
            height=30,
            corner_radius=8,
            command=self.resetear
        )
        btn_limpiar.pack(fill="x", padx=15, pady=(0, 15))

        self.actualizar_ticket()

    def toggle_metodo_pago(self):
        if self.metodoPagoVar.get() == "Efectivo":
            self.frame_efectivo.pack(fill="x", padx=15, pady=5)
        else:
            self.frame_efectivo.pack_forget()

    def agregar_servicio(self, sId):
        self.serviciosElegidos = gestionarSeleccion(sId, self.serviciosElegidos)
        self.actualizar_ticket()

    def agregar_producto(self, p_nombre):
        self.productosElegidos[p_nombre] = self.productosElegidos.get(p_nombre, 0) + 1
        self.actualizar_ticket()

    def calcular_total(self):
        total = 0.0
        for sId in self.serviciosElegidos:
            total += servicios[sId][1]
        for p_nombre, qty in self.productosElegidos.items():
            total += productos[p_nombre] * qty
        return total

    def calcular_cambio_live(self):
        try:
            monto_ingresado = float(self.ent_pago.get())
            total = self.calcular_total()
            cambio = monto_ingresado - total
            if cambio >= 0:
                self.lbl_cambio.configure(text=f"Cambio: ${cambio:.2f}", text_color="#00E676")
            else:
                self.lbl_cambio.configure(text="Insuficiente", text_color="#FF5252")
        except ValueError:
            self.lbl_cambio.configure(text="Cambio: $0.00", text_color="#D4AF37")

    def actualizar_ticket(self):
        self.txt_ticket.configure(state="normal")
        self.txt_ticket.delete("1.0", "end")
        self.txt_ticket.insert("end", "====== SERVICIOS SELECCIONADOS ======\n")
        
        total = 0.0
        for sId in self.serviciosElegidos:
            nombre, precio = servicios[sId]
            self.txt_ticket.insert("end", f"• {nombre[:20]:<20} ${precio:>6.2f}\n")
            total += precio

        if self.productosElegidos:
            self.txt_ticket.insert("end", "\n====== PRODUCTOS ADICIONALES ======\n")
            for p_nombre, qty in self.productosElegidos.items():
                subt = productos[p_nombre] * qty
                self.txt_ticket.insert("end", f"• {qty}x {p_nombre[:16]:<16} ${subt:>6.2f}\n")
                total += subt

        self.txt_ticket.configure(state="disabled")
        self.lbl_total.configure(text=f"TOTAL: ${total:.2f}")
        comision = total * 0.40
        self.lbl_comision.configure(text=f"Comisión Barbero (40%): ${comision:.2f}")
        self.calcular_cambio_live()

    def resetear(self):
        self.serviciosElegidos = []
        self.productosElegidos = {}
        self.ent_pago.delete(0, "end")
        self.actualizar_ticket()

    def procesar_cobro(self):
        total = self.calcular_total()
        if total == 0:
            messagebox.showwarning("Atención", "No hay servicios ni productos en la cuenta.")
            return

        cliente = self.ent_cliente.get().strip() or "Cliente Mostrador"
        barbero = self.cb_barbero.get()
        metodo = self.metodoPagoVar.get()

        pago_con = 0.0
        cambio = 0.0

        if metodo == "Efectivo":
            try:
                pago_con = float(self.ent_pago.get())
                if pago_con < total:
                    messagebox.showerror("Error de Pago", f"El monto ingresado (${pago_con:.2f}) es menor al total a pagar (${total:.2f}).")
                    return
                cambio = pago_con - total
            except ValueError:
                messagebox.showerror("Error", "Ingresa una cantidad válida en el monto entregado por el cliente.")
                return

        self.mostrar_ticket_final(cliente, barbero, metodo, total, pago_con, cambio)

    def mostrar_ticket_final(self, cliente, barbero, metodo, total, pago_con, cambio):
        win = ctk.CTkToplevel(self)
        win.title("Ticket de Venta")
        win.geometry("380x520")
        win.configure(fg_color="#FFFFFF")
        win.attributes("-topmost", True)

        txt = ctk.CTkTextbox(win, font=ctk.CTkFont(family="Consolas", size=12), fg_color="#FFFFFF", text_color="#000000")
        txt.pack(fill="both", expand=True, padx=15, pady=15)

        recibo = "====================================\n"
        recibo += "        BARBERÍA IMPERIAL 💈        \n"
        recibo += "   Av. Principal #123, Tabasco     \n"
        recibo += "====================================\n"
        recibo += f"Cliente: {cliente}\n"
        recibo += f"Atendió: {barbero}\n"
        recibo += f"Método de Pago: {metodo}\n"
        recibo += "------------------------------------\n"
        
        for sId in self.serviciosElegidos:
            nombre, precio = servicios[sId]
            recibo += f"{nombre[:22]:<22} ${precio:>7.2f}\n"

        for p_nombre, qty in self.productosElegidos.items():
            subt = productos[p_nombre] * qty
            recibo += f"{qty}x {p_nombre[:19]:<19} ${subt:>7.2f}\n"

        recibo += "------------------------------------\n"
        recibo += f"TOTAL:                   ${total:>7.2f}\n"

        if metodo == "Efectivo":
            recibo += f"PAGÓ CON:                ${pago_con:>7.2f}\n"
            recibo += f"CAMBIO:                  ${cambio:>7.2f}\n"

        recibo += "====================================\n"
        recibo += "    ¡GRACIAS POR SU PREFERENCIA!   \n"
        recibo += "      Visita 4/5 para tu corte     \n"
        recibo += "               GRATIS               \n"
        recibo += "====================================\n"

        txt.insert("end", recibo)
        txt.configure(state="disabled")

        btn_cerrar = ctk.CTkButton(
            win, 
            text="Cerrar e Iniciar Nueva Venta", 
            fg_color="#D4AF37", 
            text_color="#000000",
            hover_color="#B38F2D",
            font=ctk.CTkFont(weight="bold"),
            command=lambda: [win.destroy(), self.resetear()]
        )
        btn_cerrar.pack(fill="x", pady=10, padx=15)

if __name__ == "__main__":
    app = POSBarberiaApp()
    app.mainloop()