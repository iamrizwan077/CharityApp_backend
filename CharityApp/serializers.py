from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from .models import Organization, CustomUser


user_types = (
    ('User', 'User'),
    ('Organization', 'Organization'),
)


class CustomRegisterSerializer(RegisterSerializer):
    user_type = serializers.ChoiceField(choices=user_types)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'user_type': self.validated_data.get('user_type', '')
        }


class CustomUserDetailsSerializer(UserDetailsSerializer):

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('user_type',)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    #     user = CustomUserSerializer()
    user = serializers.PrimaryKeyRelatedField(read_only=False, queryset = CustomUser.objects.all())

    class Meta:
        model = Organization
        fields = ['name', 'user', 'address', 'country',
                  'mission', 'description', 'image']

    # def create(self, validated_data):
    #     user_data = validated_data.pop('user')
    #     user = CustomUser.objects.create(**user_data)
    #     organization = Organization.objects.create(user=user, **validated_data)
    #     return organization
