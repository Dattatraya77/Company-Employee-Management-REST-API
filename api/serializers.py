from rest_framework import serializers
from api.models import Company, Employee



class CompanySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.CharField(source="company.company_id", read_only=True)
    # id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"