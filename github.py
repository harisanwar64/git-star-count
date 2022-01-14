import requests


class GitService(object):

    def __init__(self):
        pass

    def check_repo_exists(self, repo):
        header = {'Accept': 'application/vnd.github.v3.star+json',
                  'Authorization': "Token " + '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'}
        request_url = f"https://api.github.com/repos/{repo}"
        request_result = requests.get(request_url, headers=header)
        status_code = request_result.status_code
        if status_code == 200:
            return True
        else:
            return False

    def get_repo_star_count(self, repo):
        header = {'Accept': 'application/vnd.github.v3.star+json',
                  'Authorization': "Token " + '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'}
        request_url = f"https://api.github.com/repos/{repo}"
        request_result = requests.get(request_url, headers=header).json()
        return request_result['stargazers_count']


if __name__ == "__main__":
    repo = 'pytorch/kineto'
    # repo_exists = GitService().check_repo_exists(repo)
    star_count = GitService().get_repo_star_count(repo)