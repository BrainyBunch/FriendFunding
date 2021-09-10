from rest_framework import serializers
from .models import User, Goal

class UserSerializer(serializers.ModelSerializer):
    goal = serializers.HyperlinkedRelatedField(
        view_name = 'goal_detail',
        many= True,
        read_only=True
    )
    class Meta:
        model = User
        fields = ('name', 'amountsaved', 'description', 'goal','id')

class GoalSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
    class Meta:
        model = Goal
        fields = ('user', 'description', 'cost', 'amountsaved', 'id', )