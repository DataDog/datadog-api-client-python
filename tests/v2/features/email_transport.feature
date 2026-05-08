@endpoint(email-transport) @endpoint(email-transport-v2)
Feature: Email Transport
  Endpoints for receiving email transport webhook events for audit trail
  processing.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "EmailTransport" API
    And operation "CreateEmailTransportWebhookIntake" enabled
    And new "CreateEmailTransportWebhookIntake" request
    And body with value [{"attributes": {"category": ["transactional"], "email": {"address": "user@example.com", "domain": "example.com", "subject": "[Monitor Alert] CPU usage is high", "type": ["transactional"]}, "email_id": "abc123-def456", "email_type_display_name": "Monitor Alert", "message": {"auth": {"delivered_with_tls": "TLSv1.2"}, "custom_args": {"email_id": "abc123-def456", "email_type_display_name": "Monitor Alert", "org_uuid": "8dee7c38-00cb-11ea-a77b-8b5a08d3b091", "queue_time": "2024-01-15T10:29:00Z", "subject": "[Monitor Alert] CPU usage is high"}, "id": {"message_id": "<message-id@example.com>", "smtp_id": "<abc123@mail.example.com>", "transport_event_id": "evt_abc123"}, "name": "delivered", "response": {"enhanced_smtp_code": "2.0.0", "reason": "250 2.0.0 OK", "smtp_code": "250"}, "sender_ip": "192.168.1.1", "timestamp": {"event_timestamp": 1705312200.0, "lifetime": 3.2, "queue_time": 1.5, "scheduled_time": 1705312190.0}}, "network": {"ip": {"attributes": [{"ip": "192.168.1.1", "source": ["sendgrid"]}], "list": ["192.168.1.1"]}}, "org": 1234, "org_metadata": {}, "org_uuid": "8dee7c38-00cb-11ea-a77b-8b5a08d3b091", "queue_time": "2024-01-15T10:29:00Z", "subject": "[Monitor Alert] CPU usage is high", "useragent": "Mozilla/5.0"}, "date": "2024-01-15T10:30:00Z", "log_id": "AQAAAZPHnBT0TwJAdgAAAABBWlBIblVlNEFBQ0dFMmVkYTFDSnRR", "source": "sendgrid", "status": "info", "tags": ["env:production"]}]

  @generated @skip @team:DataDog/dogmail
  Scenario: Ingest email transport webhook events returns "Bad Request" response
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dogmail
  Scenario: Ingest email transport webhook events returns "No Content" response
    When the request is sent
    Then the response status is 204 No Content
