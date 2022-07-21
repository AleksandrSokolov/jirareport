# This is a sample Python script.
import configparser
import os
from typing import Union, List, Dict, Any

from jira import JIRA, Issue
from jira.client import ResultList

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

config = configparser.ConfigParser()
config.read(os.path.expanduser('~')+'/.config/jirareport.ini')
for key in config['DEFAULT']:
    print(key)

jira = JIRA(server=config['DEFAULT']['jira_server_url'], token_auth=config['DEFAULT']['jira_token_auth'])


# print all projects
def print_projects(print_components=False, print_versions=False):
    projects = jira.projects()

    for project in projects:
        print('project key={} name={} archived={} projectTypeKey={}'.format(project.key, project.name,
                                                                            project.archived, project.projectTypeKey))
        # components - peaces of software or team
        if print_components:
            components = jira.project_components(project)
            # [c.name for c in components]
            for c in components:
                # print('project key={} component name={} '.format(project.key, c.name))
                print('component name={} '.format(c.name))
        # sprints?
        if print_versions:
            versions = jira.project_versions(project)
            for v in versions:
                # print('project key={} version name={} '.format(project.key, v.name))
                print('version name={} '.format(v.name))


def print_issues_types(project):
    meta_in_project = jira.createmeta(projectKeys=project, expand="issuetypes")
    for prj in meta_in_project.get("projects"):
        for it in prj.get("issuetypes"):
            print('issuetype name={}, description={} '.format(it.get("name"), it.get("description")))

    #for attr, value in meta_in_project.items():
    #    print(attr, value)


# print all issues fields
def print_issues_fields(project):
    issues_in_proj = jira.search_issues('project=' + project, maxResults=1)
    for issue in issues_in_proj:
        print('issue key={} '.format(issue.key))
        for attr, value in issue.fields.__dict__.items():
            print(attr, value)
            #
            # print('issue field={} '.format(f))


def print_issues(search):
    # Search returns first 50 results, `maxResults` must be set to exceed this
    issues_in_proj = jira.search_issues(search, maxResults=-1)
    # all_proj_issues_but_mine = jira.search_issues('project=SYS and assignee != currentUser()')

    # my top 5 issues due by the end of the week, ordered by priority
    # oh_crap = jira.search_issues('assignee = currentUser() and due < endOfWeek() order by priority desc', maxResults=5)

    # Summaries of my last 3 reported issues
    # my_last_three_issues = jira.search_issues('reporter = currentUser() order by created desc', maxResults=3)

    for issue in issues_in_proj:
        # todo export to cvs
        # todo export to excel
        # todo export to html
        # todo export to saltcorn
        # todo send emails
        # todo create jira task graph
        print('{}: {}: {}: {}: {}: {}'.format(issue.key, issue.fields.issuetype.name,
                                      issue.fields.priority,
                                      issue.fields.status,
                                      issue.fields.summary, issue.fields.assignee))


def print_issue(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    issue = jira.issue(name)
    print(issue.fields.project.key)  # 'JRA'
    print(issue.fields.issuetype.name)  # 'New Feature'
    print(issue.fields.reporter.displayName)  # 'Mike Cannon-Brookes [Atlassian]'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    # print_issue('SYS-403')

    # print_projects()

    # print_issues_types("SYS")

    # print_issues_fields("SYS")

    # print_issues('project=SYS')
    print_issues(config['DEFAULT']['jql'])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
