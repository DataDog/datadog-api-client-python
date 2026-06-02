@endpoint(statuspage-integration) @endpoint(statuspage-integration-v2)
Feature: Statuspage Integration
  Configure your [Datadog Statuspage
  integration](https://docs.datadoghq.com/integrations/statuspage/) directly
  through the Datadog API.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "StatuspageIntegration" API

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Create a Statuspage URL setting returns "Bad Request" response
    Given new "CreateStatuspageUrlSetting" request
    And body with value {"data": {"attributes": {"custom_tags": "team:collaboration-integrations,env:prod", "url": "https://example.statuspage.io"}, "type": "statuspage-url-setting"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Create a Statuspage URL setting returns "CREATED" response
    Given new "CreateStatuspageUrlSetting" request
    And body with value {"data": {"attributes": {"custom_tags": "team:collaboration-integrations,env:prod", "url": "https://example.statuspage.io"}, "type": "statuspage-url-setting"}}
    When the request is sent
    Then the response status is 201 CREATED

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Create a Statuspage URL setting returns "Conflict" response
    Given new "CreateStatuspageUrlSetting" request
    And body with value {"data": {"attributes": {"custom_tags": "team:collaboration-integrations,env:prod", "url": "https://example.statuspage.io"}, "type": "statuspage-url-setting"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Create the Statuspage account returns "Bad Request" response
    Given new "CreateStatuspageAccount" request
    And body with value {"data": {"attributes": {"api_key": "00000000-0000-0000-0000-000000000000"}, "type": "statuspage-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Create the Statuspage account returns "CREATED" response
    Given new "CreateStatuspageAccount" request
    And body with value {"data": {"attributes": {"api_key": "00000000-0000-0000-0000-000000000000"}, "type": "statuspage-account"}}
    When the request is sent
    Then the response status is 201 CREATED

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Create the Statuspage account returns "Conflict" response
    Given new "CreateStatuspageAccount" request
    And body with value {"data": {"attributes": {"api_key": "00000000-0000-0000-0000-000000000000"}, "type": "statuspage-account"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete a Statuspage URL setting returns "Bad Request" response
    Given new "DeleteStatuspageUrlSetting" request
    And request contains "statuspage_url_setting_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete a Statuspage URL setting returns "Not Found" response
    Given new "DeleteStatuspageUrlSetting" request
    And request contains "statuspage_url_setting_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete a Statuspage URL setting returns "OK" response
    Given new "DeleteStatuspageUrlSetting" request
    And request contains "statuspage_url_setting_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete the Statuspage account returns "Bad Request" response
    Given new "DeleteStatuspageAccount" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete the Statuspage account returns "Not Found" response
    Given new "DeleteStatuspageAccount" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete the Statuspage account returns "OK" response
    Given new "DeleteStatuspageAccount" request
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get all Statuspage URL settings returns "Not Found" response
    Given new "ListStatuspageUrlSettings" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get all Statuspage URL settings returns "OK" response
    Given new "ListStatuspageUrlSettings" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get the Statuspage account returns "Not Found" response
    Given new "GetStatuspageAccount" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get the Statuspage account returns "OK" response
    Given new "GetStatuspageAccount" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update a Statuspage URL setting returns "Bad Request" response
    Given new "UpdateStatuspageUrlSetting" request
    And request contains "statuspage_url_setting_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"custom_tags": "team:collaboration-integrations,env:prod", "url": "https://example.statuspage.io"}, "id": "596da4af-0563-4097-90ff-07230c3f9db3", "type": "statuspage-url-setting"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update a Statuspage URL setting returns "Conflict" response
    Given new "UpdateStatuspageUrlSetting" request
    And request contains "statuspage_url_setting_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"custom_tags": "team:collaboration-integrations,env:prod", "url": "https://example.statuspage.io"}, "id": "596da4af-0563-4097-90ff-07230c3f9db3", "type": "statuspage-url-setting"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update a Statuspage URL setting returns "Not Found" response
    Given new "UpdateStatuspageUrlSetting" request
    And request contains "statuspage_url_setting_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"custom_tags": "team:collaboration-integrations,env:prod", "url": "https://example.statuspage.io"}, "id": "596da4af-0563-4097-90ff-07230c3f9db3", "type": "statuspage-url-setting"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update a Statuspage URL setting returns "OK" response
    Given new "UpdateStatuspageUrlSetting" request
    And request contains "statuspage_url_setting_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"custom_tags": "team:collaboration-integrations,env:prod", "url": "https://example.statuspage.io"}, "id": "596da4af-0563-4097-90ff-07230c3f9db3", "type": "statuspage-url-setting"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update the Statuspage account returns "Bad Request" response
    Given new "UpdateStatuspageAccount" request
    And body with value {"data": {"attributes": {"api_key": "00000000-0000-0000-0000-000000000000"}, "type": "statuspage-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update the Statuspage account returns "Not Found" response
    Given new "UpdateStatuspageAccount" request
    And body with value {"data": {"attributes": {"api_key": "00000000-0000-0000-0000-000000000000"}, "type": "statuspage-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update the Statuspage account returns "OK" response
    Given new "UpdateStatuspageAccount" request
    And body with value {"data": {"attributes": {"api_key": "00000000-0000-0000-0000-000000000000"}, "type": "statuspage-account"}}
    When the request is sent
    Then the response status is 200 OK
