@endpoint(dora-metrics) @endpoint(dora-metrics-v2)
Feature: DORA Metrics
  Search, send, or delete events for DORA Metrics to measure and improve
  your software delivery performance. See the [DORA Metrics
  page](https://docs.datadoghq.com/dora_metrics/) for more information.
  **Note**: DORA Metrics are not available in the US1-FED site.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And an instance of "DORAMetrics" API

  @skip @team:DataDog/ci-app-backend
  Scenario: Delete a deployment event returns "Accepted" response
    Given new "DeleteDORADeployment" request
    And a valid "appKeyAuth" key in the system
    And request contains "deployment_id" parameter with value "NO_VALUE"
    When the request is sent
    Then the response status is 202 Accepted

  @skip @team:DataDog/ci-app-backend
  Scenario: Delete a deployment event returns "Bad Request" response
    Given new "DeleteDORADeployment" request
    And request contains "deployment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/ci-app-backend
  Scenario: Delete a failure event returns "Accepted" response
    Given new "DeleteDORAFailure" request
    And a valid "appKeyAuth" key in the system
    And request contains "failure_id" parameter with value "NO_VALUE"
    When the request is sent
    Then the response status is 202 Accepted

  @skip @team:DataDog/ci-app-backend
  Scenario: Delete a failure event returns "Bad Request" response
    Given new "DeleteDORAFailure" request
    And a valid "appKeyAuth" key in the system
    And request contains "failure_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Delete an incident event returns "Accepted" response
    Given a valid "appKeyAuth" key in the system
    And new "DeleteDORAFailure" request
    And request contains "failure_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 202 Accepted

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Delete an incident event returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "DeleteDORAFailure" request
    And request contains "failure_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Get a deployment event returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "GetDORADeployment" request
    And request contains "deployment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Get a deployment event returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "GetDORADeployment" request
    And request contains "deployment_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/ci-app-backend
  Scenario: Get a list of deployment events returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "ListDORADeployments" request
    And body with value {"data": {"attributes": {"limit": 10}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/ci-app-backend
  Scenario: Get a list of deployment events returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "ListDORADeployments" request
    And body with value {"data": {"attributes": {"from": "2025-03-23T00:00:00Z", "limit": 1, "to": "2025-03-24T00:00:00Z"}, "type": "dora_deployments_list_request"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/ci-app-backend
  Scenario: Get a list of failure events returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "ListDORAFailures" request
    And body with value {"data": {"attributes": {"limit": 10}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/ci-app-backend
  Scenario: Get a list of failure events returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "ListDORAFailures" request
    And body with value {"data": {"attributes": {"from": "2025-03-23T00:00:00Z", "limit": 1, "to": "2025-03-24T00:00:00Z"}, "type": "dora_failures_list_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Get a list of incident events returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "ListDORAFailures" request
    And body with value {"data": {"attributes": {"from": "2025-01-01T00:00:00Z", "limit": 100, "query": "severity:(SEV-1 OR SEV-2) env:production team:backend", "sort": "-started_at", "to": "2025-01-31T23:59:59Z"}, "type": "dora_failures_list_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Get a list of incident events returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "ListDORAFailures" request
    And body with value {"data": {"attributes": {"from": "2025-01-01T00:00:00Z", "limit": 100, "query": "severity:(SEV-1 OR SEV-2) env:production team:backend", "sort": "-started_at", "to": "2025-01-31T23:59:59Z"}, "type": "dora_failures_list_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Get an incident event returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "GetDORAFailure" request
    And request contains "failure_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Get an incident event returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "GetDORAFailure" request
    And request contains "failure_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Patch a deployment event returns "Accepted" response
    Given a valid "appKeyAuth" key in the system
    And new "PatchDORADeployment" request
    And request contains "deployment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"change_failure": true, "remediation": {"id": "eG42zNIkVjM", "type": "rollback"}}, "id": "z_RwVLi7v4Y", "type": "dora_deployment_patch_request"}}
    When the request is sent
    Then the response status is 202 Accepted

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Patch a deployment event returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "PatchDORADeployment" request
    And request contains "deployment_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"change_failure": true, "remediation": {"id": "eG42zNIkVjM", "type": "rollback"}}, "id": "z_RwVLi7v4Y", "type": "dora_deployment_patch_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/ci-app-backend
  Scenario: Send a deployment event returns "Bad Request" response
    Given new "CreateDORADeployment" request
    And body with value {"data": {"attributes": {}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Send a deployment event returns "OK - but delayed due to incident" response
    Given new "CreateDORADeployment" request
    And body with value {"data": {"attributes": {"custom_tags": ["language:java", "department:engineering"], "env": "staging", "finished_at": 1693491984000000000, "git": {"commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588", "repository_url": "https://github.com/organization/example-repository"}, "service": "shopist", "started_at": 1693491974000000000, "team": "backend", "version": "v1.12.07"}}}
    When the request is sent
    Then the response status is 202 OK - but delayed due to incident

  @replay-only @team:DataDog/ci-app-backend
  Scenario: Send a deployment event returns "OK" response
    Given new "CreateDORADeployment" request
    And body with value {"data": {"attributes": {"finished_at": 1693491984000000000, "git": {"commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588", "repository_url": "https://github.com/organization/example-repository"}, "service": "shopist", "started_at": 1693491974000000000, "version": "v1.12.07"}}}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/ci-app-backend
  Scenario: Send a failure event returns "Bad Request" response
    Given new "CreateDORAIncident" request
    And body with value {"data": {"attributes": {}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/ci-app-backend
  Scenario: Send a failure event returns "OK" response
    Given new "CreateDORAIncident" request
    And body with value {"data": {"attributes": {"finished_at": 1707842944600000000, "git": {"commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588", "repository_url": "https://github.com/organization/example-repository"}, "name": "Webserver is down failing all requests", "services": ["shopist"], "severity": "High", "started_at": 1707842944500000000, "team": "backend", "version": "v1.12.07"}}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Send an incident event (legacy) returns "Bad Request" response
    Given new "CreateDORAIncident" request
    And body with value {"data": {"attributes": {"custom_tags": ["language:java", "department:engineering"], "env": "staging", "finished_at": 1693491984000000000, "git": {"commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588", "repository_url": "https://github.com/organization/example-repository"}, "name": "Webserver is down failing all requests.", "services": ["shopist"], "severity": "High", "started_at": 1693491974000000000, "team": "backend", "version": "v1.12.07"}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Send an incident event (legacy) returns "OK - but delayed due to incident" response
    Given new "CreateDORAIncident" request
    And body with value {"data": {"attributes": {"custom_tags": ["language:java", "department:engineering"], "env": "staging", "finished_at": 1693491984000000000, "git": {"commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588", "repository_url": "https://github.com/organization/example-repository"}, "name": "Webserver is down failing all requests.", "services": ["shopist"], "severity": "High", "started_at": 1693491974000000000, "team": "backend", "version": "v1.12.07"}}}
    When the request is sent
    Then the response status is 202 OK - but delayed due to incident

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Send an incident event (legacy) returns "OK" response
    Given new "CreateDORAIncident" request
    And body with value {"data": {"attributes": {"custom_tags": ["language:java", "department:engineering"], "env": "staging", "finished_at": 1693491984000000000, "git": {"commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588", "repository_url": "https://github.com/organization/example-repository"}, "name": "Webserver is down failing all requests.", "services": ["shopist"], "severity": "High", "started_at": 1693491974000000000, "team": "backend", "version": "v1.12.07"}}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Send an incident event returns "Bad Request" response
    Given new "CreateDORAFailure" request
    And body with value {"data": {"attributes": {"custom_tags": ["language:java", "department:engineering"], "env": "staging", "finished_at": 1693491984000000000, "git": {"commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588", "repository_url": "https://github.com/organization/example-repository"}, "name": "Webserver is down failing all requests.", "services": ["shopist"], "severity": "High", "started_at": 1693491974000000000, "team": "backend", "version": "v1.12.07"}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Send an incident event returns "OK - but delayed due to incident" response
    Given new "CreateDORAFailure" request
    And body with value {"data": {"attributes": {"custom_tags": ["language:java", "department:engineering"], "env": "staging", "finished_at": 1693491984000000000, "git": {"commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588", "repository_url": "https://github.com/organization/example-repository"}, "name": "Webserver is down failing all requests.", "services": ["shopist"], "severity": "High", "started_at": 1693491974000000000, "team": "backend", "version": "v1.12.07"}}}
    When the request is sent
    Then the response status is 202 OK - but delayed due to incident

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Send an incident event returns "OK" response
    Given new "CreateDORAFailure" request
    And body with value {"data": {"attributes": {"custom_tags": ["language:java", "department:engineering"], "env": "staging", "finished_at": 1693491984000000000, "git": {"commit_sha": "66adc9350f2cc9b250b69abddab733dd55e1a588", "repository_url": "https://github.com/organization/example-repository"}, "name": "Webserver is down failing all requests.", "services": ["shopist"], "severity": "High", "started_at": 1693491974000000000, "team": "backend", "version": "v1.12.07"}}}
    When the request is sent
    Then the response status is 200 OK
