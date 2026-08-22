@endpoint(rum-teams-ownership) @endpoint(rum-teams-ownership-v2)
Feature: Rum Teams Ownership
  Manage teams ownership mappings between RUM views and the teams that own
  them. See
  <https://docs.datadoghq.com/real_user_monitoring/ownership_of_views/>.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RumTeamsOwnership" API

  @team:DataDog/rum-backend
  Scenario: Bulk create and remove teams ownership mappings returns "Bad Request" response
    Given new "CreateTeamsOwnershipMappingsBatch" request
    And body with value {"atomic:operations":[{"op":"add","data":{"type":"teams_ownership_mappings","attributes":{"team_handle":"team-rum","view_name":"/checkout","service":"web-checkout","application_id":"invalid-uuid","match_type":"exact"}}}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/rum-backend
  Scenario: Bulk create and remove teams ownership mappings returns "Bad Request. One or more operations failed validation, so none of the operations were applied." response
    Given operation "CreateTeamsOwnershipMappingsBatch" enabled
    And new "CreateTeamsOwnershipMappingsBatch" request
    And body with value {"atomic:operations": [{"data": {"attributes": {"application_id": "11111111-2222-3333-4444-555555555555", "match_type": "exact", "service": "web-checkout", "team_handle": "team-rum", "view_name": "/checkout"}, "type": "teams_ownership_mappings"}, "op": "add", "ref": {"id": "{{ unique }}", "type": "teams_ownership_mappings"}}]}
    When the request is sent
    Then the response status is 400 Bad Request. One or more operations failed validation, so none of the operations were applied.

  @generated @skip @team:DataDog/rum-backend
  Scenario: Bulk create and remove teams ownership mappings returns "Conflict. One or more mappings requested for creation already exist." response
    Given operation "CreateTeamsOwnershipMappingsBatch" enabled
    And new "CreateTeamsOwnershipMappingsBatch" request
    And body with value {"atomic:operations": [{"data": {"attributes": {"application_id": "11111111-2222-3333-4444-555555555555", "match_type": "exact", "service": "web-checkout", "team_handle": "team-rum", "view_name": "/checkout"}, "type": "teams_ownership_mappings"}, "op": "add", "ref": {"id": "456", "type": "teams_ownership_mappings"}}]}
    When the request is sent
    Then the response status is 409 Conflict. One or more mappings requested for creation already exist.

  @generated @skip @team:DataDog/rum-backend
  Scenario: Bulk create and remove teams ownership mappings returns "Not Found. One or more mappings requested for removal do not exist." response
    Given operation "CreateTeamsOwnershipMappingsBatch" enabled
    And new "CreateTeamsOwnershipMappingsBatch" request
    And body with value {"atomic:operations": [{"data": {"attributes": {"application_id": "11111111-2222-3333-4444-555555555555", "match_type": "exact", "service": "web-checkout", "team_handle": "team-rum", "view_name": "/checkout"}, "type": "teams_ownership_mappings"}, "op": "add", "ref": {"id": "456", "type": "teams_ownership_mappings"}}]}
    When the request is sent
    Then the response status is 404 Not Found. One or more mappings requested for removal do not exist.

  @team:DataDog/rum-backend
  Scenario: Bulk create and remove teams ownership mappings returns "OK" response
    Given new "CreateTeamsOwnershipMappingsBatch" request
    And body with value {"atomic:operations":[{"op":"add","data":{"type":"teams_ownership_mappings","attributes":{"team_handle":"team-rum","view_name":"/checkout-{{ unique_lower_alnum }}","service":"web-checkout-{{ unique_lower_alnum }}","match_type":"exact"}}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "atomic:results[0].data.type" is equal to "teams_ownership_mappings"
    And the response "atomic:results[0].data.attributes.team_handle" is equal to "team-rum"
    And the response "atomic:results[0].data.attributes.match_type" is equal to "exact"

  @team:DataDog/rum-backend
  Scenario: Bulk create teams ownership mappings without a service or application ID returns "Bad Request" response
    Given new "CreateTeamsOwnershipMappingsBatch" request
    And body with value {"atomic:operations":[{"op":"add","data":{"type":"teams_ownership_mappings","attributes":{"team_handle":"team-rum","view_name":"/checkout-{{ unique_lower_alnum }}","match_type":"exact"}}}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: Create a teams ownership mapping returns "Bad Request" response
    Given operation "CreateTeamsOwnershipMapping" enabled
    And new "CreateTeamsOwnershipMapping" request
    And body with value {"data": {"attributes": {"application_id": "11111111-2222-3333-4444-555555555555", "match_type": "exact", "service": "web-checkout", "team_handle": "team-rum", "view_name": "/checkout"}, "type": "teams_ownership_mappings"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: Create a teams ownership mapping returns "Created" response
    Given operation "CreateTeamsOwnershipMapping" enabled
    And new "CreateTeamsOwnershipMapping" request
    And body with value {"data": {"attributes": {"application_id": "11111111-2222-3333-4444-555555555555", "match_type": "exact", "service": "web-checkout", "team_handle": "team-rum", "view_name": "/checkout"}, "type": "teams_ownership_mappings"}}
    When the request is sent
    Then the response status is 201 Created

  @team:DataDog/rum-backend
  Scenario: Create teams ownership mapping returns "Bad Request" response
    Given new "CreateTeamsOwnershipMapping" request
    And body with value {"data":{"type":"teams_ownership_mappings","attributes":{"team_handle":"team-rum","view_name":"/checkout","service":"web-checkout","application_id":"invalid-uuid","match_type":"exact"}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/rum-backend
  Scenario: Create teams ownership mapping returns "Created" response
    Given new "CreateTeamsOwnershipMapping" request
    And body with value {"data":{"type":"teams_ownership_mappings","attributes":{"team_handle":"team-rum","view_name":"/checkout-{{ unique_lower_alnum }}","service":"web-checkout-{{ unique_lower_alnum }}","match_type":"exact"}}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.type" is equal to "teams_ownership_mappings"
    And the response "data.attributes.team_handle" is equal to "team-rum"
    And the response "data.attributes.view_name" is equal to "/checkout-{{ unique_lower_alnum }}"
    And the response "data.attributes.service" is equal to "web-checkout-{{ unique_lower_alnum }}"
    And the response "data.attributes.match_type" is equal to "exact"

  @team:DataDog/rum-backend
  Scenario: Delete a teams ownership mapping returns "No Content" response
    Given there is a valid "teams_ownership_mapping" in the system
    And new "DeleteTeamsOwnershipMapping" request
    And request contains "id" parameter from "teams_ownership_mapping.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/rum-backend
  Scenario: Delete a teams ownership mapping returns "Not Found" response
    Given new "DeleteTeamsOwnershipMapping" request
    And request contains "id" parameter with value "{{ unique }}"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/rum-backend
  Scenario: Get a teams ownership mapping returns "Not Found" response
    Given new "GetTeamsOwnershipMapping" request
    And request contains "id" parameter with value "{{ unique }}"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/rum-backend
  Scenario: Get a teams ownership mapping returns "OK" response
    Given there is a valid "teams_ownership_mapping" in the system
    And new "GetTeamsOwnershipMapping" request
    And request contains "id" parameter from "teams_ownership_mapping.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "{{ teams_ownership_mapping.data.id }}"
    And the response "data.type" is equal to "teams_ownership_mappings"
    And the response "data.attributes.team_handle" is equal to "team-rum"
    And the response "data.attributes.view_name" is equal to "{{ teams_ownership_mapping.data.attributes.view_name }}"
    And the response "data.attributes.match_type" is equal to "exact"

  @generated @skip @team:DataDog/rum-backend
  Scenario: List teams ownership mappings returns "Bad Request" response
    Given operation "ListTeamsOwnershipMappings" enabled
    And new "ListTeamsOwnershipMappings" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/rum-backend
  Scenario: List teams ownership mappings returns "OK" response
    Given there is a valid "teams_ownership_mapping" in the system
    And new "ListTeamsOwnershipMappings" request
    And request contains "filter[view_name]" parameter from "teams_ownership_mapping.data.attributes.view_name"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "data[0].type" is equal to "teams_ownership_mappings"
    And the response "data[0].attributes.team_handle" is equal to "team-rum"
    And the response "data[0].attributes.view_name" is equal to "{{ teams_ownership_mapping.data.attributes.view_name }}"
    And the response "data[0].attributes.service" is equal to "{{ teams_ownership_mapping.data.attributes.service }}"
    And the response "data[0].attributes.match_type" is equal to "exact"

  @generated @skip @team:DataDog/rum-backend
  Scenario: List teams ownership rules returns "Bad Request" response
    Given operation "ListTeamsOwnershipRules" enabled
    And new "ListTeamsOwnershipRules" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/rum-backend
  Scenario: List teams ownership rules returns "OK" response
    Given there is a valid "teams_ownership_mapping" in the system
    And new "ListTeamsOwnershipRules" request
    And request contains "filter[view_name]" parameter from "teams_ownership_mapping.data.attributes.view_name"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "data[0].type" is equal to "teams_ownership_grouped_mappings"
    And the response "data[0].attributes.view_name" is equal to "{{ teams_ownership_mapping.data.attributes.view_name }}"
    And the response "data[0].attributes.match_type" is equal to "exact"
