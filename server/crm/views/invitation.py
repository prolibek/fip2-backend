from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db import transaction

from crm.models import Invitation, Member
from crm.permissions import IsTenantMember

class InvitationAPIView(APIView):
    permission_classes = [IsTenantMember, ]

    def post(self, request):
        emails = request.data.get("emails")
        if not isinstance(emails, list):
            return Response({
                "details": "Invalid data format: a list of emails is required."
            }, status=status.HTTP_400_BAD_REQUEST)

        organisation = request.tenant
        invitation_tokens = []

        with transaction.atomic():
            for email in emails:
                invitation = Invitation.create_invitation(
                    email=email,
                    organisation=organisation,
                    request=request
                )
                invitation_tokens.append(invitation.token)

        return Response({
            "tokens": invitation_tokens,
            "details": f"Invitations sent to {len(invitation_tokens)} emails."
        }, status=status.HTTP_201_CREATED)


class InvitationAcceptAPIView(APIView):
    def post(self, request):
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

        user_invitations = Invitation.objects.filter(email=request.user.email, is_used=False)
        for user_invitation in user_invitations:
            user_invitation.is_used = True
            user_invitation.save()

        Member.objects.create(
            user=request.user,
            organisation=invitation.organisation
        )

        return Response({
            "details": f"{request.user.email} succesfully added to {invitation.organisation.name}"
        })