import csv
import logging
import tablib
from datetime import datetime, timedelta, time
from django.db.models import Model
from django.db.models.fields.files import FieldFile
from unicodedata import normalize
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.template import Context, Template
from django.conf import settings
from django.core.urlresolvers import reverse


def export_as_excel(modeladmin, request, queryset):
    if not request.user.is_staff:
        raise PermissionDenied
    opts = modeladmin.model._meta    
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename=%s.xls' % unicode(opts).replace('.', '_')
    
    try:
        #field_names = modeladmin.model.get_csv_fields()
        field_names = ['id', 'title', 'published']
        v_field_names = field_names
    except:
        field_names = [field.name for field in opts.fields]
        v_field_names = [getattr(field, 'verbose_name') or field.name for field in opts.fields]
    # print field_names
    v_field_names = map(lambda x: x.encode('utf-8') if x != 'ID' else 'Id', v_field_names)

    ax = []
    headers = v_field_names

    data = []

    data = tablib.Dataset(*data, headers=headers)
    for obj in queryset:
        acc = []
        for field in field_names:
            try:
                uf = getattr(obj, field)()
            except:
                try:
                    uf = getattr(obj, field)
                except:
                    uf = 'error obteniendo el dato'
            if uf is None:
                uf = ''
            elif isinstance(uf, datetime):
                uf = uf - timedelta(hours=5)
                uf = unicode(uf)
            elif isinstance(uf, Model):
                uf = isinstance(uf)
            elif isinstance(uf, FieldFile):
                uf = uf.url
            acc.append(uf)
        data.append(acc)
    response.write(data.xls)
    return response

export_as_excel.short_description = "Exportar como Excel"




def make_published(self, request, queryset):
	return queryset.update(published = True)
make_published.short_description = "Cambiar a publicado"