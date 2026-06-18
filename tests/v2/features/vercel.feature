@endpoint(vercel) @endpoint(vercel-v2)
Feature: Vercel
  Configure the Datadog Vercel integration. Endpoints in this section let
  you exchange a Vercel marketplace authorization code for a Datadog-managed
  access token and read or update the logs, traces, and API key
  configuration associated with a Vercel project.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Vercel" API

  @generated @skip @team:DataDog/serverless-onboarding-and-enablement
  Scenario: Create Vercel access token returns "Bad Request" response
    Given new "CreateVercelToken" request
    And body with value {"authGrantCode": "code", "vercelConfigurationId": "icfg_abc123"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/serverless-onboarding-and-enablement
  Scenario: Create Vercel access token returns "OK" response
    Given new "CreateVercelToken" request
    And body with value {"authGrantCode": "code", "vercelConfigurationId": "icfg_abc123"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/serverless-onboarding-and-enablement
  Scenario: Get Vercel configuration returns "Bad Request" response
    Given new "GetVercelConfig" request
    And request contains "configuration_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/serverless-onboarding-and-enablement
  Scenario: Get Vercel configuration returns "Not Found" response
    Given new "GetVercelConfig" request
    And request contains "configuration_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/serverless-onboarding-and-enablement
  Scenario: Get Vercel configuration returns "OK" response
    Given new "GetVercelConfig" request
    And request contains "configuration_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/serverless-onboarding-and-enablement
  Scenario: Update Vercel configuration returns "Bad Request" response
    Given new "UpdateVercelConfig" request
    And request contains "configuration_id" parameter from "REPLACE.ME"
    And body with value {"apiKey": {"id": "00000000-0000-0000-0000-000000000001", "value": ""}, "logsConfig": {"enabled": true, "environments": ["production"], "logSources": ["lambda"], "samplingPercentage": 100}, "traceConfig": {"enabled": true, "isDeprecatedOtel": false, "samplingPercentage": 100}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/serverless-onboarding-and-enablement
  Scenario: Update Vercel configuration returns "Not Found" response
    Given new "UpdateVercelConfig" request
    And request contains "configuration_id" parameter from "REPLACE.ME"
    And body with value {"apiKey": {"id": "00000000-0000-0000-0000-000000000001", "value": ""}, "logsConfig": {"enabled": true, "environments": ["production"], "logSources": ["lambda"], "samplingPercentage": 100}, "traceConfig": {"enabled": true, "isDeprecatedOtel": false, "samplingPercentage": 100}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/serverless-onboarding-and-enablement
  Scenario: Update Vercel configuration returns "OK" response
    Given new "UpdateVercelConfig" request
    And request contains "configuration_id" parameter from "REPLACE.ME"
    And body with value {"apiKey": {"id": "00000000-0000-0000-0000-000000000001", "value": ""}, "logsConfig": {"enabled": true, "environments": ["production"], "logSources": ["lambda"], "samplingPercentage": 100}, "traceConfig": {"enabled": true, "isDeprecatedOtel": false, "samplingPercentage": 100}}
    When the request is sent
    Then the response status is 200 OK
