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
    Sign_name = tables.LinkColumn('tablets:tablet_detail', args=[A('pk')])

    class Meta:
        model = Sign
        fields = ['title']
        attrs = {"class": "table table-hover table-striped table-condensed"}
