from rest_framework import views
from rest_framework.response import Response
from users.models import UserOrganisationMembership
from users.serializers import UserOrganisationMembershipSerializer  # Update with your actual app name

class UserOrganisations(views.APIView):
    def get(self, request):
        memberships = UserOrganisationMembership.objects.filter(user=request.user)
        serializer = UserOrganisationMembershipSerializer(memberships, many=True)
        return Response(serializer.data)
