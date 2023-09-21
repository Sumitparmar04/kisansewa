from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate


class UserRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "mobile_no",
            "password",
            "city",
            "postal_code",
            "address",
        ]

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=100, style={"input_type": "password"}, write_only=True
    )
    password2 = serializers.CharField(
        max_length=100, style={"input_type": "password"}, write_only=True
    )

    class Meta:
        model = User
        fields = ["password", "password2"]

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        user = self.context.get("user")
        if password != password2:
            raise serializers.ValidationError(
                "Password and Confirm Password doesn't match"
            )
        user.set_password(password)
        user.save()
        return attrs


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "custuser",
            "name",
            "mobile",
            "pin",
            "adres",
            "locality",
            "city",
            "state",
        ]

    def to_representation(self, instance):
        self.fields["custuser"] = UserRegSerializer(read_only=True)
        return super(AddressSerializer, self).to_representation(instance)


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            "id",
            "blog_title",
            "blog_img",
            "blog_desc",
            "blog_topic",
            "created_at",
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "cat_name", "cat_img", "cat_desc"]


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Sub_Category
        fields = ["id", "category", "sub_cat_name", "sub_cat_img", "sub_cat_desc"]


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "company_name"]


class ProductSerializer(serializers.ModelSerializer):
    sub_cat = SubCategorySerializer()
    comapny_name = CompanySerializer()

    class Meta:
        model = Product
        fields = [
            "id",
            "sub_cat",
            "comapny_name",
            "pro_name",
            "pro_img",
            "pro_desc",
            "pro_price",
            "stock",
            "varient",
            "discount_price",
            "qty_type",
            "quantity",
        ]


class VolumeSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Volume
        fields = ["id", "product", "quanity", "price"]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "customer", "product", "quantity"]

    def to_representation(self, instance):
        self.fields["customer"] = UserRegSerializer(read_only=True)
        self.fields["product"] = ProductSerializer(read_only=True)
        return super(CartSerializer, self).to_representation(instance)


class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    address = AddressSerializer()

    class Meta:
        model = Order
        fields = [
            "id",
            "cart",
            "address",
            "order_id",
            "payment_id",
            "total_price",
        ]


class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = ["id", "test_title", "test_img", "test_desc"]


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_Us
        fields = ["id", "first_name", "last_name", "email", "mobile_no", "msg"]


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ["id", "about_title", "about_img", "about_desc"]
