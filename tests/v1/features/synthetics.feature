@endpoint(synthetics)
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

  @generated @skip
  Scenario: Create a browser test returns "- JSON format is wrong" response
    Given new "CreateSyntheticsBrowserTest" request
    And body {"config": {"assertions": [], "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "variables": [{"example": null, "id": null, "name": "VARIABLE_NAME", "pattern": null, "type": "element"}]}, "locations": [null], "message": "", "monitor_id": null, "name": null, "options": {"accept_self_signed": null, "allow_insecure": null, "device_ids": ["laptop_large"], "disableCors": null, "follow_redirects": null, "min_failure_duration": null, "min_location_failed": null, "monitor_options": {"renotify_interval": null}, "noScreenshot": null, "retry": {"count": null, "interval": null}, "tick_every": 60}, "public_id": null, "status": "live", "steps": [{"allowFailure": null, "name": null, "params": null, "timeout": null, "type": "assertCurrentUrl"}], "tags": [null], "type": "browser"}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip
  Scenario: Create a browser test returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsBrowserTest" request
    And body {"config": {"assertions": [], "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "variables": [{"example": null, "id": null, "name": "VARIABLE_NAME", "pattern": null, "type": "element"}]}, "locations": [null], "message": "", "monitor_id": null, "name": null, "options": {"accept_self_signed": null, "allow_insecure": null, "device_ids": ["laptop_large"], "disableCors": null, "follow_redirects": null, "min_failure_duration": null, "min_location_failed": null, "monitor_options": {"renotify_interval": null}, "noScreenshot": null, "retry": {"count": null, "interval": null}, "tick_every": 60}, "public_id": null, "status": "live", "steps": [{"allowFailure": null, "name": null, "params": null, "timeout": null, "type": "assertCurrentUrl"}], "tags": [null], "type": "browser"}
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.

  @generated @skip
  Scenario: Create a browser test returns "Test quota is reached" response
    Given new "CreateSyntheticsBrowserTest" request
    And body {"config": {"assertions": [], "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "variables": [{"example": null, "id": null, "name": "VARIABLE_NAME", "pattern": null, "type": "element"}]}, "locations": [null], "message": "", "monitor_id": null, "name": null, "options": {"accept_self_signed": null, "allow_insecure": null, "device_ids": ["laptop_large"], "disableCors": null, "follow_redirects": null, "min_failure_duration": null, "min_location_failed": null, "monitor_options": {"renotify_interval": null}, "noScreenshot": null, "retry": {"count": null, "interval": null}, "tick_every": 60}, "public_id": null, "status": "live", "steps": [{"allowFailure": null, "name": null, "params": null, "timeout": null, "type": "assertCurrentUrl"}], "tags": [null], "type": "browser"}
    When the request is sent
    Then the response status is 402 Test quota is reached

  @generated @skip
  Scenario: Create a global variable returns "Invalid request" response
    Given new "CreateGlobalVariable" request
    And body {"description": "Example description", "name": "MY_VARIABLE", "parse_test_options": {"field": "content-type", "parser": {"type": "regex", "value": ".*"}, "type": "http_body"}, "parse_test_public_id": "abc-def-123", "tags": ["team:front", "test:workflow-1"], "value": {"secure": true, "value": "value"}}
    When the request is sent
    Then the response status is 400 Invalid request

  @generated @skip
  Scenario: Create a global variable returns "OK" response
    Given new "CreateGlobalVariable" request
    And body {"description": "Example description", "name": "MY_VARIABLE", "parse_test_options": {"field": "content-type", "parser": {"type": "regex", "value": ".*"}, "type": "http_body"}, "parse_test_public_id": "abc-def-123", "tags": ["team:front", "test:workflow-1"], "value": {"secure": true, "value": "value"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Create a private location returns "OK" response
    Given new "CreatePrivateLocation" request
    And body {"description": "Description of private location", "name": "New private location", "tags": ["team:front"]}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Create a private location returns "Private locations are not activated for the user" response
    Given new "CreatePrivateLocation" request
    And body {"description": "Description of private location", "name": "New private location", "tags": ["team:front"]}
    When the request is sent
    Then the response status is 404 Private locations are not activated for the user

  @generated @skip
  Scenario: Create a private location returns "Quota reached for private locations" response
    Given new "CreatePrivateLocation" request
    And body {"description": "Description of private location", "name": "New private location", "tags": ["team:front"]}
    When the request is sent
    Then the response status is 402 Quota reached for private locations

  @generated @skip
  Scenario: Create a test returns "- JSON format is wrong" response
    Given new "CreateTest" request
    And body {"config": {"assertions": [], "configVariables": [{"example": null, "name": "VARIABLE_NAME", "pattern": null, "type": "text"}], "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "variables": [{"example": null, "id": null, "name": "VARIABLE_NAME", "pattern": null, "type": "element"}]}, "locations": [null], "message": null, "monitor_id": null, "name": null, "options": {"accept_self_signed": null, "allow_insecure": null, "device_ids": ["laptop_large"], "disableCors": null, "follow_redirects": null, "min_failure_duration": null, "min_location_failed": null, "monitor_options": {"renotify_interval": null}, "noScreenshot": null, "retry": {"count": null, "interval": null}, "tick_every": 60}, "public_id": null, "status": "live", "steps": [{"allowFailure": null, "name": null, "params": null, "timeout": null, "type": "assertCurrentUrl"}], "subtype": "http", "tags": [null], "type": "api"}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip
  Scenario: Create a test returns "OK - Returns the created test details." response
    Given new "CreateTest" request
    And body {"config": {"assertions": [], "configVariables": [{"example": null, "name": "VARIABLE_NAME", "pattern": null, "type": "text"}], "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "variables": [{"example": null, "id": null, "name": "VARIABLE_NAME", "pattern": null, "type": "element"}]}, "locations": [null], "message": null, "monitor_id": null, "name": null, "options": {"accept_self_signed": null, "allow_insecure": null, "device_ids": ["laptop_large"], "disableCors": null, "follow_redirects": null, "min_failure_duration": null, "min_location_failed": null, "monitor_options": {"renotify_interval": null}, "noScreenshot": null, "retry": {"count": null, "interval": null}, "tick_every": 60}, "public_id": null, "status": "live", "steps": [{"allowFailure": null, "name": null, "params": null, "timeout": null, "type": "assertCurrentUrl"}], "subtype": "http", "tags": [null], "type": "api"}
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.

  @generated @skip
  Scenario: Create a test returns "Test quota is reached" response
    Given new "CreateTest" request
    And body {"config": {"assertions": [], "configVariables": [{"example": null, "name": "VARIABLE_NAME", "pattern": null, "type": "text"}], "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "variables": [{"example": null, "id": null, "name": "VARIABLE_NAME", "pattern": null, "type": "element"}]}, "locations": [null], "message": null, "monitor_id": null, "name": null, "options": {"accept_self_signed": null, "allow_insecure": null, "device_ids": ["laptop_large"], "disableCors": null, "follow_redirects": null, "min_failure_duration": null, "min_location_failed": null, "monitor_options": {"renotify_interval": null}, "noScreenshot": null, "retry": {"count": null, "interval": null}, "tick_every": 60}, "public_id": null, "status": "live", "steps": [{"allowFailure": null, "name": null, "params": null, "timeout": null, "type": "assertCurrentUrl"}], "subtype": "http", "tags": [null], "type": "api"}
    When the request is sent
    Then the response status is 402 Test quota is reached

  @generated @skip
  Scenario: Create an API test returns "- JSON format is wrong" response
    Given new "CreateSyntheticsAPITest" request
    And body {"config": {"assertions": [], "configVariables": [{"example": null, "name": "VARIABLE_NAME", "pattern": null, "type": "text"}], "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "steps": [{"assertions": [], "extractedValues": [{"field": "content-type", "name": null, "parser": {"type": "regex", "value": ".*"}, "type": "http_body"}], "name": null, "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "subtype": "http"}]}, "locations": [null], "message": null, "monitor_id": null, "name": null, "options": {"accept_self_signed": null, "allow_insecure": null, "device_ids": ["laptop_large"], "disableCors": null, "follow_redirects": null, "min_failure_duration": null, "min_location_failed": null, "monitor_options": {"renotify_interval": null}, "noScreenshot": null, "retry": {"count": null, "interval": null}, "tick_every": 60}, "public_id": null, "status": "live", "subtype": "http", "tags": [null], "type": "api"}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip
  Scenario: Create an API test returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsAPITest" request
    And body {"config": {"assertions": [], "configVariables": [{"example": null, "name": "VARIABLE_NAME", "pattern": null, "type": "text"}], "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "steps": [{"assertions": [], "extractedValues": [{"field": "content-type", "name": null, "parser": {"type": "regex", "value": ".*"}, "type": "http_body"}], "name": null, "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "subtype": "http"}]}, "locations": [null], "message": null, "monitor_id": null, "name": null, "options": {"accept_self_signed": null, "allow_insecure": null, "device_ids": ["laptop_large"], "disableCors": null, "follow_redirects": null, "min_failure_duration": null, "min_location_failed": null, "monitor_options": {"renotify_interval": null}, "noScreenshot": null, "retry": {"count": null, "interval": null}, "tick_every": 60}, "public_id": null, "status": "live", "subtype": "http", "tags": [null], "type": "api"}
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.

  @generated @skip
  Scenario: Create an API test returns "Test quota is reached" response
    Given new "CreateSyntheticsAPITest" request
    And body {"config": {"assertions": [], "configVariables": [{"example": null, "name": "VARIABLE_NAME", "pattern": null, "type": "text"}], "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "steps": [{"assertions": [], "extractedValues": [{"field": "content-type", "name": null, "parser": {"type": "regex", "value": ".*"}, "type": "http_body"}], "name": null, "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "subtype": "http"}]}, "locations": [null], "message": null, "monitor_id": null, "name": null, "options": {"accept_self_signed": null, "allow_insecure": null, "device_ids": ["laptop_large"], "disableCors": null, "follow_redirects": null, "min_failure_duration": null, "min_location_failed": null, "monitor_options": {"renotify_interval": null}, "noScreenshot": null, "retry": {"count": null, "interval": null}, "tick_every": 60}, "public_id": null, "status": "live", "subtype": "http", "tags": [null], "type": "api"}
    When the request is sent
    Then the response status is 402 Test quota is reached

  @generated @skip
  Scenario: Delete a global variable returns "JSON format is wrong" response
    Given new "DeleteGlobalVariable" request
    And request contains "variable_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 400 JSON format is wrong

  @generated @skip
  Scenario: Delete a global variable returns "Not found" response
    Given new "DeleteGlobalVariable" request
    And request contains "variable_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip
  Scenario: Delete a global variable returns "OK" response
    Given new "DeleteGlobalVariable" request
    And request contains "variable_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Delete a private location returns "- Private locations are not activated for the user" response
    Given new "DeletePrivateLocation" request
    And request contains "location_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 - Private locations are not activated for the user

  @generated @skip
  Scenario: Delete a private location returns "OK" response
    Given new "DeletePrivateLocation" request
    And request contains "location_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip
  Scenario: Delete tests returns "- JSON format is wrong" response
    Given new "DeleteTests" request
    And body {"public_ids": []}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip
  Scenario: Delete tests returns "- Tests to be deleted can't be found" response
    Given new "DeleteTests" request
    And body {"public_ids": []}
    When the request is sent
    Then the response status is 404 - Tests to be deleted can't be found

  @generated @skip
  Scenario: Delete tests returns "OK." response
    Given new "DeleteTests" request
    And body {"public_ids": []}
    When the request is sent
    Then the response status is 200 OK.

  @generated @skip
  Scenario: Edit a browser test returns "- JSON format is wrong" response
    Given new "UpdateBrowserTest" request
    And request contains "public_id" parameter from "<PATH>"
    And body {"config": {"assertions": [], "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "variables": [{"example": null, "id": null, "name": "VARIABLE_NAME", "pattern": null, "type": "element"}]}, "locations": [null], "message": "", "monitor_id": null, "name": null, "options": {"accept_self_signed": null, "allow_insecure": null, "device_ids": ["laptop_large"], "disableCors": null, "follow_redirects": null, "min_failure_duration": null, "min_location_failed": null, "monitor_options": {"renotify_interval": null}, "noScreenshot": null, "retry": {"count": null, "interval": null}, "tick_every": 60}, "public_id": null, "status": "live", "steps": [{"allowFailure": null, "name": null, "params": null, "timeout": null, "type": "assertCurrentUrl"}], "tags": [null], "type": "browser"}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip
  Scenario: Edit a browser test returns "- Synthetic Monitoring is not activated for the user" response
    Given new "UpdateBrowserTest" request
    And request contains "public_id" parameter from "<PATH>"
    And body {"config": {"assertions": [], "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "variables": [{"example": null, "id": null, "name": "VARIABLE_NAME", "pattern": null, "type": "element"}]}, "locations": [null], "message": "", "monitor_id": null, "name": null, "options": {"accept_self_signed": null, "allow_insecure": null, "device_ids": ["laptop_large"], "disableCors": null, "follow_redirects": null, "min_failure_duration": null, "min_location_failed": null, "monitor_options": {"renotify_interval": null}, "noScreenshot": null, "retry": {"count": null, "interval": null}, "tick_every": 60}, "public_id": null, "status": "live", "steps": [{"allowFailure": null, "name": null, "params": null, "timeout": null, "type": "assertCurrentUrl"}], "tags": [null], "type": "browser"}
    When the request is sent
    Then the response status is 404 - Synthetic Monitoring is not activated for the user

  @generated @skip
  Scenario: Edit a browser test returns "OK" response
    Given new "UpdateBrowserTest" request
    And request contains "public_id" parameter from "<PATH>"
    And body {"config": {"assertions": [], "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "variables": [{"example": null, "id": null, "name": "VARIABLE_NAME", "pattern": null, "type": "element"}]}, "locations": [null], "message": "", "monitor_id": null, "name": null, "options": {"accept_self_signed": null, "allow_insecure": null, "device_ids": ["laptop_large"], "disableCors": null, "follow_redirects": null, "min_failure_duration": null, "min_location_failed": null, "monitor_options": {"renotify_interval": null}, "noScreenshot": null, "retry": {"count": null, "interval": null}, "tick_every": 60}, "public_id": null, "status": "live", "steps": [{"allowFailure": null, "name": null, "params": null, "timeout": null, "type": "assertCurrentUrl"}], "tags": [null], "type": "browser"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Edit a global variable returns "Invalid request" response
    Given new "EditGlobalVariable" request
    And request contains "variable_id" parameter from "<PATH>"
    And body {"description": "Example description", "name": "MY_VARIABLE", "parse_test_options": {"field": "content-type", "parser": {"type": "regex", "value": ".*"}, "type": "http_body"}, "parse_test_public_id": "abc-def-123", "tags": ["team:front", "test:workflow-1"], "value": {"secure": true, "value": "value"}}
    When the request is sent
    Then the response status is 400 Invalid request

  @generated @skip
  Scenario: Edit a global variable returns "OK" response
    Given new "EditGlobalVariable" request
    And request contains "variable_id" parameter from "<PATH>"
    And body {"description": "Example description", "name": "MY_VARIABLE", "parse_test_options": {"field": "content-type", "parser": {"type": "regex", "value": ".*"}, "type": "http_body"}, "parse_test_public_id": "abc-def-123", "tags": ["team:front", "test:workflow-1"], "value": {"secure": true, "value": "value"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Edit a private location returns "- Private locations are not activated for the user" response
    Given new "UpdatePrivateLocation" request
    And request contains "location_id" parameter from "<PATH>"
    And body {"description": "Description of private location", "name": "New private location", "tags": ["team:front"]}
    When the request is sent
    Then the response status is 404 - Private locations are not activated for the user

  @generated @skip
  Scenario: Edit a private location returns "OK" response
    Given new "UpdatePrivateLocation" request
    And request contains "location_id" parameter from "<PATH>"
    And body {"description": "Description of private location", "name": "New private location", "tags": ["team:front"]}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Edit a test returns "- JSON format is wrong" response
    Given new "UpdateTest" request
    And request contains "public_id" parameter from "<PATH>"
    And body {"config": {"assertions": [], "configVariables": [{"example": null, "name": "VARIABLE_NAME", "pattern": null, "type": "text"}], "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "variables": [{"example": null, "id": null, "name": "VARIABLE_NAME", "pattern": null, "type": "element"}]}, "locations": [null], "message": null, "monitor_id": null, "name": null, "options": {"accept_self_signed": null, "allow_insecure": null, "device_ids": ["laptop_large"], "disableCors": null, "follow_redirects": null, "min_failure_duration": null, "min_location_failed": null, "monitor_options": {"renotify_interval": null}, "noScreenshot": null, "retry": {"count": null, "interval": null}, "tick_every": 60}, "public_id": null, "status": "live", "steps": [{"allowFailure": null, "name": null, "params": null, "timeout": null, "type": "assertCurrentUrl"}], "subtype": "http", "tags": [null], "type": "api"}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip
  Scenario: Edit a test returns "- Synthetic is not activated for the user" response
    Given new "UpdateTest" request
    And request contains "public_id" parameter from "<PATH>"
    And body {"config": {"assertions": [], "configVariables": [{"example": null, "name": "VARIABLE_NAME", "pattern": null, "type": "text"}], "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "variables": [{"example": null, "id": null, "name": "VARIABLE_NAME", "pattern": null, "type": "element"}]}, "locations": [null], "message": null, "monitor_id": null, "name": null, "options": {"accept_self_signed": null, "allow_insecure": null, "device_ids": ["laptop_large"], "disableCors": null, "follow_redirects": null, "min_failure_duration": null, "min_location_failed": null, "monitor_options": {"renotify_interval": null}, "noScreenshot": null, "retry": {"count": null, "interval": null}, "tick_every": 60}, "public_id": null, "status": "live", "steps": [{"allowFailure": null, "name": null, "params": null, "timeout": null, "type": "assertCurrentUrl"}], "subtype": "http", "tags": [null], "type": "api"}
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @generated @skip
  Scenario: Edit a test returns "OK" response
    Given new "UpdateTest" request
    And request contains "public_id" parameter from "<PATH>"
    And body {"config": {"assertions": [], "configVariables": [{"example": null, "name": "VARIABLE_NAME", "pattern": null, "type": "text"}], "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "variables": [{"example": null, "id": null, "name": "VARIABLE_NAME", "pattern": null, "type": "element"}]}, "locations": [null], "message": null, "monitor_id": null, "name": null, "options": {"accept_self_signed": null, "allow_insecure": null, "device_ids": ["laptop_large"], "disableCors": null, "follow_redirects": null, "min_failure_duration": null, "min_location_failed": null, "monitor_options": {"renotify_interval": null}, "noScreenshot": null, "retry": {"count": null, "interval": null}, "tick_every": 60}, "public_id": null, "status": "live", "steps": [{"allowFailure": null, "name": null, "params": null, "timeout": null, "type": "assertCurrentUrl"}], "subtype": "http", "tags": [null], "type": "api"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Edit an API test returns "- JSON format is wrong" response
    Given new "UpdateAPITest" request
    And request contains "public_id" parameter from "<PATH>"
    And body {"config": {"assertions": [], "configVariables": [{"example": null, "name": "VARIABLE_NAME", "pattern": null, "type": "text"}], "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "steps": [{"assertions": [], "extractedValues": [{"field": "content-type", "name": null, "parser": {"type": "regex", "value": ".*"}, "type": "http_body"}], "name": null, "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "subtype": "http"}]}, "locations": [null], "message": null, "monitor_id": null, "name": null, "options": {"accept_self_signed": null, "allow_insecure": null, "device_ids": ["laptop_large"], "disableCors": null, "follow_redirects": null, "min_failure_duration": null, "min_location_failed": null, "monitor_options": {"renotify_interval": null}, "noScreenshot": null, "retry": {"count": null, "interval": null}, "tick_every": 60}, "public_id": null, "status": "live", "subtype": "http", "tags": [null], "type": "api"}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip
  Scenario: Edit an API test returns "- Synthetic Monitoring is not activated for the user" response
    Given new "UpdateAPITest" request
    And request contains "public_id" parameter from "<PATH>"
    And body {"config": {"assertions": [], "configVariables": [{"example": null, "name": "VARIABLE_NAME", "pattern": null, "type": "text"}], "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "steps": [{"assertions": [], "extractedValues": [{"field": "content-type", "name": null, "parser": {"type": "regex", "value": ".*"}, "type": "http_body"}], "name": null, "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "subtype": "http"}]}, "locations": [null], "message": null, "monitor_id": null, "name": null, "options": {"accept_self_signed": null, "allow_insecure": null, "device_ids": ["laptop_large"], "disableCors": null, "follow_redirects": null, "min_failure_duration": null, "min_location_failed": null, "monitor_options": {"renotify_interval": null}, "noScreenshot": null, "retry": {"count": null, "interval": null}, "tick_every": 60}, "public_id": null, "status": "live", "subtype": "http", "tags": [null], "type": "api"}
    When the request is sent
    Then the response status is 404 - Synthetic Monitoring is not activated for the user

  @generated @skip
  Scenario: Edit an API test returns "OK" response
    Given new "UpdateAPITest" request
    And request contains "public_id" parameter from "<PATH>"
    And body {"config": {"assertions": [], "configVariables": [{"example": null, "name": "VARIABLE_NAME", "pattern": null, "type": "text"}], "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "steps": [{"assertions": [], "extractedValues": [{"field": "content-type", "name": null, "parser": {"type": "regex", "value": ".*"}, "type": "http_body"}], "name": null, "request": {"basicAuth": {"password": "", "username": ""}, "body": null, "certificate": {"cert": {"content": null, "filename": null, "updatedAt": null}, "key": {"content": null, "filename": null, "updatedAt": null}}, "dnsServer": null, "headers": null, "host": null, "method": "GET", "noSavingResponseBody": null, "port": null, "query": null, "timeout": null, "url": null}, "subtype": "http"}]}, "locations": [null], "message": null, "monitor_id": null, "name": null, "options": {"accept_self_signed": null, "allow_insecure": null, "device_ids": ["laptop_large"], "disableCors": null, "follow_redirects": null, "min_failure_duration": null, "min_location_failed": null, "monitor_options": {"renotify_interval": null}, "noScreenshot": null, "retry": {"count": null, "interval": null}, "tick_every": 60}, "public_id": null, "status": "live", "subtype": "http", "tags": [null], "type": "api"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a browser test result returns "- Synthetic is not activated for the user" response
    Given new "GetBrowserTestResult" request
    And request contains "public_id" parameter from "<PATH>"
    And request contains "result_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @generated @skip
  Scenario: Get a browser test result returns "OK" response
    Given new "GetBrowserTestResult" request
    And request contains "public_id" parameter from "<PATH>"
    And request contains "result_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a browser test returns "- Synthetic is not activated for the user" response
    Given new "GetBrowserTest" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @generated @skip
  Scenario: Get a browser test returns "OK" response
    Given new "GetBrowserTest" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a browser test's latest results summaries returns "- Synthetic is not activated for the user" response
    Given new "GetBrowserTestLatestResults" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @generated @skip
  Scenario: Get a browser test's latest results summaries returns "OK" response
    Given new "GetBrowserTestLatestResults" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a global variable returns "Not found" response
    Given new "GetGlobalVariable" request
    And request contains "variable_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip
  Scenario: Get a global variable returns "OK" response
    Given new "GetGlobalVariable" request
    And request contains "variable_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a private location returns "- Synthetic private locations are not activated for the user" response
    Given new "GetPrivateLocation" request
    And request contains "location_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 - Synthetic private locations are not activated for the user

  @generated @skip
  Scenario: Get a private location returns "OK" response
    Given new "GetPrivateLocation" request
    And request contains "location_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a test configuration returns "- Synthetic is not activated for the user" response
    Given new "GetTest" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @generated @skip
  Scenario: Get a test configuration returns "OK" response
    Given new "GetTest" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get all locations (public and private) returns "OK" response
    Given new "ListLocations" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get an API test result returns "- Synthetic is not activated for the user" response
    Given new "GetAPITestResult" request
    And request contains "public_id" parameter from "<PATH>"
    And request contains "result_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @generated @skip
  Scenario: Get an API test result returns "OK" response
    Given new "GetAPITestResult" request
    And request contains "public_id" parameter from "<PATH>"
    And request contains "result_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get an API test returns "- Synthetic Monitoring is not activated for the user" response
    Given new "GetAPITest" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 - Synthetic Monitoring is not activated for the user

  @generated @skip
  Scenario: Get an API test returns "OK" response
    Given new "GetAPITest" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get an API test's latest results summaries returns "- Synthetic is not activated for the user" response
    Given new "GetAPITestLatestResults" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @generated @skip
  Scenario: Get an API test's latest results summaries returns "OK" response
    Given new "GetAPITestLatestResults" request
    And request contains "public_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get the list of all tests returns "OK - Returns the list of all Synthetic tests." response
    Given new "ListTests" request
    When the request is sent
    Then the response status is 200 OK - Returns the list of all Synthetic tests.

  @generated @skip
  Scenario: Get the list of all tests returns "Synthetics is not activated for the user." response
    Given new "ListTests" request
    When the request is sent
    Then the response status is 404 Synthetics is not activated for the user.

  @generated @skip
  Scenario: Pause or start a test returns "- Synthetic is not activated for the user" response
    Given new "UpdateTestPauseStatus" request
    And request contains "public_id" parameter from "<PATH>"
    And body {"new_status": "live"}
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @generated @skip
  Scenario: Pause or start a test returns "JSON format is wrong." response
    Given new "UpdateTestPauseStatus" request
    And request contains "public_id" parameter from "<PATH>"
    And body {"new_status": "live"}
    When the request is sent
    Then the response status is 400 JSON format is wrong.

  @generated @skip
  Scenario: Pause or start a test returns "OK - Returns a boolean indicating if the update was successful." response
    Given new "UpdateTestPauseStatus" request
    And request contains "public_id" parameter from "<PATH>"
    And body {"new_status": "live"}
    When the request is sent
    Then the response status is 200 OK - Returns a boolean indicating if the update was successful.

  @generated @skip
  Scenario: Trigger tests from CI/CD pipelines returns "JSON format is wrong" response
    Given new "TriggerCITests" request
    And body {"tests": [{"allowInsecureCertificates": null, "basicAuth": {"password": "", "username": ""}, "body": null, "bodyType": null, "cookies": null, "deviceIds": ["laptop_large"], "followRedirects": null, "headers": null, "locations": [null], "metadata": {"ci": {"pipeline": null, "provider": null}, "git": {"branch": null, "commit_sha": null}}, "public_id": "aaa-aaa-aaa", "retry": {"count": null, "interval": null}, "startUrl": null, "variables": null}]}
    When the request is sent
    Then the response status is 400 JSON format is wrong

  @generated @skip
  Scenario: Trigger tests from CI/CD pipelines returns "OK" response
    Given new "TriggerCITests" request
    And body {"tests": [{"allowInsecureCertificates": null, "basicAuth": {"password": "", "username": ""}, "body": null, "bodyType": null, "cookies": null, "deviceIds": ["laptop_large"], "followRedirects": null, "headers": null, "locations": [null], "metadata": {"ci": {"pipeline": null, "provider": null}, "git": {"branch": null, "commit_sha": null}}, "public_id": "aaa-aaa-aaa", "retry": {"count": null, "interval": null}, "startUrl": null, "variables": null}]}
    When the request is sent
    Then the response status is 200 OK
