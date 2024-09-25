from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "ThAnK yOu FoR vIsItInG mY sItE!",
    }
    return render(request, "home.html", context)

class AboutPageView(TemplateView):
    template_name = "about.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main St, Springfield, IL"
        context["phone_number"] = "555-555-5555"
        return context
    
class ProductsPageView(TemplateView):
    template_name = "products.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_list"] = [
            {"name": "Product 1", "price": 99.99},
            {"name": "Product 2", "price": 149.99},
            {"name": "Product 3", "price": 199.99},
            {"name": "Product 4", "price": 249.99},
        ]
        return context