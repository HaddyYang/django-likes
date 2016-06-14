# django-likes
this is a app for django. It can liked or unliked something (comments, blog, and so on)

<b>How to use</b>:
1、Download and copy into you Django project.
2、Add this app into settings.py
<pre>INSTALLED_APPS = [
        'likes',
        #others...
    ]</pre>

3、Add this app urls into project's urls
<pre>urlpatterns = [
        url(r'^admin/', admin.site.urls),
        #open project's urls.py add this code
        url(r'^likes/', include('likes.urls')),
    ]</pre>

4、you can use it by ajax. request url link
    <pre>/likes/likes_change?type=blog&id=1&direct=1</pre>
    to add a likes in blog that blog id is 1.
   
    <pre>/likes/likes_change?type=blog&id=1&direct=-1</pre>
    to remove a likes
