from pathlib import Path

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from PIL import Image, ImageDraw, ImageFont

from main.models import Book


class Command(BaseCommand):
    help = 'Seed the database with football shirt records and generated images'

    def handle(self, *args, **options):
        base_dir = Path('media/shirts')
        base_dir.mkdir(parents=True, exist_ok=True)

        items = [
            ('Real Madrid 2022', 'Real Madrid', 'Camiseta clásica de la temporada 2022 con diseño blanco y detalles dorados.', '2022-06-01', 'real_madrid.png', '#FFFFFF', '#DBA111'),
            ('Bayern Munich 2020', 'Bayern Munich', 'Camiseta oficial del Bayern con tonos rojos y negro.', '2020-08-01', 'bayern.png', '#F5F5F5', '#DC052D'),
            ('Manchester City 2023', 'Manchester City', 'Diseño azul eléctrico para la temporada 2023.', '2023-07-01', 'city.png', '#1C2C5B', '#6CABDD'),
            ('Inter Milan 2022', 'Inter Milan', 'Camiseta histórica con detalles azules y negros.', '2022-09-01', 'inter.png', '#0B1F3A', '#FFFFFF'),
            ('PSG 2021', 'Paris Saint-Germain', 'Camiseta azul con líneas elegantes y estilizadas.', '2021-06-01', 'psg.png', '#0B1F3A', '#FFFFFF'),
            ('Argentina 2022', 'Selección Argentina', 'Camiseta de la Copa del Mundo con diseño icónico.', '2022-11-01', 'argentina.png', '#6BB6FF', '#FFFFFF'),
            ('Brasil 2022', 'Selección Brasil', 'Camiseta amarilla con el famoso brillo de la Canarinha.', '2022-11-01', 'brasil.png', '#F7D000', '#009C3B'),
            ('Francia 2022', 'Selección Francia', 'Camiseta azul con detalles de campeón.', '2022-11-01', 'francia.png', '#002654', '#FFFFFF'),
            ('Alemania 2022', 'Selección Alemania', 'Camiseta blanca con detalles en negro y rojo.', '2022-11-01', 'alemania.png', '#FFFFFF', '#DD0000'),
            ('España 2022', 'Selección España', 'Camiseta roja con diseño clásica y elegante.', '2022-11-01', 'espana.png', '#C60B1E', '#F7D000'),
        ]

        for title, author, description, published_date, filename, bg, accent in items:
            if Book.objects.filter(title=title).exists():
                continue

            img = Image.new('RGBA', (800, 1000), bg)
            draw = ImageDraw.Draw(img)
            draw.rounded_rectangle((40, 40, 760, 960), radius=40, fill=bg, outline=accent, width=12)
            draw.ellipse((120, 120, 680, 680), fill=accent)
            draw.rectangle((120, 260, 680, 760), fill=accent)
            draw.rectangle((140, 600, 660, 720), fill=bg)
            try:
                font = ImageFont.truetype('arial.ttf', 44)
            except Exception:
                font = ImageFont.load_default()
            draw.text((120, 760), title, fill=accent if bg != accent else '#111111', font=font)
            draw.text((120, 830), author, fill='#111111' if bg != '#FFFFFF' else '#222222', font=ImageFont.load_default())
            path = base_dir / filename
            img.save(path)
            with path.open('rb') as fh:
                Book.objects.create(
                    title=title,
                    author=author,
                    description=description,
                    published_date=published_date,
                    image=ContentFile(fh.read(), name=filename),
                )

        self.stdout.write(self.style.SUCCESS('Seeded football shirts and images successfully'))
