from PIL import Image, ImageDraw
import pandas as pd

def imagem_circular(caminho_img):
        img = Image.open(caminho_img).convert("RGBA")

        # Criar máscara circular
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, img.size[0], img.size[1]), fill=255)

        # Aplicar máscara
        img_circular = Image.new("RGBA", img.size)
        img_circular.paste(img, (0, 0), mask)
        return img_circular

def formatar_moeda_brl(valor):
    try:
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except:
        return valor

def formatar_valor_curto(valor):
    unidades = [
        (1_000_000_000_000, "trilhão"),
        (1_000_000_000, "bilhões"),
        (1_000_000, "milhão"),
        (1_000, "mil")
    ]
    
    for fator, nome in unidades:
        if valor >= fator:
            return f"R$ {valor / fator:.2f} {nome}".replace(".", ",")
    
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def formatar_valor_grande(valor):
    try:
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except:
        return valor


def formatar_populacao(valor):
    try:
        return f"{valor:,.0f}".replace(",", ".")
    except:
        return valor
    
def formatar_compacto(valor):
    if valor >= 1_000_000_000:
        return f"R$ {valor/1_000_000_000:,.2f} bilhões".replace(",", "X").replace(".", ",").replace("X", ".")
    elif valor >= 1_000_000:
        return f"R$ {valor/1_000_000:,.2f} milhões".replace(",", "X").replace(".", ",").replace("X", ".")
    else:
        return formatar_valor_grande(valor)