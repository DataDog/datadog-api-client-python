@endpoint(dashboard-lists) @endpoint(dashboard-lists-v2)
Feature: Dashboard Lists
  Interact with your dashboard lists through the API to organize, find, and
  share all of your dashboards with your team and organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "DashboardLists" API

  @generated @skip @team:DataDog/dashboards
  Scenario: Add Items to a Dashboard List returns "Bad Request" response
    Given new "CreateDashboardListItems" request
    And request contains "dashboard_list_id" parameter from "REPLACE.ME"
    And body with value {"dashboards": [{"id": "q5j-nti-fv6", "type": "host_timeboard"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dashboards
  Scenario: Add Items to a Dashboard List returns "Not Found" response
    Given new "CreateDashboardListItems" request
    And request contains "dashboard_list_id" parameter from "REPLACE.ME"
    And body with value {"dashboards": [{"id": "q5j-nti-fv6", "type": "host_timeboard"}]}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dashboards
  Scenario: Add Items to a Dashboard List returns "OK" response
    Given new "CreateDashboardListItems" request
    And request contains "dashboard_list_id" parameter from "REPLACE.ME"
    And body with value {"dashboards": [{"id": "q5j-nti-fv6", "type": "host_timeboard"}]}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/dashboards
  Scenario: Add custom screenboard dashboard to an existing dashboard list returns "OK" response
    Given there is a valid "dashboard_list" in the system
    And there is a valid "screenboard_dashboard" in the system
    And new "CreateDashboardListItems" request
    And request contains "dashboard_list_id" parameter from "dashboard_list.id"
    And body with value {"dashboards": [{"id": "{{ screenboard_dashboard.id }}", "type": "custom_screenboard"}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "added_dashboards_to_list[0].type" is equal to "custom_screenboard"
    And the response "added_dashboards_to_list[0].id" is equal to "{{ screenboard_dashboard.id }}"
    And the response "added_dashboards_to_list" has length 1

  @team:DataDog/dashboards
  Scenario: Add custom timeboard dashboard to an existing dashboard list returns "OK" response
    Given there is a valid "dashboard_list" in the system
    And there is a valid "dashboard" in the system
    And new "CreateDashboardListItems" request
    And request contains "dashboard_list_id" parameter from "dashboard_list.id"
    And body with value {"dashboards": [{"id": "{{ dashboard.id }}", "type": "custom_timeboard"}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "added_dashboards_to_list[0].type" is equal to "custom_timeboard"
    And the response "added_dashboards_to_list[0].id" is equal to "{{ dashboard.id }}"
    And the response "added_dashboards_to_list" has length 1

  @team:DataDog/dashboards
  Scenario: Delete custom screenboard dashboard from an existing dashboard list returns "OK" response
    Given there is a valid "dashboard_list" in the system
    And there is a valid "screenboard_dashboard" in the system
    And the "dashboard_list" has the "screenboard_dashboard"
    And new "DeleteDashboardListItems" request
    And request contains "dashboard_list_id" parameter from "dashboard_list.id"
    And body with value {"dashboards": [{"id": "{{ screenboard_dashboard.id }}", "type": "custom_screenboard"}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "deleted_dashboards_from_list[0].type" is equal to "custom_screenboard"
    And the response "deleted_dashboards_from_list[0].id" is equal to "{{ screenboard_dashboard.id }}"
    And the response "deleted_dashboards_from_list" has length 1

  @team:DataDog/dashboards
  Scenario: Delete custom timeboard dashboard from an existing dashboard list returns "OK" response
    Given there is a valid "dashboard_list" in the system
    And there is a valid "dashboard" in the system
    And the "dashboard_list" has the "dashboard"
    And new "DeleteDashboardListItems" request
    And request contains "dashboard_list_id" parameter from "dashboard_list.id"
    And body with value {"dashboards": [{"id": "{{ dashboard.id }}", "type": "custom_timeboard"}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "deleted_dashboards_from_list[0].type" is equal to "custom_timeboard"
    And the response "deleted_dashboards_from_list[0].id" is equal to "{{ dashboard.id }}"
    And the response "deleted_dashboards_from_list" has length 1

  @generated @skip @team:DataDog/dashboards
  Scenario: Delete items from a dashboard list returns "Bad Request" response
    Given new "DeleteDashboardListItems" request
    And request contains "dashboard_list_id" parameter from "REPLACE.ME"
    And body with value {"dashboards": [{"id": "q5j-nti-fv6", "type": "host_timeboard"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dashboards
  Scenario: Delete items from a dashboard list returns "Not Found" response
    Given new "DeleteDashboardListItems" request
    And request contains "dashboard_list_id" parameter from "REPLACE.ME"
    And body with value {"dashboards": [{"id": "q5j-nti-fv6", "type": "host_timeboard"}]}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dashboards
  Scenario: Delete items from a dashboard list returns "OK" response
    Given new "DeleteDashboardListItems" request
    And request contains "dashboard_list_id" parameter from "REPLACE.ME"
    And body with value {"dashboards": [{"id": "q5j-nti-fv6", "type": "host_timeboard"}]}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dashboards
  Scenario: Get items of a Dashboard List returns "Not Found" response
    Given new "GetDashboardListItems" request
    And request contains "dashboard_list_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/dashboards
  Scenario: Get items of a Dashboard List returns "OK" response
    Given there is a valid "dashboard_list" in the system
    And there is a valid "dashboard" in the system
    And the "dashboard_list" has the "dashboard"
    And new "GetDashboardListItems" request
    And request contains "dashboard_list_id" parameter from "dashboard_list.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "dashboards[0].id" is equal to "{{ dashboard.id }}"
    And the response "dashboards[0].type" is equal to "custom_timeboard"
    And the response "dashboards" has length 1

  @generated @skip @team:DataDog/dashboards
  Scenario: Update items of a dashboard list returns "Bad Request" response
    Given new "UpdateDashboardListItems" request
    And request contains "dashboard_list_id" parameter from "REPLACE.ME"
    And body with value {"dashboards": [{"id": "q5j-nti-fv6", "type": "host_timeboard"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dashboards
  Scenario: Update items of a dashboard list returns "Not Found" response
    Given new "UpdateDashboardListItems" request
    And request contains "dashboard_list_id" parameter from "REPLACE.ME"
    And body with value {"dashboards": [{"id": "q5j-nti-fv6", "type": "host_timeboard"}]}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/dashboards
  Scenario: Update items of a dashboard list returns "OK" response
    Given there is a valid "dashboard_list" in the system
    And there is a valid "dashboard" in the system
    And there is a valid "screenboard_dashboard" in the system
    And the "dashboard_list" has the "dashboard"
    And new "UpdateDashboardListItems" request
    And request contains "dashboard_list_id" parameter from "dashboard_list.id"
    And body with value {"dashboards": [{"id": "{{ screenboard_dashboard.id }}", "type": "custom_screenboard"}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "dashboards[0].id" is equal to "{{ screenboard_dashboard.id }}"
    And the response "dashboards[0].type" is equal to "custom_screenboard"
    And the response "dashboards" has length 1
