from rest_framework import serializers
from ..models import Pant_list , Store_list


class PantSerializer (serializers.ModelSerializer):
    class Meta :
        model = Pant_list
        fields = '__all__'

class StoreSerializer (serializers.ModelSerializer):
    # store_list = PantSerializer (many = True , read_only = True)
    # store_list = serializers.StringRelatedField (many = True )
    # store_list = serializers.PrimaryKeyRelatedField (many = True  , read_only = True)
    store_list = serializers.HyperlinkedRelatedField (many = True  , read_only = True , view_name='pant_detail')
    
    class Meta:
        model = Store_list
        fields = '__all__'