"""
info: flask API page: Controller
@author: Haris Anwar <harisanwar64@gmail.com>
"""
from flask import Flask, render_template, make_response, request
from app import github

app = Flask(__name__)


@app.route('/')
def home_page():
    """After accessing url (with port) the page user will see is home page.
    Home page resides in template directory with name page.html"""
    return render_template('page.html')


@app.route('/<different_page>')
def other_page(different_page):
    """Adding default message (instead of error -> page not found) whenever user acess path/page other than a home
    page and instruct him to return to only home page"""
    response = make_response('The page: %s unaccessable or not found.' % different_page, 404)
    return response


@app.route('/submit_repo', methods=['POST'])
def submit_repo():
    """This method submits user input (git owner/repo) from home page"""
    git_repo = request.form['repo-name']
    repo_exists = github.GitService().check_repo_exists(git_repo)
    if repo_exists:
        df = github.GitService().get_repo_star_info_dataframe(git_repo)
        return render_template('result.html', table=[df.to_html()])


if __name__ == '__main__':
    app.run(debug=True)
