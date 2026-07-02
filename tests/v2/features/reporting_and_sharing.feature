@endpoint(reporting-and-sharing) @endpoint(reporting-and-sharing-v2)
Feature: Reporting And Sharing
  The Reporting and Sharing endpoints allow you to create snapshots of graph
  widgets and other shareable resources.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ReportingAndSharing" API
    And operation "CreateSnapshot" enabled
    And new "CreateSnapshot" request
    And body with value {"data": {"attributes": {"additional_config": {"template_variables": [{"name": "host", "prefix": "host", "values": ["web-server-1", "web-server-2"]}], "timeseries_legend_type": "expanded", "timezone_offset_minutes": 300}, "end": 1692464800000, "height": 185, "is_authenticated": false, "start": 1692464000000, "ttl": "60d", "widget_definition": {"requests": [{"q": "avg:system.cpu.user{*}"}], "type": "timeseries"}, "width": 300}, "type": "create_snapshot"}}

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Create a graph snapshot returns "Bad Request" response
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Create a graph snapshot returns "Not Found" response
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Create a graph snapshot returns "OK" response
    When the request is sent
    Then the response status is 200 OK
