"""
==============================================================================
 BARBERÍA EL PELÓN - Sistema de gestión y punto de venta (POS)
 Frontend con CustomTkinter  |  Requiere: pip install customtkinter
==============================================================================
Estructura del archivo:
  1. Tema y constantes de diseño
  2. Catálogos y lógica de negocio (portados de proyecto.py, sin input/print)
  3. Almacén de datos en memoria
  4. Componentes reutilizables (Tarjeta, Métrica, Tabla, Sidebar)
  5. Páginas (Dashboard, Citas, Clientes, Inventario, Caja/POS)
  6. Ventana principal (App)
"""

import datetime
import os
import customtkinter as ctk
from tkinter import messagebox

# ==============================================================================
# 1. TEMA Y CONSTANTES DE DISEÑO
# ==============================================================================
ctk.set_appearance_mode("Light")           # Modo claro explícito
ctk.set_default_color_theme("blue")

BG = "#F8F9FA"            # Fondo principal
CARD = "#FFFFFF"          # Fondo de tarjetas
BORDER = "#E2E8F0"        # Bordes sutiles
TEXT = "#1E293B"          # Azul marino / gris pizarra
MUTED = "#64748B"         # Texto secundario
ACCENT = "#2F6B4F"        # Verde bosque (acciones principales)
ACCENT_HOVER = "#245640"
SOFT = "#EEF2F6"          # Fondo de elementos activos / encabezados
DANGER = "#B42318"
DANGER_HOVER = "#8F1D14"
SELECCION = "#CFE3D8"    # Verde claro para opción seleccionada (texto legible)

RADIO_TARJETA = 14
RADIO_CONTROL = 10


# ==============================================================================
# 2. CATÁLOGOS Y LÓGICA DE NEGOCIO (de proyecto.py)
# ==============================================================================
SERVICIOS = {
    1: ("Corte de Cabello Tradicional", 200.00),
    2: ("Arreglo / Delineado de Barba", 150.00),
    3: ("Combo Imperial (Corte + Barba)", 300.00),
    4: ("Tinte / Camuflaje de Canas", 400.00),
    5: ("Limpieza Facial y Mascarilla", 180.00),
}

PRODUCTOS = {
    "Cera": 120.00,
    "Minoxidil": 350.00,
    "Gel": 80.00,
    "Espuma de afeitar": 110.00,
    "Shampoo": 160.00,
}

DESCUENTO_VIP = 0.15
PRECIO_MEMBRESIA = 500.00


def gestionar_seleccion(opcion, servicios_elegidos):
    """Reglas de unificación y sustitución de combos."""
    seleccion = list(servicios_elegidos)

    if opcion in (1, 2):
        if 3 in seleccion:
            seleccion.remove(3)
        if opcion not in seleccion:
            seleccion.append(opcion)
    elif opcion == 3:
        seleccion = [s for s in seleccion if s not in (1, 2)]
        if 3 not in seleccion:
            seleccion.append(3)
    elif opcion in (4, 5):
        if opcion not in seleccion:
            seleccion.append(opcion)

    # Regla de unificación automática: corte + barba = combo
    if 1 in seleccion and 2 in seleccion:
        seleccion.remove(1)
        seleccion.remove(2)
        seleccion.append(3)

    return seleccion


def calcular_ticket(servicios_elegidos):
    """Devuelve (lista de (nombre, precio), subtotal) de los servicios."""
    ticket, total = [], 0.0
    for s_id in servicios_elegidos:
        nombre, precio = SERVICIOS[s_id]
        ticket.append((nombre, precio))
        total += precio
    return ticket, total


def calcular_total_productos(productos_elegidos):
    """Subtotal de los productos {nombre: cantidad}."""
    return sum(PRODUCTOS[n] * c for n, c in productos_elegidos.items())


def guardar_ticket(cliente, peluquero, ticket, productos_elegidos, datos):
    """Escribe el ticket .txt (mismo formato que el original). Devuelve la ruta."""
    os.makedirs("tickets", exist_ok=True)
    marca = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    ruta = os.path.join("tickets", f"ticket_{cliente.replace(' ', '_')}_{marca}.txt")

    with open(ruta, "w", encoding="utf-8") as f:
        f.write("=============================================\n")
        f.write("             TICKET DE COMPRA                \n")
        f.write("=============================================\n")
        f.write(f"Cliente:   {cliente}\n")
        f.write(f"Atendió:   {peluquero}\n")
        f.write("---------------------------------------------\n")
        f.write("SERVICIOS:\n")
        if ticket:
            for concepto, precio in ticket:
                f.write(f" • {concepto:<30} ${precio:.2f}\n")
        else:
            f.write(" • Sin servicios\n")
        f.write("\nPRODUCTOS:\n")
        if productos_elegidos:
            for nombre, cant in productos_elegidos.items():
                f.write(f" • {cant}x {nombre:<27} ${PRODUCTOS[nombre] * cant:.2f}\n")
        else:
            f.write(" • Sin productos\n")
        f.write("---------------------------------------------\n")
        f.write(f"Subtotal Servicios:                 ${datos['sub_serv']:.2f}\n")
        f.write(f"Subtotal Productos:                 ${datos['sub_prod']:.2f}\n")
        f.write(f"Compra de Membresía VIP:            ${datos['membresia']:.2f}\n")
        f.write(f"Descuento:                          ${datos['descuento']:.2f}\n")
        f.write(f"Propina:                            ${datos['propina']:.2f}\n")
        f.write(f"TOTAL A PAGAR:                      ${datos['total']:.2f}\n")
        f.write(f"Tipo de pago:                       {datos['tipo_pago']}\n")
        f.write(f"Monto pagado:                       ${datos['pagado']:.2f}\n")
        f.write(f"Cambio a devolver:                  ${datos['cambio']:.2f}\n")
        f.write("=============================================\n")
    return ruta


# ==============================================================================
# 3. ALMACÉN DE DATOS EN MEMORIA (compartido entre páginas)
# ==============================================================================
class Datos:
    """Guarda transacciones, citas, clientes e inventario durante la sesión."""

    def __init__(self):
        self.transacciones = []   # dict: fecha, hora, cliente, barbero, concepto, total
        self.citas = []           # dict: fecha, hora, cliente, servicio, barbero
        self.clientes = []        # dict: nombre, telefono, vip
        self.stock = {nombre: 20 for nombre in PRODUCTOS}
        self.barberos = [         # dict: nombre, experiencia
            {"nombre": "Josué", "experiencia": ""},
            {"nombre": "John", "experiencia": ""},
            {"nombre": "Alfredo", "experiencia": ""},
        ]


# ==============================================================================
# 4. COMPONENTES REUTILIZABLES
# ==============================================================================
def fuente(size=14, bold=False):
    return ctk.CTkFont(size=size, weight="bold" if bold else "normal")


def crear_entry(parent, placeholder="", width=200, textvariable=None):
    return ctk.CTkEntry(
        parent, placeholder_text=placeholder, width=width, height=38,
        corner_radius=RADIO_CONTROL, border_width=1, border_color=BORDER,
        fg_color="#FFFFFF", text_color=TEXT, placeholder_text_color=MUTED,
        textvariable=textvariable,
    )


