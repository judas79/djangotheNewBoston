# L39 convert class model into JSON for saving to a HD or sending over a network
from rest_framework import serializers
from .models import Stock

# L39 create name, using class from model + serializer, and pass in from rest_framework
# blueprint using serializers to convert Model to JSON
class StockSerializer(serializers.ModelSerializer):

    # L39 further ability to configure the fields passed in to StockSerializer
    class Meta:

        # specify which model we're serializing
        model = Stock

        # send the following fields upon request to user
        # fields = ('ticker', 'volume')

        # send all fields upon request from user
        fields = '__all__'





