@endpoint(spa) @endpoint(spa-v2)
Feature: Spa
  SPA (Spark Pod Autosizing) API. Provides resource recommendations and cost
  insights to help optimize Spark job configurations.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Spa" API
    And operation "GetSPARecommendations" enabled
    And new "GetSPARecommendations" request

  @generated @skip @team:DataDog/data-and-analytics-processing
  Scenario: Get SPA Recommendations returns "Bad Request" response
    Given request contains "shard" parameter from "REPLACE.ME"
    And request contains "service" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/data-and-analytics-processing
  Scenario: Get SPA Recommendations returns "OK" response
    Given request contains "shard" parameter from "REPLACE.ME"
    And request contains "service" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/data-and-analytics-processing
  Scenario: GetSPARecommendations returns a JSON:API Recommendation with driver and executor estimations
    Given request contains "service" parameter with value "dedupeactivecontexts"
    And request contains "shard" parameter with value "adp_dedupeactivecontexts_org2"
    When the request is sent
    Then the response status is 404 Not Found
    And the response "data.type" is equal to "recommendation"
    And the response "data" has field "attributes"
    And the response "data.attributes" has field "driver"
    And the response "data.attributes" has field "executor"
    And the response "data.attributes.driver" has field "estimation"
    And the response "data.attributes.driver.estimation" has field "cpu"
    And the response "data.attributes.driver.estimation" has field "memory"
    And the response "data.attributes.driver.estimation" has field "ephemeral_storage"
    And the response "data.attributes.driver.estimation" has field "heap"
    And the response "data.attributes.driver.estimation" has field "overhead"
    And the response "data.attributes.driver.estimation.cpu" has field "max"
    And the response "data.attributes.driver.estimation.cpu" has field "p95"
    And the response "data.attributes.driver.estimation.cpu" has field "p75"
    And the response "data.attributes.executor" has field "estimation"
    And the response "data.attributes.executor.estimation" has field "cpu"
    And the response "data.attributes.executor.estimation" has field "memory"
    And the response "data.attributes.executor.estimation" has field "ephemeral_storage"
    And the response "data.attributes.executor.estimation" has field "heap"
    And the response "data.attributes.executor.estimation" has field "overhead"
    And the response "data.attributes.executor.estimation.cpu" has field "max"
    And the response "data.attributes.executor.estimation.cpu" has field "p95"
    And the response "data.attributes.executor.estimation.cpu" has field "p75"
