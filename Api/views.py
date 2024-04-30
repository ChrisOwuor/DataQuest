from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Api.models import Department, LegalInstrument, Service
from Api.serializers import DepartmentSerializer, LegalInstrumentSerializer, ServiceSerializer

# Create your views here.


class AddData(APIView):

    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True).data

        for item in serializer:
            department = Department.objects.get(id=item['dept'])
            legal_policy = LegalInstrument.objects.get(
                id=item['legal_instrument'])
            item["dept_details"] = DepartmentSerializer(department).data
            item['policy'] = LegalInstrumentSerializer(legal_policy).data

            item.pop('dept')
            item.pop('legal_instrument')

        return Response({"data": serializer, "msg": "success"}, status=status.HTTP_200_OK)

    def post(self, request):
        try:

            dept_info_data = {
                "dept_name": request.data['dept_name'],
                "owner": request.data['owner']
            }

            dept_serializer = DepartmentSerializer(data=dept_info_data)

            if dept_serializer.is_valid():
                department_instance = dept_serializer.save()
            else:
                return Response(dept_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            policy_data = request.data['policy']
            policy_info = {
                "name": policy_data.get('name'),
                "requires_change": policy_data.get('requireChange'),
                "change_text": policy_data.get('requiredDescription')
            }
            if policy_info:
                legal_instrument_serializer = LegalInstrumentSerializer(
                    data=policy_info)
                if legal_instrument_serializer.is_valid():
                    legal_instance = legal_instrument_serializer.save()
                else:
                    return Response(legal_instrument_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            for service_data in request.data.get('services', []):

                service_info = {
                    'dept': department_instance.id,
                    'legal_instrument': legal_instance.id,
                    "status": service_data['status'],
                    "timeline": service_data['timeline'],
                    "ecitizen": service_data['ecitizen'],
                    "enhancement": service_data['enhancement'],
                    'service_name': service_data['name']


                }
                service_serializer = ServiceSerializer(data=service_info)
                if service_serializer.is_valid():
                    service_serializer.save()
                else:
                    return Response(service_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({"msg": "success"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
