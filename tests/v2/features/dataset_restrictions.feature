@endpoint(dataset-restrictions) @endpoint(dataset-restrictions-v2)
Feature: Dataset Restrictions
  Configure dataset-level access restrictions per Datadog product type.
  Dataset restrictions control whether data is visible by default or hidden
  until explicitly granted, and how ownership-based access is determined.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "DatasetRestrictions" API

  @generated @skip @team:DataDog/access-enforcement
  Scenario: List dataset restrictions returns "Not Found" response
    Given operation "ListDatasetRestrictions" enabled
    And new "ListDatasetRestrictions" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/access-enforcement
  Scenario: List dataset restrictions returns "OK" response
    Given operation "ListDatasetRestrictions" enabled
    And new "ListDatasetRestrictions" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/access-enforcement
  Scenario: Update a dataset restriction returns "Bad Request" response
    Given operation "UpdateDatasetRestriction" enabled
    And new "UpdateDatasetRestriction" request
    And request contains "product_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"ownership_mode": "team_tag_based", "restriction_mode": "default_hide", "unrestricted_principals": []}, "type": "dataset_restrictions"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/access-enforcement
  Scenario: Update a dataset restriction returns "Not Found" response
    Given operation "UpdateDatasetRestriction" enabled
    And new "UpdateDatasetRestriction" request
    And request contains "product_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"ownership_mode": "team_tag_based", "restriction_mode": "default_hide", "unrestricted_principals": []}, "type": "dataset_restrictions"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/access-enforcement
  Scenario: Update a dataset restriction returns "OK" response
    Given operation "UpdateDatasetRestriction" enabled
    And new "UpdateDatasetRestriction" request
    And request contains "product_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"ownership_mode": "team_tag_based", "restriction_mode": "default_hide", "unrestricted_principals": []}, "type": "dataset_restrictions"}}
    When the request is sent
    Then the response status is 200 OK
