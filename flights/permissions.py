from rest_framework.permissions import BasePermission
from datetime import date,timedelta

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.user == request.user):
            return True
        return False


class IsFutureBooking(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.date > (date.today() + timedelta(days=3)):
            return True
        return False
