from django.urls import path

from blog.views.comment import CommentCreate
from blog.views.home import home
from blog.views.post import PostView, PostCreate, PostUpdate, PostDelete
from django.conf.urls.static import static
from mysite import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "blog"
urlpatterns = [
    path("", home, name="home"),
    path("<str:username>", home, name="user_posts"),
    path("post/<int:pk>/", PostView.as_view(), name="post"),
    path("post/create/", PostCreate.as_view(), name="create_post"),
    path("post/create/<int:pk>/update", PostUpdate.as_view(), name="update_post"),
    path("post/<int:pk>/delete/", PostDelete.as_view(), name="delete_post"),
    path("post/<int:pk>/comment/", CommentCreate.as_view(), name="create_comment"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
