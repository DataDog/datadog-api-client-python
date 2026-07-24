@endpoint(customer-org) @endpoint(customer-org-v2)
Feature: Customer Org
  Programmatic management of a customer's Datadog organization. Use this API
  to perform self-service organization lifecycle actions such as disabling
  the authenticated org.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CustomerOrg" API
    And operation "DisableCustomerOrg" enabled
    And new "DisableCustomerOrg" request
    And body with value {"data": {"attributes": {"org_uuid": "abcdef01-2345-6789-abcd-ef0123456789"}, "id": "1", "type": "customer_org_disable"}}

  @generated @skip @team:DataDog/org-management
  Scenario: Disable the authenticated customer organization returns "Bad Request" response
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/org-management
  Scenario: Disable the authenticated customer organization returns "Conflict" response
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/org-management
  Scenario: Disable the authenticated customer organization returns "OK" response
    When the request is sent
    Then the response status is 200 OK
