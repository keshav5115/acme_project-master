from django.urls import path
from authe import views

from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("homepage/", views.homepage, name="homepage"),
    path("deptcreate/", views.Departmentview, name="dept"),
    path("deptupdate/<pk>/", views.deptupdate.as_view(), name="deptupdate"),
    path("deptdelete/<pk>/", views.deptdelete.as_view(), name="deptdelete"),
    path("deptlist/", views.deptlist.as_view(), name="deptlist"),
    path("usercreate/", views.Userview, name="usercreate"),
    path('ticketview/', views.TicketList.as_view(), name="ticketview"),
    path('ticketdetail/<int:pk>/', views.TicketDetail.as_view())


]

urlpatterns = format_suffix_patterns(urlpatterns)
