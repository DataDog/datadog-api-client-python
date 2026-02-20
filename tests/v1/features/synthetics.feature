@endpoint(synthetics) @endpoint(synthetics-v1)
Feature: Synthetics
  Synthetic tests use simulated requests and actions so you can monitor the
  availability and performance of systems and applications. Datadog supports
  the following types of synthetic tests: - [API
  tests](https://docs.datadoghq.com/synthetics/api_tests/) - [Browser
  tests](https://docs.datadoghq.com/synthetics/browser_tests) - [Network
  Path tests](https://docs.datadoghq.com/synthetics/network_path_tests/) -
  [Mobile Application
  tests](https://docs.datadoghq.com/synthetics/mobile_app_testing)  You can
  use the Datadog API to create, manage, and organize tests and test suites
  programmatically.  For more information, see the [Synthetic Monitoring
  documentation](https://docs.datadoghq.com/synthetics/).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Synthetics" API

  @replay-only @skip-validation @team:DataDog/synthetics-managing
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

  @team:DataDog/synthetics-managing
  Scenario: Create a FIDO global variable returns "OK" response
    Given there is a valid "synthetics_api_test_multi_step" in the system
    And new "CreateGlobalVariable" request
    And body from file "synthetics_global_variable_fido_payload.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "GLOBAL_VARIABLE_FIDO_PAYLOAD_{{ unique_upper_alnum }}"

  @team:DataDog/synthetics-managing
  Scenario: Create a TOTP global variable returns "OK" response
    Given there is a valid "synthetics_api_test_multi_step" in the system
    And new "CreateGlobalVariable" request
    And body from file "synthetics_global_variable_totp_payload.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "GLOBAL_VARIABLE_TOTP_PAYLOAD_{{ unique_upper_alnum }}"

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Create a browser test returns "- JSON format is wrong" response
    Given new "CreateSyntheticsBrowserTest" request
    And body with value {"config": {"assertions": [], "configVariables": [{"name": "VARIABLE_NAME", "secure": false, "type": "text"}], "request": {"basicAuth": {"password": "PaSSw0RD!", "type": "web", "username": "my_username"}, "bodyType": "text/plain", "callType": "unary", "certificate": {"cert": {}, "key": {}}, "certificateDomains": [], "files": [{}], "httpVersion": "http1", "proxy": {"url": "https://example.com"}, "service": "Greeter", "url": "https://example.com"}, "variables": [{"name": "VARIABLE_NAME", "type": "text"}]}, "locations": ["aws:eu-west-3"], "message": "", "name": "Example test name", "options": {"blockedRequestPatterns": [], "ci": {"executionRule": "blocking"}, "device_ids": ["chrome.laptop_large"], "httpVersion": "http1", "monitor_options": {"notification_preset_name": "show_all"}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "rumSettings": {"applicationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "clientTokenId": 12345, "isEnabled": true}, "scheduling": {"timeframes": [{"day": 1, "from": "07:00", "to": "16:00"}, {"day": 3, "from": "07:00", "to": "16:00"}], "timezone": "America/New_York"}}, "status": "live", "steps": [{"type": "assertElementContent"}], "tags": ["env:prod"], "type": "browser"}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @team:DataDog/synthetics-managing
  Scenario: Create a browser test returns "OK - Returns saved rumSettings." response
    Given new "CreateSyntheticsBrowserTest" request
    And body from file "synthetics_browser_test_payload_with_rum_settings.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "options.rumSettings.isEnabled" is equal to true
    And the response "options.rumSettings.applicationId" is equal to "mockApplicationId"
    And the response "options.rumSettings.clientTokenId" is equal to 12345
    And the response "steps[0]" has field "public_id"

  @team:DataDog/synthetics-managing
  Scenario: Create a browser test returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsBrowserTest" request
    And body from file "synthetics_browser_test_payload.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "name" is equal to "{{ unique }}"
    And the response "config.configVariables" has item with field "secure" with value true
    And the response "config.variables" has item with field "secure" with value true
    And the response "steps[0].alwaysExecute" is equal to true
    And the response "steps[0].exitIfSucceed" is equal to true

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Create a browser test returns "Test quota is reached" response
    Given new "CreateSyntheticsBrowserTest" request
    And body with value {"config": {"assertions": [], "configVariables": [{"name": "VARIABLE_NAME", "secure": false, "type": "text"}], "request": {"basicAuth": {"password": "PaSSw0RD!", "type": "web", "username": "my_username"}, "bodyType": "text/plain", "callType": "unary", "certificate": {"cert": {}, "key": {}}, "certificateDomains": [], "files": [{}], "httpVersion": "http1", "proxy": {"url": "https://example.com"}, "service": "Greeter", "url": "https://example.com"}, "variables": [{"name": "VARIABLE_NAME", "type": "text"}]}, "locations": ["aws:eu-west-3"], "message": "", "name": "Example test name", "options": {"blockedRequestPatterns": [], "ci": {"executionRule": "blocking"}, "device_ids": ["chrome.laptop_large"], "httpVersion": "http1", "monitor_options": {"notification_preset_name": "show_all"}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "rumSettings": {"applicationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "clientTokenId": 12345, "isEnabled": true}, "scheduling": {"timeframes": [{"day": 1, "from": "07:00", "to": "16:00"}, {"day": 3, "from": "07:00", "to": "16:00"}], "timezone": "America/New_York"}}, "status": "live", "steps": [{"type": "assertElementContent"}], "tags": ["env:prod"], "type": "browser"}
    When the request is sent
    Then the response status is 402 Test quota is reached

  @team:DataDog/synthetics-managing
  Scenario: Create a browser test with advanced scheduling options returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsBrowserTest" request
    And body from file "synthetics_browser_test_payload_with_advanced_scheduling.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "name" is equal to "{{ unique }}"
    And the response "options.scheduling.timeframes[0].day" is equal to 1
    And the response "options.scheduling.timeframes[0].from" is equal to "07:00"
    And the response "options.scheduling.timeframes[1].to" is equal to "16:00"
    And the response "options.scheduling.timezone" is equal to "America/New_York"

  @team:DataDog/synthetics-managing
  Scenario: Create a global variable from test returns "OK" response
    Given there is a valid "synthetics_api_test_multi_step" in the system
    And new "CreateGlobalVariable" request
    And body from file "synthetics_global_variable_from_test_payload.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "GLOBAL_VARIABLE_FROM_TEST_PAYLOAD_{{ unique_upper_alnum }}"

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Create a global variable returns "Conflict" response
    Given new "CreateGlobalVariable" request
    And body with value {"attributes": {"restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"]}, "description": "Example description", "name": "MY_VARIABLE", "parse_test_options": {"field": "content-type", "localVariableName": "LOCAL_VARIABLE", "parser": {"type": "regex", "value": ".*"}, "type": "http_body"}, "parse_test_public_id": "abc-def-123", "tags": ["team:front", "test:workflow-1"], "value": {"secure": true, "value": "value"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Create a global variable returns "Invalid request" response
    Given new "CreateGlobalVariable" request
    And body with value {"attributes": {"restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"]}, "description": "Example description", "name": "MY_VARIABLE", "parse_test_options": {"field": "content-type", "localVariableName": "LOCAL_VARIABLE", "parser": {"type": "regex", "value": ".*"}, "type": "http_body"}, "parse_test_public_id": "abc-def-123", "tags": ["team:front", "test:workflow-1"], "value": {"secure": true, "value": "value"}}
    When the request is sent
    Then the response status is 400 Invalid request

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Create a global variable returns "OK" response
    Given new "CreateGlobalVariable" request
    And body with value {"attributes": {"restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"]}, "description": "Example description", "name": "MY_VARIABLE", "parse_test_options": {"field": "content-type", "localVariableName": "LOCAL_VARIABLE", "parser": {"type": "regex", "value": ".*"}, "type": "http_body"}, "parse_test_public_id": "abc-def-123", "tags": ["team:front", "test:workflow-1"], "value": {"secure": true, "value": "value"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Create a mobile test returns "- JSON format is wrong" response
    Given new "CreateSyntheticsMobileTest" request
    And body with value {"config": {"variables": [{"name": "VARIABLE_NAME", "secure": false, "type": "text"}]}, "device_ids": ["chrome.laptop_large"], "message": "Notification message", "name": "Example test name", "options": {"bindings": [{"principals": [], "relation": "editor"}], "ci": {"executionRule": "blocking"}, "device_ids": ["synthetics:mobile:device:apple_ipad_10th_gen_2022_ios_16"], "mobileApplication": {"applicationId": "00000000-0000-0000-0000-aaaaaaaaaaaa", "referenceId": "00000000-0000-0000-0000-aaaaaaaaaaab", "referenceType": "latest"}, "monitor_options": {"notification_preset_name": "show_all"}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "scheduling": {"timeframes": [{"day": 1, "from": "07:00", "to": "16:00"}, {"day": 3, "from": "07:00", "to": "16:00"}], "timezone": "America/New_York"}, "tick_every": 300}, "status": "live", "steps": [{"name": "", "params": {"check": "equals", "direction": "up", "element": {"contextType": "native", "relativePosition": {}, "userLocator": {"values": [{"type": "accessibility-id"}]}}, "positions": [{}], "variable": {"example": "", "name": "VAR_NAME"}}, "publicId": "pub-lic-id0", "type": "assertElementContent"}], "tags": ["env:production"], "type": "mobile"}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @team:DataDog/synthetics-managing
  Scenario: Create a mobile test returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsMobileTest" request
    And body from file "synthetics_mobile_test_payload.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "name" is equal to "{{ unique }}"
    And the response "options.device_ids[0]" is equal to "synthetics:mobile:device:iphone_15_ios_17"
    And the response "options.mobileApplication.applicationId" is equal to "ab0e0aed-536d-411a-9a99-5428c27d8f8e"
    And the response "options.mobileApplication.referenceId" is equal to "6115922a-5f5d-455e-bc7e-7955a57f3815"
    And the response "options.mobileApplication.referenceType" is equal to "version"

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Create a mobile test returns "Test quota is reached" response
    Given new "CreateSyntheticsMobileTest" request
    And body with value {"config": {"variables": [{"name": "VARIABLE_NAME", "secure": false, "type": "text"}]}, "device_ids": ["chrome.laptop_large"], "message": "Notification message", "name": "Example test name", "options": {"bindings": [{"principals": [], "relation": "editor"}], "ci": {"executionRule": "blocking"}, "device_ids": ["synthetics:mobile:device:apple_ipad_10th_gen_2022_ios_16"], "mobileApplication": {"applicationId": "00000000-0000-0000-0000-aaaaaaaaaaaa", "referenceId": "00000000-0000-0000-0000-aaaaaaaaaaab", "referenceType": "latest"}, "monitor_options": {"notification_preset_name": "show_all"}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "scheduling": {"timeframes": [{"day": 1, "from": "07:00", "to": "16:00"}, {"day": 3, "from": "07:00", "to": "16:00"}], "timezone": "America/New_York"}, "tick_every": 300}, "status": "live", "steps": [{"name": "", "params": {"check": "equals", "direction": "up", "element": {"contextType": "native", "relativePosition": {}, "userLocator": {"values": [{"type": "accessibility-id"}]}}, "positions": [{}], "variable": {"example": "", "name": "VAR_NAME"}}, "publicId": "pub-lic-id0", "type": "assertElementContent"}], "tags": ["env:production"], "type": "mobile"}
    When the request is sent
    Then the response status is 402 Test quota is reached

  @team:DataDog/synthetics-managing
  Scenario: Create a multi-step api test with every type of basicAuth returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsAPITest" request
    And body from file "synthetics_api_test_multi_step_with_every_type_of_basic_auth.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "name" is equal to "{{ unique }}"
    And the response "config.steps[0].request.basicAuth" is equal to {"password": "password", "username": "username"}
    And the response "config.steps[1].request.basicAuth.type" is equal to "web"
    And the response "config.steps[2].request.basicAuth.type" is equal to "sigv4"
    And the response "config.steps[3].request.basicAuth.type" is equal to "ntlm"
    And the response "config.steps[4].request.basicAuth.type" is equal to "digest"
    And the response "config.steps[5].request.basicAuth.type" is equal to "oauth-client"
    And the response "config.steps[6].request.basicAuth.type" is equal to "oauth-rop"

  @team:DataDog/synthetics-managing
  Scenario: Create a multistep test with subtest returns "OK" response
    Given there is a valid "synthetics_api_test" in the system
    And new "CreateSyntheticsAPITest" request
    And body from file "synthetics_api_test_multi_step_with_subtest.json"
    When the request is sent
    Then the response status is 200 OK

  @replay-only @team:DataDog/synthetics-managing
  Scenario: Create a private location returns "OK" response
    Given there is a valid "role" in the system
    And new "CreatePrivateLocation" request
    And body with value {"description": "Test {{ unique }} description", "metadata": {"restricted_roles": ["{{ role.data.id }}"]}, "name": "{{ unique }}", "tags": ["test:{{ unique_lower_alnum }}"]}
    When the request is sent
    Then the response status is 200 OK
    And the response "private_location.name" is equal to "{{ unique }}"
    And the response "private_location.metadata.restricted_roles[0]" has the same value as "role.data.id"

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Create a private location returns "Private locations are not activated for the user" response
    Given new "CreatePrivateLocation" request
    And body with value {"description": "Description of private location", "metadata": {"restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"]}, "name": "New private location", "tags": ["team:front"]}
    When the request is sent
    Then the response status is 404 Private locations are not activated for the user

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Create a private location returns "Quota reached for private locations" response
    Given new "CreatePrivateLocation" request
    And body with value {"description": "Description of private location", "metadata": {"restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"]}, "name": "New private location", "tags": ["team:front"]}
    When the request is sent
    Then the response status is 402 Quota reached for private locations

  @team:DataDog/synthetics-managing
  Scenario: Create an API GRPC test returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsAPITest" request
    And body from file "synthetics_api_grpc_test_payload.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "name" is equal to "{{ unique }}"

  @team:DataDog/synthetics-managing
  Scenario: Create an API HTTP test has bodyHash filled out
    Given new "CreateSyntheticsAPITest" request
    And body from file "synthetics_api_http_test_payload.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "config.assertions[6].operator" is equal to "md5"
    And the response "config.assertions[6].target" is equal to "a"
    And the response "config.assertions[6].type" is equal to "bodyHash"

  @team:DataDog/synthetics-managing
  Scenario: Create an API HTTP test returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsAPITest" request
    And body from file "synthetics_api_http_test_payload.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "name" is equal to "{{ unique }}"
    And the response "config.assertions[7].type" is equal to "javascript"
    And the response "config.assertions[7].code" is equal to "const hello = 'world';"

  @team:DataDog/synthetics-managing
  Scenario: Create an API HTTP with oauth-rop test returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsAPITest" request
    And body from file "synthetics_api_http_test_oauth_rop_payload.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "name" is equal to "{{ unique }}"

  @team:DataDog/synthetics-managing
  Scenario: Create an API SSL test returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsAPITest" request
    And body from file "synthetics_api_ssl_test_payload.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "name" is equal to "{{ unique }}"

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Create an API test returns "- JSON format is wrong" response
    Given new "CreateSyntheticsAPITest" request
    And body with value {"config": {"assertions": [{"operator": "lessThan", "target": 1000, "type": "responseTime"}], "request": {"method": "GET", "url": "https://example.com"}}, "locations": ["aws:eu-west-3"], "message": "Notification message", "name": "Example test name", "options": {"blockedRequestPatterns": [], "ci": {"executionRule": "blocking"}, "device_ids": ["chrome.laptop_large"], "httpVersion": "http1", "monitor_options": {"notification_preset_name": "show_all"}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "rumSettings": {"applicationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "clientTokenId": 12345, "isEnabled": true}, "scheduling": {"timeframes": [{"day": 1, "from": "07:00", "to": "16:00"}, {"day": 3, "from": "07:00", "to": "16:00"}], "timezone": "America/New_York"}}, "status": "live", "subtype": "http", "tags": ["env:production"], "type": "api"}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Create an API test returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsAPITest" request
    And body with value {"config": {"assertions": [{"operator": "lessThan", "target": 1000, "type": "responseTime"}], "request": {"method": "GET", "url": "https://example.com"}}, "locations": ["aws:eu-west-3"], "message": "Notification message", "name": "Example test name", "options": {"blockedRequestPatterns": [], "ci": {"executionRule": "blocking"}, "device_ids": ["chrome.laptop_large"], "httpVersion": "http1", "monitor_options": {"notification_preset_name": "show_all"}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "rumSettings": {"applicationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "clientTokenId": 12345, "isEnabled": true}, "scheduling": {"timeframes": [{"day": 1, "from": "07:00", "to": "16:00"}, {"day": 3, "from": "07:00", "to": "16:00"}], "timezone": "America/New_York"}}, "status": "live", "subtype": "http", "tags": ["env:production"], "type": "api"}
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Create an API test returns "Test quota is reached" response
    Given new "CreateSyntheticsAPITest" request
    And body with value {"config": {"assertions": [{"operator": "lessThan", "target": 1000, "type": "responseTime"}], "request": {"method": "GET", "url": "https://example.com"}}, "locations": ["aws:eu-west-3"], "message": "Notification message", "name": "Example test name", "options": {"blockedRequestPatterns": [], "ci": {"executionRule": "blocking"}, "device_ids": ["chrome.laptop_large"], "httpVersion": "http1", "monitor_options": {"notification_preset_name": "show_all"}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "rumSettings": {"applicationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "clientTokenId": 12345, "isEnabled": true}, "scheduling": {"timeframes": [{"day": 1, "from": "07:00", "to": "16:00"}, {"day": 3, "from": "07:00", "to": "16:00"}], "timezone": "America/New_York"}}, "status": "live", "subtype": "http", "tags": ["env:production"], "type": "api"}
    When the request is sent
    Then the response status is 402 Test quota is reached

  @team:DataDog/synthetics-managing
  Scenario: Create an API test with UDP subtype returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsAPITest" request
    And body from file "synthetics_api_test_udp_payload.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "name" is equal to "{{ unique }}"

  @team:DataDog/synthetics-managing
  Scenario: Create an API test with WEBSOCKET subtype returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsAPITest" request
    And body from file "synthetics_api_test_websocket_payload.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "name" is equal to "{{ unique }}"

  @team:DataDog/synthetics-managing
  Scenario: Create an API test with a file payload returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsAPITest" request
    And body from file "synthetics_api_http_test_with_file_payload.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "name" is equal to "{{ unique }}"
    And the response "config.request.files[0].name" is equal to "file name"
    And the response "config.request.files[0].originalFileName" is equal to "image.png"
    And the response "config.request.files[0].type" is equal to "file type"
    And the response "config.request.files[0]" has field "bucketKey"

  @team:DataDog/synthetics-managing
  Scenario: Create an API test with multi subtype returns "OK - Returns the created test details." response
    Given new "CreateSyntheticsAPITest" request
    And body from file "synthetics_api_test_multi_step_payload.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "name" is equal to "{{ unique }}"
    And the response "config.steps[0].retry.count" is equal to 5
    And the response "config.steps[0].retry.interval" is equal to 1000
    And the response "config.steps[0].request.httpVersion" is equal to "http2"
    And the response "config.steps[0].exitIfSucceed" is equal to true
    And the response "config.steps[0].extractedValues[0].secure" is equal to true
    And the response "config.steps[0].extractedValuesFromScript" is equal to "dd.variable.set('STATUS_CODE', dd.response.statusCode);"
    And the response "config.steps[1].subtype" is equal to "wait"
    And the response "config.steps[1].value" is equal to 1
    And the response "config.steps[2].request.host" is equal to "grpcbin.test.k6.io"
    And the response "config.steps[3].subtype" is equal to "ssl"
    And the response "config.steps[3].request.host" is equal to "example.org"
    And the response "config.steps[3].request.port" is equal to 443
    And the response "config.steps[3].request.checkCertificateRevocation" is equal to true
    And the response "config.steps[3].request.disableAiaIntermediateFetching" is equal to true
    And the response "config.steps[4].subtype" is equal to "dns"
    And the response "config.steps[4].request.host" is equal to "troisdizaines.com"
    And the response "config.steps[4].request.dnsServer" is equal to "8.8.8.8"
    And the response "config.steps[4].request.dnsServerPort" is equal to "53"
    And the response "config.steps[5].subtype" is equal to "tcp"
    And the response "config.steps[5].request.host" is equal to "34.95.79.70"
    And the response "config.steps[5].request.shouldTrackHops" is equal to true
    And the response "config.steps[6].subtype" is equal to "icmp"
    And the response "config.steps[6].request.host" is equal to "34.95.79.70"
    And the response "config.steps[6].request.numberOfPackets" is equal to 4
    And the response "config.steps[7].subtype" is equal to "websocket"
    And the response "config.steps[7].request.url" is equal to "ws://34.95.79.70/web-socket"
    And the response "config.steps[7].request.message" is equal to "My message"
    And the response "config.steps[7].request.isMessageBase64Encoded" is equal to true
    And the response "config.steps[8].subtype" is equal to "udp"
    And the response "config.steps[8].request.host" is equal to "8.8.8.8"

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Delete a global variable returns "JSON format is wrong" response
    Given new "DeleteGlobalVariable" request
    And request contains "variable_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 JSON format is wrong

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Delete a global variable returns "Not found" response
    Given new "DeleteGlobalVariable" request
    And request contains "variable_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Delete a global variable returns "OK" response
    Given new "DeleteGlobalVariable" request
    And request contains "variable_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Delete a private location returns "- Private locations are not activated for the user" response
    Given new "DeletePrivateLocation" request
    And request contains "location_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 - Private locations are not activated for the user

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Delete a private location returns "OK" response
    Given new "DeletePrivateLocation" request
    And request contains "location_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Delete tests returns "- JSON format is wrong" response
    Given new "DeleteTests" request
    And body with value {"force_delete_dependencies": false, "public_ids": []}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Delete tests returns "- Tests to be deleted can't be found" response
    Given new "DeleteTests" request
    And body with value {"force_delete_dependencies": false, "public_ids": []}
    When the request is sent
    Then the response status is 404 - Tests to be deleted can't be found

  @skip @team:DataDog/synthetics-managing
  Scenario: Delete tests returns "OK." response
    Given there is a valid "synthetics_api_test" in the system
    And new "DeleteTests" request
    And body with value {"public_ids": ["{{ synthetics_api_test.public_id }}"]}
    When the request is sent
    Then the response status is 200 OK.
    And the response "deleted_tests[0].public_id" is equal to "{{ synthetics_api_test.public_id }}"

  @team:DataDog/synthetics-managing
  Scenario: Edit a Mobile test returns "OK" response
    Given there is a valid "synthetics_mobile_test" in the system
    And new "UpdateMobileTest" request
    And request contains "public_id" parameter from "synthetics_mobile_test.public_id"
    And body from file "synthetics_mobile_test_update_payload.json"
    When the request is sent
    Then the response status is 200 OK - Returns the created test details.
    And the response "name" is equal to "{{ unique }}-updated"
    And the response "options.device_ids[0]" is equal to "synthetics:mobile:device:iphone_15_ios_17"
    And the response "options.mobileApplication.applicationId" is equal to "ab0e0aed-536d-411a-9a99-5428c27d8f8e"
    And the response "options.mobileApplication.referenceId" is equal to "6115922a-5f5d-455e-bc7e-7955a57f3815"
    And the response "options.mobileApplication.referenceType" is equal to "version"

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Edit a browser test returns "- JSON format is wrong" response
    Given new "UpdateBrowserTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"config": {"assertions": [], "configVariables": [{"name": "VARIABLE_NAME", "secure": false, "type": "text"}], "request": {"basicAuth": {"password": "PaSSw0RD!", "type": "web", "username": "my_username"}, "bodyType": "text/plain", "callType": "unary", "certificate": {"cert": {}, "key": {}}, "certificateDomains": [], "files": [{}], "httpVersion": "http1", "proxy": {"url": "https://example.com"}, "service": "Greeter", "url": "https://example.com"}, "variables": [{"name": "VARIABLE_NAME", "type": "text"}]}, "locations": ["aws:eu-west-3"], "message": "", "name": "Example test name", "options": {"blockedRequestPatterns": [], "ci": {"executionRule": "blocking"}, "device_ids": ["chrome.laptop_large"], "httpVersion": "http1", "monitor_options": {"notification_preset_name": "show_all"}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "rumSettings": {"applicationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "clientTokenId": 12345, "isEnabled": true}, "scheduling": {"timeframes": [{"day": 1, "from": "07:00", "to": "16:00"}, {"day": 3, "from": "07:00", "to": "16:00"}], "timezone": "America/New_York"}}, "status": "live", "steps": [{"type": "assertElementContent"}], "tags": ["env:prod"], "type": "browser"}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Edit a browser test returns "- Synthetic Monitoring is not activated for the user" response
    Given new "UpdateBrowserTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"config": {"assertions": [], "configVariables": [{"name": "VARIABLE_NAME", "secure": false, "type": "text"}], "request": {"basicAuth": {"password": "PaSSw0RD!", "type": "web", "username": "my_username"}, "bodyType": "text/plain", "callType": "unary", "certificate": {"cert": {}, "key": {}}, "certificateDomains": [], "files": [{}], "httpVersion": "http1", "proxy": {"url": "https://example.com"}, "service": "Greeter", "url": "https://example.com"}, "variables": [{"name": "VARIABLE_NAME", "type": "text"}]}, "locations": ["aws:eu-west-3"], "message": "", "name": "Example test name", "options": {"blockedRequestPatterns": [], "ci": {"executionRule": "blocking"}, "device_ids": ["chrome.laptop_large"], "httpVersion": "http1", "monitor_options": {"notification_preset_name": "show_all"}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "rumSettings": {"applicationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "clientTokenId": 12345, "isEnabled": true}, "scheduling": {"timeframes": [{"day": 1, "from": "07:00", "to": "16:00"}, {"day": 3, "from": "07:00", "to": "16:00"}], "timezone": "America/New_York"}}, "status": "live", "steps": [{"type": "assertElementContent"}], "tags": ["env:prod"], "type": "browser"}
    When the request is sent
    Then the response status is 404 - Synthetic Monitoring is not activated for the user

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Edit a browser test returns "OK" response
    Given new "UpdateBrowserTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"config": {"assertions": [], "configVariables": [{"name": "VARIABLE_NAME", "secure": false, "type": "text"}], "request": {"basicAuth": {"password": "PaSSw0RD!", "type": "web", "username": "my_username"}, "bodyType": "text/plain", "callType": "unary", "certificate": {"cert": {}, "key": {}}, "certificateDomains": [], "files": [{}], "httpVersion": "http1", "proxy": {"url": "https://example.com"}, "service": "Greeter", "url": "https://example.com"}, "variables": [{"name": "VARIABLE_NAME", "type": "text"}]}, "locations": ["aws:eu-west-3"], "message": "", "name": "Example test name", "options": {"blockedRequestPatterns": [], "ci": {"executionRule": "blocking"}, "device_ids": ["chrome.laptop_large"], "httpVersion": "http1", "monitor_options": {"notification_preset_name": "show_all"}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "rumSettings": {"applicationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "clientTokenId": 12345, "isEnabled": true}, "scheduling": {"timeframes": [{"day": 1, "from": "07:00", "to": "16:00"}, {"day": 3, "from": "07:00", "to": "16:00"}], "timezone": "America/New_York"}}, "status": "live", "steps": [{"type": "assertElementContent"}], "tags": ["env:prod"], "type": "browser"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Edit a global variable returns "Invalid request" response
    Given new "EditGlobalVariable" request
    And request contains "variable_id" parameter from "REPLACE.ME"
    And body with value {"attributes": {"restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"]}, "description": "Example description", "name": "MY_VARIABLE", "parse_test_options": {"field": "content-type", "localVariableName": "LOCAL_VARIABLE", "parser": {"type": "regex", "value": ".*"}, "type": "http_body"}, "parse_test_public_id": "abc-def-123", "tags": ["team:front", "test:workflow-1"], "value": {"secure": true, "value": "value"}}
    When the request is sent
    Then the response status is 400 Invalid request

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Edit a global variable returns "OK" response
    Given new "EditGlobalVariable" request
    And request contains "variable_id" parameter from "REPLACE.ME"
    And body with value {"attributes": {"restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"]}, "description": "Example description", "name": "MY_VARIABLE", "parse_test_options": {"field": "content-type", "localVariableName": "LOCAL_VARIABLE", "parser": {"type": "regex", "value": ".*"}, "type": "http_body"}, "parse_test_public_id": "abc-def-123", "tags": ["team:front", "test:workflow-1"], "value": {"secure": true, "value": "value"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Edit a mobile test returns "- JSON format is wrong" response
    Given new "UpdateMobileTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"config": {"variables": [{"name": "VARIABLE_NAME", "secure": false, "type": "text"}]}, "device_ids": ["chrome.laptop_large"], "message": "Notification message", "name": "Example test name", "options": {"bindings": [{"principals": [], "relation": "editor"}], "ci": {"executionRule": "blocking"}, "device_ids": ["synthetics:mobile:device:apple_ipad_10th_gen_2022_ios_16"], "mobileApplication": {"applicationId": "00000000-0000-0000-0000-aaaaaaaaaaaa", "referenceId": "00000000-0000-0000-0000-aaaaaaaaaaab", "referenceType": "latest"}, "monitor_options": {"notification_preset_name": "show_all"}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "scheduling": {"timeframes": [{"day": 1, "from": "07:00", "to": "16:00"}, {"day": 3, "from": "07:00", "to": "16:00"}], "timezone": "America/New_York"}, "tick_every": 300}, "status": "live", "steps": [{"name": "", "params": {"check": "equals", "direction": "up", "element": {"contextType": "native", "relativePosition": {}, "userLocator": {"values": [{"type": "accessibility-id"}]}}, "positions": [{}], "variable": {"example": "", "name": "VAR_NAME"}}, "publicId": "pub-lic-id0", "type": "assertElementContent"}], "tags": ["env:production"], "type": "mobile"}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Edit a mobile test returns "- Synthetic Monitoring is not activated for the user" response
    Given new "UpdateMobileTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"config": {"variables": [{"name": "VARIABLE_NAME", "secure": false, "type": "text"}]}, "device_ids": ["chrome.laptop_large"], "message": "Notification message", "name": "Example test name", "options": {"bindings": [{"principals": [], "relation": "editor"}], "ci": {"executionRule": "blocking"}, "device_ids": ["synthetics:mobile:device:apple_ipad_10th_gen_2022_ios_16"], "mobileApplication": {"applicationId": "00000000-0000-0000-0000-aaaaaaaaaaaa", "referenceId": "00000000-0000-0000-0000-aaaaaaaaaaab", "referenceType": "latest"}, "monitor_options": {"notification_preset_name": "show_all"}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "scheduling": {"timeframes": [{"day": 1, "from": "07:00", "to": "16:00"}, {"day": 3, "from": "07:00", "to": "16:00"}], "timezone": "America/New_York"}, "tick_every": 300}, "status": "live", "steps": [{"name": "", "params": {"check": "equals", "direction": "up", "element": {"contextType": "native", "relativePosition": {}, "userLocator": {"values": [{"type": "accessibility-id"}]}}, "positions": [{}], "variable": {"example": "", "name": "VAR_NAME"}}, "publicId": "pub-lic-id0", "type": "assertElementContent"}], "tags": ["env:production"], "type": "mobile"}
    When the request is sent
    Then the response status is 404 - Synthetic Monitoring is not activated for the user

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Edit a mobile test returns "OK" response
    Given new "UpdateMobileTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"config": {"variables": [{"name": "VARIABLE_NAME", "secure": false, "type": "text"}]}, "device_ids": ["chrome.laptop_large"], "message": "Notification message", "name": "Example test name", "options": {"bindings": [{"principals": [], "relation": "editor"}], "ci": {"executionRule": "blocking"}, "device_ids": ["synthetics:mobile:device:apple_ipad_10th_gen_2022_ios_16"], "mobileApplication": {"applicationId": "00000000-0000-0000-0000-aaaaaaaaaaaa", "referenceId": "00000000-0000-0000-0000-aaaaaaaaaaab", "referenceType": "latest"}, "monitor_options": {"notification_preset_name": "show_all"}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "scheduling": {"timeframes": [{"day": 1, "from": "07:00", "to": "16:00"}, {"day": 3, "from": "07:00", "to": "16:00"}], "timezone": "America/New_York"}, "tick_every": 300}, "status": "live", "steps": [{"name": "", "params": {"check": "equals", "direction": "up", "element": {"contextType": "native", "relativePosition": {}, "userLocator": {"values": [{"type": "accessibility-id"}]}}, "positions": [{}], "variable": {"example": "", "name": "VAR_NAME"}}, "publicId": "pub-lic-id0", "type": "assertElementContent"}], "tags": ["env:production"], "type": "mobile"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Edit a private location returns "- Private locations are not activated for the user" response
    Given new "UpdatePrivateLocation" request
    And request contains "location_id" parameter from "REPLACE.ME"
    And body with value {"description": "Description of private location", "metadata": {"restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"]}, "name": "New private location", "tags": ["team:front"]}
    When the request is sent
    Then the response status is 404 - Private locations are not activated for the user

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Edit a private location returns "OK" response
    Given new "UpdatePrivateLocation" request
    And request contains "location_id" parameter from "REPLACE.ME"
    And body with value {"description": "Description of private location", "metadata": {"restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"]}, "name": "New private location", "tags": ["team:front"]}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Edit an API test returns "- JSON format is wrong" response
    Given new "UpdateAPITest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"config": {"assertions": [{"operator": "lessThan", "target": 1000, "type": "responseTime"}], "request": {"method": "GET", "url": "https://example.com"}}, "locations": ["aws:eu-west-3"], "message": "Notification message", "name": "Example test name", "options": {"blockedRequestPatterns": [], "ci": {"executionRule": "blocking"}, "device_ids": ["chrome.laptop_large"], "httpVersion": "http1", "monitor_options": {"notification_preset_name": "show_all"}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "rumSettings": {"applicationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "clientTokenId": 12345, "isEnabled": true}, "scheduling": {"timeframes": [{"day": 1, "from": "07:00", "to": "16:00"}, {"day": 3, "from": "07:00", "to": "16:00"}], "timezone": "America/New_York"}}, "status": "live", "subtype": "http", "tags": ["env:production"], "type": "api"}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Edit an API test returns "- Synthetic Monitoring is not activated for the user" response
    Given new "UpdateAPITest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"config": {"assertions": [{"operator": "lessThan", "target": 1000, "type": "responseTime"}], "request": {"method": "GET", "url": "https://example.com"}}, "locations": ["aws:eu-west-3"], "message": "Notification message", "name": "Example test name", "options": {"blockedRequestPatterns": [], "ci": {"executionRule": "blocking"}, "device_ids": ["chrome.laptop_large"], "httpVersion": "http1", "monitor_options": {"notification_preset_name": "show_all"}, "restricted_roles": ["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"], "retry": {}, "rumSettings": {"applicationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "clientTokenId": 12345, "isEnabled": true}, "scheduling": {"timeframes": [{"day": 1, "from": "07:00", "to": "16:00"}, {"day": 3, "from": "07:00", "to": "16:00"}], "timezone": "America/New_York"}}, "status": "live", "subtype": "http", "tags": ["env:production"], "type": "api"}
    When the request is sent
    Then the response status is 404 - Synthetic Monitoring is not activated for the user

  @team:DataDog/synthetics-managing
  Scenario: Edit an API test returns "OK" response
    Given there is a valid "synthetics_api_test" in the system
    And new "UpdateAPITest" request
    And request contains "public_id" parameter from "synthetics_api_test.public_id"
    And body from file "synthetics_api_test_update_payload.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ synthetics_api_test.name }}-updated"

  @team:DataDog/synthetics-managing
  Scenario: Fetch uptime for multiple tests returns "- JSON format is wrong" response
    Given new "FetchUptimes" request
    And body with value {"from_ts": 0, "public_ids": [], "to_ts": 0}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @replay-only @team:DataDog/synthetics-managing
  Scenario: Fetch uptime for multiple tests returns "OK." response
    Given new "FetchUptimes" request
    And body with value {"from_ts": 1726041488, "public_ids": ["p8m-9gw-nte"], "to_ts": 1726055954}
    When the request is sent
    Then the response status is 200 OK
    And the response "[0].public_id" is equal to "p8m-9gw-nte"
    And the response "[0].overall.uptime" is equal to 83.05682373046875
    And the response "[0].overall.history" has length 2

  @team:DataDog/synthetics-managing
  Scenario: Get a Mobile test returns "OK" response
    Given there is a valid "synthetics_mobile_test" in the system
    And new "GetMobileTest" request
    And request contains "public_id" parameter from "synthetics_mobile_test.public_id"
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ synthetics_mobile_test.name }}"
    And the response "options.device_ids[0]" is equal to "synthetics:mobile:device:iphone_15_ios_17"
    And the response "options.mobileApplication.applicationId" is equal to "ab0e0aed-536d-411a-9a99-5428c27d8f8e"
    And the response "options.mobileApplication.referenceId" is equal to "6115922a-5f5d-455e-bc7e-7955a57f3815"
    And the response "options.mobileApplication.referenceType" is equal to "version"
    And the response "type" is equal to "mobile"

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get a browser test result returns "- Synthetic Monitoring is not activated for the user" response
    Given new "GetBrowserTestResult" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And request contains "result_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 - Synthetic Monitoring is not activated for the user

  @replay-only @team:DataDog/synthetics-managing
  Scenario: Get a browser test result returns "OK" response
    Given new "GetBrowserTestResult" request
    And request contains "public_id" parameter with value "2yy-sem-mjh"
    And request contains "result_id" parameter with value "5671719892074090418"
    When the request is sent
    Then the response status is 200 OK
    And the response "result_id" is equal to "5671719892074090418"
    And the response "probe_dc" is equal to "aws:ca-central-1"

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get a browser test returns "- Synthetic Monitoring is not activated for the user" response
    Given new "GetBrowserTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 - Synthetic Monitoring is not activated for the user

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get a browser test returns "OK" response
    Given new "GetBrowserTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get a browser test's latest results summaries returns "- Synthetic Monitoring is not activated for the user" response
    Given new "GetBrowserTestLatestResults" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 - Synthetic Monitoring is not activated for the user

  @replay-only @team:DataDog/synthetics-managing
  Scenario: Get a browser test's latest results summaries returns "OK" response
    Given new "GetBrowserTestLatestResults" request
    And request contains "public_id" parameter with value "2yy-sem-mjh"
    When the request is sent
    Then the response status is 200 OK
    And the response "results" has length 3
    And the response "results[0].status" is equal to 0
    And the response "results[0].probe_dc" is equal to "aws:ca-central-1"

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get a global variable returns "Not found" response
    Given new "GetGlobalVariable" request
    And request contains "variable_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get a global variable returns "OK" response
    Given new "GetGlobalVariable" request
    And request contains "variable_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get a mobile test returns "- Synthetic Monitoring is not activated for the user" response
    Given new "GetMobileTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 - Synthetic Monitoring is not activated for the user

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get a mobile test returns "OK" response
    Given new "GetMobileTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get a private location returns "- Synthetic private locations are not activated for the user" response
    Given new "GetPrivateLocation" request
    And request contains "location_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 - Synthetic private locations are not activated for the user

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get a private location returns "OK" response
    Given new "GetPrivateLocation" request
    And request contains "location_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get a test configuration returns "- Synthetic is not activated for the user" response
    Given new "GetTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get a test configuration returns "OK" response
    Given new "GetTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get all global variables returns "OK" response
    Given new "ListGlobalVariables" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get all locations (public and private) returns "OK" response
    Given new "ListLocations" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get an API test result returns "- Synthetic Monitoring is not activated for the user" response
    Given new "GetAPITestResult" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And request contains "result_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 - Synthetic Monitoring is not activated for the user

  @replay-only @team:DataDog/synthetics-managing
  Scenario: Get an API test result returns "OK" response
    Given new "GetAPITestResult" request
    And request contains "public_id" parameter with value "hwb-332-3xe"
    And request contains "result_id" parameter with value "3420446318379485707"
    When the request is sent
    Then the response status is 200 OK
    And the response "result_id" is equal to "3420446318379485707"
    And the response "probe_dc" is equal to "aws:us-west-1"

  @replay-only @team:DataDog/synthetics-managing
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

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get an API test returns "- Synthetic Monitoring is not activated for the user" response
    Given new "GetAPITest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 - Synthetic Monitoring is not activated for the user

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get an API test returns "OK" response
    Given new "GetAPITest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get an API test's latest results summaries returns "- Synthetic is not activated for the user" response
    Given new "GetAPITestLatestResults" request
    And request contains "public_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 - Synthetic is not activated for the user

  @replay-only @team:DataDog/synthetics-managing
  Scenario: Get an API test's latest results summaries returns "OK" response
    Given new "GetAPITestLatestResults" request
    And request contains "public_id" parameter with value "hwb-332-3xe"
    When the request is sent
    Then the response status is 200 OK
    And the response "results" has length 150
    And the response "results[0].status" is equal to 0
    And the response "results[0].probe_dc" is equal to "aws:us-west-1"

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get details of batch returns "Batch does not exist." response
    Given new "GetSyntheticsCIBatch" request
    And request contains "batch_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Batch does not exist.

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get details of batch returns "OK" response
    Given new "GetSyntheticsCIBatch" request
    And request contains "batch_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get the default locations returns "OK" response
    Given new "GetSyntheticsDefaultLocations" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get the list of all Synthetic tests returns "OK - Returns the list of all Synthetic tests." response
    Given new "ListTests" request
    When the request is sent
    Then the response status is 200 OK - Returns the list of all Synthetic tests.

  @replay-only @skip-validation @team:DataDog/synthetics-managing @with-pagination
  Scenario: Get the list of all Synthetic tests returns "OK - Returns the list of all Synthetic tests." response with pagination
    Given new "ListTests" request
    And request contains "page_size" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK - Returns the list of all Synthetic tests.
    And the response has 3 items

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Get the list of all Synthetic tests returns "Synthetic Monitoring is not activated for the user." response
    Given new "ListTests" request
    When the request is sent
    Then the response status is 404 Synthetic Monitoring is not activated for the user.

  @team:DataDog/synthetics-managing
  Scenario: Get the list of default locations returns "OK" response
    Given new "GetSyntheticsDefaultLocations" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Patch a Synthetic test returns "- JSON format is wrong" response
    Given new "PatchTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"data": [{"op": "replace", "path": "/name", "value": "New test name"}, {"op": "remove", "path": "/config/assertions/0"}]}
    When the request is sent
    Then the response status is 400 - JSON format is wrong

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Patch a Synthetic test returns "- Synthetic Monitoring is not activated for the user" response
    Given new "PatchTest" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"data": [{"op": "replace", "path": "/name", "value": "New test name"}, {"op": "remove", "path": "/config/assertions/0"}]}
    When the request is sent
    Then the response status is 404 - Synthetic Monitoring is not activated for the user

  @team:DataDog/synthetics-managing
  Scenario: Patch a Synthetic test returns "OK" response
    Given there is a valid "synthetics_api_test" in the system
    And new "PatchTest" request
    And request contains "public_id" parameter from "synthetics_api_test.public_id"
    And body with value {"data": [{"op": "replace", "path": "/name", "value": "New test name"}, {"op": "remove", "path": "/config/assertions/0"}]}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Pause or start a test returns "- Synthetic Monitoring is not activated for the user" response
    Given new "UpdateTestPauseStatus" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"new_status": "live"}
    When the request is sent
    Then the response status is 404 - Synthetic Monitoring is not activated for the user

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Pause or start a test returns "JSON format is wrong." response
    Given new "UpdateTestPauseStatus" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"new_status": "live"}
    When the request is sent
    Then the response status is 400 JSON format is wrong.

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Pause or start a test returns "OK - Returns a boolean indicating if the update was successful." response
    Given new "UpdateTestPauseStatus" request
    And request contains "public_id" parameter from "REPLACE.ME"
    And body with value {"new_status": "live"}
    When the request is sent
    Then the response status is 200 OK - Returns a boolean indicating if the update was successful.

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Search Synthetic tests returns "Not found" response
    Given new "SearchTests" request
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Search Synthetic tests returns "OK - Returns the list of Synthetic tests matching the search." response
    Given new "SearchTests" request
    When the request is sent
    Then the response status is 200 OK - Returns the list of Synthetic tests matching the search.

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Trigger Synthetic tests returns "Bad Request" response
    Given new "TriggerTests" request
    And body with value {"tests": [{"metadata": {"ci": {"pipeline": {}, "provider": {}}, "git": {}}, "public_id": "aaa-aaa-aaa"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/synthetics-managing
  Scenario: Trigger Synthetic tests returns "OK" response
    Given there is a valid "synthetics_api_test" in the system
    And new "TriggerTests" request
    And body with value {"tests": [{"public_id": "{{ synthetics_api_test.public_id }}"}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "triggered_check_ids" array contains value "{{ synthetics_api_test.public_id }}"
    And the response "results" has item with field "public_id" with value "{{ synthetics_api_test.public_id }}"

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Trigger tests from CI/CD pipelines returns "JSON format is wrong" response
    Given new "TriggerCITests" request
    And body with value {"tests": [{"basicAuth": {"password": "PaSSw0RD!", "type": "web", "username": "my_username"}, "deviceIds": ["chrome.laptop_large"], "locations": ["aws:eu-west-3"], "metadata": {"ci": {"pipeline": {}, "provider": {}}, "git": {}}, "public_id": "aaa-aaa-aaa", "retry": {}}]}
    When the request is sent
    Then the response status is 400 JSON format is wrong

  @generated @skip @team:DataDog/synthetics-managing
  Scenario: Trigger tests from CI/CD pipelines returns "OK" response
    Given new "TriggerCITests" request
    And body with value {"tests": [{"basicAuth": {"password": "PaSSw0RD!", "type": "web", "username": "my_username"}, "deviceIds": ["chrome.laptop_large"], "locations": ["aws:eu-west-3"], "metadata": {"ci": {"pipeline": {}, "provider": {}}, "git": {}}, "public_id": "aaa-aaa-aaa", "retry": {}}]}
    When the request is sent
    Then the response status is 200 OK
