from PIL import Image
import io
import os
import uuid
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm, inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import getSampleStyleSheet, StyleSheet1
from typing import List
from django.template.defaultfilters import slugify as django_slugify

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(s):
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))

def compress_image(img, target_size=2 * 1024 * 1024):
    """
    Сжимает изображение по объему, уменьшая качество до достижения целевого размера.
    Поддерживает изображения с альфа-каналом.
    """
    quality = 85
    output = io.BytesIO()

    # Если изображение имеет альфа-канал, конвертируем его в RGB
    if img.mode == 'RGBA':
        img = img.convert('RGB')

    # Постепенное снижение качества до тех пор, пока объем файла не станет меньше target_size
    while True:
        output.seek(0)
        img.save(output, format='JPEG', quality=quality, optimize=True)
        size = output.tell()

        if size <= target_size or quality <= 10:
            break

        # Уменьшаем качество при каждом цикле
        quality -= 5

    output.seek(0)
    return Image.open(output)


def product_image_upload_to(instance, filename):
    """Динамически создаем папку на основе slug и уникальное имя файла"""
    extension = filename.split('.')[-1]
    unique_filename = f"img_{uuid.uuid4().hex}.{extension}"
    return os.path.join('images', instance.complectation.slug, unique_filename)


def procurements_xlsx_upload_to(instance, filename):
    """Динамически создаем папку на основе slug и уникальное имя файла"""
    extension = filename.split('.')[-1]
    unique_filename = f"table_{uuid.uuid4().hex}.{extension}"
    return os.path.join('xlsx_estimates', instance.complectation.slug, unique_filename)


def check_img_upload_to(instance, filename):
    """Динамически создаем папку на основе slug и уникальное имя файла"""
    extension = filename.split('.')[-1]
    unique_filename = f"check_{uuid.uuid4().hex}.{extension}"
    return os.path.join('checks', instance.complectation.slug, unique_filename)


# Утилиты для работы PDF View Комплектаций
def setup_pdf(buffer: io.BytesIO, size=False) -> SimpleDocTemplate:
    """Настраивает и возвращает PDF-документ с отступами."""
    if size:
        orent = landscape(A4)
    else:
        orent = A4
    left_margin = 3 * cm
    right_margin = 1.5 * cm
    pdf = SimpleDocTemplate(
        buffer,
        pagesize=orent,
        leftMargin=left_margin,
        rightMargin=right_margin
    )

    try:
        pdfmetrics.registerFont(TTFont('FreeSans', 'fonts/FreeSans.ttf'))
    except Exception as e:
        print(f"Ошибка при регистрации шрифта 'FreeSans': {e}")

    return pdf


def setup_styles() -> StyleSheet1:
    """Настраивает и возвращает стили для PDF-документа."""
    styles = getSampleStyleSheet()
    styles["Normal"].fontName = "FreeSans"
    styles["Heading1"].fontName = "FreeSans"
    return styles


def create_table(data: List[List[str]], col_widths: List[float]) -> Table:
    """Создает и возвращает таблицу с заданными данными и ширинами колонок."""
    table = Table(data, colWidths=col_widths)
    table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'FreeSans'),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))
    return table


def get_filename(products: List['Product']) -> str:
    """Формирует и возвращает имя файла PDF."""
    unique_number = products.first().id if products.exists() else 1
    complectation_name = products.first().complectation if products.exists() else 'default'
    return f"complectation_{complectation_name}_{unique_number}.pdf"