def boton_primario(parent, texto, comando, width=140, height=40):
    return ctk.CTkButton(
        parent, text=texto, command=comando, width=width, height=height,
        corner_radius=RADIO_CONTROL, fg_color=ACCENT, hover_color=ACCENT_HOVER,
        text_color="#FFFFFF", font=fuente(14, True),
    )


def boton_secundario(parent, texto, comando, width=120, height=40):
    return ctk.CTkButton(
        parent, text=texto, command=comando, width=width, height=height,
        corner_radius=RADIO_CONTROL, fg_color="#FFFFFF", hover_color=SOFT,
        text_color=TEXT, border_width=1, border_color=BORDER, font=fuente(14),
    )


def option_menu(parent, valores, width=200):
    return ctk.CTkOptionMenu(
        parent, values=valores, width=width, height=38, corner_radius=RADIO_CONTROL,
        fg_color="#FFFFFF", button_color=SOFT, button_hover_color=BORDER,
        text_color=TEXT, dropdown_fg_color="#FFFFFF", dropdown_text_color=TEXT,
        dropdown_hover_color=SOFT,
    )


def crear_combo(parent, valores, width=200, placeholder="Barbero"):
    """Campo de barbero: se puede escribir un nombre libre o elegir uno existente."""
    combo = ctk.CTkComboBox(
        parent, values=valores or [""], width=width, height=38,
        corner_radius=RADIO_CONTROL, border_width=1, border_color=BORDER,
        fg_color="#FFFFFF", text_color=TEXT, button_color=SOFT, button_hover_color=BORDER,
        dropdown_fg_color="#FFFFFF", dropdown_text_color=TEXT, dropdown_hover_color=SOFT,
    )
    combo.set("")
    return combo


class Tarjeta(ctk.CTkFrame):
    """Contenedor blanco con borde sutil y título opcional."""

    def __init__(self, parent, titulo=None, **kwargs):
        super().__init__(parent, fg_color=CARD, border_width=1, border_color=BORDER,
                         corner_radius=RADIO_TARJETA, **kwargs)
        if titulo:
            ctk.CTkLabel(self, text=titulo, font=fuente(16, True), text_color=TEXT,
                         anchor="w").pack(fill="x", padx=22, pady=(18, 6))


class TarjetaMetrica(Tarjeta):
    """Tarjeta pequeña con un título y un valor grande."""

    def __init__(self, parent, titulo, valor="0"):
        super().__init__(parent)
        ctk.CTkLabel(self, text=titulo, font=fuente(13), text_color=MUTED,
                     anchor="w").pack(fill="x", padx=22, pady=(18, 0))
        self.lbl_valor = ctk.CTkLabel(self, text=valor, font=fuente(28, True),
                                      text_color=TEXT, anchor="w")
        self.lbl_valor.pack(fill="x", padx=22, pady=(2, 18))

    def actualizar(self, valor):
        self.lbl_valor.configure(text=valor)


class Tabla(ctk.CTkFrame):
    """Tabla limpia: encabezado fijo + filas dentro de un CTkScrollableFrame.

    `accion`, si se da, es un dict {"texto": "Editar", "comando": callable(clave)} que
    agrega una columna extra con un botón por fila; se usa junto con `claves` en
    `set_filas` para identificar cada registro. Si no se pasa, la tabla se comporta
    exactamente igual que antes.
    """

    def __init__(self, parent, columnas, pesos=None, altura=260, accion=None):
        super().__init__(parent, fg_color="transparent")
        self.accion = accion
        columnas = list(columnas)
        pesos = list(pesos) if pesos else [1] * len(columnas)
        if accion:
            columnas = columnas + [""]
            pesos = pesos + [1]
        self.columnas = columnas
        self.pesos = pesos

        encabezado = ctk.CTkFrame(self, fg_color=SOFT, corner_radius=8, height=36)
        encabezado.pack(fill="x", padx=(0, 14))
        for i, (col, peso) in enumerate(zip(self.columnas, self.pesos)):
            encabezado.grid_columnconfigure(i, weight=peso, uniform="col")
            ctk.CTkLabel(encabezado, text=col, font=fuente(12, True), text_color=MUTED,
                         anchor="w").grid(row=0, column=i, sticky="ew", padx=12, pady=8)

        self.cuerpo = ctk.CTkScrollableFrame(self, fg_color="transparent", height=altura)
        self.cuerpo.pack(fill="both", expand=True)
        for i, peso in enumerate(self.pesos):
            self.cuerpo.grid_columnconfigure(i, weight=peso, uniform="col")

    def set_filas(self, filas, claves=None):
        for w in self.cuerpo.winfo_children():
            w.destroy()
        if not filas:
            ctk.CTkLabel(self.cuerpo, text="Sin registros todavía", text_color=MUTED,
                         font=fuente(13)).grid(row=0, column=0, columnspan=len(self.columnas),
                                               pady=24)
            return
        for r, fila in enumerate(filas):
            for c, valor in enumerate(fila):
                ctk.CTkLabel(self.cuerpo, text=str(valor), font=fuente(13), text_color=TEXT,
                             anchor="w").grid(row=r * 2, column=c, sticky="ew", padx=12, pady=8)
            if self.accion and claves is not None:
                clave = claves[r]
                ctk.CTkButton(
                    self.cuerpo, text=self.accion.get("texto", "Editar"), width=76, height=28,
                    corner_radius=8, fg_color="#FFFFFF", hover_color=SOFT, text_color=TEXT,
                    border_width=1, border_color=BORDER, font=fuente(12),
                    command=lambda k=clave: self.accion["comando"](k),
                ).grid(row=r * 2, column=len(fila), sticky="w", padx=12, pady=4)
            ctk.CTkFrame(self.cuerpo, height=1, fg_color=BORDER).grid(
                row=r * 2 + 1, column=0, columnspan=len(self.columnas), sticky="ew")


class Sidebar(ctk.CTkFrame):
    """Menú lateral fijo. Llama a `on_navegar(nombre)` al pulsar una opción."""

    OPCIONES = ["Dashboard", "Citas", "Clientes", "Barberos", "Inventario", "Caja / POS"]

    def __init__(self, parent, on_navegar):
        super().__init__(parent, width=230, fg_color=CARD, corner_radius=0,
                         border_width=1, border_color=BORDER)
        self.grid_propagate(False)
        self.on_navegar = on_navegar
        self.botones = {}

        ctk.CTkLabel(self, text="✂  EL PELÓN", font=fuente(20, True),
                     text_color=TEXT).pack(anchor="w", padx=26, pady=(32, 2))
        ctk.CTkLabel(self, text="Barbería · Gestión", font=fuente(12),
                     text_color=MUTED).pack(anchor="w", padx=28, pady=(0, 28))

        for nombre in self.OPCIONES:
            btn = ctk.CTkButton(
                self, text=nombre, anchor="w", height=42, corner_radius=RADIO_CONTROL,
                fg_color="transparent", hover_color=SOFT, text_color=TEXT,
                font=fuente(14), command=lambda n=nombre: self.on_navegar(n),
            )
            btn.pack(fill="x", padx=16, pady=3)
            self.botones[nombre] = btn

        ctk.CTkLabel(self, text="v1.0", font=fuente(11), text_color=MUTED).pack(
            side="bottom", pady=18)

    def marcar_activo(self, nombre):
        for n, btn in self.botones.items():
            if n == nombre:
                btn.configure(fg_color=TEXT, text_color="#FFFFFF", hover_color=TEXT)
            else:
                btn.configure(fg_color="transparent", text_color=TEXT, hover_color=SOFT)


