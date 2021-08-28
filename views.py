from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect

from .models import Category,SubCategory
from .forms import CategoryForm

def index(request):
    all_categories = Category.objects.all()    #retrive all categories
    context = {'all_categories': all_categories}
    return render(request, 'categories/index.html', context)


def detail_category(request, pk):
    category = get_object_or_404(Category, pk=pk)   #retrive single category
    return render(request, 'categories/detail.html', {'category': category})

#create   
def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('categories:detail', pk=category.pk)
    else:
        form = CategoryForm()
    return render(request, 'categories/add.html', {'form': form})

#update
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('categories:detail', pk=category.pk)
    else:
        form = CategoryForm()
    return render(request, 'categories/edit.html', {'form': form})

#delete
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories:index')