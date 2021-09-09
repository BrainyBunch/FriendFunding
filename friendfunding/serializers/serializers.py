# from rest_framework import serializers
# from .models import User, Goal

# class UserSerializer(serializers.ModelSerializer):
#     user = serializers.HyperlinkedRelatedField(
#         view_name = 'song_detail',
#         many= True,
#         read_only=True
#     )
#     class Meta:
#         model = User
#         fields = ('id', 'title', 'description', 'completed')