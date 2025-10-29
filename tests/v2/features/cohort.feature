@endpoint(cohort) @endpoint(cohort-v2)
Feature: Cohort
  API for Cohort.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Cohort" API

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Get rum cohort returns "Successful response with cohort analysis data" response
    Given operation "GetRumCohort" enabled
    And new "GetRumCohort" request
    And body with value {"data": {"attributes": {"definition": {"audience_filters": {"accounts": [{"name": ""}], "segments": [{"name": "", "segment_id": ""}], "users": [{"name": ""}]}}, "time": {}}, "type": "cohort_request"}}
    When the request is sent
    Then the response status is 200 Successful response with cohort analysis data

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Get rum cohort users returns "Successful response with cohort users" response
    Given operation "GetRumCohortUsers" enabled
    And new "GetRumCohortUsers" request
    And body with value {"data": {"attributes": {"definition": {"audience_filters": {"accounts": [{"name": ""}], "segments": [{"name": "", "segment_id": ""}], "users": [{"name": ""}]}}, "time": {}}, "type": "cohort_users_request"}}
    When the request is sent
    Then the response status is 200 Successful response with cohort users
