# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.transport_webhook_log import TransportWebhookLog


class EmailTransportApi:
    """
    Endpoints for receiving email transport webhook events for audit trail processing.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_email_transport_webhook_intake_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/email/transport/webhook_intake",
                "operation_id": "create_email_transport_webhook_intake",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": ([TransportWebhookLog],),
                    "location": "body",
                    "collection_format": "multi",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_email_transport_webhook_intake(
        self,
        body: List[TransportWebhookLog],
    ) -> None:
        """Ingest email transport webhook events.

        Receives a batch of email transport webhook log events and emits an audit trail entry
        for each event with a final delivery status (delivered, dropped, or bounced).
        Only authorized organizations can submit events.

        :type body: [TransportWebhookLog]
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_email_transport_webhook_intake_endpoint.call_with_http_info(**kwargs)
