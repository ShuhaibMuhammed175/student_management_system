from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer, AddOrUpdateStudentSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class AddStudentAPIView(APIView):
    permission_classes = [IsAdminUser & IsAuthenticated]

    def post(self, request):
        try:
            if isinstance(request.data, list):
                serializer = AddOrUpdateStudentSerializer(data=request.data, many=True)
            else:
                serializer = AddOrUpdateStudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class all_students(APIView):
    permission_classes = [IsAdminUser & IsAuthenticated]

    def get(self, request):
        try:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class StudentUpdateAPIView(APIView):
    permission_classes = [IsAdminUser & IsAuthenticated]

    def put(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = AddOrUpdateStudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class StudentDetailAPIView(APIView):
    permission_classes = [IsAdminUser & IsAuthenticated]

    def get(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class StudentDeleteAPIView(APIView):
    permission_classes = [IsAdminUser & IsAuthenticated]

    def delete(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            student.delete()
            return Response({'message': 'Successfully Deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
