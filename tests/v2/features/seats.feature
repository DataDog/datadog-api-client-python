@endpoint(seats) @endpoint(seats-v2)
Feature: Seats
  The seats API allows you to view, assign, and unassign seats for your
  organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Seats" API

  @generated @skip @team:DataDog/billing-experience
  Scenario: Assign seats to users returns "Bad Request" response
    Given new "AssignSeatsUser" request
    And body with value {"data": {"attributes": {"product_code": "", "user_uuids": [""]}, "type": "seat-assignments"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @skip-validation @team:DataDog/billing-experience
  Scenario: Assign seats to users returns "Created" response
    Given there is a valid "user" in the system
    And new "AssignSeatsUser" request
    And body with value {"data": {"type": "seat-assignments", "attributes": {"product_code": "incident_response", "user_uuids": ["{{ user.data.id }}"]}}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.type" is equal to "seat-assignments"
    And the response "data.attributes.product_code" is equal to "incident_response"
    And the response "data.attributes.assigned_ids[0]" is equal to "{{ user.data.id }}"

  @skip-validation @team:DataDog/billing-experience
  Scenario: Assign seats to users returns "Unprocessable Entity" response
    Given new "AssignSeatsUser" request
    And body with value {"data": {"attributes": {"product_code": "", "user_uuids": [""]}, "type": "seat-assignments"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @team:DataDog/billing-experience
  Scenario: Assign seats to users returns "Unprocessable Entity" response when product_code is empty
    Given there is a valid "user" in the system
    And new "AssignSeatsUser" request
    And body with value {"data": {"type": "seat-assignments", "attributes": {"product_code": "", "user_uuids": ["{{ user.data.id }}"]}}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @team:DataDog/billing-experience
  Scenario: Assign seats to users returns "Unprocessable Entity" response when user_uuids is empty
    Given new "AssignSeatsUser" request
    And body with value {"data": {"type": "seat-assignments", "attributes": {"product_code": "incident_response", "user_uuids": []}}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @generated @skip @team:DataDog/billing-experience
  Scenario: Get users with seats returns "Bad Request" response
    Given new "GetSeatsUsers" request
    And request contains "product_code" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/billing-experience
  Scenario: Get users with seats returns "OK" response
    Given new "GetSeatsUsers" request
    And request contains "product_code" parameter with value "incident_response"
    And request contains "page[limit]" parameter with value 100
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/billing-experience
  Scenario: Get users with seats returns "Unprocessable Entity" response
    Given new "GetSeatsUsers" request
    And request contains "product_code" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @generated @skip @team:DataDog/billing-experience
  Scenario: Unassign seats from users returns "Bad Request" response
    Given new "UnassignSeatsUser" request
    And body with value {"data": {"attributes": {"product_code": "", "user_uuids": [""]}, "type": "seat-assignments"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @skip-validation @team:DataDog/billing-experience
  Scenario: Unassign seats from users returns "No Content" response
    Given there is a valid "user" in the system
    And new "UnassignSeatsUser" request
    And body with value {"data": {"type": "seat-assignments", "attributes": {"product_code": "incident_response", "user_uuids": ["{{ user.data.id }}"]}}}
    When the request is sent
    Then the response status is 204 No Content

  @skip-validation @team:DataDog/billing-experience
  Scenario: Unassign seats from users returns "Unprocessable Entity" response
    Given new "UnassignSeatsUser" request
    And body with value {"data": {"attributes": {"product_code": "", "user_uuids": [""]}, "type": "seat-assignments"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @team:DataDog/billing-experience
  Scenario: Unassign seats from users returns "Unprocessable Entity" response when product_code is empty
    Given there is a valid "user" in the system
    And new "UnassignSeatsUser" request
    And body with value {"data": {"type": "seat-assignments", "attributes": {"product_code": "", "user_uuids": ["{{ user.data.id }}"]}}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @team:DataDog/billing-experience
  Scenario: Unassign seats from users returns "Unprocessable Entity" response when user_uuids is empty
    Given new "UnassignSeatsUser" request
    And body with value {"data": {"type": "seat-assignments", "attributes": {"product_code": "incident_response", "user_uuids": []}}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity
