import django_filters
from tablets.models import Tablet

django_filters.filters.LOOKUP_TYPES = [
    ('', '---------'),
    ('exact', 'Is equal to'),
    ('iexact', 'Is equal to (case insensitive)'),
    ('not_exact', 'Is not equal to'),
    ('lt', 'Lesser than/before'),
    ('gt', 'Greater than/after'),
    ('gte', 'Greater than or equal to'),
    ('lte', 'Lesser than or equal to'),
    ('startswith', 'Starts with'),
    ('endswith', 'Ends with'),
    ('contains', 'Contains'),
    ('icontains', 'Contains (case insensitive)'),
    ('not_contains', 'Does not contain'),
]


class TabletListFilter(django_filters.FilterSet):
    text_reference = django_filters.CharFilter(
        lookup_expr='icontains', label='Tablet', help_text=False)
    title = django_filters.CharFilter(lookup_expr='icontains', help_text=False)
    cdli_no = django_filters.CharFilter(lookup_expr='icontains', label='CDLI no.', help_text=False)
    nabucco_no = django_filters.CharFilter(
        lookup_expr='icontains', label='NABUCCO no.', help_text=False)
    museum_no = django_filters.CharFilter(
        lookup_expr='icontains', label='Museum no.', help_text=False)
    date_not_before = django_filters.NumberFilter(
        lookup_expr='gte', label='Date not before', help_text='Greater than or equal to'
    )
    date_not_after = django_filters.NumberFilter(
        lookup_expr='lte', label='Date not after', help_text='Lesser than or equal to')
    babyloneian_time = django_filters.CharFilter(lookup_expr='icontains', help_text=False)
    content = django_filters.CharFilter(lookup_expr='icontains', help_text=False)
    distinctive_protagonists = django_filters.CharFilter(lookup_expr='icontains', help_text=False)
    bibliography = django_filters.CharFilter(lookup_expr='icontains', help_text=False)

    class Meta:
        model = Tablet


class SignListFilter(django_filters.FilterSet):
    sign_name = django_filters.CharFilter(lookup_expr='icontains', help_text=False)
    abz_number = django_filters.CharFilter(lookup_expr='icontains', help_text=False)
    meszl_number = django_filters.CharFilter(lookup_expr='icontains', help_text=False)
