@endpoint(org-authorized-clients) @endpoint(org-authorized-clients-v2)
Feature: Org Authorized Clients
  Manage OAuth2 client authorizations at the organization level.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "OrgAuthorizedClients" API

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Delete a user authorization for a client returns "No Content" response
    Given new "DeleteOrgAuthorizedClientUserAuthorization" request
    And request contains "org_authorized_client_id" parameter from "REPLACE.ME"
    And request contains "user_authorized_client_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Delete a user authorization for a client returns "Not Found" response
    Given new "DeleteOrgAuthorizedClientUserAuthorization" request
    And request contains "org_authorized_client_id" parameter from "REPLACE.ME"
    And request contains "user_authorized_client_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Delete a user's authorizations for a client returns "No Content" response
    Given new "DeleteOrgAuthorizedClientAllUserAuthorizations" request
    And request contains "org_authorized_client_id" parameter from "REPLACE.ME"
    And request contains "user_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Delete a user's authorizations for a client returns "Not Found" response
    Given new "DeleteOrgAuthorizedClientAllUserAuthorizations" request
    And request contains "org_authorized_client_id" parameter from "REPLACE.ME"
    And request contains "user_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Delete an org authorized client returns "No Content" response
    Given new "DeleteOrgAuthorizedClient" request
    And request contains "org_authorized_client_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Delete an org authorized client returns "Not Found" response
    Given new "DeleteOrgAuthorizedClient" request
    And request contains "org_authorized_client_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Get an org authorized client returns "Not Found" response
    Given new "GetOrgAuthorizedClient" request
    And request contains "org_authorized_client_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Get an org authorized client returns "OK" response
    Given new "GetOrgAuthorizedClient" request
    And request contains "org_authorized_client_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: List org authorized clients returns "OK" response
    Given new "ListOrgAuthorizedClients" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/delegated-auth-login @with-pagination
  Scenario: List org authorized clients returns "OK" response with pagination
    Given new "ListOrgAuthorizedClients" request
    When the request with pagination is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: List user authorizations for a client returns "Not Found" response
    Given new "ListOrgAuthorizedClientUserAuthorizations" request
    And request contains "org_authorized_client_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: List user authorizations for a client returns "OK" response
    Given new "ListOrgAuthorizedClientUserAuthorizations" request
    And request contains "org_authorized_client_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/delegated-auth-login @with-pagination
  Scenario: List user authorizations for a client returns "OK" response with pagination
    Given new "ListOrgAuthorizedClientUserAuthorizations" request
    And request contains "org_authorized_client_id" parameter from "REPLACE.ME"
    When the request with pagination is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Update an org authorized client returns "Bad Request" response
    Given new "UpdateOrgAuthorizedClient" request
    And request contains "org_authorized_client_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"disabled": true}, "id": "00000000-0000-0000-0000-000000000001", "type": "org_authorized_clients"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Update an org authorized client returns "Not Found" response
    Given new "UpdateOrgAuthorizedClient" request
    And request contains "org_authorized_client_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"disabled": true}, "id": "00000000-0000-0000-0000-000000000001", "type": "org_authorized_clients"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Update an org authorized client returns "OK" response
    Given new "UpdateOrgAuthorizedClient" request
    And request contains "org_authorized_client_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"disabled": true}, "id": "00000000-0000-0000-0000-000000000001", "type": "org_authorized_clients"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Update an org authorized client returns "Unprocessable Entity" response
    Given new "UpdateOrgAuthorizedClient" request
    And request contains "org_authorized_client_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"disabled": true}, "id": "00000000-0000-0000-0000-000000000001", "type": "org_authorized_clients"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity
