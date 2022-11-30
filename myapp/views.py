from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .models import Product

# Create your views here.


def product(request):
    page_obj = products = Product.objects.all()
    product_name = request.GET.get('product_name')
    if product_name != '' and product_name is not None:
        page_obj = products.filter(name__icontains=product_name)

    paginator = Paginator(page_obj, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }
    # when you decide to use the fn base view rema to use a for loop in html as
    # for product in page_obj ...
    return render(request, 'myapp/index.html', context)
# class based view for the above product view[ListView]


class ProdutListView(ListView):
    model = Product
    template_name = 'myapp/index.html'
    context_object_name = 'products'
    paginate_by = 3


def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product': product
    }
    return render(request, 'myapp/details.html', context)
# class based view for the above product detail view[DetailView]


class ProductDetailView(DetailView):
    model = Product
    template_name = 'myapp/details.html'
    context_object_name = 'product'


@login_required
def add_product(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
        seller_name = request.user
        product = Product(name=name, price=int(price), desc=desc,
                          image=image, seller_name=seller_name)
        product.save()
    return render(request, 'myapp/addProduct.html')
# class based view for creating a user[CreateView]


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price', 'desc', 'image', 'seller_name']
    # template must be create and named as: product_form.html
    # Also define get_absolute_url in the Product Model for redirecting


def update_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == "POST":
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.desc = request.POST.get('desc')
        product.image = request.FILES['upload']
        product.save()
        return redirect('/myapp/products/')

    context = {
        'product': product
    }
    return render(request, 'myapp/update.html', context)
# class based view for updating product[UpdateView]


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price', 'desc', 'image', 'seller_name']
    template_name_suffix = '_update_form'
    # You can give a template sufix as it starts with product_
    # Also define get_absolute_url in the Product Model for redirecting


def delete_product(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product': product
    }

    if request.method == "POST":
        product.delete()
        return redirect('/myapp/products/')

    return render(request, 'myapp/delete.html', context)
# class based for deleting a product [DeleteView]


class ProductDeteleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('myapp:products')
    # Here the success_url deletes the selected product and redirects the user


@login_required
def mylistings(request):
    products = Product.objects.filter(seller_name=request.user)
    context = {
        'products': products,
    }

    return render(request, 'myapp/mylistings.html', context)
