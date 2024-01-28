from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db import transaction

from crm.models import Invitation, Member

class InvitationAPIView(APIView):
    def post(self, request):
        email = request.data["email"]
        organisation = request.tenant

        with transaction.atomic():
            invitation = Invitation.create_invitation(
                email=email,
                organisation=organisation
            )

        return Response({
            "token": invitation.token,
            "details": "Invitation sent to an email."
        }, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        token = request.data.get("token")
        
        if not token:
            return Response({
                "details": "Token must be provided."
            }, status=status.HTTP_403_FORBIDDEN)
        
        try: 
            invitation = Invitation.objects.get(token=token)
        except Invitation.DoesNotExist:
            return Response({
                "details": "Invitation not found or expired."
            }, status=status.HTTP_404_NOT_FOUND)
        
        if invitation.is_used:
            return Response({
                "details": "Invitation is already used."
            }, status=status.HTTP_403_FORBIDDEN)

        if invitation.email != request.user.email:
            return Response({
                "details": "Invitation is not for this user."
            }, status=status.HTTP_403_FORBIDDEN)

        invitation.is_used = True 
        invitation.save()

        member = Member.objects.create(
            user=request.user,
            organisation=invitation.organisation
        )
        member.save()

        return Response({
            "details": f"{request.user.email} succesfully added to {invitation.organisation.name}"
        })