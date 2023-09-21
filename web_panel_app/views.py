from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth import login
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.db.models import Q
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
import razorpay
from django.conf import settings
import json


media = settings.MEDIA_URL

client = razorpay.Client(
    auth=(settings.RAZORPAY_CLIENT_ID, settings.RAZORPAY_CLIENT_SECRET)
)


class RegisterApi(APIView):
    def post(self, request, format=None):
        serializer = UserRegSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            if user is not None:
                return Response(
                    {
                        "message": "Registration successful & token Generated",
                        "data": serializer.data,
                        "token": str(token),
                        "status": status.HTTP_200_OK,
                    }
                )
        return Response(
            {
                "msg": "something went wrong",
                "error": serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST,
            }
        )


class LoginApi(APIView):
    def post(self, request, format=None):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = (
            User.objects.filter(
                Q(username=username) | Q(mobile_no=username) | Q(email=username)
            )
            .exclude(delete_status=1)
            .first()
        )
        if user is not None:
            usr = authenticate(username=user.username, password=password)
            if usr:
                token, created = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response(
                    {
                        "message": "Login successful & token Generated",
                        "id": user.id,
                        "username": username,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "email": user.email,
                        "mobile_no": user.mobile_no,
                        "token": str(token),
                        "status": status.HTTP_200_OK,
                    }
                )
        return Response(
            {
                "msg": "Invalid credentials",
                "status": status.HTTP_401_UNAUTHORIZED,
            }
        )


class Change_Password_View(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, formate=None):
        serializer = ChangePasswordSerializer(
            data=request.data, context={"user": request.user}
        )
        if serializer.is_valid(raise_exception=True):
            return Response(
                {
                    "message": "Password changed successfully",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                }
            )
        return Response(
            {
                "message": "Something Went Wrong",
                "errors": serializer.errors,
                "status": status.HTTP_404_NOT_FOUND,
            }
        )


class Post_Address(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Your data is updated",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                }
            )

        return Response(
            {
                "message": "Something went wrong",
                "error": serializer.errors,
            }
        )


class Get_Address(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        usr = Address.objects.filter(custuser=user)
        serializer = AddressSerializer(usr, many=True)
        return Response(
            {
                "msg": "your data is here",
                "data": serializer.data,
                "status": status.HTTP_200_OK,
            }
        )


class Blog_View(APIView):
    def get(self, request):
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many=True)
        return Response(
            {
                "msg": "your data is here",
                "data": serializer.data,
                "status": status.HTTP_200_OK,
            }
        )


class Blog_View_Detail(APIView):
    def get(self, request):
        id = request.GET.get("id")
        if id is not None and id != "":
            blog = Blog.objects.filter(id=id)
        serializer = BlogSerializer(blog, many=True)
        return Response(
            {
                "msg": "your data is here",
                "data": serializer.data,
                "status": status.HTTP_200_OK,
            }
        )


class Category_View(APIView):
    def get(self, request):
        cat = Category.objects.all()
        serializer = CategorySerializer(cat, many=True)
        return Response(
            {
                "msg": "your data is here",
                "data": serializer.data,
                "status": status.HTTP_200_OK,
            }
        )


class SubCategory_View(APIView):
    def get(self, request):
        sub_cat = Sub_Category.objects.all()
        serializer = SubCategorySerializer(sub_cat, many=True)
        return Response(
            {
                "msg": "your data is here",
                "data": serializer.data,
                "status": status.HTTP_200_OK,
            }
        )


class Product_View(APIView):
    def get(self, request):
        cat_id = request.GET.get("cat_id")
        if cat_id is not None and cat_id != "":
            sub_category = Sub_Category.objects.filter(id=cat_id)
            pro = Product.objects.filter(sub_cat__in=sub_category)
        else:
            pro = Product.objects.all()
        serializer = ProductSerializer(pro, many=True)
        return Response(
            {
                "msg": "your data is here",
                "data": serializer.data,
                "status": status.HTTP_200_OK,
            }
        )


class Product_View_Detail(APIView):
    def get(self, request):
        id = request.GET.get("id")
        if id is not None and id != "":
            pro = Product.objects.filter(id=id)
        serializer = ProductSerializer(pro, many=True)
        return Response(
            {
                "msg": "your data is here",
                "data": serializer.data,
                "status": status.HTTP_200_OK,
            }
        )


