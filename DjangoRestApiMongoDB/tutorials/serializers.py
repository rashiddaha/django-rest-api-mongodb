from rest_framework import serializers 
from tutorials.models import Tutorial, Teacher

 
# Serializer for Tutorial Model
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')


# Serializer for Teacher Model

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model= Teacher
        fields = (
            'id',
            'name',
            'professional',
            'age'
        )