class PaginaBase(ctk.CTkFrame):
    """Página con encabezado (título + subtítulo). `refrescar()` se llama al mostrarla."""

    def __init__(self, parent, datos, titulo, subtitulo=""):
        super().__init__(parent, fg_color=BG, corner_radius=0)
        self.datos = datos
        cab = ctk.CTkFrame(self, fg_color="transparent")
        cab.pack(fill="x", padx=36, pady=(30, 14))
        ctk.CTkLabel(cab, text=titulo, font=fuente(26, True), text_color=TEXT,
                     anchor="w").pack(fill="x")
        if subtitulo:
            ctk.CTkLabel(cab, text=subtitulo, font=fuente(14), text_color=MUTED,
                         anchor="w").pack(fill="x", pady=(2, 0))

    def refrescar(self):
        pass


def dinero(valor):
    return f"${valor:,.2f}"


# ==============================================================================
# 5. PÁGINAS
# ==============================================================================
class PaginaDashboard(PaginaBase):
    def __init__(self, parent, datos):
        super().__init__(parent, datos, "Bienvenido de nuevo 👋",
                         f"Resumen de hoy · {datetime.date.today():%d/%m/%Y}")

        fila = ctk.CTkFrame(self, fg_color="transparent")
        fila.pack(fill="x", padx=36)
        self.metricas = {}
        for i, (clave, titulo) in enumerate([
            ("citas", "Citas del día"), ("ingresos", "Ingresos del día"),
            ("ventas", "Ventas realizadas"), ("promedio", "Ticket promedio"),
        ]):
            fila.grid_columnconfigure(i, weight=1, uniform="m")
            m = TarjetaMetrica(fila, titulo)
            m.grid(row=0, column=i, sticky="ew", padx=(0 if i == 0 else 8, 0 if i == 3 else 8))
            self.metricas[clave] = m

        tarjeta = Tarjeta(self, "Transacciones recientes")
        tarjeta.pack(fill="both", expand=True, padx=36, pady=22)
        self.tabla = Tabla(tarjeta, ["Hora", "Cliente", "Atendió", "Concepto", "Total"],
                           pesos=[1, 2, 2, 4, 1])
        self.tabla.pack(fill="both", expand=True, padx=18, pady=(0, 18))

    def refrescar(self):
        hoy = datetime.date.today()
        citas_hoy = [c for c in self.datos.citas if c["fecha"] == hoy]
        ventas_hoy = [t for t in self.datos.transacciones if t["fecha"] == hoy]
        ingresos = sum(t["total"] for t in ventas_hoy)
        promedio = ingresos / len(ventas_hoy) if ventas_hoy else 0

        self.metricas["citas"].actualizar(str(len(citas_hoy)))
        self.metricas["ingresos"].actualizar(dinero(ingresos))
        self.metricas["ventas"].actualizar(str(len(ventas_hoy)))
        self.metricas["promedio"].actualizar(dinero(promedio))

        recientes = list(reversed(self.datos.transacciones))[:15]
        self.tabla.set_filas([
            (t["hora"], t["cliente"], t["barbero"], t["concepto"], dinero(t["total"]))
            for t in recientes
        ])


class PaginaCitas(PaginaBase):
    def __init__(self, parent, datos):
        super().__init__(parent, datos, "Citas", "Agenda del día")

        form = Tarjeta(self, "Nueva cita")
        form.pack(fill="x", padx=36)
        fila = ctk.CTkFrame(form, fg_color="transparent")
        fila.pack(fill="x", padx=22, pady=(0, 20))
        self.e_cliente = crear_entry(fila, "Cliente", 200)
        self.e_hora = crear_entry(fila, "Hora (HH:MM)", 120)
        self.m_servicio = option_menu(fila, [s[0] for s in SERVICIOS.values()], 260)
        self.m_barbero = crear_combo(fila, [b["nombre"] for b in datos.barberos], 170)
        for w in (self.e_cliente, self.e_hora, self.m_servicio, self.m_barbero):
            w.pack(side="left", padx=(0, 10))
        boton_primario(fila, "Agendar", self._agendar, 110).pack(side="left")

        tarjeta = Tarjeta(self, "Citas de hoy")
        tarjeta.pack(fill="both", expand=True, padx=36, pady=22)
        self.tabla = Tabla(tarjeta, ["Hora", "Cliente", "Servicio", "Barbero"],
                           pesos=[1, 2, 4, 2])
        self.tabla.pack(fill="both", expand=True, padx=18, pady=(0, 18))

    def _agendar(self):
        cliente, hora = self.e_cliente.get().strip(), self.e_hora.get().strip()
        barbero = self.m_barbero.get().strip()
        if not cliente or not barbero:
            messagebox.showwarning("Datos incompletos", "Ingresa cliente y barbero.")
            return
        try:
            datetime.datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showwarning("Hora inválida", "Usa el formato HH:MM (ej. 14:30).")
            return
        self.datos.citas.append({
            "fecha": datetime.date.today(), "hora": hora, "cliente": cliente,
            "servicio": self.m_servicio.get(), "barbero": barbero,
        })
        for e in (self.e_cliente, self.e_hora):
            e.delete(0, "end")
        self.m_barbero.set("")
        self.refrescar()

    def actualizar_barberos(self, nombres):
        """Actualiza las opciones del combo de barbero sin borrar lo ya escrito."""
        self.m_barbero.configure(values=nombres or [""])

    def refrescar(self):
        hoy = datetime.date.today()
        citas = sorted((c for c in self.datos.citas if c["fecha"] == hoy),
                       key=lambda c: c["hora"])
        self.tabla.set_filas([(c["hora"], c["cliente"], c["servicio"], c["barbero"])
                              for c in citas])


class PaginaClientes(PaginaBase):
    def __init__(self, parent, datos):
        super().__init__(parent, datos, "Clientes", "Directorio y membresías VIP")

        form = Tarjeta(self, "Nuevo cliente")
        form.pack(fill="x", padx=36)
        fila = ctk.CTkFrame(form, fg_color="transparent")
        fila.pack(fill="x", padx=22, pady=(0, 20))
        self.e_nombre = crear_entry(fila, "Nombre completo", 260)
        self.e_tel = crear_entry(fila, "Teléfono", 180)
        self.chk_vip = ctk.CTkCheckBox(fila, text="Membresía VIP", text_color=TEXT,
                                       fg_color=ACCENT, hover_color=ACCENT_HOVER,
                                       border_color=BORDER, corner_radius=6)
        for w in (self.e_nombre, self.e_tel):
            w.pack(side="left", padx=(0, 10))
        self.chk_vip.pack(side="left", padx=(6, 14))
        boton_primario(fila, "Guardar", self._guardar, 110).pack(side="left")

        tarjeta = Tarjeta(self, "Lista de clientes")
        tarjeta.pack(fill="both", expand=True, padx=36, pady=22)
        self.tabla = Tabla(tarjeta, ["Nombre", "Teléfono", "Membresía"], pesos=[3, 2, 1])
        self.tabla.pack(fill="both", expand=True, padx=18, pady=(0, 18))

    def _guardar(self):
        nombre = self.e_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Datos incompletos", "El nombre no puede estar vacío.")
            return
        self.datos.clientes.append({
            "nombre": nombre, "telefono": self.e_tel.get().strip() or "—",
            "vip": bool(self.chk_vip.get()),
        })
        self.e_nombre.delete(0, "end")
        self.e_tel.delete(0, "end")
        self.chk_vip.deselect()
        self.refrescar()

    def refrescar(self):
        self.tabla.set_filas([
            (c["nombre"], c["telefono"], "VIP" if c["vip"] else "Regular")
            for c in self.datos.clientes
        ])


