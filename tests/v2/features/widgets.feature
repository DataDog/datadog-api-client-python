@endpoint(widgets) @endpoint(widgets-v2)
Feature: Widgets
  Auto-generated tag Widgets

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Widgets" API

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Create a widget returns "Successful Response" response
    Given new "CreateWidgetApiV2WidgetsExperienceTypePost" request
    And request contains "experience_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"definition": {"requests": [{"queries": [{"data_source": "metrics", "name": "query1", "query": "avg:system.cpu.user{*}"}], "response_format": "timeseries"}], "time": {"type": "live", "unit": "day", "value": 30}, "title": "My Timeseries Widget", "type": "timeseries"}, "tags": []}, "id": null, "lid": null, "links": {"describedBy": null, "first": null, "last": null, "next": null, "prev": null, "related": null, "self": null}, "meta": null, "relationships": null, "type": ""}, "errors": [{"code": null, "detail": null, "id": null, "links": {"about": ""}, "meta": null, "source": {"header": null, "parameter": null, "pointer": null}, "status": null, "title": null}], "included": [{"attributes": null, "id": "", "links": {"describedBy": null, "first": null, "last": null, "next": null, "prev": null, "related": null, "self": null}, "meta": null, "relationships": null, "type": ""}], "links": {"describedBy": null, "first": null, "last": null, "next": null, "prev": null, "related": null, "self": null}, "meta": null}
    When the request is sent
    Then the response status is 200 Successful Response

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Delete a widget returns "Successful Response" response
    Given new "DeleteWidgetApiV2WidgetsExperienceTypeUuidDelete" request
    And request contains "uuid" parameter from "REPLACE.ME"
    And request contains "experience_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 Successful Response

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Get a widget returns "Successful Response" response
    Given new "GetWidgetApiV2WidgetsExperienceTypeUuidGet" request
    And request contains "uuid" parameter from "REPLACE.ME"
    And request contains "experience_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 Successful Response

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Search widgets returns "Successful Response" response
    Given new "SearchWidgetsApiV2WidgetsExperienceTypeGet" request
    And request contains "experience_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 Successful Response

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: Update a widget returns "Successful Response" response
    Given new "UpdateWidgetApiV2WidgetsExperienceTypeUuidPut" request
    And request contains "uuid" parameter from "REPLACE.ME"
    And request contains "experience_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"definition": {"requests": [{"queries": [{"data_source": "metrics", "name": "query1", "query": "avg:system.cpu.user{*}"}], "response_format": "timeseries"}], "time": {"type": "live", "unit": "day", "value": 30}, "title": "My Timeseries Widget", "type": "timeseries"}, "tags": []}, "id": null, "lid": null, "links": {"describedBy": null, "first": null, "last": null, "next": null, "prev": null, "related": null, "self": null}, "meta": null, "relationships": null, "type": ""}, "errors": [{"code": null, "detail": null, "id": null, "links": {"about": ""}, "meta": null, "source": {"header": null, "parameter": null, "pointer": null}, "status": null, "title": null}], "included": [{"attributes": null, "id": "", "links": {"describedBy": null, "first": null, "last": null, "next": null, "prev": null, "related": null, "self": null}, "meta": null, "relationships": null, "type": ""}], "links": {"describedBy": null, "first": null, "last": null, "next": null, "prev": null, "related": null, "self": null}, "meta": null}
    When the request is sent
    Then the response status is 200 Successful Response
