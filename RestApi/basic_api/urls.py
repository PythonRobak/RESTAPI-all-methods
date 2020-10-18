from django.urls import path, include
# from .views import article_list, article_detail, ArticleAPIView, ArticleDetailsAPIView
from .views import GenericAPIView, ArticleViewSet, GenericArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', GenericArticleViewSet, basename='article')
# router.register('generic/article', GenericArticleViewSet, basename='generic article')


urlpatterns = [

    path('viewset', include(router.urls)),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    # path('generic/viewset',include(router.urls)),
    # path('generic/viewset/',include(router.urls)),
    # path('article/', article_list),
    # path('article/<int:pk>', article_detail),
    # path('article/', ArticleAPIView.as_view()),
    # path('article/<int:id>', ArticleDetailsAPIView.as_view()),
    path('generic/article', GenericAPIView.as_view()),
    path('generic/article/', GenericAPIView.as_view()),
    path('generic/article/<int:id>', GenericAPIView.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
]
