@endpoint(rum-replay-playlists) @endpoint(rum-replay-playlists-v2)
Feature: RUM Replay Playlists
  Create and manage playlists of RUM replay sessions. Organize, categorize,
  and share collections of replay sessions for analysis and collaboration.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RUMReplayPlaylists" API

  @generated @skip @team:ddoghq/session-replay
  Scenario: Add RUM replay session to playlist returns "Created" response
    Given new "AddRUMReplaySessionToPlaylist" request
    And request contains "ts" parameter from "REPLACE.ME"
    And request contains "playlist_id" parameter from "REPLACE.ME"
    And request contains "session_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/session-replay
  Scenario: Add RUM replay session to playlist returns "OK" response
    Given new "AddRUMReplaySessionToPlaylist" request
    And request contains "ts" parameter from "REPLACE.ME"
    And request contains "playlist_id" parameter from "REPLACE.ME"
    And request contains "session_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/session-replay
  Scenario: Bulk remove RUM replay playlist sessions returns "No Content" response
    Given new "BulkRemoveRUMReplayPlaylistSessions" request
    And request contains "playlist_id" parameter from "REPLACE.ME"
    And body with value {"data": [{"id": "00000000-0000-0000-0000-000000000001", "type": "rum_replay_session"}]}
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/session-replay
  Scenario: Create RUM replay playlist returns "Created" response
    Given new "CreateRUMReplayPlaylist" request
    And body with value {"data": {"attributes": {"created_by": {"handle": "john.doe@example.com", "id": "00000000-0000-0000-0000-000000000001", "uuid": "00000000-0000-0000-0000-000000000001"}, "name": "My Playlist"}, "type": "rum_replay_playlist"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/session-replay
  Scenario: Delete RUM replay playlist returns "No Content" response
    Given new "DeleteRUMReplayPlaylist" request
    And request contains "playlist_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/session-replay
  Scenario: Get RUM replay playlist returns "OK" response
    Given new "GetRUMReplayPlaylist" request
    And request contains "playlist_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/session-replay
  Scenario: List RUM replay playlist sessions returns "OK" response
    Given new "ListRUMReplayPlaylistSessions" request
    And request contains "playlist_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/session-replay
  Scenario: List RUM replay playlists returns "OK" response
    Given new "ListRUMReplayPlaylists" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/session-replay
  Scenario: Remove RUM replay session from playlist returns "No Content" response
    Given new "RemoveRUMReplaySessionFromPlaylist" request
    And request contains "playlist_id" parameter from "REPLACE.ME"
    And request contains "session_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/session-replay
  Scenario: Update RUM replay playlist returns "OK" response
    Given new "UpdateRUMReplayPlaylist" request
    And request contains "playlist_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"created_by": {"handle": "john.doe@example.com", "id": "00000000-0000-0000-0000-000000000001", "uuid": "00000000-0000-0000-0000-000000000001"}, "name": "My Playlist"}, "type": "rum_replay_playlist"}}
    When the request is sent
    Then the response status is 200 OK