class PaginaBarberos(PaginaBase):
    """Equipo de barberos: alta, edición, baja y citas del día por barbero."""

    def __init__(self, parent, datos, on_cambio_barberos=None):
        super().__init__(parent, datos, "Barberos", "Equipo y citas del día")
        self.on_cambio_barberos = on_cambio_barberos

        form = Tarjeta(self, "Nuevo barbero")
        form.pack(fill="x", padx=36)
        fila = ctk.CTkFrame(form, fg_color="transparent")
        fila.pack(fill="x", padx=22, pady=(0, 20))
        self.e_nombre = crear_entry(fila, "Nombre completo", 220)
        self.e_experiencia = crear_entry(fila, "Experiencia (ej. 3 años)", 220)
        self.e_nombre.pack(side="left", padx=(0, 10))
        self.e_experiencia.pack(side="left", padx=(0, 10))
        boton_primario(fila, "Guardar", self._guardar, 120).pack(side="left")

        tarjeta = Tarjeta(self, "Equipo de barberos")
        tarjeta.pack(fill="both", expand=True, padx=36, pady=22)
        self.tabla = Tabla(tarjeta, ["Nombre", "Experiencia", "Citas hoy"], pesos=[2, 3, 1],
                           accion={"texto": "Editar", "comando": self._editar_barbero})
        self.tabla.pack(fill="both", expand=True, padx=18, pady=(0, 18))

    def _avisar_cambio(self):
        if self.on_cambio_barberos:
            self.on_cambio_barberos()

    def _guardar(self):
        nombre = self.e_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Datos incompletos", "El nombre no puede estar vacío.")
            return
        if any(b["nombre"].lower() == nombre.lower() for b in self.datos.barberos):
            messagebox.showwarning("Barbero duplicado", "Ya existe un barbero con ese nombre.")
            return
        self.datos.barberos.append({
            "nombre": nombre, "experiencia": self.e_experiencia.get().strip(),
        })
        self.e_nombre.delete(0, "end")
        self.e_experiencia.delete(0, "end")
        self.refrescar()
        self._avisar_cambio()

    def _editar_barbero(self, nombre_actual):
        """Ventana emergente para renombrar, cambiar la experiencia o eliminar un barbero."""
        barbero = next((b for b in self.datos.barberos if b["nombre"] == nombre_actual), None)
        if barbero is None:
            return

        ventana = ctk.CTkToplevel(self)
        ventana.title("Editar barbero")
        ventana.geometry("360x420")
        ventana.resizable(False, False)
        ventana.configure(fg_color=BG)
        ventana.transient(self.winfo_toplevel())
        ventana.grab_set()

        tarjeta = ctk.CTkFrame(ventana, fg_color=CARD, corner_radius=RADIO_TARJETA,
                               border_width=1, border_color=BORDER)
        tarjeta.pack(fill="both", expand=True, padx=18, pady=18)

        ctk.CTkLabel(tarjeta, text="✏️  Editar barbero", font=fuente(16, True),
                     text_color=TEXT).pack(pady=(22, 4))
        ctk.CTkLabel(tarjeta, text=f"Editando: {barbero['nombre']}", font=fuente(12),
                     text_color=MUTED, wraplength=280).pack(pady=(0, 16))

        e_nombre = crear_entry(tarjeta, "Nombre completo", width=260)
        e_nombre.insert(0, barbero["nombre"])
        e_nombre.pack(pady=6)
        e_experiencia = crear_entry(tarjeta, "Experiencia", width=260)
        e_experiencia.insert(0, barbero["experiencia"])
        e_experiencia.pack(pady=6)

        lbl_error = ctk.CTkLabel(tarjeta, text="", font=fuente(12), text_color=DANGER,
                                 wraplength=260)
        lbl_error.pack(pady=(4, 4))

        def _guardar_cambios():
            nuevo_nombre = e_nombre.get().strip()
            if not nuevo_nombre:
                lbl_error.configure(text="El nombre no puede estar vacío.")
                return
            choque = any(b["nombre"].lower() == nuevo_nombre.lower() and b is not barbero
                        for b in self.datos.barberos)
            if choque:
                lbl_error.configure(text="Ya existe otro barbero con ese nombre.")
                return
            barbero["nombre"] = nuevo_nombre
            barbero["experiencia"] = e_experiencia.get().strip()
            self.refrescar()
            self._avisar_cambio()
            ventana.destroy()
            messagebox.showinfo("Barbero actualizado", f"'{nuevo_nombre}' se actualizó con éxito.")

        def _eliminar_barbero():
            if not messagebox.askyesno(
                    "Eliminar barbero",
                    f"¿Seguro que quieres eliminar a '{barbero['nombre']}' del equipo?"):
                return
            self.datos.barberos.remove(barbero)
            self.refrescar()
            self._avisar_cambio()
            ventana.destroy()
            messagebox.showinfo("Barbero eliminado", f"'{nombre_actual}' se eliminó del equipo.")

        fila_botones = ctk.CTkFrame(tarjeta, fg_color="transparent")
        fila_botones.pack(pady=(6, 18))
        boton_primario(fila_botones, "Guardar cambios", _guardar_cambios,
                       width=160).pack(side="left", padx=(0, 8))
        ctk.CTkButton(fila_botones, text="Eliminar", command=_eliminar_barbero,
                     width=90, height=40, corner_radius=RADIO_CONTROL, fg_color=DANGER,
                     hover_color=DANGER_HOVER, text_color="#FFFFFF",
                     font=fuente(14, True)).pack(side="left")
        e_nombre.focus()

    def refrescar(self):
        hoy = datetime.date.today()
        filas, claves = [], []
        for b in self.datos.barberos:
            citas_hoy = sum(1 for c in self.datos.citas
                            if c["fecha"] == hoy and c["barbero"] == b["nombre"])
            filas.append((b["nombre"], b["experiencia"] or "—", citas_hoy))
            claves.append(b["nombre"])
        self.tabla.set_filas(filas, claves=claves)


