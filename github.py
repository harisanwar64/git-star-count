"""
info: github util functions
@author: Haris Anwar <harisanwar64@gmail.com>
"""

import requests
from math import ceil
import pandas as pd


def get_header():
    header = {'Accept': 'application/vnd.github.v3.star+json',
              'Authorization': "Token " + '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'}
    return header

class GitService(object):

    def __init__(self):
        pass

    def check_repo_exists(self, repo):
        header = get_header()
        request_url = f"https://api.github.com/repos/{repo}"
        request_result = requests.get(request_url, headers=header)
        status_code = request_result.status_code
        if status_code == 200:
            return True
        else:
            return False

    def get_repo_star_count(self, repo):
        header = get_header()
        request_url = f"https://api.github.com/repos/{repo}"
        request_result = requests.get(request_url, headers=header).json()
        return request_result['stargazers_count']

    def get_repo_total_pages(self, repo):
        per_page = 100
        star_count = self.get_repo_star_count(repo)
        required_pages = ceil(star_count / per_page)
        return required_pages

    def get_repo_star_info_list(self, repo):
        total_pages = self.get_repo_total_pages(repo)
        header = get_header()
        star_info_list = []
        for page in range(1, total_pages):
            request_url = f"https://api.github.com/repos/{repo}/stargazers?per_page=100&page={page}"
            request_result = requests.get(request_url, headers=header).json()
            star_info_list.append(request_result)
        return star_info_list


if __name__ == "__main__":
    #todo: need to input repo from user (ui)
    repo = 'pytorch/kineto'
    star_list = GitService().get_repo_star_info_list(repo)
    dataframe = pd.DataFrame(star_list)