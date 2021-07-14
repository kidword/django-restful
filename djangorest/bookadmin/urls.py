from rest_framework import routers
from .views import BookInfoViews, HeroInfoViews

router = routers.DefaultRouter()

router.register(r'', BookInfoViews)
router.register(r'hero/', HeroInfoViews)


urlpatterns = []

urlpatterns += router.urls
