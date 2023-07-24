# from django.forms import ValidationError
# from rest_framework import serializers
# from django.contrib.auth.models import User
# from django.contrib.auth.password_validation import validate_password
# from rest_framework.validators import UniqueValidator

# # Registration Serializers
# class UserRegistrationSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#         required = True,
#         validators=[UniqueValidator(queryset=User.objects.all())]
#     )

#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password], style={'input_type':'password'})
#     password2 = serializers.CharField(write_only=True, required=True, style={'input_type':'password'})


#     class Meta:
#         model = User
#         fields = ('username', 'password','password2', 'email', 'first_name','last_name')
#         extra_kwargs = {
#             'first_name': {'required':True},
#             'last_name': {'required':True},
#             'password': {'write_only':True}
#         }

# # validating password and confirm password while registration

# # def validate(self, attrs):
# #     if attrs['password'] != attrs['password2']:
# #         raise serializers.ValidationError[{'password':'Password not match'}]
# #     return attrs

# class UserLoginSerializers(serializers.ModelSerializer):
#     username = serializers.CharField(max_length=50)
#     class Meta:
#         model = User
#         field = ('username','password')