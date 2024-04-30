from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='department.name', read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'registration_number', 'first_name', 'last_name', 'email', 'date_of_birth', 'department',
                  'enrollment_date']


class AddOrUpdateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'registration_number', 'first_name', 'last_name', 'email', 'date_of_birth', 'department',
                  'enrollment_date']
