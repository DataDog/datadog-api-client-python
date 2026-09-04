@endpoint(timeseries-anomaly-investigations) @endpoint(timeseries-anomaly-investigations-v2)
Feature: Timeseries Anomaly Investigations
  Investigate metrics timeseries anomalies and return deterministic
  findings.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "TimeseriesAnomalyInvestigations" API
    And operation "CreateTimeseriesAnomalyInvestigation" enabled
    And new "CreateTimeseriesAnomalyInvestigation" request
    And body with value {"data": {"attributes": {"requests": [{"formulas": [{"formula": "anomalies(query1, 'agile', 3)"}], "from": 1754406000000, "queries": [{"data_source": "metrics", "name": "query1", "query": "avg:system.cpu.user{env:prod} by {service}"}], "to": 1754423940000}]}, "type": "timeseries_anomaly_investigation"}}

  @generated @skip @team:DataDog/dataviz-backend-maintainers
  Scenario: Investigate a timeseries anomaly returns "Bad Request" response
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dataviz-backend-maintainers
  Scenario: Investigate a timeseries anomaly returns "OK" response
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dataviz-backend-maintainers
  Scenario: Investigate a timeseries anomaly returns "Unprocessable Entity" response
    When the request is sent
    Then the response status is 422 Unprocessable Entity
