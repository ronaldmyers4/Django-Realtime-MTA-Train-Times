from django.urls import path
from TrainTimes import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	#18.218.160.12
	path('', views.HomePageView.as_view()),
	
	# /about/
	path('about/', views.AboutPageView.as_view()),
	
	#/train/
	path('<int:train_id>/train/', views.detail, name='detail'),
	
	#/choice/
	path('choice/', views.ChoicePage, name='ChoicePage'),
	
	path('SearchStop/', views.SearchStop, name='SearchStop'),
	
	#/response123456
	path('response123456/',views.Response123456, name='Response123456')
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)