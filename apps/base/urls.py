from django.urls import path
from apps.base.views import Home, KmeansView, DBScanView, SpectralView
# from apps.kmeans.views import UserListApiView, UserDetailApiView 

app_name = 'base'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    #path('req83/', Req83View.as_view(), name='req83'),
    path('kmeans/', KmeansView.as_view(), name='kmeans'),
    path('dbscan/', DBScanView.as_view(), name='dbscan'),
    path('spectral/', SpectralView.as_view(), name='spectral'),
]
