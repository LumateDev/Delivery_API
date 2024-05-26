from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DeliveryDepartment, Courier
from .serializers import DeliveryDepartmentSerializer, CourierSerializer


class CourierActionAPIView(APIView):

    def get(self, request):
        courier_id = request.query_params.get('external_id')
        if courier_id:
            try:
                courier = Courier.objects.get(external_id=courier_id)
                serializer = CourierSerializer(courier)
                return Response({'couriers': serializer.data})
            except Courier.DoesNotExist:
                return Response({'error': 'Courier not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            couriers = Courier.objects.all()
            serializer = CourierSerializer(couriers, many=True)
            return Response({'couriers': serializer.data})

    def post(self, request):
        data = request.data
        action = data.get('action')
        debug = f"{data}\n{action}"
        print(debug)

        if action == 11:  # Добавление курьера
            serializer = CourierSerializer(data=data.get('courier'))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif action == 12:  # Обновление курьера
            courier_data = data.get('courier')
            try:
                courier = Courier.objects.get(external_id=courier_data.get('external_id'))
                serializer = CourierSerializer(courier, data=courier_data, partial=True)  # частичное обновление
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Courier.DoesNotExist:
                return Response({'error': 'Courier not found'}, status=status.HTTP_404_NOT_FOUND)

        elif action == 13:  # Удаление курьера
            courier_id = data.get('courier', {}).get('external_id')
            try:
                courier = Courier.objects.get(external_id=courier_id)
                courier.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Courier.DoesNotExist:
                return Response({'error': 'Courier not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'error': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)


class DeliveryDepartmentActionAPIView(APIView):
    def get(self, request):
        department_id = request.query_params.get('external_id')
        if department_id:
            try:
                department = DeliveryDepartment.objects.get(external_id=department_id)
                serializer = DeliveryDepartmentSerializer(department)
                return Response({'departments': serializer.data})
            except DeliveryDepartment.DoesNotExist:
                return Response({'error': 'Delivery Department not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            departments = DeliveryDepartment.objects.all()
            serializer = DeliveryDepartmentSerializer(departments, many=True)
            return Response({'departments': serializer.data})

    def post(self, request):
        data = request.data
        action = data.get('action')
        debug = f"{data}\n{action}"
        print(debug)


        if action == 11:
            serializer = DeliveryDepartmentSerializer(data=data.get('department'))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif action == 12:
            department_data = data.get('department')
            try:
                department = DeliveryDepartment.objects.get(external_id=department_data.get('external_id'))
                serializer = DeliveryDepartmentSerializer(department, data=department_data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except DeliveryDepartment.DoesNotExist:
                return Response({'error': 'Delivery Department not found'}, status=status.HTTP_404_NOT_FOUND)

        elif action == 13:
            department_id = data.get('department', {}).get('external_id')
            try:
                department = DeliveryDepartment.objects.get(external_id=department_id)
                department.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except DeliveryDepartment.DoesNotExist:
                return Response({'error': 'Delivery Department not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'error': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)
