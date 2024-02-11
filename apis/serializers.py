from rest_framework import serializers
from todos import models

class TodoSerilizer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id','title','description'
        )
        #  import our desired model and specify which fields we want exposed 
        model = models.Todo