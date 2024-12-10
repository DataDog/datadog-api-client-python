@endpoint(apps) @endpoint(apps-v2)
Feature: Apps
  Create, read, update, and delete apps in App Builder.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Apps" API

  @team:DataDog/app-builder-backend
  Scenario: Create App returns "App Created" response
    Given operation "CreateApp" enabled
    And new "CreateApp" request
    And body with value {"data": {"attributes": {"components": [{"events": [], "name": "grid0", "properties": {"children": [{"events": [], "name": "gridCell0", "properties": {"children": [{"events": [], "name": "calloutValue0", "properties": {"isDisabled": false, "isLoading": false, "isVisible": true, "label": "CPU Usage", "size": "sm", "style": "vivid_yellow", "unit": "kB", "value": "42"}, "type": "calloutValue"}], "isVisible": "true", "layout": {"default": {"height": 8, "width": 2, "x": 0, "y": 0}}}, "type": "gridCell"}]}, "type": "grid"}], "description": "This is a simple example app", "embeddedQueries": [], "name": "Example App", "rootInstanceName": "grid0"}, "type": "appDefinitions"}}
    When the request is sent
    Then the response status is 201 App Created
    And the response "data.type" is equal to "appDefinitions"

  @team:DataDog/app-builder-backend
  Scenario: Create App returns "Bad Request" response
    Given operation "CreateApp" enabled
    And new "CreateApp" request
    And body with value {"data": {"attributes": {"description": "This is a bad example app", "embeddedQueries": [], "rootInstanceName": "grid0"}, "type": "appDefinitions"}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].detail" is equal to "missing required field"

  @team:DataDog/app-builder-backend
  Scenario: Delete App returns "Bad Request" response
    Given operation "DeleteApp" enabled
    And new "DeleteApp" request
    And request contains "app_id" parameter with value "bad-app-id"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: Delete App returns "Gone" response
    Given operation "DeleteApp" enabled
    And new "DeleteApp" request
    And request contains "app_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 410 Gone

  @team:DataDog/app-builder-backend
  Scenario: Delete App returns "Not Found" response
    Given operation "DeleteApp" enabled
    And new "DeleteApp" request
    And request contains "app_id" parameter with value "7addb29b-f935-472c-ae79-d1963979a23e"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/app-builder-backend
  Scenario: Delete App returns "OK" response
    Given operation "DeleteApp" enabled
    And there is a valid "app" in the system
    And new "DeleteApp" request
    And request contains "app_id" parameter from "app.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" has the same value as "app.data.id"
    And the response "data.type" is equal to "appDefinitions"

  @team:DataDog/app-builder-backend
  Scenario: Delete Multiple Apps returns "Bad Request" response
    Given operation "DeleteApps" enabled
    And new "DeleteApps" request
    And body with value {"data": [{"id": "71c0d358-eac5-41e3-892d-a7467571b9b", "type": "appDefinitions"}, {"id": "71c0d358-eac5-41e3-892d-a7467571b9b0", "type": "appDefinitions"}, {"id": "98e7e44d-1562-474a-90f7-3a94e739c006", "type": "appDefinitions"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/app-builder-backend
  Scenario: Delete Multiple Apps returns "Not Found" response
    Given operation "DeleteApps" enabled
    And new "DeleteApps" request
    And body with value {"data": [{"id": "29494ddd-ac13-46a7-8558-b05b050ee755", "type": "appDefinitions"}, {"id": "71c0d358-eac5-41e3-892d-a7467571b9b0", "type": "appDefinitions"}, {"id": "98e7e44d-1562-474a-90f7-3a94e739c006", "type": "appDefinitions"}]}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/app-builder-backend
  Scenario: Delete Multiple Apps returns "OK" response
    Given operation "DeleteApps" enabled
    And new "DeleteApps" request
    And there is a valid "app" in the system
    And body with value {"data": [{"id": "{{ app.data.id }}", "type": "appDefinitions"}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "data[0].id" has the same value as "app.data.id"

  @team:DataDog/app-builder-backend
  Scenario: Get App returns "Bad Request" response
    Given operation "GetApp" enabled
    And new "GetApp" request
    And request contains "app_id" parameter with value "invalid-uuid"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/app-builder-backend
  Scenario: Get App returns "Not Found" response
    Given operation "GetApp" enabled
    And new "GetApp" request
    And request contains "app_id" parameter with value "7addb29b-f935-472c-ae79-d1963979a23e"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/app-builder-backend
  Scenario: Get App returns "OK" response
    Given operation "GetApp" enabled
    And new "GetApp" request
    And there is a valid "app" in the system
    And request contains "app_id" parameter from "app.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" has the same value as "app.data.id"
    And the response "data.type" is equal to "appDefinitions"

  @generated @skip @team:DataDog/app-builder-backend
  Scenario: List Apps returns "Bad Request, e.g. invalid sort parameter" response
    Given operation "ListApps" enabled
    And new "ListApps" request
    When the request is sent
    Then the response status is 400 Bad Request, e.g. invalid sort parameter

  @team:DataDog/app-builder-backend
  Scenario: List Apps returns "OK" response
    Given operation "ListApps" enabled
    And new "ListApps" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/app-builder-backend
  Scenario: Update App returns "Bad Request" response
    Given operation "UpdateApp" enabled
    And new "UpdateApp" request
    And there is a valid "app" in the system
    And request contains "app_id" parameter from "app.data.id"
    And body with value {"data": {"attributes": {"rootInstanceName": ""}, "id": "{{ app.data.id }}", "type": "appDefinitions"}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].detail" is equal to "missing required field"

  @team:DataDog/app-builder-backend
  Scenario: Update App returns "OK" response
    Given operation "UpdateApp" enabled
    And new "UpdateApp" request
    And there is a valid "app" in the system
    And request contains "app_id" parameter from "app.data.id"
    And body with value {"data": {"attributes": {"name": "Updated Name", "rootInstanceName": "grid0"}, "id": "{{ app.data.id }}", "type": "appDefinitions"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" has the same value as "app.data.id"
    And the response "data.type" is equal to "appDefinitions"
    And the response "data.attributes.name" is equal to "Updated Name"