class PaginaInventario(PaginaBase):
    def __init__(self, parent, datos, on_cambio_productos=None):
        super().__init__(parent, datos, "Inventario", "Existencias de productos")
        self.on_cambio_productos = on_cambio_productos

        form = Tarjeta(self, "Reabastecer")
        form.pack(fill="x", padx=36)
        fila = ctk.CTkFrame(form, fg_color="transparent")
        fila.pack(fill="x", padx=22, pady=(0, 20))
        self.m_producto = option_menu(fila, list(PRODUCTOS.keys()), 220)
        self.e_cant = crear_entry(fila, "Cantidad", 120)
        self.m_producto.pack(side="left", padx=(0, 10))
        self.e_cant.pack(side="left", padx=(0, 10))
        boton_primario(fila, "Agregar stock", self._agregar, 140).pack(side="left", padx=(0, 10))
        boton_secundario(fila, "+  Nuevo producto", self._abrir_nuevo_producto, 170).pack(side="left")

        tarjeta = Tarjeta(self, "Productos")
        tarjeta.pack(fill="both", expand=True, padx=36, pady=22)
        self.tabla = Tabla(tarjeta, ["Producto", "Precio", "Stock"], pesos=[3, 1, 1],
                           accion={"texto": "Editar", "comando": self._editar_producto})
        self.tabla.pack(fill="both", expand=True, padx=18, pady=(0, 18))

    def _agregar(self):
        producto = self.m_producto.get()
        if producto not in PRODUCTOS:
            messagebox.showwarning("Sin productos", "Agrega primero un producto al catálogo.")
            return
        try:
            cant = int(self.e_cant.get())
            if cant <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Cantidad inválida", "Ingresa un entero positivo.")
            return
        self.datos.stock[producto] += cant
        self.e_cant.delete(0, "end")
        self.refrescar()

    def _avisar_cambio_catalogo(self):
        if self.on_cambio_productos:
            self.on_cambio_productos()

    def _abrir_nuevo_producto(self):
        """Ventana emergente para dar de alta un producto que no existe en el catálogo."""
        ventana = ctk.CTkToplevel(self)
        ventana.title("Nuevo producto")
        ventana.geometry("360x360")
        ventana.resizable(False, False)
        ventana.configure(fg_color=BG)
        ventana.transient(self.winfo_toplevel())
        ventana.grab_set()

        tarjeta = ctk.CTkFrame(ventana, fg_color=CARD, corner_radius=RADIO_TARJETA,
                               border_width=1, border_color=BORDER)
        tarjeta.pack(fill="both", expand=True, padx=18, pady=18)

        ctk.CTkLabel(tarjeta, text="➕ Agregar producto nuevo", font=fuente(16, True),
                     text_color=TEXT).pack(pady=(22, 4))
        ctk.CTkLabel(tarjeta, text="Para artículos que aún no están en el catálogo",
                     font=fuente(12), text_color=MUTED, wraplength=280).pack(pady=(0, 16))

        e_nombre = crear_entry(tarjeta, "Nombre del producto", width=260)
        e_nombre.pack(pady=6)
        e_precio = crear_entry(tarjeta, "Precio (ej. 150.00)", width=260)
        e_precio.pack(pady=6)
        e_stock = crear_entry(tarjeta, "Stock inicial (opcional)", width=260)
        e_stock.pack(pady=6)

        lbl_error = ctk.CTkLabel(tarjeta, text="", font=fuente(12), text_color=DANGER,
                                 wraplength=260)
        lbl_error.pack(pady=(4, 4))

        def _guardar_producto():
            nombre = e_nombre.get().strip()
            if not nombre:
                lbl_error.configure(text="El nombre del producto no puede estar vacío.")
                return
            if nombre.lower() in {n.lower() for n in PRODUCTOS}:
                lbl_error.configure(text="Ese producto ya existe en el catálogo.")
                return
            try:
                precio = float(e_precio.get())
                if precio <= 0:
                    raise ValueError
            except ValueError:
                lbl_error.configure(text="Ingresa un precio válido mayor a 0.")
                return
            texto_stock = e_stock.get().strip()
            try:
                stock_inicial = int(texto_stock) if texto_stock else 0
                if stock_inicial < 0:
                    raise ValueError
            except ValueError:
                lbl_error.configure(text="El stock inicial debe ser un entero mayor o igual a 0.")
                return

            PRODUCTOS[nombre] = precio
            self.datos.stock[nombre] = stock_inicial
            self.m_producto.configure(values=list(PRODUCTOS.keys()))
            self.m_producto.set(nombre)
            self.refrescar()
            self._avisar_cambio_catalogo()
            ventana.destroy()
            messagebox.showinfo("Producto agregado",
                                f"'{nombre}' se agregó al catálogo con éxito.")

        boton_primario(tarjeta, "Agregar", _guardar_producto, width=260).pack(pady=(6, 18))
        e_nombre.focus()

    def _editar_producto(self, nombre_actual):
        """Ventana emergente para renombrar, cambiar el precio o eliminar un producto."""
        ventana = ctk.CTkToplevel(self)
        ventana.title("Editar producto")
        ventana.geometry("360x420")
        ventana.resizable(False, False)
        ventana.configure(fg_color=BG)
        ventana.transient(self.winfo_toplevel())
        ventana.grab_set()

        tarjeta = ctk.CTkFrame(ventana, fg_color=CARD, corner_radius=RADIO_TARJETA,
                               border_width=1, border_color=BORDER)
        tarjeta.pack(fill="both", expand=True, padx=18, pady=18)

        ctk.CTkLabel(tarjeta, text="✏️  Editar producto", font=fuente(16, True),
                     text_color=TEXT).pack(pady=(22, 4))
        ctk.CTkLabel(tarjeta, text=f"Editando: {nombre_actual}", font=fuente(12),
                     text_color=MUTED, wraplength=280).pack(pady=(0, 16))

        e_nombre = crear_entry(tarjeta, "Nombre del producto", width=260)
        e_nombre.insert(0, nombre_actual)
        e_nombre.pack(pady=6)
        e_precio = crear_entry(tarjeta, "Precio", width=260)
        e_precio.insert(0, f"{PRODUCTOS[nombre_actual]:.2f}")
        e_precio.pack(pady=6)

        lbl_error = ctk.CTkLabel(tarjeta, text="", font=fuente(12), text_color=DANGER,
                                 wraplength=260)
        lbl_error.pack(pady=(4, 4))

        def _seleccionar_producto_restante():
            valores = list(PRODUCTOS.keys())
            self.m_producto.configure(values=valores or ["Sin productos"])
            self.m_producto.set(valores[0] if valores else "Sin productos")

        def _guardar_cambios():
            nuevo_nombre = e_nombre.get().strip()
            if not nuevo_nombre:
                lbl_error.configure(text="El nombre del producto no puede estar vacío.")
                return
            choque = any(n.lower() == nuevo_nombre.lower() and n != nombre_actual
                        for n in PRODUCTOS)
            if choque:
                lbl_error.configure(text="Ya existe otro producto con ese nombre.")
                return
            try:
                nuevo_precio = float(e_precio.get())
                if nuevo_precio <= 0:
                    raise ValueError
            except ValueError:
                lbl_error.configure(text="Ingresa un precio válido mayor a 0.")
                return

            stock_actual = self.datos.stock.get(nombre_actual, 0)
            if nuevo_nombre != nombre_actual:
                PRODUCTOS.pop(nombre_actual, None)
                self.datos.stock.pop(nombre_actual, None)
            PRODUCTOS[nuevo_nombre] = nuevo_precio
            self.datos.stock[nuevo_nombre] = stock_actual
            _seleccionar_producto_restante()
            self.refrescar()
            self._avisar_cambio_catalogo()
            ventana.destroy()
            messagebox.showinfo("Producto actualizado",
                                f"'{nuevo_nombre}' se actualizó con éxito.")

        def _eliminar_producto():
            if not messagebox.askyesno(
                    "Eliminar producto",
                    f"¿Seguro que quieres eliminar '{nombre_actual}' del catálogo?"):
                return
            PRODUCTOS.pop(nombre_actual, None)
            self.datos.stock.pop(nombre_actual, None)
            _seleccionar_producto_restante()
            self.refrescar()
            self._avisar_cambio_catalogo()
            ventana.destroy()
            messagebox.showinfo("Producto eliminado",
                                f"'{nombre_actual}' se eliminó del catálogo.")

        fila_botones = ctk.CTkFrame(tarjeta, fg_color="transparent")
        fila_botones.pack(pady=(6, 18))
        boton_primario(fila_botones, "Guardar cambios", _guardar_cambios,
                       width=160).pack(side="left", padx=(0, 8))
        ctk.CTkButton(fila_botones, text="Eliminar", command=_eliminar_producto,
                     width=90, height=40, corner_radius=RADIO_CONTROL, fg_color=DANGER,
                     hover_color=DANGER_HOVER, text_color="#FFFFFF",
                     font=fuente(14, True)).pack(side="left")
        e_nombre.focus()

    def refrescar(self):
        productos = list(PRODUCTOS.items())
        self.tabla.set_filas(
            [(n, dinero(p), self.datos.stock.get(n, 0)) for n, p in productos],
            claves=[n for n, _ in productos],
        )


