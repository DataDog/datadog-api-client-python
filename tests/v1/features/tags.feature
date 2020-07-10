@endpoint(tags)
Feature: Tags
  The tag endpoint allows you to assign tags to hosts, for example:
  `role:database`. Those tags are applied to all metrics sent by the host.
  Refer to hosts by name (`yourhost.example.com`) when fetching and applying
  tags to a particular host.  The component of your infrastructure
  responsible for a tag is identified by a source. For example, some valid
  sources include nagios, hudson, jenkins, users, feed, chef, puppet, git,
  bitbucket, fabric, capistrano, etc.  Read more about tags on the dedicated
  [documentation page](https://docs.datadoghq.com/tagging).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Tags" API

  @generated @skip
  Scenario: Get Tags returns "OK" response
    Given new "ListHostTags" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Remove host tags returns "OK" response
    Given new "DeleteHostTags" request
    And request contains "host_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip
  Scenario: Get host tags returns "OK" response
    Given new "GetHostTags" request
    And request contains "host_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Add tags to a host returns "Created" response
    Given new "CreateHostTags" request
    And request contains "host_name" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip
  Scenario: Update host tags returns "OK" response
    Given new "UpdateHostTags" request
    And request contains "host_name" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 201 OK
