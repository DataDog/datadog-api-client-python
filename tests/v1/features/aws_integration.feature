@endpoint(aws-integration)
Feature: AWS Integration
  Configure your Datadog-AWS integration directly through the Datadog API.
  For more information, see the [AWS integration
  page](https://docs.datadoghq.com/integrations/amazon_web_services).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "AWSIntegration" API

  @generated @skip
  Scenario: Create an AWS integration returns "Bad Request" response
    Given new "CreateAWSAccount" request
    And body {"access_key_id": null, "account_id": "1234567", "account_specific_namespace_rules": {"auto_scaling": false, "opswork": false}, "excluded_regions": ["us-east-1", "us-west-2"], "filter_tags": ["<KEY>:<VALUE>"], "host_tags": ["<KEY>:<VALUE>"], "role_name": "DatadogAWSIntegrationRole", "secret_access_key": null}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Create an AWS integration returns "Conflict Error" response
    Given new "CreateAWSAccount" request
    And body {"access_key_id": null, "account_id": "1234567", "account_specific_namespace_rules": {"auto_scaling": false, "opswork": false}, "excluded_regions": ["us-east-1", "us-west-2"], "filter_tags": ["<KEY>:<VALUE>"], "host_tags": ["<KEY>:<VALUE>"], "role_name": "DatadogAWSIntegrationRole", "secret_access_key": null}
    When the request is sent
    Then the response status is 409 Conflict Error

  @generated @skip
  Scenario: Create an AWS integration returns "OK" response
    Given new "CreateAWSAccount" request
    And body {"access_key_id": null, "account_id": "1234567", "account_specific_namespace_rules": {"auto_scaling": false, "opswork": false}, "excluded_regions": ["us-east-1", "us-west-2"], "filter_tags": ["<KEY>:<VALUE>"], "host_tags": ["<KEY>:<VALUE>"], "role_name": "DatadogAWSIntegrationRole", "secret_access_key": null}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Delete a tag filtering entry returns "Bad Request" response
    Given new "DeleteAWSTagFilter" request
    And body {"account_id": "FAKEAC0FAKEAC2FAKEAC", "namespace": "elb"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Delete a tag filtering entry returns "OK" response
    Given new "DeleteAWSTagFilter" request
    And body {"account_id": "FAKEAC0FAKEAC2FAKEAC", "namespace": "elb"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Delete an AWS integration returns "Bad Request" response
    Given new "DeleteAWSAccount" request
    And body {"access_key_id": null, "account_id": "1234567", "account_specific_namespace_rules": {"auto_scaling": false, "opswork": false}, "excluded_regions": ["us-east-1", "us-west-2"], "filter_tags": ["<KEY>:<VALUE>"], "host_tags": ["<KEY>:<VALUE>"], "role_name": "DatadogAWSIntegrationRole", "secret_access_key": null}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Delete an AWS integration returns "Conflict Error" response
    Given new "DeleteAWSAccount" request
    And body {"access_key_id": null, "account_id": "1234567", "account_specific_namespace_rules": {"auto_scaling": false, "opswork": false}, "excluded_regions": ["us-east-1", "us-west-2"], "filter_tags": ["<KEY>:<VALUE>"], "host_tags": ["<KEY>:<VALUE>"], "role_name": "DatadogAWSIntegrationRole", "secret_access_key": null}
    When the request is sent
    Then the response status is 409 Conflict Error

  @generated @skip
  Scenario: Delete an AWS integration returns "OK" response
    Given new "DeleteAWSAccount" request
    And body {"access_key_id": null, "account_id": "1234567", "account_specific_namespace_rules": {"auto_scaling": false, "opswork": false}, "excluded_regions": ["us-east-1", "us-west-2"], "filter_tags": ["<KEY>:<VALUE>"], "host_tags": ["<KEY>:<VALUE>"], "role_name": "DatadogAWSIntegrationRole", "secret_access_key": null}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Generate a new external ID returns "Bad Request" response
    Given new "CreateNewAWSExternalID" request
    And body {"access_key_id": null, "account_id": "1234567", "account_specific_namespace_rules": {"auto_scaling": false, "opswork": false}, "excluded_regions": ["us-east-1", "us-west-2"], "filter_tags": ["<KEY>:<VALUE>"], "host_tags": ["<KEY>:<VALUE>"], "role_name": "DatadogAWSIntegrationRole", "secret_access_key": null}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Generate a new external ID returns "OK" response
    Given new "CreateNewAWSExternalID" request
    And body {"access_key_id": null, "account_id": "1234567", "account_specific_namespace_rules": {"auto_scaling": false, "opswork": false}, "excluded_regions": ["us-east-1", "us-west-2"], "filter_tags": ["<KEY>:<VALUE>"], "host_tags": ["<KEY>:<VALUE>"], "role_name": "DatadogAWSIntegrationRole", "secret_access_key": null}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get all AWS tag filters returns "Bad Request" response
    Given new "ListAWSTagFilters" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get all AWS tag filters returns "OK" response
    Given new "ListAWSTagFilters" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: List all AWS integrations returns "Bad Request" response
    Given new "ListAWSAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: List all AWS integrations returns "OK" response
    Given new "ListAWSAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: List namespace rules returns "OK" response
    Given new "ListAvailableAWSNamespaces" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Set an AWS tag filter returns "Bad Request" response
    Given new "CreateAWSTagFilter" request
    And body {"account_id": "1234567", "namespace": "elb", "tag_filter_str": "prod*"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Set an AWS tag filter returns "OK" response
    Given new "CreateAWSTagFilter" request
    And body {"account_id": "1234567", "namespace": "elb", "tag_filter_str": "prod*"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update an AWS integration returns "Bad Request" response
    Given new "UpdateAWSAccount" request
    And body {"access_key_id": null, "account_id": "1234567", "account_specific_namespace_rules": {"auto_scaling": false, "opswork": false}, "excluded_regions": ["us-east-1", "us-west-2"], "filter_tags": ["<KEY>:<VALUE>"], "host_tags": ["<KEY>:<VALUE>"], "role_name": "DatadogAWSIntegrationRole", "secret_access_key": null}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Update an AWS integration returns "Conflict Error" response
    Given new "UpdateAWSAccount" request
    And body {"access_key_id": null, "account_id": "1234567", "account_specific_namespace_rules": {"auto_scaling": false, "opswork": false}, "excluded_regions": ["us-east-1", "us-west-2"], "filter_tags": ["<KEY>:<VALUE>"], "host_tags": ["<KEY>:<VALUE>"], "role_name": "DatadogAWSIntegrationRole", "secret_access_key": null}
    When the request is sent
    Then the response status is 409 Conflict Error

  @generated @skip
  Scenario: Update an AWS integration returns "OK" response
    Given new "UpdateAWSAccount" request
    And body {"access_key_id": null, "account_id": "1234567", "account_specific_namespace_rules": {"auto_scaling": false, "opswork": false}, "excluded_regions": ["us-east-1", "us-west-2"], "filter_tags": ["<KEY>:<VALUE>"], "host_tags": ["<KEY>:<VALUE>"], "role_name": "DatadogAWSIntegrationRole", "secret_access_key": null}
    When the request is sent
    Then the response status is 200 OK
