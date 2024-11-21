import re
from datetime import datetime
import locale
from quotesync.apps.quotes.models import Author, Book, Quote
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def save_quotes_from_file(file_content):
    # Primero, dividimos el contenido del archivo en bloques de citas usando una expresión regular
    quote_blocks = re.split(r'(\n?==========\n?)', file_content)

    for block in quote_blocks:
        block = block.strip()

        if block:
            # Separamos la información por líneas
            lines = block.split("\n")

            if len(lines) < 4:
                continue  # Si la cita no tiene el formato esperado, la omitimos

            # 1. Título del libro y autor (extraído de la primera línea)
            title_and_author = lines[0].split('(')
            book_title = title_and_author[0].strip()
            author_name = title_and_author[1].replace(')', '').strip() if len(title_and_author) > 1 else "No author"

            # 2. Extraemos el texto de la cita (cuerpo)
            quote_body = "\n".join(lines[3:]).strip()

            # 3. Extracto del texto relacionado con la página y fecha
            # En la línea 1, que sigue al título del libro, tenemos algo como: "- La subrayado en la página 55 | posición 843-843 | Añadido el miércoles, 4 de julio de 2018 18:19:38"
            quote_info = lines[1]
            date_match = re.search(r'Añadido el (.+)', quote_info)
            quote_date = date_match.group(1).strip() if date_match else None

            # Limpiar cualquier salto de línea extra y luego convertir la fecha al formato adecuado
            # locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
            if quote_date:
                try:
                    created_at = None
                    # created_at = datetime.strptime(quote_date, "%A, %d de %B de %Y %H:%M:%S")
                except ValueError:
                    # Si ocurre un error al parsear, puedes manejarlo aquí
                    print(f"Error parsing date: {quote_date}")
                    created_at = None
            else:
                created_at = None

            # Buscar libro en base de datos, si no existe, crear uno
            author, created = Author.objects.get_or_create(name=author_name)
            book, created = Book.objects.get_or_create(title=book_title, author=author)

            # Crear la cita (quote)
            quote = Quote.objects.create(
                title=book_title,
                body=quote_body,
                created=created_at,
                book=book
            )

            # Opcional: Si deseas agregar tags, puedes extraerlos del texto o agregar manualmente
            # quote.tags.add(tag) # Asumiendo que ya tienes tags definidos.

            # Guardamos la cita
            quote.save()

            print(f"Quote saved: {quote.title} from {book.title} by {author.name}.")

