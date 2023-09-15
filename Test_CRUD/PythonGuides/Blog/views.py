from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog

# Add Blog

def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('search/')
            except:
                pass
    else:
        form = BlogForm()
    return render(request, 'create.html', {'form':form})

# Search Blog
        
def retrieve_blog(request):
    blogs = Blog.objects.all()
    return render(request,'search.html',{'blogs':blogs} )

# Update Blog

def update_blog(request,pk):
    blogs = Blog.objects.get(id=pk)
    form = BlogForm(instance=blogs)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blogs)
        if form.is_valid():
            form.save()
            return redirect('/search')

    context = {
        'blogs': blogs,
        'form': form,
    }
    return render(request,'update.html',context)

# Delete Blog

def delete_blog(request, pk):
    blogs = Blog.objects.get(id=pk)

    if request.method == 'POST':
        blogs.delete()
        return redirect('/search')

    context = {
        'blogs': blogs,
    }
    return render(request, 'remove.html', context)




