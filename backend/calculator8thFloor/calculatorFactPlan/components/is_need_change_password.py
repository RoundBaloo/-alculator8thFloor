from ..models import LastPasswordChangeDate
from datetime import date

class ChangePassword:
    def get_need_change_password(user):
        if user.is_superuser:
                last_password_change = LastPasswordChangeDate.objects.get(username=user.username)
                return (date.today() - last_password_change.last_password_change_date).days > 90
        return False