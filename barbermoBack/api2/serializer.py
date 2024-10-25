
from api2.models import Barber
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class BarberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barber
        fields = ('id', 'name','money','t1','t2','t3','t4','t5','t6','t7','t8','t9','t10','t11','t12','t13','t14','t15','t16','t17','t18','t19','t20','t21','t22','t23','t24')

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # These are claims, you can add custom claims
        token['id'] = user.id
        token['name'] = user.name
        token['money'] = user.money
        token['t1'] = user.t1
        token['t2'] = user.t2
        token['t3'] = user.t3
        token['t4'] = user.t4
        token['t5'] = user.t5
        token['t6'] = user.t6
        token['t7'] = user.t7
        token['t8'] = user.t8
        token['t9'] = user.t9
        token['t10'] = user.t10
        token['t11'] = user.t11
        token['t12'] = user.t12
        token['t13'] = user.t13
        token['t14'] = user.t14
        token['t15'] = user.t15
        token['t16'] = user.t16
        token['t17'] = user.t17
        token['t18'] = user.t18
        token['t19'] = user.t19
        token['t20'] = user.t20
        token['t21'] = user.t21
        token['t22'] = user.t22
        token['t23'] = user.t23
        token['t24'] = user.t24
        
        return token


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Barber
        fields = ('id', 'name','money','t1','t2','t3','t4','t5','t6','t7','t8','t9','t10','t11','t12','t13','t14','t15','t16','t17','t18','t19','t20','t21','t22','t23','t24')


    def create(self, validated_data):
        barber = Barber.objects.create(
            id = validated_data['id'],
            name = validated_data['name'],
            money = validated_data['money'],
            t1 = validated_data['t1'],
            t2 = validated_data['t2'],
            t3 = validated_data['t3'],
            t4 = validated_data['t4'],
            t5 = validated_data['t5'],
            t6 = validated_data['t6'],
            t7 = validated_data['t7'],
            t8 = validated_data['t8'],
            t9 = validated_data['t9'],
            t10 = validated_data['t10'],
            t11 = validated_data['t11'],
            t12 = validated_data['t12'],
            t13 = validated_data['t13'],
            t14 = validated_data['t14'],
            t15 = validated_data['t15'],
            t16 = validated_data['t16'],
            t17 = validated_data['t17'],
            t18 = validated_data['t18'],
            t19 = validated_data['t19'],
            t20 = validated_data['t20'],
            t21 = validated_data['t21'],
            t22 = validated_data['t22'],
            t23 = validated_data['t23'],
            t24 = validated_data['t24'],

        )

        barber.save()

        return barber