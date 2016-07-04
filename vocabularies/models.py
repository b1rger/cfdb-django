from django.db import models


class VocabsBase(models.Model):
    name = models.CharField(
        max_length=250, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def get_classname(self):
        """Returns the name of the class as lowercase string"""
        class_name = str(self.__class__.__name__).lower()
        return class_name


class Region(VocabsBase):
    pass


class Archive(VocabsBase):
    pass


class Dossier(VocabsBase):
    pass


class Scribe(VocabsBase):
    pass


class Period(VocabsBase):
    pass


class TextType(VocabsBase):
    pass
