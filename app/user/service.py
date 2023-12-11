from django.contrib.auth.tokens import PasswordResetTokenGenerator
from datetime import datetime

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                str(user.pk) + str(timestamp) + str(user.is_active)
        )


generate_token = TokenGenerator()


def save_picture(instance, filename):
    app_name = instance._meta.app_label
    model_name = instance._meta.model_name

    raw_date = datetime.now()
    formatted_date = raw_date.strftime("%Y-%m-%d %H:%M:%S")

    picture_name = "".join(
        [
            "".join(filename.split('.')[:-1]),
            formatted_date,
            ".",
            filename.split('.')[-1]
        ]
    )
    return (f"{app_name}/{model_name}/{instance.pk}/{instance.pk}_"
            f"{picture_name}")
