from django.shortcuts import render, get_object_or_404, redirect
from storage_app.models import Post, Picture, PrivatePost
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PostForm, PictureForm


# Import the exporter
import markdown
import nbformat
from nbconvert import HTMLExporter
from bs4 import BeautifulSoup

def home_page(request):
    return render(request, 'home.html', {})

@login_required
def all_posts(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "all_posts.html", context)


@login_required
def all_pictures(request):
    pics = Picture.objects.all().order_by('-created_on')
    context = {
        "pics": pics,
    }
    return render(request, "all_pictures.html", context)

def public_posts(request):
    posts = Post.objects.filter(public=True)
    context = {
        "posts": posts,
    }
    return render(request, "public_posts.html", context)

# def file_document_detail(request, uuid):
#     post = FileDocument.objects.get(uuid=uuid)
#     aws_url = post.content.url
#     file_on_aws = urlopen(aws_url).read().decode()
#     if post.document_type == "NOTEBOOK" :
#         # https://nbconvert.readthedocs.io/en/latest/nbconvert_library.html
#         # 2. Instantiate the exporter. We use the `basic` template
#             a_notebook = nbformat.reads(file_on_aws, as_version=4)
#             # 2. Instantiate the exporter. We use the `basic` template
#             html_exporter = HTMLExporter()
#             html_exporter.template_file = 'basic'
#             # 3. Process the notebook
#             (body, resources) = html_exporter.from_notebook_node(a_notebook)
#             # process titles for having a link for left menu and remove pilcrow
#             soup = BeautifulSoup(body, 'lxml')
#             for h in soup.find_all('h2'):
#                 oldstr = str(h['id'])
#                 titleh2 = oldstr.replace("-", " ")
#                 h.string = titleh2
#                 h['id'] = titleh2
#             for h in soup.find_all('h1'):
#                 old = str(h['id'])
#                 titleh1 = old.replace("-", " ")
#                 h.string = titleh1
#                 h['id'] = titleh1
#             for img in soup.findAll('img'):
#                 image_name = str(img['src'])[:3]
#                 try:
#                     pics = Picture.objects.get(name__startswith=image_name)
#                     print(pics.picture.url)
#                     img['src'] = pics.picture.url
#                 except:
#                     pass
#
#             output_html = soup.prettify()
#             # structure full left menu
#             dico = dict()
#             n = 0
#             for i in soup.find_all('h1'):
#                 n = n + 1
#                 a = 'node1' + str(n)
#                 dico[a] = i.text
#                 b = a + 'children'
#                 list = []
#                 for j in i.find_all_next():
#                     dico[b] = list
#                     if j.name == 'h1': break
#                     if j.name == "h2":
#                         list.append(j.text)
#             #f = open("log.txt", "a")
#             #f.write(output_html)
#             #f.close()
#             context = {
#                 "title": dico.get('node11'),
#                 "html_content": output_html,
#                 "htitles": dico,
#                 "created":post.created_on,
#                         }
#
#     return render(request, "file_document_detail.html", context)


def post_detail(request, uuid):
    post = Post.objects.get(uuid=uuid)
    #aws_url = post.content.url
    #file_on_aws = urlopen(aws_url).read().decode()
    print(post.content)
    soup = BeautifulSoup(post.content, 'lxml')
            # structure full left menu
    dico = dict()
    n = 0
    for i in soup.find_all('h1'):
                 n = n + 1
                 a = 'node1' + str(n)
                 dico[a] = i.text
                 b = a + 'children'
                 list = []
                 for j in i.find_all_next():
                     dico[b] = list
                     if j.name == 'h1': break
                     if j.name == "h2":
                         list.append(j.text)

    context = {
            "title":post.title,
            "htitles": dico,
            "post": post,
            "created": post.created_on,

    }
    return render(request, "post_detail.html", context)


@login_required
def post_form(request):
    form = PostForm(request.POST or None,  request.FILES or None)
    if form.is_valid():
        #instance.save()
        instance = form.instance
        if instance.public == False:
            p= PrivatePost(content=instance.content)
            print(instance.content)
            print(p.content)
            print(p.uuid)
            p.save()

        else:
            instance = form.save(commit=False)
            instance.save()

        messages.success(request, "Successfully created")
        return render(request, "home.html", {})
    context = {"form": form}
    return render(request, "post_form.html", context)

@login_required
def edit(request, uuid):
    post = Post.objects.get(uuid=uuid)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully modify")
        return render(request, "home.html", {})
    context = {"form": form}
    return render(request, "post_form.html", context)

@login_required
def delete(request, uuid):
    post = Post.objects.get(uuid=uuid)
    post.delete()
    messages.success(request, "Successfully deleted")
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "all_posts.html", context)




@login_required
def picture_form(request):
    form = PictureForm(request.POST or None,  request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #file_type = instance.url.split('.')[-1]
        #if file_type not in IMAGE_FILE_TYPES:
        #        return render(request, 'profile_maker/error.html')
        messages.success(request, "Successfully created")
        return render(request, "home.html", {})
    context = {"form": form}
    return render(request, "picture_form.html", context)

@login_required
def edit_picture(request, uuid):
    pic = Picture.objects.get(uuid=uuid)
    form = PictureForm(request.POST or None, request.FILES or None, instance=pic)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully modify")
        return render(request, "home.html", {})
    context = {"form": form}
    return render(request, "picture_form.html", context)

@login_required
def picture_detail(request, uuid):
    pic = Picture.objects.get(uuid=uuid)
    context = {"pic": pic}
    return render(request, "picture_detail.html", context)

@login_required
def delete_picture(request, uuid):
    pic = Picture.objects.get(uuid=uuid)
    pic.delete()
    messages.success(request, "Successfully deleted")
    pics = Picture.objects.all().order_by('-created_on')
    context = {
        "pics": pics,
    }
    return render(request, "all_pictures.html", context)



