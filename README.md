## Just simple reporter for JIRA standalone server
Currently, just shows some examples how to work with jira api.
Prints list of issues based on jql in ~/.config/jirareport.ini 

## License
MIT

## jirareport.ini
[DEFAULT]
jira_server_url=https://jira.ourcompany.com/
jira_token_auth=token
jql=assignee was in (jon, fred, mira)