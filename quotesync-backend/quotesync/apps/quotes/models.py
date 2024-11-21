from django.db import models


class Author(models.Model):
    name = models.CharField(
        max_length=1024, unique=True, help_text="Nombre"
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Book(models.Model):
    title = models.CharField(
        max_length=1024, unique=True, help_text="Nombre"
    )

    author = models.ForeignKey(
        Author, blank=True, null=True, related_name="books", on_delete=models.SET_NULL, help_text="Autor"
    )

    def __str__(self):
        return "{} ({})".format(self.title, self.author)

    class Meta:
        ordering = ('title',)


class Tag(models.Model):
    title = models.SlugField(
        unique=True, help_text="Título"
    )
    description = models.CharField(
        max_length=1024, blank=True, null=True, help_text="Descripción"
    )

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return "{}: {}".format(self.title, self.description)


class Quote(models.Model):
    title = models.CharField(
        max_length=1024, help_text="Título"
    )
    body = models.TextField(
        blank=True, null=True, help_text="Cita"
    )
    archive = models.BooleanField(
        default=False, help_text="Archivada"
    )

    created = models.DateField(
        help_text="Fecha de creación", auto_now_add=True
    )
    updated = models.DateField(
        help_text="Fecha de actualización", auto_now=True
    )
    hash = models.SlugField(
        blank=True, null=True, help_text="Hash"
    )

    book = models.ForeignKey(
        Book, blank=True, null=True, related_name="quotes", on_delete=models.SET_NULL, help_text="Libro"
    )
    tags = models.ManyToManyField(
        Tag, blank=True, related_name="quotes", help_text="Etiquetas"
    )

    def save(self, *args, **kwargs):
        self.hash = str(hash(self.body))
        super().save(*args, **kwargs)

    def __str__(self):
        return "{} [{}]".format(self.title, self.book)

    class Meta:
        ordering = ('created', 'title')

