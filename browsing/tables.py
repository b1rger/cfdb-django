import django_tables2 as tables
from django_tables2.utils import A
from tablets.models import Tablet, Sign, Glyph


class TabletTable(tables.Table):
    title = tables.LinkColumn('tablets:tablet_detail', args=[A('pk')], verbose_name='Tablet')
    period = tables.Column(verbose_name='Period')
    place = tables.Column(verbose_name='Place')
    text_type = tables.Column(verbose_name='Text Type')
    nrglyphs = tables.Column(empty_values=(), orderable=False, verbose_name='Number of Glyphs')

    def render_nrglyphs(self, value, record):
        glyphs = Glyph.objects.filter(tablet=record.id)
        return len(glyphs)

    class Meta:
        model = Tablet
        fields = ['title']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class SignTable(tables.Table):
    sign_name = tables.LinkColumn('tablets:sign_detail', args=[A('pk')], verbose_name='Sign Name')
    nrglyphs = tables.Column(empty_values=(), orderable=False, verbose_name='Number of Glyphs')

    def render_nrglyphs(self, value, record):
        glyphs = Glyph.objects.filter(sign=record.id)
        return len(glyphs)

    class Meta:
        model = Sign
        exclude = ['image_1', 'image_2']
        attrs = {"class": "table table-hover table-striped table-condensed"}
