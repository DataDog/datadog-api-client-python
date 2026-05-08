"""
Ingest email transport webhook events returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.email_transport_api import EmailTransportApi
from datadog_api_client.v2.model.transport_webhook_log import TransportWebhookLog
from datadog_api_client.v2.model.transport_webhook_log_attributes import TransportWebhookLogAttributes
from datadog_api_client.v2.model.transport_webhook_log_email import TransportWebhookLogEmail
from datadog_api_client.v2.model.transport_webhook_log_ip_attribute import TransportWebhookLogIpAttribute
from datadog_api_client.v2.model.transport_webhook_log_message import TransportWebhookLogMessage
from datadog_api_client.v2.model.transport_webhook_log_message_auth import TransportWebhookLogMessageAuth
from datadog_api_client.v2.model.transport_webhook_log_message_custom_args import TransportWebhookLogMessageCustomArgs
from datadog_api_client.v2.model.transport_webhook_log_message_id import TransportWebhookLogMessageId
from datadog_api_client.v2.model.transport_webhook_log_message_response import TransportWebhookLogMessageResponse
from datadog_api_client.v2.model.transport_webhook_log_message_timestamp import TransportWebhookLogMessageTimestamp
from datadog_api_client.v2.model.transport_webhook_log_network import TransportWebhookLogNetwork
from datadog_api_client.v2.model.transport_webhook_log_network_ip import TransportWebhookLogNetworkIp
from datadog_api_client.v2.model.transport_webhook_log_org_metadata import TransportWebhookLogOrgMetadata
from datetime import datetime
from dateutil.tz import tzutc

body = [
    TransportWebhookLog(
        attributes=TransportWebhookLogAttributes(
            category=[
                "transactional",
            ],
            email=TransportWebhookLogEmail(
                address="user@example.com",
                domain="example.com",
                subject="[Monitor Alert] CPU usage is high",
                type=[
                    "transactional",
                ],
            ),
            email_id="abc123-def456",
            email_type_display_name="Monitor Alert",
            message=TransportWebhookLogMessage(
                auth=TransportWebhookLogMessageAuth(
                    delivered_with_tls="TLSv1.2",
                ),
                custom_args=TransportWebhookLogMessageCustomArgs(
                    email_id="abc123-def456",
                    email_type_display_name="Monitor Alert",
                    org_uuid="8dee7c38-00cb-11ea-a77b-8b5a08d3b091",
                    queue_time="2024-01-15T10:29:00Z",
                    subject="[Monitor Alert] CPU usage is high",
                ),
                id=TransportWebhookLogMessageId(
                    message_id="<message-id@example.com>",
                    smtp_id="<abc123@mail.example.com>",
                    transport_event_id="evt_abc123",
                ),
                name="delivered",
                response=TransportWebhookLogMessageResponse(
                    enhanced_smtp_code="2.0.0",
                    reason="250 2.0.0 OK",
                    smtp_code="250",
                ),
                sender_ip="192.168.1.1",
                timestamp=TransportWebhookLogMessageTimestamp(
                    event_timestamp=1705312200.0,
                    lifetime=3.2,
                    queue_time=1.5,
                    scheduled_time=1705312190.0,
                ),
            ),
            network=TransportWebhookLogNetwork(
                ip=TransportWebhookLogNetworkIp(
                    attributes=[
                        TransportWebhookLogIpAttribute(
                            ip="192.168.1.1",
                            source=[
                                "sendgrid",
                            ],
                        ),
                    ],
                    list=[
                        "192.168.1.1",
                    ],
                ),
            ),
            org=1234,
            org_metadata=TransportWebhookLogOrgMetadata(),
            org_uuid="8dee7c38-00cb-11ea-a77b-8b5a08d3b091",
            queue_time="2024-01-15T10:29:00Z",
            subject="[Monitor Alert] CPU usage is high",
            useragent="Mozilla/5.0",
        ),
        date=datetime(2024, 1, 15, 10, 30, tzinfo=tzutc()),
        log_id="AQAAAZPHnBT0TwJAdgAAAABBWlBIblVlNEFBQ0dFMmVkYTFDSnRR",
        source="sendgrid",
        status="info",
        tags=[
            "env:production",
        ],
    ),
]

configuration = Configuration()
configuration.unstable_operations["create_email_transport_webhook_intake"] = True
with ApiClient(configuration) as api_client:
    api_instance = EmailTransportApi(api_client)
    api_instance.create_email_transport_webhook_intake(body=body)
