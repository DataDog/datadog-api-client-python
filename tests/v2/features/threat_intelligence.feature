@endpoint(threat-intelligence) @endpoint(threat-intelligence-v2)
Feature: Threat Intelligence
  Ingest and manage threat intelligence data for security enrichment and
  investigation.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ThreatIntelligence" API
    And operation "AddSTIXThreatIntel" enabled
    And new "AddSTIXThreatIntel" request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Ingest STIX threat intelligence returns "Bad Request" response
    Given body with value {"id": "bundle--11111111-1111-4111-8111-111111111111", "objects": [{"created": "2026-07-22T12:00:00Z", "id": "indicator--22222222-2222-4222-8222-222222222222", "modified": "2026-07-22T12:00:00Z", "pattern": "[ipv4-addr:value = '198.51.100.42']", "pattern_type": "stix", "spec_version": "2.1", "type": "indicator", "valid_from": "2026-07-22T12:00:00Z"}], "spec_version": "2.1", "type": "bundle"}
    And request contains "ti_vendor" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @skip-validation @team:DataDog/cloud-siem
  Scenario: Ingest STIX threat intelligence returns "OK" response
    Given request contains "ti_vendor" parameter with value "Acme-Inc"
    And body with value {"id": "bundle--44444444-4444-4444-8444-444444444444", "objects": [{"created": "2026-07-22T12:00:00Z", "id": "indicator--55555555-5555-4555-8555-555555555555", "modified": "2026-07-22T12:00:00Z", "pattern": "[ipv4-addr:value = '198.51.100.42']", "pattern_type": "stix", "spec_version": "2.1", "type": "indicator", "valid_from": "2026-07-22T12:00:00Z"}], "spec_version": "2.1", "type": "bundle"}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "threat-intel-stix-ingest"
    And the response "data.id" is equal to "acme_inc"
    And the response "data.attributes.accepted" is equal to 1
    And the response "data.attributes.unsupported" is equal to 0
    And the response "data.attributes.invalid" is equal to 0

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Ingest STIX threat intelligence returns "The request body exceeds 50 MB as received or 100 MB after decompression." response
    Given body with value {"id": "bundle--11111111-1111-4111-8111-111111111111", "objects": [{"created": "2026-07-22T12:00:00Z", "id": "indicator--22222222-2222-4222-8222-222222222222", "modified": "2026-07-22T12:00:00Z", "pattern": "[ipv4-addr:value = '198.51.100.42']", "pattern_type": "stix", "spec_version": "2.1", "type": "indicator", "valid_from": "2026-07-22T12:00:00Z"}], "spec_version": "2.1", "type": "bundle"}
    And request contains "ti_vendor" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 413 The request body exceeds 50 MB as received or 100 MB after decompression.
