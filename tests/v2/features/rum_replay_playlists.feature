@endpoint(rum-replay-playlists) @endpoint(rum-replay-playlists-v2)
Feature: Rum Replay Playlists
  Create and manage playlists of RUM replay sessions. Organize, categorize,
  and share collections of replay sessions for analysis and collaboration.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RumReplayPlaylists" API

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: Add rum replay session to playlist returns "Created" response
    Given new "AddRumReplaySessionToPlaylist" request
    And request contains "ts" parameter from "REPLACE.ME"
    And request contains "playlist_id" parameter from "REPLACE.ME"
    And request contains "session_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: Add rum replay session to playlist returns "OK" response
    Given new "AddRumReplaySessionToPlaylist" request
    And request contains "ts" parameter from "REPLACE.ME"
    And request contains "playlist_id" parameter from "REPLACE.ME"
    And request contains "session_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: Bulk remove rum replay playlist sessions returns "No Content" response
    Given new "BulkRemoveRumReplayPlaylistSessions" request
    And request contains "playlist_id" parameter from "REPLACE.ME"
    And body with value {"data": [{"id": "00000000-0000-0000-0000-000000000001", "type": "rum_replay_session"}]}
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: Create rum replay playlist returns "Created" response
    Given new "CreateRumReplayPlaylist" request
    And body with value {"data": {"attributes": {"created_by": {"handle": "john.doe@example.com", "id": "00000000-0000-0000-0000-000000000001", "uuid": "00000000-0000-0000-0000-000000000001"}, "name": "My Playlist"}, "type": "rum_replay_playlist"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: Delete rum replay playlist returns "No Content" response
    Given new "DeleteRumReplayPlaylist" request
    And request contains "playlist_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: Get rum replay playlist returns "OK" response
    Given new "GetRumReplayPlaylist" request
    And request contains "playlist_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: List rum replay playlist sessions returns "OK" response
    Given new "ListRumReplayPlaylistSessions" request
    And request contains "playlist_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: List rum replay playlists returns "OK" response
    Given new "ListRumReplayPlaylists" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: Remove rum replay session from playlist returns "No Content" response
    Given new "RemoveRumReplaySessionFromPlaylist" request
    And request contains "playlist_id" parameter from "REPLACE.ME"
    And request contains "session_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/product-analytics-backend @team:DataDog/rum-backend @team:DataDog/session-replay-backend
  Scenario: Update rum replay playlist returns "OK" response
    Given new "UpdateRumReplayPlaylist" request
    And request contains "playlist_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"created_by": {"handle": "john.doe@example.com", "id": "00000000-0000-0000-0000-000000000001", "uuid": "00000000-0000-0000-0000-000000000001"}, "name": "My Playlist"}, "type": "rum_replay_playlist"}}
    When the request is sent
    Then the response status is 200 OK
