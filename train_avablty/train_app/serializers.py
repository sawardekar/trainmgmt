from rest_framework import serializers
from .models import Train, SeatAvabilty,Compartment, STATUS


class TrainSerializer(serializers.ModelSerializer):
    train_name = serializers.CharField(max_length=120,required=False,allow_blank=True)
    schedule_date = serializers.DateTimeField(required=False,input_formats=None)

    class Meta:
        model = Train
        fields = "__all__"


class CompartmentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=120,required=False,allow_blank=True)

    class Meta:
        model = Compartment
        fields = "__all__"


class SeatAvabiltySerializer(serializers.ModelSerializer):
    comp_id = serializers.SlugRelatedField(slug_field='comp_id', queryset=Compartment.objects.all())
    train_id = serializers.SlugRelatedField(slug_field='train_id', queryset=Train.objects.all())
    seat_no = serializers.CharField(max_length=10,required=False,allow_null=True)
    status = serializers.ChoiceField(choices=STATUS,required=False,allow_blank=True, default="Open")
    user_name = serializers.CharField(max_length=200,required=False,allow_blank=True)
    user_pancard = serializers.CharField(max_length=15,required=False,allow_blank=True)
    user_mobile = serializers.IntegerField(required=False,allow_null=True)

    class Meta:
        model = SeatAvabilty
        fields = "__all__"

