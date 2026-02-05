@endpoint(seats) @endpoint(seats-v2)
Feature: Seats
  The seats API allows you to view, assign, and unassign seats for your
  organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Seats" API

  @generated @skip @team:DataDog/billing-experience
  Scenario: Assign seats to users for a product code returns "Created" response
    Given new "AssignSeatsUserV2" request
    And body with value {"data": {"attributes": {"user_uuids": []}, "type": "seat-assignments"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/billing-experience
  Scenario: Get seats users for a product code returns "OK" response
    Given new "GetSeatsUsersV2" request
    And request contains "product_code" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/billing-experience
  Scenario: Unassign seats from users for a product code returns "No Content" response
    Given new "UnassignSeatsUserV2" request
    And body with value {"data": {"attributes": {"user_uuids": []}, "type": "seat-assignments"}}
    When the request is sent
    Then the response status is 204 No Content
