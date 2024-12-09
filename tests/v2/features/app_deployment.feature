@endpoint(app-deployment) @endpoint(app-deployment-v2)
Feature: App Deployment
  Deploy and disable apps in App Builder.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "AppDeployment" API

  @team:DataDog/app-builder-backend
  Scenario: Deploy App returns "Bad Request" response
    Given operation "DeployApp" enabled
    And new "DeployApp" request
    And request contains "app_id" parameter with value "invalid-uuid"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/app-builder-backend
  Scenario: Deploy App returns "Created" response
    Given operation "DeployApp" enabled
    And new "DeployApp" request
    And there is a valid "app" in the system
    And request contains "app_id" parameter from "app.data.id"
    When the request is sent
    Then the response status is 201 Created

  @team:DataDog/app-builder-backend
  Scenario: Deploy App returns "Not Found" response
    Given operation "DeployApp" enabled
    And new "DeployApp" request
    And request contains "app_id" parameter with value "7addb29b-f935-472c-ae79-d1963979a23e"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/app-builder-backend
  Scenario: Disable App returns "Bad Request" response
    Given operation "DisableApp" enabled
    And new "DisableApp" request
    And request contains "app_id" parameter with value "invalid-uuid"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/app-builder-backend
  Scenario: Disable App returns "Not Found" response
    Given operation "DisableApp" enabled
    And new "DisableApp" request
    And request contains "app_id" parameter with value "7addb29b-f935-472c-ae79-d1963979a23e"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/app-builder-backend
  Scenario: Disable App returns "OK" response
    Given operation "DisableApp" enabled
    And new "DisableApp" request
    And there is a valid "app" in the system
    And request contains "app_id" parameter from "app.data.id"
    When the request is sent
    Then the response status is 200 OK
