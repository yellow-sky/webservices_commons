from django import template
register = template.Library()

external_links = {
    'nextgis_online': 'http://online.nextgis.com',
    'my_nextgis': 'https://my.nextgis.com',

    'nextgis_com_en': 'http://nextgis.com',
    'nextgis_com_ru': 'http://nextgis.ru',

    'terms_ru': 'http://nextgis.ru/terms/',
    'terms_en': 'http://nextgis.com/terms/',

    'privacy_ru': 'http://nextgis.ru/privacy',
    'privacy_en': 'http://nextgis.com/privacy',

    'docs_ru': 'http://docs.nextgis.ru',
    'docs_en': 'http://docs.nextgis.com',

    # temporary?
    'ngid_profile': 'https://my.nextgis.com/profile',
    'ngid_public_profile': 'https://my.nextgis.com/public_profile',
    'webgis': 'https://my.nextgis.com/webgis',

}


@register.simple_tag
def external_url(url_name, lang):
    if lang != "":
        url_name = url_name + "_" + lang
    return external_links[url_name] if url_name in external_links.keys() else ''
