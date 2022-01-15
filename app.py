"""
info: flask API page: Controller
@author: Haris Anwar <harisanwar64@gmail.com>
"""
from flask import Flask, render_template, make_response, request
from app import github
import os

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
    """This method submit user input (git owner/repo) and output results in html with star count, graph plot,
    dataframe as table and download csv file in csv_download directory"""
    git_repo = request.form['repo-name']
    repo_exists = github.GitService().check_repo_exists(git_repo)
    if repo_exists:
        star_count = github.GitService().get_repo_star_count(git_repo)
        df = github.GitService().get_repo_star_info_dataframe(git_repo)
        star_history_plot = github.GitService().draw_plot_for_dataframe(df, git_repo)
        # getting current directory to output .csv file (star info) into directory 'csv_downloads'
        directory = os.getcwd()
        # todo: button need to be on UI to download csv (optional for user) instead of download everytime.
        df.to_csv(directory + '/csv_downloads' + '/star-history-' + git_repo.split('/')[1] + '.csv')
        return render_template('result.html', stars=star_count, table=[df.to_html()],
                               star_history_plot=star_history_plot)
    else:
        # todo: if repo not exists, display proper message on UI to let user know.
        return render_template('page.html')


if __name__ == '__main__':
    app.run(debug=True)
