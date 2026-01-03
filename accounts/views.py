# users/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# ساخت توکن JWT
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }

# API ورود یا ثبت‌نام با شماره موبایل
@api_view(["POST"])
def login_or_register(request):
    phone_number = request.data.get("phone_number")
    if not phone_number:
        return Response({"error": "شماره موبایل الزامی است"}, status=400)

    # اگر کاربر وجود نداشت بساز
    user, created = CustomUser.objects.get_or_create(phone_number=phone_number)

    # ساخت توکن JWT
    tokens = get_tokens_for_user(user)

    return Response({
        "user": UserSerializer(user).data,
        "new_user": created,
        "tokens": tokens
    })
