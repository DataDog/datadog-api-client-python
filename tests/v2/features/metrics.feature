@endpoint(metrics)
Feature: Metrics
  The metrics endpoint allows you to:  - Post metrics data so it can be
  graphed on Datadog’s dashboards - Query metrics from any time period -
  Modify tag configurations for metrics  **Note**: A graph can only contain
  a set number of points and as the timeframe over which a metric is viewed
  increases, aggregation between points occurs to stay below that set
  number.  The Post, Patch, and Delete `manage_tags` API methods can only be
  performed by a user who has the `Manage Tags for Metrics` permission.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Metrics" API

  @generated @skip
  Scenario: Create a Tag Configuration returns "Bad Request" response
    Given operation "CreateTagConfiguration" enabled
    And new "CreateTagConfiguration" request
    And request contains "metric_name" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Create a Tag Configuration returns "Conflict" response
    Given operation "CreateTagConfiguration" enabled
    And new "CreateTagConfiguration" request
    And request contains "metric_name" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 409 Conflict

  Scenario: Create a Tag Configuration returns "Created" response
    Given operation "CreateTagConfiguration" enabled
    And new "CreateTagConfiguration" request
    And request contains "metric_name" parameter with value "{{ unique_alnum }}"
    And body {"data": {"type": "manage_tags", "id": "{{ unique_alnum }}", "attributes": {"tags": ["app","datacenter"], "metric_type": "distribution"}}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip
  Scenario: Create a Tag Configuration returns "Too Many Requests" response
    Given operation "CreateTagConfiguration" enabled
    And new "CreateTagConfiguration" request
    And request contains "metric_name" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 429 Too Many Requests

  Scenario: Delete a Tag Configuration returns "No Content" response
    Given there is a valid "metric_tag_configuration" in the system
    And operation "DeleteTagConfiguration" enabled
    And new "DeleteTagConfiguration" request
    And request contains "metric_name" parameter from "metric_tag_configuration.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip
  Scenario: Delete a Tag Configuration returns "Not found" response
    Given operation "DeleteTagConfiguration" enabled
    And new "DeleteTagConfiguration" request
    And request contains "metric_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip
  Scenario: Delete a Tag Configuration returns "Too Many Requests" response
    Given operation "DeleteTagConfiguration" enabled
    And new "DeleteTagConfiguration" request
    And request contains "metric_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 429 Too Many Requests

  @generated @skip
  Scenario: List Tag Configuration by Name returns "Not Found" response
    Given operation "ListTagConfigurationByName" enabled
    And new "ListTagConfigurationByName" request
    And request contains "metric_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not Found

  Scenario: List Tag Configuration by Name returns "Success" response
    Given there is a valid "metric_tag_configuration" in the system
    And operation "ListTagConfigurationByName" enabled
    And new "ListTagConfigurationByName" request
    And request contains "metric_name" parameter from "metric_tag_configuration.data.id"
    When the request is sent
    Then the response status is 200 Success
    And the response "data.id" has the same value as "metric_tag_configuration.data.id"

  @generated @skip
  Scenario: List Tag Configuration by Name returns "Too Many Requests" response
    Given operation "ListTagConfigurationByName" enabled
    And new "ListTagConfigurationByName" request
    And request contains "metric_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 429 Too Many Requests

  @generated @skip
  Scenario: List Tag Configurations returns "Bad Request" response
    Given operation "ListTagConfigurations" enabled
    And new "ListTagConfigurations" request
    When the request is sent
    Then the response status is 400 Bad Request

  Scenario: List Tag Configurations returns "Success" response
    Given there is a valid "metric_tag_configuration" in the system
    And operation "ListTagConfigurations" enabled
    And new "ListTagConfigurations" request
    And request contains "filter[tags_configured]" parameter with value "{{ unique_alnum }}"
    When the request is sent
    Then the response status is 200 Success
    And the response "data[0].id" has the same value as "metric_tag_configuration.data.id"

  @generated @skip
  Scenario: List Tag Configurations returns "Too Many Requests" response
    Given operation "ListTagConfigurations" enabled
    And new "ListTagConfigurations" request
    When the request is sent
    Then the response status is 429 Too Many Requests

  @generated @skip
  Scenario: Update a Tag Configuration returns "Bad Request" response
    Given operation "UpdateTagConfiguration" enabled
    And new "UpdateTagConfiguration" request
    And request contains "metric_name" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  Scenario: Update a Tag Configuration returns "OK" response
    Given operation "UpdateTagConfiguration" enabled
    And there is a valid "metric_tag_configuration" in the system
    And new "UpdateTagConfiguration" request
    And request contains "metric_name" parameter from "metric_tag_configuration.data.id"
    And body {"data": {"type": "manage_tags", "id": "{{ metric_tag_configuration.data.id }}", "attributes": {"tags": ["app"]}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.tags[0]" is equal to "app"

  @generated @skip
  Scenario: Update a Tag Configuration returns "Too Many Requests" response
    Given operation "UpdateTagConfiguration" enabled
    And new "UpdateTagConfiguration" request
    And request contains "metric_name" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 429 Too Many Requests

  @generated @skip
  Scenario: Update a Tag Configuration returns "Unprocessable Entity" response
    Given operation "UpdateTagConfiguration" enabled
    And new "UpdateTagConfiguration" request
    And request contains "metric_name" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 422 Unprocessable Entity
