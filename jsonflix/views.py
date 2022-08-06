import json
import re

from django.http import HttpResponse

from jsonflix.scripts.scripts import country_code_converter

from .models import Netflix


def all(request):
    qs = Netflix.objects.all()
    dict = [Netflix.json_dict(content) for content in qs]

    return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=2), content_type="application/json")


def api(request):

    fields = Netflix._meta.get_fields()
    fields_list = ['limit', ]
    fields_list += [field.attname for field in fields]
    params = set(request.GET.keys())

    if not params:
        return HttpResponse(json.dumps({}, ensure_ascii=False, indent=2), content_type="application/json")

    if not params.issubset(fields_list):
        diff = params.difference(fields_list)
        dict = {f'Error {index}': f'Field {parameter} does not exist' for parameter, index in zip(
            diff, range(1, len(diff)+1))}
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=2), content_type="application/json")

    type = request.GET.get("type")
    title = request.GET.get("title")
    cast = request.GET.get("cast")
    country = request.GET.get("country")
    genres = request.GET.get("genres")
    # date_added = request.GET.get("date_added")
    release_year = request.GET.get("release_year")
    description = request.GET.get("description")
    limit = request.GET.get("limit")
    qs = Netflix.objects.all()

    if type:
        qs = qs.filter(type__icontains=type).order_by('id')
        if len(qs) == 0:
            dict = {
                'error': "Only 'movie' and 'tv_show' are accepted in the type field"
            }
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=2), content_type="application/json")
        else:
            type = type.replace('_', ' ')
            qs = qs.filter(type__icontains=type).order_by('id')

    if title:
        title = title.replace('_', ' ')
        qs = qs.filter(title__icontains=title).order_by('id')

    if country:
        if len(country) <= 3:
            country = country_code_converter(country)
        else:
            country = country.replace('_', ' ').capitalize()
        qs = qs.filter(country__icontains=country).order_by('id')

    if release_year:
        release_year = release_year.split(',')
        if len(release_year) > 1:
            qs = qs.filter(release_year__gte=release_year[0]).order_by('id')
            qs = qs.filter(release_year__lte=release_year[1]).order_by('id')
        else:
            qs = qs.filter(release_year=release_year).order_by('id')

    if cast:
        cast = cast.split(',')
        for actor in cast:
            actor = actor.replace('_', ' ')
            qs = qs.filter(cast__icontains=actor).order_by('id')

    if genres:
        genres = genres.split(',')
        for genre in genres:
            genre = genre.replace('_', ' ')
            qs = qs.filter(genres__icontains=genre).order_by('id')

    if description:
        description = set(description.split(','))

        desc = []
        for show in qs:
            ds = show.description
            ds = set(re.findall(r"[\w']+", ds))
            if description.issubset(ds):
                desc.append(show.id)
        qs = qs.filter(id__in=desc)

    if limit:
        try:
            limit = int(request.GET.get("limit"))
            qs = qs[:limit]
        except ValueError:
            dict = {
                'error': 'Only numerics are accepted in the limit field'
            }
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=2), content_type="application/json")
    dict = [Netflix.json_dict(content) for content in qs]

    return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=2), content_type="application/json")
