from django.shortcuts import render
from .models import Pages


def index(request):

    IS_ADMIN = request.user.has_perm('admin')

    page = Pages.objects.filter(home_page=True).get()
    components = page.components_set.filter(name__in={"home_title_slider", "home_site_title"})
    comments = page.comments_set.all().order_by('-created_at')

    print('request.user >> ')
    print(IS_ADMIN)

    comps = {}
    comps.clear()
    for com in components:
        comps[com.name] = com.value

    return render(
        request,
        'page/index.html',
        {
            'page': page,
            'component': comps,
            'comments': comments
        }
    )
