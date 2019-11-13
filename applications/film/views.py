from django.shortcuts import render
from applications.film.models import Films


def index(request, slug):
    # page = Pages.objects.filter(slug='film__inner')
    # components = page.components_set.filter(name__in={"film__inner_"})
    # comps = {}
    # comps.clear()
    # for com in components:
    #     comps[com.name] = com.value

    film = Films.objects.get(slug=slug)
    sessions = film.session_set.all()

    return render(
        request,
        'film/index.html',
        {
            'film': film,
            'sessions': sessions
        }
    )