class Volume_View(APIView):
    def get(self, request):
        vol = Volume.objects.all()
        serializer = VolumeSerializer(vol, many=True)
        return Response(
            {
                "msg": "your data is here",
                "data": serializer.data,
                "status": status.HTTP_200_OK,
            }
        )


class Company_View(APIView):
    def get(self, request):
        vol = Company.objects.all()
        serializer = CompanySerializer(vol, many=True)
        return Response(
            {
                "msg": "your data is here",
                "data": serializer.data,
                "status": status.HTTP_200_OK,
            }
        )


class Get_CartAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        cart = Cart.objects.filter(customer=user, delete_status=0)
        serializer = CartSerializer(cart, many=True)
        return Response(
            {
                "msg": "your data is here",
                "data": serializer.data,
                "status": status.HTTP_200_OK,
            }
        )


class Post_CartAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "msg": "your data is here",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                }
            )
        return Response(
            {
                "msg": "Something went wrong",
                "error": serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST,
            }
        )


class Delete_Cart(APIView):
    def delete(self, request, pk):
        cart = Cart.objects.filter(pk=pk)
        cart.delete()
        return Response({"message": "Your data is deleted"})


class Get_OrderAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user_cart = list(Cart.objects.filter(customer=request.user).values_list("id"))
        order = Order.objects.filter(cart__in=user_cart)
        serializer = OrderSerializer(order, many=True)
        return Response(
            {
                "msg": "your data is here",
                "key": settings.RAZORPAY_CLIENT_ID,
                "Company": "AgroStore",
                "data": serializer.data,
                "status": status.HTTP_200_OK,
            }
        )


class Post_Place_OrderAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart = request.POST.get("cart")
        if cart is not None or cart != "":
            res = json.loads(cart)
            a = client.order.create(
                {
                    "currency": "INR",
                    "amount": int(res["total_price"]) * 100,
                }
            )
            for i in res["cart"]:
                Order.objects.create(
                    cart_id=i,
                    order_id=a["id"],
                    total_price=res["total_price"],
                    address_id=res["address"],
                )
                cart = Cart.objects.filter(id=i).update(delete_status=1)
            order = Order.objects.filter(order_id=a["id"]).first()
            order1 = Order.objects.filter(order_id=a["id"])
            serializer = OrderSerializer(order1, many=True)

            return Response(
                {
                    "msg": "Your data is added",
                    "key": settings.RAZORPAY_CLIENT_ID,
                    "Company": "AgroStore",
                    "a": a,
                    "order_id": order.order_id,
                    "data": serializer.data,
                    "status": status.HTTP_201_CREATED,
                }
            )
        else:
            return Response(
                {
                    "msg": "Something went wrong",
                    "status": status.HTTP_400_BAD_REQUEST,
                }
            )


class Patch_Order_API(APIView):
    def patch(self, request):
        order_ids = request.data.getlist("order_id")
        ords = Order.objects.filter(order_id__in=order_ids).all()
        if ords is not None or ords != "":
            for i in ords:
                i.payment_id = request.POST.get("payment_id")
                i.save()
            # ords1 = Order.objects.filter(order_id__in=order_ids).all()
            serializer = OrderSerializer(ords, many=True)
            return Response(
                {
                    "msg": "Your Data is Updated",
                    "data": serializer.data,
                    "status": status.HTTP_206_PARTIAL_CONTENT,
                }
            )
        else:
            return Response(
                {
                    "msg": "Something went wrong",
                    "status": status.HTTP_400_BAD_REQUEST,
                }
            )


class Testimonials_View(APIView):
    def get(self, request):
        testi = Testimonials.objects.all()
        serializer = TestimonialsSerializer(testi, many=True)
        return Response(
            {
                "msg": "your data is here",
                "data": serializer.data,
                "status": status.HTTP_200_OK,
            }
        )


class ContactUs_View(APIView):
    def post(self, request):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "msg": "Your data is added",
                    "data": serializer.data,
                    "status": status.HTTP_201_CREATED,
                }
            )
        return Response(
            {
                "msg": "Something went wrong",
                "error": serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST,
            }
        )


class AboutUs_View(APIView):
    def get(self, request):
        about = AboutUs.objects.all()
        serializer = AboutUsSerializer(about, many=True)
        return Response(
            {
                "msg": "your data is here",
                "data": serializer.data,
                "status": status.HTTP_200_OK,
            }
        )
