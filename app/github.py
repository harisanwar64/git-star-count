"""
info: github util functions
@author: Haris Anwar <harisanwar64@gmail.com>
"""

import requests
from math import ceil
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from config import GitConfig


def get_header():
    header = {'Accept': GitConfig.GIT_DEV_VERSION, 'Authorization': "Token " + GitConfig.GIT_API_TOKEN}
    return header


class GitService(object):

    def __init__(self):
        pass

    def check_repo_exists(self, repo):
        header = get_header()
        request_url = f"{GitConfig.GIT_API_URL}/repos/{repo}"
        request_result = requests.get(request_url, headers=header)
        status_code = request_result.status_code
        if status_code == 200:
            return True
        else:
            return False

    def get_repo_star_count(self, repo):
        header = get_header()
        request_url = f"{GitConfig.GIT_API_URL}/repos/{repo}"
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
        for page in range(1, total_pages + 1):
            request_url = f"{GitConfig.GIT_API_URL}/repos/{repo}/stargazers?per_page=100&page={page}"
            request_result = requests.get(request_url, headers=header).json()
            star_info_list.extend(request_result)
        return star_info_list

    def get_repo_star_info_dataframe(self, repo):
        star_list = self.get_repo_star_info_list(repo)
        dataframe = pd.DataFrame(star_list)
        dataframe = (dataframe["user"].apply(pd.Series).merge(dataframe, left_index=True, right_index=True))
        return dataframe

    def extract_df_datetime_column_to_list(self, dataframe):
        time_list = list(pd.to_datetime(dataframe.starred_at))
        return time_list

    def draw_plot_for_dataframe(self, dataframe, repo):
        time_list = self.extract_df_datetime_column_to_list(dataframe)
        ax = plt.axes()
        img = BytesIO()
        ax.plot(time_list, dataframe.index, label=repo)
        plt.savefig(img, format='png')
        plt.close()
        star_history_plot = base64.b64encode(img.getvalue()).decode('utf8')
        return star_history_plot


if __name__ == "__main__":
    # todo: need to add try catch exceptions for above github functions for error handling
    repo = 'pytorch/probot'
    df = GitService().get_repo_star_info_dataframe(repo)
    # print(df)
