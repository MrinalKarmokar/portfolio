from django.contrib.auth.models import User
from matplotlib.style import context

def project_context(request):

    context = {
        'me': User.objects.first(),
    }
    return context