@endpoint(app-builder) @endpoint(app-builder-v2)
Feature: App Builder
  Datadog App Builder provides a low-code solution to rapidly develop and
  integrate secure, customized applications into your monitoring stack that
  are built to accelerate remediation at scale. These API endpoints allow
  you to create, read, update, delete, and publish apps.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "AppBuilder" API

  @skip-typescript @team:DataDog/app-builder-backend @team:DataDog/web-frameworks
  Scenario: Create App returns "Bad Request" response
    Given operation "CreateApp" enabled
    And new "CreateApp" request
    And body with value {"data": {"attributes": {"description": "This is a bad example app", "embeddedQueries": [], "rootInstanceName": "grid0"}, "type": "appDefinitions"}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].detail" is equal to "missing required field"

  @skip-typescript @team:DataDog/app-builder-backend @team:DataDog/web-frameworks
  Scenario: Create App returns "Created" response
    Given operation "CreateApp" enabled
    And new "CreateApp" request
    And body with value {"data": {"attributes": {"components": [{"events": [], "name": "grid0", "properties": {"children": [{"events": [], "name": "gridCell0", "properties": {"children": [{"events": [], "name": "calloutValue0", "properties": {"isVisible": true, "isUnpublishd": false, "isLoading": false, "label": "CPU Usage", "size": "sm", "style": "vivid_yellow", "unit": "kB", "value": "42"}, "type": "calloutValue"}], "isVisible": "true", "layout": {"default": {"height": 8, "width": 2, "x": 0, "y": 0}}}, "type": "gridCell"}]}, "type": "grid"}], "description": "This is a simple example app", "embeddedQueries": [], "name": "Example App", "rootInstanceName": "grid0"}, "type": "appDefinitions"}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.type" is equal to "appDefinitions"

  @skip @team:DataDog/app-builder-backend @team:DataDog/web-frameworks
  Scenario: Delete App returns "Bad Request" response
    Given operation "DeleteApp" enabled
    And new "DeleteApp" request
    And request contains "app_id" parameter with value "bad-app-id"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/app-builder-backend @team:DataDog/web-frameworks
  Scenario: Delete App returns "Gone" response
    Given operation "DeleteApp" enabled
    And new "DeleteApp" request
    And request contains "app_id" parameter with value "7addb29b-f935-472c-ae79-d1963979a23e"
    When the request is sent
    Then the response status is 410 Gone

  @skip-typescript @team:DataDog/app-builder-backend @team:DataDog/web-frameworks
  Scenario: Delete App returns "Not Found" response
    Given operation "DeleteApp" enabled
    And new "DeleteApp" request
    And request contains "app_id" parameter with value "7addb29b-f935-472c-ae79-d1963979a23e"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-typescript @team:DataDog/app-builder-backend @team:DataDog/web-frameworks
  Scenario: Delete App returns "OK" response
    Given operation "DeleteApp" enabled
    And there is a valid "app" in the system
    And new "DeleteApp" request
    And request contains "app_id" parameter from "app.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" has the same value as "app.data.id"
    And the response "data.type" is equal to "appDefinitions"

  @generated @skip @team:DataDog/app-builder-backend @team:DataDog/web-frameworks
  Scenario: Delete Multiple Apps returns "Bad Request" response
    Given operation "DeleteApps" enabled
    And new "DeleteApps" request
    And body with value {"data": [{"id": "aea2ed17-b45f-40d0-ba59-c86b7972c901", "type": "appDefinitions"}, {"id": "f69bb8be-6168-4fe7-a30d-370256b6504a", "type": "appDefinitions"}, {"id": "ab1ed73e-13ad-4426-b0df-a0ff8876a088", "type": "appDefinitions"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-typescript @team:DataDog/app-builder-backend @team:DataDog/web-frameworks
  Scenario: Delete Multiple Apps returns "Not Found" response
    Given operation "DeleteApps" enabled
    And new "DeleteApps" request
    And body with value {"data": [{"id": "aea2ed17-b45f-40d0-ba59-c86b7972c901", "type": "appDefinitions"}, {"id": "f69bb8be-6168-4fe7-a30d-370256b6504a", "type": "appDefinitions"}, {"id": "ab1ed73e-13ad-4426-b0df-a0ff8876a088", "type": "appDefinitions"}]}
    When the request is sent
    Then the response status is 404 Not Found

  @skip-typescript @team:DataDog/app-builder-backend @team:DataDog/web-frameworks
  Scenario: Delete Multiple Apps returns "OK" response
    Given operation "DeleteApps" enabled
    And new "DeleteApps" request
    And there is a valid "app" in the system
    And body with value {"data": [{"id": "{{ app.data.id }}", "type": "appDefinitions"}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "data[0].id" has the same value as "app.data.id"

  @skip @team:DataDog/app-builder-backend @team:DataDog/web-frameworks
  Scenario: Get App returns "Bad Request" response
    Given operation "GetApp" enabled
    And new "GetApp" request
    And request contains "app_id" parameter with value "invalid-uuid"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-typescript @team:DataDog/app-builder-backend @team:DataDog/web-frameworks
  Scenario: Get App returns "Not Found" response
    Given operation "GetApp" enabled
    And new "GetApp" request
    And request contains "app_id" parameter with value "7addb29b-f935-472c-ae79-d1963979a23e"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-typescript @team:DataDog/app-builder-backend @team:DataDog/web-frameworks
  Scenario: Get App returns "OK" response
    Given operation "GetApp" enabled
    And new "GetApp" request
    And there is a valid "app" in the system
    And request contains "app_id" parameter from "app.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" has the same value as "app.data.id"
    And the response "data.type" is equal to "appDefinitions"

  @generated @skip @team:DataDog/app-builder-backend @team:DataDog/web-frameworks
  Scenario: List Apps returns "Bad Request" response
    Given operation "ListApps" enabled
    And new "ListApps" request
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-typescript @team:DataDog/app-builder-backend @team:DataDog/web-frameworks
  Scenario: List Apps returns "OK" response
    Given operation "ListApps" enabled
    And new "ListApps" request
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/app-builder-backend @team:DataDog/web-frameworks
  Scenario: Publish App returns "Bad Request" response
    Given operation "PublishApp" enabled
    And new "PublishApp" request
    And request contains "app_id" parameter with value "invalid-uuid"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-typescript @team:DataDog/app-builder-backend @team:DataDog/web-frameworks
  Scenario: Publish App returns "Created" response
    Given operation "PublishApp" enabled
    And new "PublishApp" request
    And there is a valid "app" in the system
    And request contains "app_id" parameter from "app.data.id"
    When the request is sent
    Then the response status is 201 Created

  @skip-typescript @team:DataDog/app-builder-backend @team:DataDog/web-frameworks
  Scenario: Publish App returns "Not Found" response
    Given operation "PublishApp" enabled
    And new "PublishApp" request
    And request contains "app_id" parameter with value "7addb29b-f935-472c-ae79-d1963979a23e"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/app-builder-backend @team:DataDog/web-frameworks
  Scenario: Unpublish App returns "Bad Request" response
    Given operation "UnpublishApp" enabled
    And new "UnpublishApp" request
    And request contains "app_id" parameter with value "invalid-uuid"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-typescript @team:DataDog/app-builder-backend @team:DataDog/web-frameworks
  Scenario: Unpublish App returns "Not Found" response
    Given operation "UnpublishApp" enabled
    And new "UnpublishApp" request
    And request contains "app_id" parameter with value "7addb29b-f935-472c-ae79-d1963979a23e"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-typescript @team:DataDog/app-builder-backend @team:DataDog/web-frameworks
  Scenario: Unpublish App returns "OK" response
    Given operation "UnpublishApp" enabled
    And new "UnpublishApp" request
    And there is a valid "app" in the system
    And request contains "app_id" parameter from "app.data.id"
    When the request is sent
    Then the response status is 200 OK

  @skip-typescript @team:DataDog/app-builder-backend @team:DataDog/web-frameworks
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

  @skip-typescript @team:DataDog/app-builder-backend @team:DataDog/web-frameworks
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
