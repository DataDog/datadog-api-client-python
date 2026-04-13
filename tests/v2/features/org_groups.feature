@endpoint(org-groups) @endpoint(org-groups-v2)
Feature: Org Groups
  Manage organization groups, memberships, policies, policy overrides, and
  policy configurations.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "OrgGroups" API

  @generated @skip @team:DataDog/org-management
  Scenario: Bulk update org group memberships returns "Bad Request" response
    Given operation "BulkUpdateOrgGroupMemberships" enabled
    And new "BulkUpdateOrgGroupMemberships" request
    And body with value {"data": {"attributes": {"orgs": [{"org_site": "datadoghq.com", "org_uuid": "c3d4e5f6-a7b8-9012-cdef-012345678901"}]}, "relationships": {"source_org_group": {"data": {"id": "a1b2c3d4-e5f6-7890-abcd-ef0123456789", "type": "org_groups"}}, "target_org_group": {"data": {"id": "a1b2c3d4-e5f6-7890-abcd-ef0123456789", "type": "org_groups"}}}, "type": "org_group_membership_bulk_updates"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/org-management
  Scenario: Bulk update org group memberships returns "Not Found" response
    Given operation "BulkUpdateOrgGroupMemberships" enabled
    And new "BulkUpdateOrgGroupMemberships" request
    And body with value {"data": {"attributes": {"orgs": [{"org_site": "datadoghq.com", "org_uuid": "c3d4e5f6-a7b8-9012-cdef-012345678901"}]}, "relationships": {"source_org_group": {"data": {"id": "a1b2c3d4-e5f6-7890-abcd-ef0123456789", "type": "org_groups"}}, "target_org_group": {"data": {"id": "a1b2c3d4-e5f6-7890-abcd-ef0123456789", "type": "org_groups"}}}, "type": "org_group_membership_bulk_updates"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/org-management
  Scenario: Bulk update org group memberships returns "OK" response
    Given operation "BulkUpdateOrgGroupMemberships" enabled
    And new "BulkUpdateOrgGroupMemberships" request
    And body with value {"data": {"attributes": {"orgs": [{"org_site": "datadoghq.com", "org_uuid": "c3d4e5f6-a7b8-9012-cdef-012345678901"}]}, "relationships": {"source_org_group": {"data": {"id": "a1b2c3d4-e5f6-7890-abcd-ef0123456789", "type": "org_groups"}}, "target_org_group": {"data": {"id": "a1b2c3d4-e5f6-7890-abcd-ef0123456789", "type": "org_groups"}}}, "type": "org_group_membership_bulk_updates"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/org-management
  Scenario: Create an org group policy override returns "Bad Request" response
    Given operation "CreateOrgGroupPolicyOverride" enabled
    And new "CreateOrgGroupPolicyOverride" request
    And body with value {"data": {"attributes": {"org_site": "datadoghq.com", "org_uuid": "c3d4e5f6-a7b8-9012-cdef-012345678901"}, "relationships": {"org_group": {"data": {"id": "a1b2c3d4-e5f6-7890-abcd-ef0123456789", "type": "org_groups"}}, "org_group_policy": {"data": {"id": "1a2b3c4d-5e6f-7890-abcd-ef0123456789", "type": "org_group_policies"}}}, "type": "org_group_policy_overrides"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/org-management
  Scenario: Create an org group policy override returns "Conflict" response
    Given operation "CreateOrgGroupPolicyOverride" enabled
    And new "CreateOrgGroupPolicyOverride" request
    And body with value {"data": {"attributes": {"org_site": "datadoghq.com", "org_uuid": "c3d4e5f6-a7b8-9012-cdef-012345678901"}, "relationships": {"org_group": {"data": {"id": "a1b2c3d4-e5f6-7890-abcd-ef0123456789", "type": "org_groups"}}, "org_group_policy": {"data": {"id": "1a2b3c4d-5e6f-7890-abcd-ef0123456789", "type": "org_group_policies"}}}, "type": "org_group_policy_overrides"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/org-management
  Scenario: Create an org group policy override returns "Created" response
    Given operation "CreateOrgGroupPolicyOverride" enabled
    And new "CreateOrgGroupPolicyOverride" request
    And body with value {"data": {"attributes": {"org_site": "datadoghq.com", "org_uuid": "c3d4e5f6-a7b8-9012-cdef-012345678901"}, "relationships": {"org_group": {"data": {"id": "a1b2c3d4-e5f6-7890-abcd-ef0123456789", "type": "org_groups"}}, "org_group_policy": {"data": {"id": "1a2b3c4d-5e6f-7890-abcd-ef0123456789", "type": "org_group_policies"}}}, "type": "org_group_policy_overrides"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/org-management
  Scenario: Create an org group policy returns "Bad Request" response
    Given operation "CreateOrgGroupPolicy" enabled
    And new "CreateOrgGroupPolicy" request
    And body with value {"data": {"attributes": {"content": {"value": "UTC"}, "policy_name": "monitor_timezone"}, "relationships": {"org_group": {"data": {"id": "a1b2c3d4-e5f6-7890-abcd-ef0123456789", "type": "org_groups"}}}, "type": "org_group_policies"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/org-management
  Scenario: Create an org group policy returns "Conflict" response
    Given operation "CreateOrgGroupPolicy" enabled
    And new "CreateOrgGroupPolicy" request
    And body with value {"data": {"attributes": {"content": {"value": "UTC"}, "policy_name": "monitor_timezone"}, "relationships": {"org_group": {"data": {"id": "a1b2c3d4-e5f6-7890-abcd-ef0123456789", "type": "org_groups"}}}, "type": "org_group_policies"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/org-management
  Scenario: Create an org group policy returns "Created" response
    Given operation "CreateOrgGroupPolicy" enabled
    And new "CreateOrgGroupPolicy" request
    And body with value {"data": {"attributes": {"content": {"value": "UTC"}, "policy_name": "monitor_timezone"}, "relationships": {"org_group": {"data": {"id": "a1b2c3d4-e5f6-7890-abcd-ef0123456789", "type": "org_groups"}}}, "type": "org_group_policies"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/org-management
  Scenario: Create an org group returns "Bad Request" response
    Given operation "CreateOrgGroup" enabled
    And new "CreateOrgGroup" request
    And body with value {"data": {"attributes": {"name": "My Org Group"}, "type": "org_groups"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/org-management
  Scenario: Create an org group returns "Conflict" response
    Given operation "CreateOrgGroup" enabled
    And new "CreateOrgGroup" request
    And body with value {"data": {"attributes": {"name": "My Org Group"}, "type": "org_groups"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/org-management
  Scenario: Create an org group returns "Created" response
    Given operation "CreateOrgGroup" enabled
    And new "CreateOrgGroup" request
    And body with value {"data": {"attributes": {"name": "My Org Group"}, "type": "org_groups"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/org-management
  Scenario: Delete an org group policy override returns "Bad Request" response
    Given operation "DeleteOrgGroupPolicyOverride" enabled
    And new "DeleteOrgGroupPolicyOverride" request
    And request contains "org_group_policy_override_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/org-management
  Scenario: Delete an org group policy override returns "No Content" response
    Given operation "DeleteOrgGroupPolicyOverride" enabled
    And new "DeleteOrgGroupPolicyOverride" request
    And request contains "org_group_policy_override_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/org-management
  Scenario: Delete an org group policy override returns "Not Found" response
    Given operation "DeleteOrgGroupPolicyOverride" enabled
    And new "DeleteOrgGroupPolicyOverride" request
    And request contains "org_group_policy_override_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/org-management
  Scenario: Delete an org group policy returns "Bad Request" response
    Given operation "DeleteOrgGroupPolicy" enabled
    And new "DeleteOrgGroupPolicy" request
    And request contains "org_group_policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/org-management
  Scenario: Delete an org group policy returns "No Content" response
    Given operation "DeleteOrgGroupPolicy" enabled
    And new "DeleteOrgGroupPolicy" request
    And request contains "org_group_policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/org-management
  Scenario: Delete an org group policy returns "Not Found" response
    Given operation "DeleteOrgGroupPolicy" enabled
    And new "DeleteOrgGroupPolicy" request
    And request contains "org_group_policy_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/org-management
  Scenario: Delete an org group returns "Bad Request" response
    Given operation "DeleteOrgGroup" enabled
    And new "DeleteOrgGroup" request
    And request contains "org_group_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/org-management
  Scenario: Delete an org group returns "No Content" response
    Given operation "DeleteOrgGroup" enabled
    And new "DeleteOrgGroup" request
    And request contains "org_group_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/org-management
  Scenario: Delete an org group returns "Not Found" response
    Given operation "DeleteOrgGroup" enabled
    And new "DeleteOrgGroup" request
    And request contains "org_group_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/org-management
  Scenario: Get an org group membership returns "Bad Request" response
    Given operation "GetOrgGroupMembership" enabled
    And new "GetOrgGroupMembership" request
    And request contains "org_group_membership_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/org-management
  Scenario: Get an org group membership returns "Not Found" response
    Given operation "GetOrgGroupMembership" enabled
    And new "GetOrgGroupMembership" request
    And request contains "org_group_membership_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/org-management
  Scenario: Get an org group membership returns "OK" response
    Given operation "GetOrgGroupMembership" enabled
    And new "GetOrgGroupMembership" request
    And request contains "org_group_membership_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/org-management
  Scenario: Get an org group returns "Bad Request" response
    Given operation "GetOrgGroup" enabled
    And new "GetOrgGroup" request
    And request contains "org_group_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/org-management
  Scenario: Get an org group returns "Not Found" response
    Given operation "GetOrgGroup" enabled
    And new "GetOrgGroup" request
    And request contains "org_group_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/org-management
  Scenario: Get an org group returns "OK" response
    Given operation "GetOrgGroup" enabled
    And new "GetOrgGroup" request
    And request contains "org_group_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/org-management
  Scenario: List org group memberships returns "Bad Request" response
    Given operation "ListOrgGroupMemberships" enabled
    And new "ListOrgGroupMemberships" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/org-management
  Scenario: List org group memberships returns "OK" response
    Given operation "ListOrgGroupMemberships" enabled
    And new "ListOrgGroupMemberships" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/org-management
  Scenario: List org group policies returns "Bad Request" response
    Given operation "ListOrgGroupPolicies" enabled
    And new "ListOrgGroupPolicies" request
    And request contains "filter[org_group_id]" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/org-management
  Scenario: List org group policies returns "OK" response
    Given operation "ListOrgGroupPolicies" enabled
    And new "ListOrgGroupPolicies" request
    And request contains "filter[org_group_id]" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/org-management
  Scenario: List org group policy configs returns "OK" response
    Given operation "ListOrgGroupPolicyConfigs" enabled
    And new "ListOrgGroupPolicyConfigs" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/org-management
  Scenario: List org group policy overrides returns "Bad Request" response
    Given operation "ListOrgGroupPolicyOverrides" enabled
    And new "ListOrgGroupPolicyOverrides" request
    And request contains "filter[org_group_id]" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/org-management
  Scenario: List org group policy overrides returns "OK" response
    Given operation "ListOrgGroupPolicyOverrides" enabled
    And new "ListOrgGroupPolicyOverrides" request
    And request contains "filter[org_group_id]" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/org-management
  Scenario: List org groups returns "Bad Request" response
    Given operation "ListOrgGroups" enabled
    And new "ListOrgGroups" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/org-management
  Scenario: List org groups returns "OK" response
    Given operation "ListOrgGroups" enabled
    And new "ListOrgGroups" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/org-management
  Scenario: Update an org group membership returns "Bad Request" response
    Given operation "UpdateOrgGroupMembership" enabled
    And new "UpdateOrgGroupMembership" request
    And request contains "org_group_membership_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "f1e2d3c4-b5a6-7890-1234-567890abcdef", "relationships": {"org_group": {"data": {"id": "a1b2c3d4-e5f6-7890-abcd-ef0123456789", "type": "org_groups"}}}, "type": "org_group_memberships"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/org-management
  Scenario: Update an org group membership returns "Not Found" response
    Given operation "UpdateOrgGroupMembership" enabled
    And new "UpdateOrgGroupMembership" request
    And request contains "org_group_membership_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "f1e2d3c4-b5a6-7890-1234-567890abcdef", "relationships": {"org_group": {"data": {"id": "a1b2c3d4-e5f6-7890-abcd-ef0123456789", "type": "org_groups"}}}, "type": "org_group_memberships"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/org-management
  Scenario: Update an org group membership returns "OK" response
    Given operation "UpdateOrgGroupMembership" enabled
    And new "UpdateOrgGroupMembership" request
    And request contains "org_group_membership_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "f1e2d3c4-b5a6-7890-1234-567890abcdef", "relationships": {"org_group": {"data": {"id": "a1b2c3d4-e5f6-7890-abcd-ef0123456789", "type": "org_groups"}}}, "type": "org_group_memberships"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/org-management
  Scenario: Update an org group policy override returns "Bad Request" response
    Given operation "UpdateOrgGroupPolicyOverride" enabled
    And new "UpdateOrgGroupPolicyOverride" request
    And request contains "org_group_policy_override_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"org_site": "datadoghq.com", "org_uuid": "c3d4e5f6-a7b8-9012-cdef-012345678901"}, "id": "9f8e7d6c-5b4a-3210-fedc-ba0987654321", "type": "org_group_policy_overrides"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/org-management
  Scenario: Update an org group policy override returns "Not Found" response
    Given operation "UpdateOrgGroupPolicyOverride" enabled
    And new "UpdateOrgGroupPolicyOverride" request
    And request contains "org_group_policy_override_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"org_site": "datadoghq.com", "org_uuid": "c3d4e5f6-a7b8-9012-cdef-012345678901"}, "id": "9f8e7d6c-5b4a-3210-fedc-ba0987654321", "type": "org_group_policy_overrides"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/org-management
  Scenario: Update an org group policy override returns "OK" response
    Given operation "UpdateOrgGroupPolicyOverride" enabled
    And new "UpdateOrgGroupPolicyOverride" request
    And request contains "org_group_policy_override_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"org_site": "datadoghq.com", "org_uuid": "c3d4e5f6-a7b8-9012-cdef-012345678901"}, "id": "9f8e7d6c-5b4a-3210-fedc-ba0987654321", "type": "org_group_policy_overrides"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/org-management
  Scenario: Update an org group policy returns "Bad Request" response
    Given operation "UpdateOrgGroupPolicy" enabled
    And new "UpdateOrgGroupPolicy" request
    And request contains "org_group_policy_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"content": {"value": "UTC"}}, "id": "1a2b3c4d-5e6f-7890-abcd-ef0123456789", "type": "org_group_policies"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/org-management
  Scenario: Update an org group policy returns "Not Found" response
    Given operation "UpdateOrgGroupPolicy" enabled
    And new "UpdateOrgGroupPolicy" request
    And request contains "org_group_policy_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"content": {"value": "UTC"}}, "id": "1a2b3c4d-5e6f-7890-abcd-ef0123456789", "type": "org_group_policies"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/org-management
  Scenario: Update an org group policy returns "OK" response
    Given operation "UpdateOrgGroupPolicy" enabled
    And new "UpdateOrgGroupPolicy" request
    And request contains "org_group_policy_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"content": {"value": "UTC"}}, "id": "1a2b3c4d-5e6f-7890-abcd-ef0123456789", "type": "org_group_policies"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/org-management
  Scenario: Update an org group returns "Bad Request" response
    Given operation "UpdateOrgGroup" enabled
    And new "UpdateOrgGroup" request
    And request contains "org_group_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Updated Org Group Name"}, "id": "a1b2c3d4-e5f6-7890-abcd-ef0123456789", "type": "org_groups"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/org-management
  Scenario: Update an org group returns "Not Found" response
    Given operation "UpdateOrgGroup" enabled
    And new "UpdateOrgGroup" request
    And request contains "org_group_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Updated Org Group Name"}, "id": "a1b2c3d4-e5f6-7890-abcd-ef0123456789", "type": "org_groups"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/org-management
  Scenario: Update an org group returns "OK" response
    Given operation "UpdateOrgGroup" enabled
    And new "UpdateOrgGroup" request
    And request contains "org_group_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Updated Org Group Name"}, "id": "a1b2c3d4-e5f6-7890-abcd-ef0123456789", "type": "org_groups"}}
    When the request is sent
    Then the response status is 200 OK
