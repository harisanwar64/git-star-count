"""
info: github configuration information
@author: Haris Anwar <harisanwar64@gmail.com>
"""


class GitConfig:
    DEBUG = False
    GIT_API_URL = "https://api.github.com"
    GIT_USERNAME = '***********'
    GIT_API_TOKEN = '******************'
    # version required for timestamp information of star
    GIT_DEV_VERSION = 'application/vnd.github.v3.star+json'


def get_config() -> GitConfig:
    pass
