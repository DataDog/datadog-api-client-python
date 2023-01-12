@endpoint(synthetics) @endpoint(synthetics-v1)
Feature: Synthetics
  Datadog Synthetics uses simulated user requests and browser rendering to
  help you ensure uptime, identify regional issues, and track your
  application performance. Datadog Synthetics tests come in two different
  flavors, [API
  tests](https://docs.datadoghq.com/synthetics/api_tests/?tab=httptest) and
  [browser tests](https://docs.datadoghq.com/synthetics/browser_tests). You
  can use Datadog’s API to manage both test types programmatically.  For
  more information about Synthetics, see the [Synthetics
  overview](https://docs.datadoghq.com/synthetics/).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Synthetics" API

  @replay-only @team:DataDog/synthetics-app
  Scenario: Client is resilient to enum and oneOf deserialization errors
    Given new "ListTests" request
    When the request is sent
    Then the response status is 200 OK - Returns the list of all Synthetic tests.
    And the response "tests" has length 6
    And the response "tests[0].config.assertions" has length 3
    And the response "tests[0].config.assertions[0].operator" is equal to "lessThan"
    And the response "tests[0].config.assertions[2].operator" is equal to "A non existent operator"
    And the response "tests[1].config.assertions[0].operator" is equal to "lessThan"
    And the response "tests[1].config.assertions[1].type" is equal to "A non existent assertion type"
    And the response "tests[2].options.device_ids" has length 3
    And the response "tests[2].options.device_ids[2]" is equal to "A non existent device ID"
    And the response "tests[3].type" is equal to "A non existent test type"
    And the response "tests[4].config.request.method" is equal to "A non existent method"

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Create a browser test returns "- JSON format is wrong" response
    Given new "CreateSyntheticsBrowserTest" request
    And body with value {"config": {"assertions": [], "configVariables": [{"name": "VARIABLE_NAME", "secure": false, "type": "text"}], "request": {"basicAuth": {"password": "PaSSw0RD!", "type": "web", "username": "my_username"}, "bodyType": "text/plain", "callType": "unary", "certificate": {"cert": {}, "key": {}}, "certificateDomains": [], "proxy": {"url": "https://example.com"}, "service": "Greeter", "url": "https://example.com"}, "variables": [{"name": "VARIABLE_NAME", "type": "text"}]}, "locations": ["aws:eu-west-3"], "message": "", "name": "Example test name", "options": {"ci": {"executionRule": "blocking"}, "device_ids": ["laptop_large"], "monitor_options": {}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "rumSettings": {"applicationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "clientTokenId": 12345, "isEnabled": true}}, "status": "live", "steps": [{"type": "assertElementContent"}], "tags": ["env:prod"], "type": "browser"}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @team:DataDog/synthetics-app
  Scenario: Create a browser test returns "OK - Returns saved rumSettings." response
    Given new "CreateSyntheticsBrowserTest" request
    And body from file "synthetics_browser_test_payload_with_rum_settings.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "options.rumSettings.isEnabled" is equal to true
    And the response "options.rumSettings.applicationId" is equal to "mockApplicationId"
    And the response "options.rumSettings.clientTokenId" is equal to 12345

  @team:DataDog/synthetics-app
  Scenario: Create a browser test returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsBrowserTest" request
    And body from file "synthetics_browser_test_payload.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "name" is equal to "{{ unique }}"
    And the response "config.configVariables[0].secure" is equal to true

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Create a browser test returns "Test quota is reached" response
    Given new "CreateSyntheticsBrowserTest" request
    And body with value {"config": {"assertions": [], "configVariables": [{"name": "VARIABLE_NAME", "secure": false, "type": "text"}], "request": {"basicAuth": {"password": "PaSSw0RD!", "type": "web", "username": "my_username"}, "bodyType": "text/plain", "callType": "unary", "certificate": {"cert": {}, "key": {}}, "certificateDomains": [], "proxy": {"url": "https://example.com"}, "service": "Greeter", "url": "https://example.com"}, "variables": [{"name": "VARIABLE_NAME", "type": "text"}]}, "locations": ["aws:eu-west-3"], "message": "", "name": "Example test name", "options": {"ci": {"executionRule": "blocking"}, "device_ids": ["laptop_large"], "monitor_options": {}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "rumSettings": {"applicationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "clientTokenId": 12345, "isEnabled": true}}, "status": "live", "steps": [{"type": "assertElementContent"}], "tags": ["env:prod"], "type": "browser"}
    When the request is sent
    Then the response status is 402 Test quota is reached

  @team:DataDog/synthetics-app
  Scenario: Create a global variable from test returns "OK" response
    Given there is a valid "synthetics_api_test_multi_step" in the system
    And new "CreateGlobalVariable" request
    And body from file "synthetics_global_variable_payload.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "GLOBAL_VARIABLE_PAYLOAD_{{ unique_upper_alnum }}"

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Create a global variable returns "Invalid request" response
    Given new "CreateGlobalVariable" request
    And body with value {"attributes": {"restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"]}, "description": "Example description", "name": "MY_VARIABLE", "parse_test_options": {"field": "content-type", "localVariableName": "LOCAL_VARIABLE", "parser": {"type": "regex", "value": ".*"}, "type": "http_body"}, "parse_test_public_id": "abc-def-123", "tags": ["team:front", "test:workflow-1"], "value": {"secure": true, "value": "value"}}
    When the request is sent
    Then the response status is 400 Invalid request

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Create a global variable returns "OK" response
    Given new "CreateGlobalVariable" request
    And body with value {"attributes": {"restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"]}, "description": "Example description", "name": "MY_VARIABLE", "parse_test_options": {"field": "content-type", "localVariableName": "LOCAL_VARIABLE", "parser": {"type": "regex", "value": ".*"}, "type": "http_body"}, "parse_test_public_id": "abc-def-123", "tags": ["team:front", "test:workflow-1"], "value": {"secure": true, "value": "value"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/synthetics-app
  Scenario: Create a private location returns "OK" response
    Given there is a valid "role" in the system
    And new "CreatePrivateLocation" request
    And body with value {"description": "Test {{ unique }} description", "metadata": {"restricted_roles": ["{{ role.data.id }}"]}, "name": "{{ unique }}", "tags": ["test:{{ unique_lower_alnum }}"]}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Create a private location returns "Private locations are not activated for the user" response
    Given new "CreatePrivateLocation" request
    And body with value {"description": "Description of private location", "metadata": {"restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"]}, "name": "New private location", "tags": ["team:front"]}
    When the request is sent
    Then the response status is 404 Private locations are not activated for the user

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Create a private location returns "Quota reached for private locations" response
    Given new "CreatePrivateLocation" request
    And body with value {"description": "Description of private location", "metadata": {"restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"]}, "name": "New private location", "tags": ["team:front"]}
    When the request is sent
    Then the response status is 402 Quota reached for private locations

  @team:DataDog/synthetics-app
  Scenario: Create an API GRPC test returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsAPITest" request
    And body from file "synthetics_api_grpc_test_payload.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "name" is equal to "{{ unique }}"

  @team:DataDog/synthetics-app
  Scenario: Create an API HTTP test returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsAPITest" request
    And body from file "synthetics_api_http_test_payload.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "name" is equal to "{{ unique }}"

  @team:DataDog/synthetics-app
  Scenario: Create an API HTTP with oauth-rop test returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsAPITest" request
    And body from file "synthetics_api_http_test_oauth_rop_payload.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "name" is equal to "{{ unique }}"

  @team:DataDog/synthetics-app
  Scenario: Create an API SSL test returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsAPITest" request
    And body from file "synthetics_api_ssl_test_payload.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "name" is equal to "{{ unique }}"

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Create an API test returns "- JSON format is wrong" response
    Given new "CreateSyntheticsAPITest" request
    And body with value {"config": {"assertions": [{"operator": "lessThan", "target": 1000, "type": "responseTime"}], "request": {"method": "GET", "url": "https://example.com"}}, "locations": ["aws:eu-west-3"], "message": "Notification message", "name": "Example test name", "options": {"ci": {"executionRule": "blocking"}, "device_ids": ["laptop_large"], "monitor_options": {}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "rumSettings": {"applicationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "clientTokenId": 12345, "isEnabled": true}}, "status": "live", "subtype": "http", "tags": ["env:production"], "type": "api"}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Create an API test returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsAPITest" request
    And body with value {"config": {"assertions": [{"operator": "lessThan", "target": 1000, "type": "responseTime"}], "request": {"method": "GET", "url": "https://example.com"}}, "locations": ["aws:eu-west-3"], "message": "Notification message", "name": "Example test name", "options": {"ci": {"executionRule": "blocking"}, "device_ids": ["laptop_large"], "monitor_options": {}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "rumSettings": {"applicationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "clientTokenId": 12345, "isEnabled": true}}, "status": "live", "subtype": "http", "tags": ["env:production"], "type": "api"}
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Create an API test returns "Test quota is reached" response
    Given new "CreateSyntheticsAPITest" request
    And body with value {"config": {"assertions": [{"operator": "lessThan", "target": 1000, "type": "responseTime"}], "request": {"method": "GET", "url": "https://example.com"}}, "locations": ["aws:eu-west-3"], "message": "Notification message", "name": "Example test name", "options": {"ci": {"executionRule": "blocking"}, "device_ids": ["laptop_large"], "monitor_options": {}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "rumSettings": {"applicationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "clientTokenId": 12345, "isEnabled": true}}, "status": "live", "subtype": "http", "tags": ["env:production"], "type": "api"}
    When the request is sent
    Then the response status is 402 Test quota is reached

  @team:DataDog/synthetics-app
  Scenario: Create an API test with UDP subtype returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsAPITest" request
    And body from file "synthetics_api_test_udp_payload.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "name" is equal to "{{ unique }}"

  @team:DataDog/synthetics-app
  Scenario: Create an API test with WEBSOCKET subtype returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsAPITest" request
    And body from file "synthetics_api_test_websocket_payload.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "name" is equal to "{{ unique }}"

  @team:DataDog/synthetics-app
  Scenario: Create an API test with multi subtype returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsAPITest" request
    And body from file "synthetics_api_test_multi_step_payload.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "name" is equal to "{{ unique }}"
    And the response "config.steps[0].retry.count" is equal to 5
    And the response "config.steps[0].retry.interval" is equal to 1000

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Delete a global variable returns "JSON format is wrong" response
    Given new "DeleteGlobalVariable" request
    And request contains "variable_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 JSON format is wrong

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Delete a global variable returns "Not found" response
    Given new "DeleteGlobalVariable" request
    And request contains "variable_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Delete a global variable returns "OK" response
    Given new "DeleteGlobalVariable" request
    And request contains "variable_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Delete a private location returns "- Private locations are not activated for the user" response
    Given new "DeletePrivateLocation" request
    And request contains "location_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 - Private locations are not activated for the user

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Delete a private location returns "OK" response
    Given new "DeletePrivateLocation" request
    And request contains "location_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Delete tests returns "- JSON format is wrong" response
    Given new "DeleteTests" request
    And body with value {"public_ids": []}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Delete tests returns "- Tests to be deleted can't be found" response
    Given new "DeleteTests" request
    And body with value {"public_ids": []}
    When the request is sent
    Then the response status is 404 - Tests to be deleted can't be found

  @skip @team:DataDog/synthetics-app
  Scenario: Delete tests returns "OK." response
    Given there is a valid "synthetics_api_test" in the system
    And new "DeleteTests" request
    And body with value {"public_ids": ["{{ synthetics_api_test.public_id }}"]}
    When the request is sent
    Then the response status is 200 OK.
    And the response "deleted_tests[0].public_id" is equal to "{{ synthetics_api_test.public_id }}"

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Edit a browser test returns "- JSON format is wrong" response
    Given new "UpdateBrowserTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"config": {"assertions": [], "configVariables": [{"name": "VARIABLE_NAME", "secure": false, "type": "text"}], "request": {"basicAuth": {"password": "PaSSw0RD!", "type": "web", "username": "my_username"}, "bodyType": "text/plain", "callType": "unary", "certificate": {"cert": {}, "key": {}}, "certificateDomains": [], "proxy": {"url": "https://example.com"}, "service": "Greeter", "url": "https://example.com"}, "variables": [{"name": "VARIABLE_NAME", "type": "text"}]}, "locations": ["aws:eu-west-3"], "message": "", "name": "Example test name", "options": {"ci": {"executionRule": "blocking"}, "device_ids": ["laptop_large"], "monitor_options": {}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "rumSettings": {"applicationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "clientTokenId": 12345, "isEnabled": true}}, "status": "live", "steps": [{"type": "assertElementContent"}], "tags": ["env:prod"], "type": "browser"}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Edit a browser test returns "- Synthetic Monitoring is not activated for the user" response
    Given new "UpdateBrowserTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"config": {"assertions": [], "configVariables": [{"name": "VARIABLE_NAME", "secure": false, "type": "text"}], "request": {"basicAuth": {"password": "PaSSw0RD!", "type": "web", "username": "my_username"}, "bodyType": "text/plain", "callType": "unary", "certificate": {"cert": {}, "key": {}}, "certificateDomains": [], "proxy": {"url": "https://example.com"}, "service": "Greeter", "url": "https://example.com"}, "variables": [{"name": "VARIABLE_NAME", "type": "text"}]}, "locations": ["aws:eu-west-3"], "message": "", "name": "Example test name", "options": {"ci": {"executionRule": "blocking"}, "device_ids": ["laptop_large"], "monitor_options": {}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "rumSettings": {"applicationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "clientTokenId": 12345, "isEnabled": true}}, "status": "live", "steps": [{"type": "assertElementContent"}], "tags": ["env:prod"], "type": "browser"}
    When the request is sent
    Then the response status is 404 - Synthetic Monitoring is not activated for the user

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Edit a browser test returns "OK" response
    Given new "UpdateBrowserTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"config": {"assertions": [], "configVariables": [{"name": "VARIABLE_NAME", "secure": false, "type": "text"}], "request": {"basicAuth": {"password": "PaSSw0RD!", "type": "web", "username": "my_username"}, "bodyType": "text/plain", "callType": "unary", "certificate": {"cert": {}, "key": {}}, "certificateDomains": [], "proxy": {"url": "https://example.com"}, "service": "Greeter", "url": "https://example.com"}, "variables": [{"name": "VARIABLE_NAME", "type": "text"}]}, "locations": ["aws:eu-west-3"], "message": "", "name": "Example test name", "options": {"ci": {"executionRule": "blocking"}, "device_ids": ["laptop_large"], "monitor_options": {}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "rumSettings": {"applicationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "clientTokenId": 12345, "isEnabled": true}}, "status": "live", "steps": [{"type": "assertElementContent"}], "tags": ["env:prod"], "type": "browser"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Edit a global variable returns "Invalid request" response
    Given new "EditGlobalVariable" request
    And request contains "variable_id" parameter from "REPLACE.ME"
    And body with value {"attributes": {"restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"]}, "description": "Example description", "name": "MY_VARIABLE", "parse_test_options": {"field": "content-type", "localVariableName": "LOCAL_VARIABLE", "parser": {"type": "regex", "value": ".*"}, "type": "http_body"}, "parse_test_public_id": "abc-def-123", "tags": ["team:front", "test:workflow-1"], "value": {"secure": true, "value": "value"}}
    When the request is sent
    Then the response status is 400 Invalid request

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Edit a global variable returns "OK" response
    Given new "EditGlobalVariable" request
    And request contains "variable_id" parameter from "REPLACE.ME"
    And body with value {"attributes": {"restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"]}, "description": "Example description", "name": "MY_VARIABLE", "parse_test_options": {"field": "content-type", "localVariableName": "LOCAL_VARIABLE", "parser": {"type": "regex", "value": ".*"}, "type": "http_body"}, "parse_test_public_id": "abc-def-123", "tags": ["team:front", "test:workflow-1"], "value": {"secure": true, "value": "value"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Edit a private location returns "- Private locations are not activated for the user" response
    Given new "UpdatePrivateLocation" request
    And request contains "location_id" parameter from "REPLACE.ME"
    And body with value {"description": "Description of private location", "metadata": {"restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"]}, "name": "New private location", "tags": ["team:front"]}
    When the request is sent
    Then the response status is 404 - Private locations are not activated for the user

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Edit a private location returns "OK" response
    Given new "UpdatePrivateLocation" request
    And request contains "location_id" parameter from "REPLACE.ME"
    And body with value {"description": "Description of private location", "metadata": {"restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"]}, "name": "New private location", "tags": ["team:front"]}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Edit an API test returns "- JSON format is wrong" response
    Given new "UpdateAPITest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"config": {"assertions": [{"operator": "lessThan", "target": 1000, "type": "responseTime"}], "request": {"method": "GET", "url": "https://example.com"}}, "locations": ["aws:eu-west-3"], "message": "Notification message", "name": "Example test name", "options": {"ci": {"executionRule": "blocking"}, "device_ids": ["laptop_large"], "monitor_options": {}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "rumSettings": {"applicationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "clientTokenId": 12345, "isEnabled": true}}, "status": "live", "subtype": "http", "tags": ["env:production"], "type": "api"}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Edit an API test returns "- Synthetic Monitoring is not activated for the user" response
    Given new "UpdateAPITest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"config": {"assertions": [{"operator": "lessThan", "target": 1000, "type": "responseTime"}], "request": {"method": "GET", "url": "https://example.com"}}, "locations": ["aws:eu-west-3"], "message": "Notification message", "name": "Example test name", "options": {"ci": {"executionRule": "blocking"}, "device_ids": ["laptop_large"], "monitor_options": {}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "rumSettings": {"applicationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "clientTokenId": 12345, "isEnabled": true}}, "status": "live", "subtype": "http", "tags": ["env:production"], "type": "api"}
    When the request is sent
    Then the response status is 404 - Synthetic Monitoring is not activated for the user

  @team:DataDog/synthetics-app
  Scenario: Edit an API test returns "OK" response
    Given there is a valid "synthetics_api_test" in the system
    And new "UpdateAPITest" request
    And request contains "public_id" parameter from "synthetics_api_test.public_id"
    And body from file "synthetics_api_test_update_payload.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ synthetics_api_test.name }}-updated"

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Get a browser test result returns "- Synthetic is not activated for the user" response
    Given new "GetBrowserTestResult" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And request contains "result_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @replay-only @team:DataDog/synthetics-app
  Scenario: Get a browser test result returns "OK" response
    Given new "GetBrowserTestResult" request
    And request contains "public_id" parameter with value "2yy-sem-mjh"
    And request contains "result_id" parameter with value "5671719892074090418"
    When the request is sent
    Then the response status is 200 OK
    And the response "result_id" is equal to "5671719892074090418"
    And the response "probe_dc" is equal to "aws:ca-central-1"

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Get a browser test returns "- Synthetic is not activated for the user" response
    Given new "GetBrowserTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Get a browser test returns "OK" response
    Given new "GetBrowserTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Get a browser test's latest results summaries returns "- Synthetic is not activated for the user" response
    Given new "GetBrowserTestLatestResults" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @replay-only @team:DataDog/synthetics-app
  Scenario: Get a browser test's latest results summaries returns "OK" response
    Given new "GetBrowserTestLatestResults" request
    And request contains "public_id" parameter with value "2yy-sem-mjh"
    When the request is sent
    Then the response status is 200 OK
    And the response "results" has length 3
    And the response "results[0].status" is equal to 0
    And the response "results[0].probe_dc" is equal to "aws:ca-central-1"

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Get a global variable returns "Not found" response
    Given new "GetGlobalVariable" request
    And request contains "variable_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Get a global variable returns "OK" response
    Given new "GetGlobalVariable" request
    And request contains "variable_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Get a private location returns "- Synthetic private locations are not activated for the user" response
    Given new "GetPrivateLocation" request
    And request contains "location_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 - Synthetic private locations are not activated for the user

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Get a private location returns "OK" response
    Given new "GetPrivateLocation" request
    And request contains "location_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Get a test configuration returns "- Synthetic is not activated for the user" response
    Given new "GetTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Get a test configuration returns "OK" response
    Given new "GetTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Get all global variables returns "OK" response
    Given new "ListGlobalVariables" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Get all locations (public and private) returns "OK" response
    Given new "ListLocations" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Get an API test result returns "- Synthetic is not activated for the user" response
    Given new "GetAPITestResult" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And request contains "result_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @replay-only @team:DataDog/synthetics-app
  Scenario: Get an API test result returns "OK" response
    Given new "GetAPITestResult" request
    And request contains "public_id" parameter with value "hwb-332-3xe"
    And request contains "result_id" parameter with value "3420446318379485707"
    When the request is sent
    Then the response status is 200 OK
    And the response "result_id" is equal to "3420446318379485707"
    And the response "probe_dc" is equal to "aws:us-west-1"

  @replay-only @team:DataDog/synthetics-app
  Scenario: Get an API test result returns result with failure object
    Given there is a "synthetics_api_test_with_wrong_dns" in the system
    And the "synthetics_api_test_with_wrong_dns" is triggered
    And new "GetAPITestResult" request
    And request contains "public_id" parameter from "synthetics_api_test_with_wrong_dns.public_id"
    And request contains "result_id" parameter from "synthetics_api_test_with_wrong_dns_result.results[0].result_id"
    When the request is sent
    Then the response status is 200 OK
    And the response "result.failure.code" is equal to "DNS"
    And the response "result.failure.message" is equal to "Error during DNS resolution of hostname app.datadfoghq.com (ENOTFOUND)."

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Get an API test returns "- Synthetic Monitoring is not activated for the user" response
    Given new "GetAPITest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 - Synthetic Monitoring is not activated for the user

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Get an API test returns "OK" response
    Given new "GetAPITest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Get an API test's latest results summaries returns "- Synthetic is not activated for the user" response
    Given new "GetAPITestLatestResults" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @replay-only @team:DataDog/synthetics-app
  Scenario: Get an API test's latest results summaries returns "OK" response
    Given new "GetAPITestLatestResults" request
    And request contains "public_id" parameter with value "hwb-332-3xe"
    When the request is sent
    Then the response status is 200 OK
    And the response "results" has length 150
    And the response "results[0].status" is equal to 0
    And the response "results[0].probe_dc" is equal to "aws:us-west-1"

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Get details of batch returns "Batch does not exist." response
    Given new "GetSyntheticsCIBatch" request
    And request contains "batch_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Batch does not exist.

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Get details of batch returns "OK" response
    Given new "GetSyntheticsCIBatch" request
    And request contains "batch_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Get the list of all Synthetic tests returns "OK - Returns the list of all Synthetic tests." response
    Given new "ListTests" request
    When the request is sent
    Then the response status is 200 OK - Returns the list of all Synthetic tests.

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Get the list of all Synthetic tests returns "Synthetics is not activated for the user." response
    Given new "ListTests" request
    When the request is sent
    Then the response status is 404 Synthetics is not activated for the user.

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Pause or start a test returns "- Synthetic is not activated for the user" response
    Given new "UpdateTestPauseStatus" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"new_status": "live"}
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Pause or start a test returns "JSON format is wrong." response
    Given new "UpdateTestPauseStatus" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"new_status": "live"}
    When the request is sent
    Then the response status is 400 JSON format is wrong.

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Pause or start a test returns "OK - Returns a boolean indicating if the update was successful." response
    Given new "UpdateTestPauseStatus" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"new_status": "live"}
    When the request is sent
    Then the response status is 200 OK - Returns a boolean indicating if the update was successful.

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Trigger Synthetics tests returns "Bad Request" response
    Given new "TriggerTests" request
    And body with value {"tests": [{"metadata": {"ci": {"pipeline": {}, "provider": {}}, "git": {}}, "public_id": "aaa-aaa-aaa"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/synthetics-app
  Scenario: Trigger Synthetics tests returns "OK" response
    Given there is a valid "synthetics_api_test" in the system
    And new "TriggerTests" request
    And body with value {"tests": [{"public_id": "{{ synthetics_api_test.public_id }}"}]}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Trigger tests from CI/CD pipelines returns "JSON format is wrong" response
    Given new "TriggerCITests" request
    And body with value {"tests": [{"basicAuth": {"password": "PaSSw0RD!", "type": "web", "username": "my_username"}, "deviceIds": ["laptop_large"], "locations": ["aws:eu-west-3"], "metadata": {"ci": {"pipeline": {}, "provider": {}}, "git": {}}, "public_id": "aaa-aaa-aaa", "retry": {}}]}
    When the request is sent
    Then the response status is 400 JSON format is wrong

  @generated @skip @team:DataDog/synthetics-app
  Scenario: Trigger tests from CI/CD pipelines returns "OK" response
    Given new "TriggerCITests" request
    And body with value {"tests": [{"basicAuth": {"password": "PaSSw0RD!", "type": "web", "username": "my_username"}, "deviceIds": ["laptop_large"], "locations": ["aws:eu-west-3"], "metadata": {"ci": {"pipeline": {}, "provider": {}}, "git": {}}, "public_id": "aaa-aaa-aaa", "retry": {}}]}
    When the request is sent
    Then the response status is 200 OK
