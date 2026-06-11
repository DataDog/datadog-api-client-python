@endpoint(user-authorized-clients) @endpoint(user-authorized-clients-v2)
Feature: User Authorized Clients
  Manage OAuth2 client authorizations at the user level.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "UserAuthorizedClients" API

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Delete a user authorized client returns "No Content" response
    Given new "DeleteUserAuthorizedClient" request
    And request contains "user_authorized_client_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Delete a user authorized client returns "Not Found" response
    Given new "DeleteUserAuthorizedClient" request
    And request contains "user_authorized_client_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Delete all user authorized clients for a client returns "No Content" response
    Given new "DeleteUserAuthorizedClientsByClient" request
    And request contains "client_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Delete all user authorized clients for a client returns "Not Found" response
    Given new "DeleteUserAuthorizedClientsByClient" request
    And request contains "client_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Get a user authorized client returns "Not Found" response
    Given new "GetUserAuthorizedClient" request
    And request contains "user_authorized_client_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Get a user authorized client returns "OK" response
    Given new "GetUserAuthorizedClient" request
    And request contains "user_authorized_client_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: List user authorized clients returns "OK" response
    Given new "ListUserAuthorizedClients" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/delegated-auth-login @with-pagination
  Scenario: List user authorized clients returns "OK" response with pagination
    Given new "ListUserAuthorizedClients" request
    When the request with pagination is sent
    Then the response status is 200 OK
