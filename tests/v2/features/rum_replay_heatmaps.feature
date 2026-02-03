@endpoint(rum-replay-heatmaps) @endpoint(rum-replay-heatmaps-v2)
Feature: Rum Replay Heatmaps
  Manage heatmap snapshots for RUM replay sessions. Create, update, delete,
  and retrieve snapshots to visualize user interactions on specific views.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RumReplayHeatmaps" API

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: Create replay heatmap snapshot returns "Created" response
    Given new "CreateReplayHeatmapSnapshot" request
    And body with value {"data": {"attributes": {"application_id": "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb", "device_type": "desktop", "event_id": "11111111-2222-3333-4444-555555555555", "is_device_type_selected_by_user": false, "snapshot_name": "My Snapshot", "start": 0, "view_name": "/home"}, "type": "snapshots"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: Delete replay heatmap snapshot returns "No Content" response
    Given new "DeleteReplayHeatmapSnapshot" request
    And request contains "snapshot_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: List replay heatmap snapshots returns "OK" response
    Given new "ListReplayHeatmapSnapshots" request
    And request contains "filter[view_name]" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: Update replay heatmap snapshot returns "OK" response
    Given new "UpdateReplayHeatmapSnapshot" request
    And request contains "snapshot_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"event_id": "11111111-2222-3333-4444-555555555555", "is_device_type_selected_by_user": false, "start": 0}, "id": "00000000-0000-0000-0000-000000000001", "type": "snapshots"}}
    When the request is sent
    Then the response status is 200 OK
