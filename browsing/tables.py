import django_tables2 as tables
from django_tables2.utils import A
from tablets.models import Tablet


class TabletTable(tables.Table):
    title = tables.LinkColumn('tablets:tablet_detail', args=[A('pk')])

    class Meta:
        model = Tablet
        fields = ['title']
        attrs = {"class": "table table-hover table-striped table-condensed"}
