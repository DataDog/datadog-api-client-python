@endpoint(annotations) @endpoint(annotations-v2)
Feature: Annotations
  Add annotations to dashboards and notebooks to mark events such as
  deployments, incidents, or other notable moments in time.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Annotations" API

  @generated @skip @team:DataDog/dataviz-advanced-analytics
  Scenario: Create an annotation returns "Bad Request" response
    Given operation "CreateAnnotation" enabled
    And new "CreateAnnotation" request
    And body with value {"data": {"attributes": {"color": "blue", "description": "Deployed v2.3.1 to production.", "end_time": 1704070800000, "page_id": "dashboard:abc-def-xyz", "start_time": 1704067200000, "type": "pointInTime", "widget_ids": ["1234567890"]}, "type": "annotation"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/dataviz-advanced-analytics
  Scenario: Create an annotation returns "OK" response
    Given operation "CreateAnnotation" enabled
    And new "CreateAnnotation" request
    And body with value {"data": {"attributes": {"color": "blue", "description": "Deployed v2.3.1 to production.", "page_id": "dashboard:abc-def-xyz", "start_time": 1704067200000, "type": "pointInTime", "widget_ids": ["1234567890"]}, "type": "annotation"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dataviz-advanced-analytics
  Scenario: Delete an annotation returns "Bad Request" response
    Given operation "DeleteAnnotation" enabled
    And new "DeleteAnnotation" request
    And request contains "annotation_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/dataviz-advanced-analytics
  Scenario: Delete an annotation returns "No Content" response
    Given operation "DeleteAnnotation" enabled
    And there is a valid "annotation" in the system
    And new "DeleteAnnotation" request
    And request contains "annotation_id" parameter from "annotation.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/dataviz-advanced-analytics
  Scenario: Get annotations for a page returns "Bad Request" response
    Given operation "GetPageAnnotations" enabled
    And new "GetPageAnnotations" request
    And request contains "page_id" parameter from "REPLACE.ME"
    And request contains "start_time" parameter from "REPLACE.ME"
    And request contains "end_time" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/dataviz-advanced-analytics
  Scenario: Get annotations for a page returns "OK" response
    Given there is a valid "annotation" in the system
    And operation "GetPageAnnotations" enabled
    And new "GetPageAnnotations" request
    And request contains "page_id" parameter from "annotation.data.attributes.page_id"
    And request contains "start_time" parameter with value 1704067200000
    And request contains "end_time" parameter with value 1704153600000
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dataviz-advanced-analytics
  Scenario: List annotations returns "Bad Request" response
    Given operation "ListAnnotations" enabled
    And new "ListAnnotations" request
    And request contains "page_id" parameter from "REPLACE.ME"
    And request contains "start_time" parameter from "REPLACE.ME"
    And request contains "end_time" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/dataviz-advanced-analytics
  Scenario: List annotations returns "OK" response
    Given there is a valid "annotation" in the system
    And operation "ListAnnotations" enabled
    And new "ListAnnotations" request
    And request contains "page_id" parameter from "annotation.data.attributes.page_id"
    And request contains "start_time" parameter with value 1704067200000
    And request contains "end_time" parameter with value 1704153600000
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dataviz-advanced-analytics
  Scenario: Update an annotation returns "Bad Request" response
    Given operation "UpdateAnnotation" enabled
    And new "UpdateAnnotation" request
    And request contains "annotation_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"color": "blue", "description": "Deployed v2.3.1 to production.", "end_time": 1704070800000, "page_id": "dashboard:abc-def-xyz", "start_time": 1704067200000, "type": "pointInTime", "widget_ids": ["1234567890"]}, "type": "annotation"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dataviz-advanced-analytics
  Scenario: Update an annotation returns "Not Found" response
    Given operation "UpdateAnnotation" enabled
    And new "UpdateAnnotation" request
    And request contains "annotation_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"color": "blue", "description": "Deployed v2.3.1 to production.", "end_time": 1704070800000, "page_id": "dashboard:abc-def-xyz", "start_time": 1704067200000, "type": "pointInTime", "widget_ids": ["1234567890"]}, "type": "annotation"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/dataviz-advanced-analytics
  Scenario: Update an annotation returns "OK" response
    Given there is a valid "annotation" in the system
    And operation "UpdateAnnotation" enabled
    And new "UpdateAnnotation" request
    And request contains "annotation_id" parameter from "annotation.data.id"
    And body with value {"data": {"attributes": {"color": "green", "description": "Updated annotation.", "page_id": "dashboard:abc-def-xyz", "start_time": 1704067200000, "type": "pointInTime"}, "type": "annotation"}}
    When the request is sent
    Then the response status is 200 OK
