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

  @generated @skip @team:DataDog/hamr
  Scenario: Create or update HAMR organization connection returns "Bad Request" response
    Given operation "CreateHamrOrgConnection" enabled
    And new "CreateHamrOrgConnection" request
    And body with value {"data": {"attributes": {"hamr_status": 4, "is_primary": true, "modified_by": "admin@example.com", "target_org_datacenter": "us1", "target_org_name": "Production Backup Org", "target_org_uuid": "660f9511-f3ac-52e5-b827-557766551111"}, "id": "550e8400-e29b-41d4-a716-446655440000", "type": "hamr_org_connections"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/hamr
  Scenario: Create or update HAMR organization connection returns "OK" response
    Given operation "CreateHamrOrgConnection" enabled
    And new "CreateHamrOrgConnection" request
    And body with value {"data": {"attributes": {"hamr_status": 4, "is_primary": true, "modified_by": "admin@example.com", "target_org_datacenter": "us1", "target_org_name": "Production Backup Org", "target_org_uuid": "660f9511-f3ac-52e5-b827-557766551111"}, "id": "550e8400-e29b-41d4-a716-446655440000", "type": "hamr_org_connections"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/hamr
  Scenario: Get HAMR organization connection returns "Bad Request" response
    Given operation "GetHamrOrgConnection" enabled
    And new "GetHamrOrgConnection" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/hamr
  Scenario: Get HAMR organization connection returns "Not Found" response
    Given operation "GetHamrOrgConnection" enabled
    And new "GetHamrOrgConnection" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/hamr
  Scenario: Get HAMR organization connection returns "OK" response
    Given operation "GetHamrOrgConnection" enabled
    And new "GetHamrOrgConnection" request
    When the request is sent
    Then the response status is 200 OK
