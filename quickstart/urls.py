from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from graphene_django.views import GraphQLView


urlpatterns = [path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True)))]
urlpatterns += staticfiles_urlpatterns()

urlpatterns += [
    path(r'operations/', admin.site.urls),
]