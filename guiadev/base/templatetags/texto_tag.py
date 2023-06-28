from django import template

register = template.Library()


@register.filter(name='get_texto')
def get_texto(conteudo):
    return str(conteudo).split('\n')
