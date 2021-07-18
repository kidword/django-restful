from rest_framework import routers
from django.urls import path
from .views import BookInfoViews, UserInfoViews, UserGroupView

# router = routers.DefaultRouter()
#
# router.register(r'', BookInfoViews)
# router.register(r'hero/', HeroInfoViews)


urlpatterns = [
    path(r'', BookInfoViews.as_view()),
    path(r'userinfo/', UserInfoViews.as_view(), name='gp'),
    path(r'usergroup/', UserGroupView.as_view(), name='gp')
]

# urlpatterns += router.urls
