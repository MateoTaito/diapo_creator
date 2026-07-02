"""Genera grafico_lamina_1.png con la evolucion de la tasa de ocupacion informal en Chile.

Usa solo PIL (Pillow) como modulo externo para dibujar el grafico.
"""
from PIL import Image, ImageDraw, ImageFont

# Colores del proyecto
AZUL_OSCURO = (26, 39, 68)
AZUL_MEDIO = (45, 62, 95)
MAGENTA = (139, 26, 110)
NARANJA = (196, 82, 0)
GRIS_CLARO = (244, 244, 244)
GRIS_TEXTO = (90, 90, 90)
BLANCO = (255, 255, 255)

# Datos: tasa de ocupacion informal Chile, ultimos 5 trimestres (ENEt 2025-2026)
# Variacion +0.7 pp en 12 meses, terminando en 26.5% en Q1 2026
datos = [
    ("Q1 2025", 25.8),
    ("Q2 2025", 25.9),
    ("Q3 2025", 26.0),
    ("Q4 2025", 26.2),
    ("Q1 2026", 26.5),
]

ANCHO, ALTO = 1400, 800
img = Image.new("RGB", (ANCHO, ALTO), BLANCO)
draw = ImageDraw.Draw(img)

# Intentar cargar fuentes del sistema, fallback a default
def cargar_fuente(tamano, negrita=False):
    rutas = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if negrita else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if negrita else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for ruta in rutas:
        try:
            return ImageFont.truetype(ruta, tamano)
        except OSError:
            continue
    return ImageFont.load_default()

f_titulo = cargar_fuente(34, negrita=True)
f_eje = cargar_fuente(22)
f_eje_bold = cargar_fuente(22, negrita=True)
f_dato = cargar_fuente(28, negrita=True)
f_etiqueta = cargar_fuente(20)

# Margenes del area del grafico
MARGEN_IZQ = 120
MARGEN_DER = 80
MARGEN_SUP = 130
MARGEN_INF = 110
AREA_X = MARGEN_IZQ
AREA_Y = MARGEN_SUP
AREA_W = ANCHO - MARGEN_IZQ - MARGEN_DER
AREA_H = ALTO - MARGEN_SUP - MARGEN_INF

# Titulo
draw.text((ANCHO // 2, 40), "Tasa de ocupacion informal en Chile", fill=AZUL_OSCURO, font=f_titulo, anchor="mm")
draw.text((ANCHO // 2, 80), "Boletin ENE Informalidad, Instituto Nacional de Estadisticas", fill=GRIS_TEXTO, font=f_etiqueta, anchor="mm")

# Ejes
# Eje Y desde 25.0 a 27.0
Y_MIN, Y_MAX = 25.0, 27.0
RANGO = Y_MAX - Y_MIN

def y_a_pixel(valor):
    return AREA_Y + int(AREA_H * (1 - (valor - Y_MIN) / RANGO))

# Lineas de grilla horizontales y etiquetas del eje Y
for valor in [25.0, 25.5, 26.0, 26.5, 27.0]:
    y = y_a_pixel(valor)
    color = AZUL_OSCURO if valor == 26.5 else (220, 220, 220)
    draw.line([(AREA_X, y), (AREA_X + AREA_W, y)], fill=color, width=2 if valor == 26.5 else 1)
    texto = f"{valor:.1f}%"
    draw.text((AREA_X - 18, y), texto, fill=AZUL_OSCURO if valor == 26.5 else GRIS_TEXTO,
              font=f_eje_bold if valor == 26.5 else f_eje, anchor="rm")

# Barras
n = len(datos)
espacio = AREA_W / n
ancho_barra = int(espacio * 0.55)

puntos = []
for i, (etiqueta, valor) in enumerate(datos):
    cx = int(AREA_X + espacio * (i + 0.5))
    x0 = cx - ancho_barra // 2
    x1 = cx + ancho_barra // 2
    y_top = y_a_pixel(valor)
    y_base = y_a_pixel(Y_MIN)
    es_ultimo = (i == n - 1)
    color = NARANJA if es_ultimo else AZUL_MEDIO
    # Barra
    draw.rectangle([x0, y_top, x1, y_base], fill=color, outline=color)
    # Valor encima de la barra
    draw.text((cx, y_top - 18), f"{valor:.1f}%", fill=color, font=f_dato, anchor="mm")
    # Etiqueta del trimestre debajo
    draw.text((cx, y_base + 30), etiqueta, fill=AZUL_OSCURO, font=f_eje_bold, anchor="mm")
    puntos.append((cx, y_top))

# Linea de tendencia sobre los puntos
for i in range(len(puntos) - 1):
    draw.line([puntos[i], puntos[i + 1]], fill=MAGENTA, width=3)

# Puntos sobre la linea
for (cx, cy) in puntos:
    draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=MAGENTA, outline=BLANCO, width=2)

# Eje X (linea base)
draw.line([(AREA_X, y_a_pixel(Y_MIN)), (AREA_X + AREA_W, y_a_pixel(Y_MIN))], fill=AZUL_OSCURO, width=2)

# Anotacion destacada del dato final
ultimo_cx, ultimo_cy = puntos[-1]
draw.text((ultimo_cx + 110, ultimo_cy + 30), "+0.7 pp en 12 meses", fill=MAGENTA, font=f_eje_bold, anchor="lm")

# Etiqueta del eje Y rotada (simulada como texto horizontal arriba del eje)
draw.text((40, AREA_Y + AREA_H // 2), "Tasa (%)", fill=AZUL_OSCURO, font=f_eje_bold, anchor="mm")

# Pie
draw.text((ANCHO // 2, ALTO - 35), "Fuente: INE Chile, Boletin ENE Informalidad edicion 34, Q1 2026",
          fill=GRIS_TEXTO, font=f_etiqueta, anchor="mm")

img.save("/home/MTS/UAI/Profesor/diapo_creator/lamina_final_taller_1/public/grafico_lamina_1.png", "PNG")
print("grafico_lamina_1.png generado correctamente")
