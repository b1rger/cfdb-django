import os
from django.db import models
from vocabularies.models import Region, Archive, Dossier, Scribe, Period, TextType
from places.models import Place

PLACE_CHOICES = (
    ('external', 'external'),
    ('conjecture', 'conjecture'),
    ('internal', 'internal'),
    ('', '---------')
)

DCUTUS_CHOICES = (
    ('normal', 'normal'),
    ('slanting', 'slanting'),
    ('', '---------')
)


class Sign(models.Model):
    sign_name = models.CharField(max_length=50)
    abz_number = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="ABZ Number")
    meszl_number = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="MesZL Number")
    image_1 = models.FileField(upload_to='sign_img', blank=True, null=True)
    image_2 = models.FileField(upload_to='sign_img', blank=True, null=True)

    def __str__(self):
        return self.sign_name

    def image1_name(self):
        return os.path.basename(self.image_1.name)

    def image2_name(self):
        return os.path.basename(self.image_2.name)


class Tablet(models.Model):
    text_reference = models.CharField(
        max_length=250, blank=False, help_text="Eindeutiger Bezeichner des Textes")
    title = models.CharField(
        max_length=250, blank=False, help_text="Titel der Instanz")
    region = models.ForeignKey(
        Region, blank=True, null=True, help_text="Fundregion")
    archive = models.ForeignKey(
        Archive, blank=True, null=True, help_text="Archiv = Sammlung von Tafeln")
    dossier = models.ForeignKey(
        Dossier, blank=True, null=True, help_text="Unterkategorisierung v. Archiven")
    cdli_no = models.CharField(
        max_length=50, blank=True, verbose_name="CDLI no.", help_text="Nummer der Tafel in CDLI")
    nabucco_no = models.CharField(
        max_length=50, blank=True, verbose_name="NABUCCO no.",
        help_text="Nummer der Tafel in NABUCCO")
    museum_no = models.CharField(
        max_length=50, blank=True, verbose_name="Museum Number")
    place = models.ForeignKey(
        Place, blank=True, null=True)
    place_information = models.CharField(
        max_length=50, blank=True, choices=PLACE_CHOICES, default="",
        help_text="indicates the nature of the evidence supporting the reliability or accuracy of the intervention or interpretation. Suggested values include: 1] internal; 2] external; 3] conjecture")
    scribe = models.ForeignKey(
        Scribe, blank=True, null=True, help_text="Schreiber")
    period = models.ForeignKey(
        Period, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    date_not_after = models.IntegerField(blank=True, null=True)
    date_not_before = models.IntegerField(blank=True, null=True)
    babyloneian_time = models.CharField(max_length=50, blank=True)
    ductus = models.CharField(
        max_length=50, blank=True, choices=DCUTUS_CHOICES,
        help_text="Gerader oder schräger Schriftduktus", default="")
    text_type = models.ForeignKey(TextType, blank=True, null=True)
    content = models.TextField(
        blank=True, null=True, help_text="Zusammenfassung d. Inhalts")
    distinctive_protagonists = models.CharField(
        max_length=250, blank=True,
        help_text="Im Text erwähnte Personen")
    bibliography = models.CharField(
        max_length=500, blank=True,
        help_text="Transliterationen oder Abdrucke ")

    def __str__(self):
        return self.text_reference

    @property
    def number_of_glyphs(self):
        return len(Glyph.objects.filter(tablet=self.id))


class TabletImage(models.Model):
    tablet = models.ForeignKey(Tablet)
    image = models.FileField(upload_to='tablet_img')
    comment = models.TextField(blank=True, null=True)

    def filename(self):
        return os.path.basename(self.image.name)


class Glyph(models.Model):
    identifier = models.CharField(max_length=250)
    tablet = models.ForeignKey(Tablet, null=True, blank=True)
    sign = models.ForeignKey(Sign, null=True, blank=True)
    reading = models.CharField(max_length=250, blank=True, null=True)
    context = models.CharField(max_length=250, blank=True, null=True)
    note = models.CharField(max_length=250, blank=True, null=True)
    image = models.FileField(upload_to='glyph_img')

    def __str__(self):
        return "{}_{} ({})".format(self.sign, self.reading, self.tablet)

    def filename(self):
        return os.path.basename(self.image.name)
