# django-likes
<p>this is a app for django. It can liked or unliked something (comments, blog, and so on)</p>

<b>How to use</b>:
<p>1、Download and copy into you Django project.</p>
<p>2、Add this app into settings.py</p>
<pre>INSTALLED_APPS = [
        'likes',
        #others...
    ]</pre>

<p>3、Add this app urls into project's urls</p>
<pre>urlpatterns = [
        url(r'^admin/', admin.site.urls),
        #open project's urls.py add this code
        url(r'^likes/', include('likes.urls')),
    ]</pre>

<p>4、update you django database</p>
<pre>python manager.py makemigrations
python manager.py migrate</pre>

<p>5、you can use it by ajax. request url link</p>
    <pre>/likes/likes_change?type=blog&id=1&direct=1</pre>
    <p>to add a likes in blog that blog id is 1.</p>
   
    <pre>/likes/likes_change?type=blog&id=1&direct=-1</pre>
    <p>to remove a likes</p>
