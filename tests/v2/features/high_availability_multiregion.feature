@endpoint(high-availability-multiregion) @endpoint(high-availability-multiregion-v2)
Feature: High Availability MultiRegion
  Configure High Availability Multi-Region (HAMR) connections between
  Datadog organizations. HAMR provides disaster recovery capabilities by
  maintaining synchronized data between primary and secondary organizations
  across different datacenters.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "HighAvailabilityMultiRegion" API

  @generated @skip @team:ddoghq/hamr
  Scenario: Get HAMR organization connection returns "Bad Request" response
    Given operation "GetHamrOrgConnection" enabled
    And new "GetHamrOrgConnection" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/hamr
  Scenario: Get HAMR organization connection returns "Not Found" response
    Given operation "GetHamrOrgConnection" enabled
    And new "GetHamrOrgConnection" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/hamr
  Scenario: Get HAMR organization connection returns "OK" response
    Given operation "GetHamrOrgConnection" enabled
    And new "GetHamrOrgConnection" request
    When the request is sent
    Then the response status is 200 OK
