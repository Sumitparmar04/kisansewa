from django.urls import path
from .views import *
from django.conf.urls.static import static


urlpatterns = [
    path("RegisterApi/", RegisterApi.as_view()),
    path("LoginApi/", LoginApi.as_view()),
    path('changepassword/', Change_Password_View.as_view()),
    path("address/", Post_Address.as_view()),
    path("getaddress/", Get_Address.as_view()),
    path("blog/", Blog_View.as_view()),
    path("blogdetail/", Blog_View_Detail.as_view()),
    path("category/", Category_View.as_view()),
    path("subcategory/", SubCategory_View.as_view()),
    path("product/", Product_View.as_view()),
    path("productdetail/", Product_View_Detail.as_view()),
    path("volume/", Volume_View.as_view()),
    path("company/", Company_View.as_view()),
    path("getcart/", Get_CartAPI.as_view()),
    path("postcart/", Post_CartAPI.as_view()),
    path("deletecart/<int:pk>", Delete_Cart.as_view()),
    path('getorder/', Get_OrderAPI.as_view()),
    path("placeorder/", Post_Place_OrderAPI.as_view()),
    path("patchorder/", Patch_Order_API.as_view()),
    path("tesimonials/", Testimonials_View.as_view()),
    path("contactus/", ContactUs_View.as_view()),
    path("aboutus/", AboutUs_View.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
