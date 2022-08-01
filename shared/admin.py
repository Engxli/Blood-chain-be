import csv
from typing import Any, TypeVar

from django.contrib import admin
from django.db.models import Model, QuerySet
from django.http import HttpRequest, HttpResponse


_T = TypeVar("_T", bound=Model)


@admin.action(description="Export Selected as csv file")
def export_as_csv(
    modeladmin: admin.ModelAdmin[_T],
    request: HttpRequest,
    queryset: QuerySet[_T],
) -> HttpResponse:
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f"attachment; filename={meta}.csv"

    writer = csv.writer(response)

    writer.writerow(field_names)

    for obj in queryset:
        row: list[Any] = []
        for field in field_names:
            value = getattr(obj, field)
            if field == "image":
                value = request.build_absolute_uri(value)
            row.append(value)
        writer.writerow(row)
    return response
