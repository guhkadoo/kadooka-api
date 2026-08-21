from django.http import JsonResponse
from .models import Language


def translations(request):
    language_code = request.GET.get('lang')

    language = Language.objects.filter(
        code=language_code,
        active=True
    ).first()

    if not language:
        return JsonResponse(
            {
                'error': 'Language not found'
            },
            status=404
        )

    translations_data = dict(
        language.translations.values_list('key', 'value')
    )

    return JsonResponse({
        'language': language.code,
        'translations': translations_data
    })
