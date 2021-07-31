from rest_framework import serializers
from rest_framework import fields
from rest_framework.fields import CharField
from .models import CheckList , CheckListItem

# class CheckListSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     is_deleted = serializers.BooleanField()
#     is_archived = serializers.BooleanField()
#     created_on = serializers.DateTimeField()
#     updated_on = serializers.DateTimeField()


#Another Way....



#Serializer for CheckListItem Model
class CheckListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckListItem
        fields = '__all__'


class CheckListSerializer(serializers.ModelSerializer):
    items = CheckListItemSerializer(source = 'checklistitem_set',many = True,read_only=True)
    class Meta:
        model = CheckList
        fields = '__all__'