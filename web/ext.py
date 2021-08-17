from django.conf import settings


def ip_check(ip):
    ip_list = open(settings.BASE_DIR / "ip.txt", "r").readlines()
    if ip not in ip_list:
        return False
    else:
        return True
