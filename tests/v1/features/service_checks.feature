@endpoint(service-checks) @endpoint(service-checks-v1)
Feature: Service Checks
  The service check endpoint allows you to post check statuses for use with
  monitors. Service check messages are limited to 500 characters. If a check
  is posted with a message containing more than 500 characters, only the
  first 500 characters are displayed.  - [Read more about Service Check
  monitors.][1] - [Read more about Process Check monitors.][2] - [Read more
  about Network Check monitors.][3] - [Read more about Custom Check
  monitors.][4] - [Read more about Service Check and status codes.][5]  [1]:
  https://docs.datadoghq.com/monitors/monitor_types/host/?tab=checkalert
  [2]: https://docs.datadoghq.com/monitors/monitor_types/process_check/?tab=
  checkalert [3]:
  https://docs.datadoghq.com/monitors/monitor_types/network/?tab=checkalert
  [4]: https://docs.datadoghq.com/monitors/monitor_types/custom_check/?tab=c
  heckalert [5]: https://docs.datadoghq.com/developers/service_checks/

  Background:
    Given a valid "apiKeyAuth" key in the system
    And an instance of "ServiceChecks" API
    And new "SubmitServiceCheck" request

  @generated @skip
  Scenario: Submit a Service Check returns "Bad Request" response
    Given body with value [{"check": "app.ok", "host_name": "app.host1", "message": "app is running", "status": 0, "tags": ["environment:test"], "timestamp": null}]
    When the request is sent
    Then the response status is 400 Bad Request

  Scenario: Submit a Service Check returns "Payload accepted" response
    Given body with value [{"check": "app.ok", "host_name": "host", "status": 0, "tags": ["test:{{ unique_alnum }}"]}]
    When the request is sent
    Then the response status is 202 Payload accepted

  @generated @skip
  Scenario: Submit a Service Check returns "Payload too large" response
    Given body with value [{"check": "app.ok", "host_name": "app.host1", "message": "app is running", "status": 0, "tags": ["environment:test"], "timestamp": null}]
    When the request is sent
    Then the response status is 413 Payload too large

  @generated @skip
  Scenario: Submit a Service Check returns "Request timeout" response
    Given body with value [{"check": "app.ok", "host_name": "app.host1", "message": "app is running", "status": 0, "tags": ["environment:test"], "timestamp": null}]
    When the request is sent
    Then the response status is 408 Request timeout
