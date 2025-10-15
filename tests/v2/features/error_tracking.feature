@endpoint(error-tracking) @endpoint(error-tracking-v2)
Feature: Error Tracking
  View and manage issues within Error Tracking. See the [Error Tracking
  page](https://docs.datadoghq.com/error_tracking/) for more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ErrorTracking" API

  @team:DataDog/error-tracking
  Scenario: Get the details of an error tracking issue returns "Bad Request" response
    Given new "GetIssue" request
    And request contains "issue_id" parameter with value "invalid-issue-id"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/error-tracking
  Scenario: Get the details of an error tracking issue returns "Not Found" response
    Given new "GetIssue" request
    And there is a valid "issue" in the system
    And request contains "issue_id" parameter with value "67d80aa3-36ff-44b9-a694-c501a7591737"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/error-tracking
  Scenario: Get the details of an error tracking issue returns "OK" response
    Given new "GetIssue" request
    And there is a valid "issue" in the system
    And request contains "issue_id" parameter from "issue.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "{{ issue.id }}"

  @generated @skip @team:DataDog/error-tracking
  Scenario: Remove the assignee of an issue returns "Bad Request" response
    Given new "DeleteIssueAssignee" request
    And request contains "issue_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/error-tracking
  Scenario: Remove the assignee of an issue returns "No Content" response
    Given new "DeleteIssueAssignee" request
    And there is a valid "issue" in the system
    And request contains "issue_id" parameter from "issue.id"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/error-tracking
  Scenario: Remove the assignee of an issue returns "Not Found" response
    Given new "DeleteIssueAssignee" request
    And request contains "issue_id" parameter with value "67d80aa3-36ff-44b9-a694-c501a7591737"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/error-tracking
  Scenario: Search error tracking issues returns "Bad Request" response
    Given new "SearchIssues" request
    And body with value {"data": {"attributes": {"query": "service:orders-* AND @language:go", "from": 1671612804000, "to": 1671620004000, "track": "invalid-track"}, "type": "search_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/error-tracking
  Scenario: Search error tracking issues returns "OK" response
    Given new "SearchIssues" request
    And body with value {"data": {"attributes": {"query": "service:orders-* AND @language:go", "from": 1671612804000, "to": 1671620004000, "track": "trace"}, "type": "search_request"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/error-tracking
  Scenario: Update the assignee of an issue returns "Bad Request" response
    Given new "UpdateIssueAssignee" request
    And there is a valid "issue" in the system
    And request contains "issue_id" parameter from "issue.id"
    And body with value {"data": {"id": "invalid-id", "type": "assignee"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/error-tracking
  Scenario: Update the assignee of an issue returns "Not Found" response
    Given new "UpdateIssueAssignee" request
    And request contains "issue_id" parameter with value "67d80aa3-36ff-44b9-a694-c501a7591737"
    And body with value {"data": {"id": "87cb11a0-278c-440a-99fe-701223c80296", "type": "assignee"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/error-tracking
  Scenario: Update the assignee of an issue returns "OK" response
    Given new "UpdateIssueAssignee" request
    And there is a valid "issue" in the system
    And request contains "issue_id" parameter from "issue.id"
    And body with value {"data": {"id": "87cb11a0-278c-440a-99fe-701223c80296", "type": "assignee"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/error-tracking
  Scenario: Update the state of an issue returns "Bad Request" response
    Given new "UpdateIssueState" request
    And there is a valid "issue" in the system
    And request contains "issue_id" parameter from "issue.id"
    And body with value {"data": {"attributes": {"state": "invalid-state"}, "id": "{{ issue.id }}", "type": "error_tracking_issue"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/error-tracking
  Scenario: Update the state of an issue returns "Not Found" response
    Given new "UpdateIssueState" request
    And request contains "issue_id" parameter with value "67d80aa3-36ff-44b9-a694-c501a7591737"
    And body with value {"data": {"attributes": {"state": "resolved"}, "id": "67d80aa3-36ff-44b9-a694-c501a7591737", "type": "error_tracking_issue"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/error-tracking
  Scenario: Update the state of an issue returns "OK" response
    Given new "UpdateIssueState" request
    And there is a valid "issue" in the system
    And request contains "issue_id" parameter from "issue.id"
    And body with value {"data": {"attributes": {"state": "RESOLVED"}, "id": "{{ issue.id }}", "type": "error_tracking_issue"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.state" is equal to "RESOLVED"
