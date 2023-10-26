@endpoint(powerpack) @endpoint(powerpack-v2)
Feature: Powerpack
  The powerpack endpoints allow you to:  - Get a powerpack - Create a
  powerpack - Delete a powerpack - Get a list of all powerpacks  The Patch
  and Delete API methods can only be performed on a powerpack by a user who
  has the powerpack create permission for that specific powerpack.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Powerpack" API

  @team:DataDog/dashboards-backend
  Scenario: Create a new powerpack returns "Bad Request" response
    Given new "CreatePowerpack" request
    And body with value {"data": {"attributes": {"description": "Powerpack for ABC", "group_widget": {"definition": {"type": "group1", "layout_type": "ordered", "widgets": []}}, "name": "Sample Powerpack", "tags": ["tag:foo1"], "template_variables": [{"defaults": ["*"], "name": "test"}]}, "type": "powerpack"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/dashboards-backend
  Scenario: Create a new powerpack returns "OK" response
    Given new "CreatePowerpack" request
    And body from file "powerpack_payload.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "powerpack"
    And the response "data.attributes.name" is equal to "{{ unique }}"
    And the response "data.attributes.description" is equal to "Sample powerpack"
    And the response "data.attributes.template_variables[0].name" is equal to "sample"
    And the response "data.attributes.template_variables[0].defaults[0]" is equal to "*"
    And the response "data.attributes.group_widget.layout.width" is equal to 12
    And the response "data.attributes.group_widget.layout.height" is equal to 3
    And the response "data.attributes.group_widget.layout.x" is equal to 0
    And the response "data.attributes.group_widget.layout.y" is equal to 0
    And the response "data.attributes.group_widget.definition.type" is equal to "group"
    And the response "data.attributes.group_widget.definition.layout_type" is equal to "ordered"
    And the response "data.attributes.group_widget.definition.show_title" is equal to true
    And the response "data.attributes.group_widget.definition.title" is equal to "Sample Powerpack"
    And the response "data.attributes.group_widget.definition.widgets[0].definition.type" is equal to "note"

  @team:DataDog/dashboards-backend
  Scenario: Delete a powerpack returns "OK" response
    Given there is a valid "powerpack" in the system
    And new "DeletePowerpack" request
    And request contains "powerpack_id" parameter from "powerpack.data.id"
    When the request is sent
    Then the response status is 204 OK

  @team:DataDog/dashboards-backend
  Scenario: Delete a powerpack returns "Powerpack Not Found" response
    Given new "DeletePowerpack" request
    And request contains "powerpack_id" parameter with value "made-up-id"
    When the request is sent
    Then the response status is 404 Powerpack Not Found

  @team:DataDog/dashboards-backend
  Scenario: Get a Powerpack returns "OK" response
    Given there is a valid "powerpack" in the system
    And new "GetPowerpack" request
    And request contains "powerpack_id" parameter from "powerpack.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "powerpack"
    And the response "data.id" has the same value as "powerpack.data.id"
    And the response "data.attributes.name" is equal to "{{ unique }}"
    And the response "data.attributes.description" is equal to "Sample powerpack"
    And the response "data.attributes.template_variables[0].name" is equal to "sample"
    And the response "data.attributes.template_variables[0].defaults[0]" is equal to "*"
    And the response "data.attributes.group_widget.layout.width" is equal to 12
    And the response "data.attributes.group_widget.layout.height" is equal to 3
    And the response "data.attributes.group_widget.layout.x" is equal to 0
    And the response "data.attributes.group_widget.layout.y" is equal to 0
    And the response "data.attributes.group_widget.definition.type" is equal to "group"
    And the response "data.attributes.group_widget.definition.layout_type" is equal to "ordered"
    And the response "data.attributes.group_widget.definition.show_title" is equal to true
    And the response "data.attributes.group_widget.definition.title" is equal to "Sample Powerpack"
    And the response "data.attributes.group_widget.definition.widgets[0].definition.type" is equal to "note"
    And the response "data.attributes.group_widget.definition.widgets[0].definition.content" is equal to "test"

  @team:DataDog/dashboards-backend
  Scenario: Get a Powerpack returns "Powerpack Not Found." response
    Given new "GetPowerpack" request
    And request contains "powerpack_id" parameter with value "made-up-id"
    When the request is sent
    Then the response status is 404 Powerpack Not Found.

  @team:DataDog/dashboards-backend
  Scenario: Get all powerpacks returns "OK" response
    Given there is a valid "powerpack" in the system
    And new "ListPowerpacks" request
    And request contains "page[limit]" parameter with value 1000
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has item with field "type" with value "powerpack"
    And the response "data" has item with field "id" with value "{{ powerpack.data.id }}"
    And the response "data" has item with field "attributes.name" with value "{{ unique }}"
    And the response "data" has item with field "attributes.description" with value "Sample powerpack"
    And the response "data" has item with field "attributes.template_variables[0].name" with value "sample"
    And the response "data" has item with field "attributes.template_variables[0].defaults[0]" with value "*"
    And the response "data" has item with field "attributes.group_widget.layout.width" with value 12
    And the response "data" has item with field "attributes.group_widget.layout.height" with value 3
    And the response "data" has item with field "attributes.group_widget.layout.x" with value 0
    And the response "data" has item with field "attributes.group_widget.layout.y" with value 0
    And the response "data" has item with field "attributes.group_widget.definition.type" with value "group"
    And the response "data" has item with field "attributes.group_widget.definition.layout_type" with value "ordered"
    And the response "data" has item with field "attributes.group_widget.definition.show_title" with value true
    And the response "data" has item with field "attributes.group_widget.definition.title" with value "Sample Powerpack"
    And the response "data" has item with field "attributes.group_widget.definition.widgets[0].definition.type" with value "note"
    And the response "data" has item with field "attributes.group_widget.definition.widgets[0].definition.content" with value "test"

  @replay-only @skip-validation @team:DataDog/dashboards-backend @with-pagination
  Scenario: Get all powerpacks returns "OK" response with pagination
    Given new "ListPowerpacks" request
    And request contains "page[limit]" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @team:DataDog/dashboards-backend
  Scenario: Update a powerpack returns "Bad Request" response
    Given there is a valid "powerpack" in the system
    And new "UpdatePowerpack" request
    And request contains "powerpack_id" parameter from "powerpack.data.id"
    And body with value {"data":{"type": "powerpack","attributes": {"name": "Sample Powerpack","description": "Sample powerpack","group_widget": {"definition": {"type": "group1", "layout_type": "ordered", "widgets": []}},"template_variables": [{"name": "sample", "defaults": ["*"]}],"tags": ["tag:sample"]}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/dashboards-backend
  Scenario: Update a powerpack returns "OK" response
    Given there is a valid "powerpack" in the system
    And new "UpdatePowerpack" request
    And request contains "powerpack_id" parameter from "powerpack.data.id"
    And body from file "powerpack_payload.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "powerpack"
    And the response "data.id" has the same value as "powerpack.data.id"
    And the response "data.attributes.name" is equal to "{{ unique }}"
    And the response "data.attributes.description" is equal to "Sample powerpack"
    And the response "data.attributes.template_variables[0].name" is equal to "sample"
    And the response "data.attributes.template_variables[0].defaults[0]" is equal to "*"
    And the response "data.attributes.group_widget.layout.width" is equal to 12
    And the response "data.attributes.group_widget.layout.height" is equal to 3
    And the response "data.attributes.group_widget.layout.x" is equal to 0
    And the response "data.attributes.group_widget.layout.y" is equal to 0
    And the response "data.attributes.group_widget.definition.type" is equal to "group"
    And the response "data.attributes.group_widget.definition.layout_type" is equal to "ordered"
    And the response "data.attributes.group_widget.definition.show_title" is equal to true
    And the response "data.attributes.group_widget.definition.title" is equal to "Sample Powerpack"
    And the response "data.attributes.group_widget.definition.widgets[0].definition.type" is equal to "note"
    And the response "data.attributes.group_widget.definition.widgets[0].definition.content" is equal to "test"

  @team:DataDog/dashboards-backend
  Scenario: Update a powerpack returns "Powerpack Not Found" response
    Given new "UpdatePowerpack" request
    And request contains "powerpack_id" parameter with value "made-up-id"
    And body from file "powerpack_payload.json"
    When the request is sent
    Then the response status is 404 Powerpack Not Found