class PaginaCaja(PaginaBase):
    """Punto de venta: replica el flujo completo de proyecto.py en una sola pantalla."""

    SIN_VIP, YA_VIP, COMPRAR_VIP = "Sin membresía", "Ya es VIP", f"Comprar VIP (${PRECIO_MEMBRESIA:.0f})"

    def __init__(self, parent, datos, on_venta):
        super().__init__(parent, datos, "Caja / POS", "Registra servicios y productos, y cobra")
        self.on_venta = on_venta
        self.servicios_elegidos = []
        self.productos_elegidos = {}
        self.btn_servicio = {}
        self.lbl_cant, self.lbl_stock = {}, {}

        cuerpo = ctk.CTkFrame(self, fg_color="transparent")
        cuerpo.pack(fill="both", expand=True, padx=36, pady=(0, 24))
        cuerpo.grid_columnconfigure(0, weight=3, uniform="c")
        cuerpo.grid_columnconfigure(1, weight=2, uniform="c")
        cuerpo.grid_rowconfigure(0, weight=1)

        izq = ctk.CTkScrollableFrame(cuerpo, fg_color="transparent")
        izq.grid(row=0, column=0, sticky="nsew", padx=(0, 12))
        der = ctk.CTkScrollableFrame(cuerpo, fg_color="transparent")
        der.grid(row=0, column=1, sticky="nsew", padx=(12, 0))

        self._construir_izquierda(izq)
        self._construir_resumen(der)
        self._recalcular()

    # ---------- Columna izquierda: datos, servicios y productos ----------
    def _construir_izquierda(self, padre):
        t = Tarjeta(padre, "Atención")
        t.pack(fill="x", pady=(0, 14))
        fila = ctk.CTkFrame(t, fg_color="transparent")
        fila.pack(fill="x", padx=22, pady=(0, 20))
        self.e_cliente = crear_entry(fila, "Nombre del cliente", 220)
        self.m_barbero = crear_combo(fila, [b["nombre"] for b in self.datos.barberos], 220)
        self.e_cliente.pack(side="left", padx=(0, 10))
        self.m_barbero.pack(side="left")

        t = Tarjeta(padre, "Servicios")
        t.pack(fill="x", pady=(0, 14))
        grid = ctk.CTkFrame(t, fg_color="transparent")
        grid.pack(fill="x", padx=22, pady=(0, 20))
        grid.grid_columnconfigure((0, 1), weight=1, uniform="s")
        for i, (s_id, (nombre, precio)) in enumerate(SERVICIOS.items()):
            btn = ctk.CTkButton(
                grid, text=f"{nombre}\n{dinero(precio)}", height=62,
                corner_radius=RADIO_CONTROL, border_width=1, font=fuente(13),
                command=lambda s=s_id: self._toggle_servicio(s),
            )
            btn.grid(row=i // 2, column=i % 2, sticky="ew", padx=4, pady=4)
            self.btn_servicio[s_id] = btn
        self._pintar_servicios()

        self.tarjeta_productos = Tarjeta(padre, "Productos")
        self.tarjeta_productos.pack(fill="x")
        self.lista_productos = ctk.CTkFrame(self.tarjeta_productos, fg_color="transparent")
        self.lista_productos.pack(fill="x", padx=22, pady=(0, 18))
        self.lista_productos.grid_columnconfigure(0, weight=1)
        self._dibujar_productos()

    def _dibujar_productos(self):
        """(Re)pinta la lista de productos de la caja a partir del catálogo actual."""
        for w in self.lista_productos.winfo_children():
            w.destroy()
        self.lbl_cant, self.lbl_stock = {}, {}
        for r, (nombre, precio) in enumerate(PRODUCTOS.items()):
            ctk.CTkLabel(self.lista_productos, text=nombre, font=fuente(14), text_color=TEXT,
                         anchor="w").grid(row=r, column=0, sticky="w", pady=6)
            ctk.CTkLabel(self.lista_productos, text=dinero(precio), font=fuente(13),
                         text_color=MUTED, width=70).grid(row=r, column=1, padx=6)
            self.lbl_stock[nombre] = ctk.CTkLabel(self.lista_productos, text="", font=fuente(12),
                                                  text_color=MUTED, width=80)
            self.lbl_stock[nombre].grid(row=r, column=2, padx=6)
            for col, (txt, delta, color, hover) in zip(
                    (3, 5), (("−", -1, DANGER, DANGER_HOVER), ("+", 1, ACCENT, ACCENT_HOVER))):
                ctk.CTkButton(
                    self.lista_productos, text=txt, width=32, height=32, corner_radius=8,
                    fg_color=color, hover_color=hover, text_color="#FFFFFF", font=fuente(16, True),
                    command=lambda n=nombre, d=delta: self._cambiar_producto(n, d),
                ).grid(row=r, column=col, padx=2)
            self.lbl_cant[nombre] = ctk.CTkLabel(self.lista_productos, text="0", width=30,
                                                 font=fuente(14, True), text_color=TEXT)
            self.lbl_cant[nombre].grid(row=r, column=4)

    def actualizar_catalogo(self):
        """Se llama desde Inventario cuando se agrega, edita o elimina un producto."""
        self.productos_elegidos = {n: c for n, c in self.productos_elegidos.items()
                                   if n in PRODUCTOS}
        self._dibujar_productos()
        self.refrescar()
        self._recalcular()

    def actualizar_barberos(self, nombres):
        """Actualiza las opciones del combo de barbero sin borrar lo ya escrito."""
        self.m_barbero.configure(values=nombres or [""])

    # ---------- Columna derecha: resumen y cobro ----------
    def _construir_resumen(self, padre):
        t = Tarjeta(padre, "Resumen de venta")
        t.pack(fill="x")
        cont = ctk.CTkFrame(t, fg_color="transparent")
        cont.pack(fill="x", padx=22, pady=(0, 20))

        self.lbl = {}

        def fila(clave, texto, negrita=False):
            f = ctk.CTkFrame(cont, fg_color="transparent")
            f.pack(fill="x", pady=2)
            ctk.CTkLabel(f, text=texto, font=fuente(13), text_color=MUTED).pack(side="left")
            self.lbl[clave] = ctk.CTkLabel(f, text="$0.00", font=fuente(13, negrita),
                                           text_color=TEXT)
            self.lbl[clave].pack(side="right")

        def titulo(texto):
            ctk.CTkLabel(cont, text=texto, font=fuente(12, True), text_color=MUTED,
                         anchor="w").pack(fill="x", pady=(14, 4))

        fila("serv", "Subtotal servicios")
        fila("prod", "Subtotal productos")

        titulo("MEMBRESÍA VIP (15% de descuento)")
        self.seg_vip = ctk.CTkSegmentedButton(
            cont, values=[self.SIN_VIP, self.YA_VIP, self.COMPRAR_VIP], command=lambda _: self._recalcular(),
            selected_color=SELECCION, selected_hover_color=SELECCION, unselected_color=SOFT,
            unselected_hover_color=BORDER, text_color=TEXT, corner_radius=RADIO_CONTROL,
        )
        self.seg_vip.set(self.SIN_VIP)
        self.seg_vip.pack(fill="x")

        fila("memb", "Compra de membresía")
        fila("desc", "Descuento")

        titulo("PROPINA")
        self.var_propina = ctk.StringVar()
        self.var_propina.trace_add("write", lambda *_: self._recalcular())
        crear_entry(cont, "$0.00", 200, self.var_propina).pack(fill="x")

        ctk.CTkFrame(cont, height=1, fg_color=BORDER).pack(fill="x", pady=14)
        f = ctk.CTkFrame(cont, fg_color="transparent")
        f.pack(fill="x")
        ctk.CTkLabel(f, text="TOTAL", font=fuente(14, True), text_color=TEXT).pack(side="left")
        self.lbl["total"] = ctk.CTkLabel(f, text="$0.00", font=fuente(26, True), text_color=ACCENT)
        self.lbl["total"].pack(side="right")

        titulo("TIPO DE PAGO")
        self.seg_pago = ctk.CTkSegmentedButton(
            cont, values=["Efectivo", "Tarjeta", "Transferencia"], command=self._cambio_pago,
            selected_color=SELECCION, selected_hover_color=SELECCION, unselected_color=SOFT,
            unselected_hover_color=BORDER, text_color=TEXT, corner_radius=RADIO_CONTROL,
        )
        self.seg_pago.set("Efectivo")
        self.seg_pago.pack(fill="x")

        self.var_recibido = ctk.StringVar()
        self.var_recibido.trace_add("write", lambda *_: self._recalcular())
        self.e_recibido = crear_entry(cont, "Monto recibido", 200, self.var_recibido)
        self.e_recibido.pack(fill="x", pady=(10, 0))
        fila("cambio", "Cambio a devolver")

        boton_primario(cont, "Cobrar", self._cobrar, height=48).pack(fill="x", pady=(18, 8))
        ctk.CTkButton(cont, text="Limpiar venta", command=self._limpiar, height=40,
                      corner_radius=RADIO_CONTROL, fg_color=DANGER, hover_color=DANGER_HOVER,
                      text_color="#FFFFFF", font=fuente(14)).pack(fill="x")

    # ---------- Interacciones ----------
    def _toggle_servicio(self, s_id):
        if s_id in self.servicios_elegidos:            # segundo clic = quitar
            self.servicios_elegidos.remove(s_id)
        else:                                          # reglas de combos del backend
            self.servicios_elegidos = gestionar_seleccion(s_id, self.servicios_elegidos)
        self._pintar_servicios()
        self._recalcular()

    def _pintar_servicios(self):
        for s_id, btn in self.btn_servicio.items():
            if s_id in self.servicios_elegidos:
                btn.configure(fg_color=ACCENT, hover_color=ACCENT_HOVER,
                              text_color="#FFFFFF", border_color=ACCENT)
            else:
                btn.configure(fg_color="#FFFFFF", hover_color=SOFT,
                              text_color=TEXT, border_color=BORDER)

    def _cambiar_producto(self, nombre, delta):
        nuevo = self.productos_elegidos.get(nombre, 0) + delta
        if nuevo < 0:
            return
        if nuevo > self.datos.stock[nombre]:
            messagebox.showinfo("Sin existencias", f"No hay más {nombre} en inventario.")
            return
        if nuevo == 0:
            self.productos_elegidos.pop(nombre, None)
        else:
            self.productos_elegidos[nombre] = nuevo
        self.lbl_cant[nombre].configure(text=str(nuevo))
        self._recalcular()

    def _cambio_pago(self, _valor=None):
        efectivo = self.seg_pago.get() == "Efectivo"
        self.e_recibido.configure(state="normal" if efectivo else "disabled")
        self._recalcular()

    def _leer_propina(self):
        """Igual que el original: inválido o negativo se toma como $0."""
        try:
            return max(0.0, float(self.var_propina.get() or 0))
        except ValueError:
            return 0.0

    def _calcular(self):
        _, sub_serv = calcular_ticket(self.servicios_elegidos)
        sub_prod = calcular_total_productos(self.productos_elegidos)
        base = sub_serv + sub_prod
        modo = self.seg_vip.get()
        descuento = DESCUENTO_VIP * base if modo != self.SIN_VIP else 0.0
        membresia = PRECIO_MEMBRESIA if modo == self.COMPRAR_VIP else 0.0
        propina = self._leer_propina()
        total = base - descuento + membresia + propina
        return dict(sub_serv=sub_serv, sub_prod=sub_prod, base=base, descuento=descuento,
                    membresia=membresia, propina=propina, total=total)

    def _recalcular(self):
        d = self._calcular()
        self.lbl["serv"].configure(text=dinero(d["sub_serv"]))
        self.lbl["prod"].configure(text=dinero(d["sub_prod"]))
        self.lbl["memb"].configure(text=dinero(d["membresia"]))
        self.lbl["desc"].configure(text=f"− {dinero(d['descuento'])}")
        self.lbl["total"].configure(text=dinero(d["total"]))
        cambio = 0.0
        if self.seg_pago.get() == "Efectivo":
            try:
                cambio = max(0.0, float(self.var_recibido.get()) - d["total"])
            except ValueError:
                pass
        self.lbl["cambio"].configure(text=dinero(cambio))

    def _cobrar(self):
        cliente, barbero = self.e_cliente.get().strip(), self.m_barbero.get().strip()
        if not cliente or not barbero:
            messagebox.showwarning("Datos incompletos",
                                   "Ingresa el nombre del cliente y del peluquero.")
            return
        d = self._calcular()
        if d["base"] == 0 and d["membresia"] == 0:
            messagebox.showwarning("Venta vacía",
                                   "No se seleccionó ningún servicio, producto ni membresía.")
            return

        efectivo = self.seg_pago.get() == "Efectivo"
        if efectivo:
            try:
                pagado = float(self.var_recibido.get())
            except ValueError:
                messagebox.showwarning("Monto inválido", "Ingresa el monto recibido en efectivo.")
                return
            if pagado < d["total"]:
                messagebox.showwarning("Monto insuficiente",
                                       f"Ingresa un monto igual o mayor a {dinero(d['total'])}.")
                return
        else:
            pagado = d["total"]
        cambio = pagado - d["total"]

        d.update(tipo_pago=self.seg_pago.get(), pagado=pagado, cambio=cambio)
        ticket, _ = calcular_ticket(self.servicios_elegidos)
        ruta = guardar_ticket(cliente, barbero, ticket, self.productos_elegidos, d)

        # Actualiza inventario y registra la transacción
        for nombre, cant in self.productos_elegidos.items():
            self.datos.stock[nombre] -= cant
        conceptos = [n for n, _ in ticket] + [f"{c}x {n}" for n, c in self.productos_elegidos.items()]
        if d["membresia"]:
            conceptos.append("Membresía VIP")
            self.datos.clientes.append({"nombre": cliente, "telefono": "—", "vip": True})
        ahora = datetime.datetime.now()
        self.datos.transacciones.append({
            "fecha": ahora.date(), "hora": ahora.strftime("%H:%M"), "cliente": cliente,
            "barbero": barbero, "concepto": ", ".join(conceptos), "total": d["total"],
        })

        messagebox.showinfo("Venta registrada",
                            f"Total: {dinero(d['total'])}\nCambio: {dinero(cambio)}\n\n"
                            f"Ticket guardado en:\n{ruta}")
        self._limpiar()
        self.on_venta()

    def _limpiar(self):
        self.servicios_elegidos = []
        self.productos_elegidos = {}
        self.e_cliente.delete(0, "end")
        self.m_barbero.set("")
        self.var_propina.set("")
        self.var_recibido.set("")
        self.seg_vip.set(self.SIN_VIP)
        self.seg_pago.set("Efectivo")
        self._cambio_pago()
        for n in PRODUCTOS:
            self.lbl_cant[n].configure(text="0")
        self._pintar_servicios()
        self.refrescar()
        self._recalcular()

    def refrescar(self):
        for nombre, lbl in self.lbl_stock.items():
            lbl.configure(text=f"Stock: {self.datos.stock[nombre]}")


# ==============================================================================
# 6. VENTANA PRINCIPAL
# ==============================================================================
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Barbería El Pelón · Sistema de gestión")
        self.geometry("1280x780")
        self.minsize(1080, 680)
        self.configure(fg_color=BG)

        self.datos = Datos()

        # Layout de dos columnas: sidebar fijo + contenido amplio
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = Sidebar(self, self.mostrar)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.contenedor = ctk.CTkFrame(self, fg_color=BG, corner_radius=0)
        self.contenedor.grid(row=0, column=1, sticky="nsew")
        self.contenedor.grid_columnconfigure(0, weight=1)
        self.contenedor.grid_rowconfigure(0, weight=1)

        pagina_citas = PaginaCitas(self.contenedor, self.datos)
        pagina_caja = PaginaCaja(self.contenedor, self.datos,
                                 on_venta=lambda: self.mostrar("Dashboard"))

        def _actualizar_barberos_en_selectores():
            nombres = [b["nombre"] for b in self.datos.barberos]
            pagina_citas.actualizar_barberos(nombres)
            pagina_caja.actualizar_barberos(nombres)

        self.paginas = {
            "Dashboard": PaginaDashboard(self.contenedor, self.datos),
            "Citas": pagina_citas,
            "Clientes": PaginaClientes(self.contenedor, self.datos),
            "Barberos": PaginaBarberos(self.contenedor, self.datos,
                                       on_cambio_barberos=_actualizar_barberos_en_selectores),
            "Inventario": PaginaInventario(self.contenedor, self.datos,
                                           on_cambio_productos=pagina_caja.actualizar_catalogo),
            "Caja / POS": pagina_caja,
        }
        for pagina in self.paginas.values():
            pagina.grid(row=0, column=0, sticky="nsew")

        self.mostrar("Dashboard")

    def mostrar(self, nombre):
        """Trae al frente la página elegida y refresca sus datos."""
        pagina = self.paginas[nombre]
        pagina.refrescar()
        pagina.tkraise()
        self.sidebar.marcar_activo(nombre)


# ==============================================================================
# 7. AUTENTIFICACIÓN DE USUARIOS (inicio de sesión al abrir el sistema)
# ==============================================================================
USUARIO_AUTORIZADO = "barbero123"
PASSWORD_AUTORIZADA = "secret123"


class VentanaLogin(ctk.CTk):
    """Ventana de inicio de sesión. Se repite hasta ingresar credenciales válidas."""

    def __init__(self):
        super().__init__()
        self.title("Barbería El Pelón · Autentificación")
        self.geometry("420x420")
        self.resizable(False, False)
        self.configure(fg_color=BG)
        self.autorizado = False

        tarjeta = ctk.CTkFrame(self, fg_color=CARD, corner_radius=RADIO_TARJETA,
                               border_width=1, border_color=BORDER)
        tarjeta.pack(fill="both", expand=True, padx=24, pady=24)

        ctk.CTkLabel(tarjeta, text="AUTENTIFICACIÓN DE USUARIOS", font=fuente(16, True),
                     text_color=TEXT).pack(pady=(28, 20))

        ctk.CTkLabel(tarjeta, text="Ingresa el usuario:", font=fuente(13),
                     text_color=MUTED, anchor="w").pack(fill="x", padx=32)
        self.e_usuario = crear_entry(tarjeta, "Usuario", width=300)
        self.e_usuario.pack(padx=32, pady=(4, 12))

        ctk.CTkLabel(tarjeta, text="Ingresa su contraseña:", font=fuente(13),
                     text_color=MUTED, anchor="w").pack(fill="x", padx=32)
        self.e_password = crear_entry(tarjeta, "Contraseña", width=300)
        self.e_password.configure(show="*")
        self.e_password.pack(padx=32, pady=(4, 8))

        self.lbl_error = ctk.CTkLabel(tarjeta, text="", font=fuente(12),
                                      text_color=DANGER, wraplength=300)
        self.lbl_error.pack(pady=(4, 8))

        boton_primario(tarjeta, "Ingresar", self._validar, width=300).pack(padx=32)

        self.bind("<Return>", lambda _e: self._validar())
        self.e_usuario.focus()

    def _validar(self):
        usuario = self.e_usuario.get().strip()
        password = self.e_password.get().strip()
        if usuario == USUARIO_AUTORIZADO and password == PASSWORD_AUTORIZADA:
            messagebox.showinfo("Acceso autorizado",
                                "¡Acceso autorizado!, ¡Bienvenido al sistema!")
            self.autorizado = True
            self.destroy()
        else:
            self.lbl_error.configure(text="Usuario o contraseña incorrectos. Intente nuevamente.")
            self.e_password.delete(0, "end")
            self.e_usuario.focus()


if __name__ == "__main__":
    login = VentanaLogin()
    login.mainloop()
    if login.autorizado:          # si cierran la ventana sin autenticarse, no abre el sistema
        App().mainloop()