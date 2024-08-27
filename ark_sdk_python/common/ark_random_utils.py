import string
from ipaddress import IPv4Address
import secrets


class ArkRandomUtils:
    @staticmethod
    def random_ip_address():
        secrets.SystemRandom().seed(secrets.SystemRandom().randint(1, 10001))
        return str(IPv4Address(secrets.SystemRandom().getrandbits(32)))

    @staticmethod
    def random_string(n=8):
        return ''.join(secrets.SystemRandom().choices(string.ascii_letters, k=n))

    @staticmethod
    def random_password(n=10):
        return ''.join(
            secrets.SystemRandom().choices(string.digits, k=1)
            + secrets.SystemRandom().choices(string.ascii_lowercase, k=1)
            + secrets.SystemRandom().choices(string.ascii_uppercase, k=1)
            + secrets.SystemRandom().choices(string.ascii_letters + string.digits, k=n - 3)
        )
