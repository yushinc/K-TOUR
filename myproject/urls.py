from django.contrib import admin
from django.urls import path
from tourapp import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # tourapp
    path('', views.home, name='home'),
    # 검색 기능
    path('search/', views.search, name='search'), 
    # 게시판, 글생성, 게시판 상세 페이지, 댓글
    path('board/', views.board, name='board'),
    path('postcreate/', views.postcreate, name='postcreate'), 
    path('detail/<int:post_id>', views.detail, name='detail'), 
    path('comment/<int:post_id>', views.comment, name='comment'),
    # 코스 추천 
    path('region/', views.region, name='region'),
    path('jeju/', views.jeju, name='jeju'),
    #축제 
    path('festival/', views.festival, name='festival'),
    path('festivalnext/', views.festivalnext, name='festivalnext'),
    path('festivalpre/', views.festivalpre, name='festivalpre'),
    path('festivaldetail/', views.festivaldetail, name='festivaldetail'),  
    
    
    #accounts
    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),
]
