@endpoint(ip-allowlist) @endpoint(ip-allowlist-v2)
Feature: IP Allowlist
  The IP allowlist API is used to manage the IP addresses that can access
  the Datadog API and web UI. It does not block access to intake APIs or
  public dashboards.  This is an enterprise-only feature. Request access by
  contacting Datadog support.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "IPAllowlist" API

  @generated @skip @team:DataDog/aaa-core-access
  Scenario: Get IP Allowlist returns "Not Found" response
    Given new "GetIPAllowlist" request
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/aaa-core-access
  Scenario: Get IP Allowlist returns "OK" response
    Given the "ip_allowlist_nonempty_disabled" has two entries and is disabled
    And new "GetIPAllowlist" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "{{ ip_allowlist_nonempty_disabled.data.type }}"
    And the response "data.attributes.enabled" has the same value as "ip_allowlist_nonempty_disabled.data.attributes.enabled"
    And the response "data.attributes.entries" has length 2
    And the response "data.attributes.entries[0].data.attributes.note" has the same value as "ip_allowlist_nonempty_disabled.data.attributes.entries[0].data.attributes.note"
    And the response "data.attributes.entries[0].data.type" is equal to "{{ ip_allowlist_nonempty_disabled.data.attributes.entries[0].data.type }}"
    And the response "data.attributes.entries[1].data.attributes.note" has the same value as "ip_allowlist_nonempty_disabled.data.attributes.entries[1].data.attributes.note"
    And the response "data.attributes.entries[1].data.type" is equal to "{{ ip_allowlist_nonempty_disabled.data.attributes.entries[1].data.type }}"

  @team:DataDog/aaa-core-access
  Scenario: Update IP Allowlist returns "Bad Request" response
    Given new "UpdateIPAllowlist" request
    And body with value {"data": {"type": "ip_allowlist", "attributes": {"enabled": true, "entries": []}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-core-access
  Scenario: Update IP Allowlist returns "Not Found" response
    Given new "UpdateIPAllowlist" request
    And body with value {"data": {"attributes": {"entries": [{"data": {"attributes": {}, "type": "ip_allowlist_entry"}}]}, "type": "ip_allowlist"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/aaa-core-access
  Scenario: Update IP Allowlist returns "OK" response
    Given the "ip_allowlist_empty_disabled" has no entries and is disabled
    And new "UpdateIPAllowlist" request
    And body with value {"data": {"attributes": {"entries": [{"data": {"attributes": {"note": "{{ unique }}", "cidr_block": "127.0.0.1"}, "type": "ip_allowlist_entry"}}], "enabled": false}, "type": "ip_allowlist"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "ip_allowlist"
    And the response "data.attributes.entries" has length 1
    And the response "data.attributes.entries[0].data.attributes.note" is equal to "{{ unique }}"
    And the response "data.attributes.entries[0].data.attributes.cidr_block" is equal to "127.0.0.1/32"
    And the response "data.attributes.entries[0].data.type" is equal to "ip_allowlist_entry"
    And the response "data.attributes.enabled" is equal to false
