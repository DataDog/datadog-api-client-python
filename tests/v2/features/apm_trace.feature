@endpoint(apm-trace) @endpoint(apm-trace-v2)
Feature: APM Trace
  Retrieve full or pruned APM traces by trace ID.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "APMTrace" API

  @generated @skip @team:DataDog/apm-reliability
  Scenario: Get a pruned trace by ID returns "Not Found" response
    Given operation "GetPrunedTraceByID" enabled
    And new "GetPrunedTraceByID" request
    And request contains "trace_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/apm-reliability
  Scenario: Get a pruned trace by ID returns "OK" response
    Given operation "GetPrunedTraceByID" enabled
    And new "GetPrunedTraceByID" request
    And request contains "trace_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/apm-reliability
  Scenario: Get a trace by ID returns "Not Found" response
    Given operation "GetTraceByID" enabled
    And new "GetTraceByID" request
    And request contains "trace_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/apm-reliability
  Scenario: Get a trace by ID returns "OK" response
    Given operation "GetTraceByID" enabled
    And new "GetTraceByID" request
    And request contains "trace_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/apm-reliability
  Scenario: Get a trace by ID returns "Payload Too Large" response
    Given operation "GetTraceByID" enabled
    And new "GetTraceByID" request
    And request contains "trace_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 413 Payload Too Large
