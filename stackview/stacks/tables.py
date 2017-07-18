import django_tables2 as tables

from .models import Stack


class StackTable(tables.Table):
    name = tables.Column()
    backend = tables.Column()
    owner = tables.Column()
    created = tables.Column()
    status = tables.Column()

    class Meta:
        attrs = {'class': 'table table-hover'}
        sequence = ('name', 'backend', 'owner', 'created', 'status')

