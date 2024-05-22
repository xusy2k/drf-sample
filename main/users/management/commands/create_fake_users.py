import logging
import time

from django.core.management.base import BaseCommand
from django.urls import reverse
from django.utils.translation import gettext as _
from faker import Faker

from ...models import User

log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = _("Create fake users")
    execute_update = False
    base_url = "http://localhost:8000"

    def add_arguments(self, parser):
        parser.add_argument(
            "-n",
            "--number",
            type=int,
            help=_("Number of fake users. Default: 100"),
        )
        parser.add_argument(
            "-c",
            "--curl",
            dest="curl",
            action="store_true",
            help=_("Show only curl command"),
        )
        parser.add_argument(
            "-s",
            "--server",
            dest="base_url",
            help=_("Set server URL. Default='%s'") % self.base_url,
        )

    @staticmethod
    def print_header(text):
        print("###########################################################")
        print("   %s" % text)
        print("###########################################################")

    def handle(self, *args, **kwargs):
        number_of_users = kwargs.get("number") or 10
        curl = bool(kwargs.get("curl"))
        base_url = kwargs.get("server") or self.base_url
        fake = Faker("es_ES")
        if curl:
            data = {
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "phone_number": fake.phone_number(),
                "email": fake.email(),
                "hobbies": fake.sentence(nb_words=30),
                "password": fake.password(),
            }
            url_signup = reverse("api:users:signup")

            result = [f"curl -X POST {base_url}{url_signup} "]
            for k, v in data.items():
                result.append(f"-F {k}='{v}' ")
            print("Create user")
            print("-" * 80)
            print(" ".join(result))
            print("")
            print("")

            print("Retrieve user")
            print("-" * 80)
            url_login = reverse("obtain_token")
            url_profile = reverse("api:users:profile")
            cmd_list = [
                "export token_json_tmp=`curl -X POST -d 'username=%(email)s&password=%(password)s' %(url)s 2> /dev/null`"  # noqa: E501
                % {
                    "email": data["email"],
                    "password": data["password"],
                    "url": "%s%s" % (base_url, url_login),
                },
                """export token_tmp=`echo ${token_json_tmp} | cut -f4 -d '"'`""",
                """curl -H "Authorization: Token ${token_tmp}" %(url)s""" % {"url": f"{base_url}{url_profile}"},
                """unset token_json_tmp; unset token_tmp """,
            ]
            print(";".join(cmd_list))
            print("")
            print("")
        else:
            t1 = time.time()
            user_count = 0
            for idx in range(number_of_users):
                kw = {
                    "first_name": fake.first_name(),
                    "last_name": fake.last_name(),
                    "phone_number": fake.phone_number(),
                    "email": fake.email(),
                    "hobbies": fake.sentence(nb_words=30),
                    "password": fake.password(),
                }
                try:
                    User.objects.create_user(**kw)
                    print(f"""{kw["email"]}\t{kw["password"]}""")
                    user_count += 1
                except Exception:
                    pass

            t2 = time.time()
            self.print_header(
                "Created %s new users in %0.3fs" % (user_count, (t2 - t1)),
            )
