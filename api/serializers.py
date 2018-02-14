from rest_framework import serializers
from receipts.models import Receipt, Category

class ReceiptSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Receipt
        fields = ('id', 'category', 'name', 'scan', 'amount', 'date_created',
                'date_updated')


