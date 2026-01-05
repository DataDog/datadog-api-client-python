# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.product_analytics_server_side_event_item import ProductAnalyticsServerSideEventItem


class ProductAnalyticsApi:
    """
    Send server-side events to Product Analytics. Server-Side Events Ingestion allows you to collect custom events
    from any server-side source, and retains events for 15 months. Server-side events are helpful for understanding
    causes of a funnel drop-off which are external to the client-side (for example, payment processing error).
    See the `Product Analytics page <https://docs.datadoghq.com/product_analytics/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._submit_product_analytics_event_endpoint = _Endpoint(
            settings={
                "response_type": (dict,),
                "auth": ["apiKeyAuth"],
                "endpoint_path": "/api/v2/prodlytics",
                "operation_id": "submit_product_analytics_event",
                "http_method": "POST",
                "version": "v2",
                "servers": [
                    {
                        "url": "https://{subdomain}.{site}",
                        "variables": {
                            "site": {
                                "description": "The regional site for customers.",
                                "default_value": "datadoghq.com",
                                "enum_values": [
                                    "datadoghq.com",
                                    "us3.datadoghq.com",
                                    "us5.datadoghq.com",
                                    "ap1.datadoghq.com",
                                    "ap2.datadoghq.com",
                                    "datadoghq.eu",
                                ],
                            },
                            "subdomain": {
                                "description": "The subdomain where the API is deployed.",
                                "default_value": "browser-intake",
                            },
                        },
                    },
                    {
                        "url": "{protocol}://{name}",
                        "variables": {
                            "name": {
                                "description": "Full site DNS name.",
                                "default_value": "browser-intake-datadoghq.com",
                            },
                            "protocol": {
                                "description": "The protocol for accessing the API.",
                                "default_value": "https",
                            },
                        },
                    },
                    {
                        "url": "https://{subdomain}.{site}",
                        "variables": {
                            "site": {
                                "description": "Any Datadog deployment.",
                                "default_value": "datadoghq.com",
                            },
                            "subdomain": {
                                "description": "The subdomain where the API is deployed.",
                                "default_value": "browser-intake",
                            },
                        },
                    },
                ],
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ProductAnalyticsServerSideEventItem,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def submit_product_analytics_event(
        self,
        body: ProductAnalyticsServerSideEventItem,
    ) -> dict:
        """Send server-side events.

        Send server-side events to Product Analytics. Server-side events are retained for 15 months.

        Server-Side events in Product Analytics are helpful for tracking events that occur on the server,
        as opposed to client-side events, which are captured by Real User Monitoring (RUM) SDKs.
        This allows for a more comprehensive view of the user journey by including actions that happen on the server.
        Typical examples could be ``checkout.completed`` or ``payment.processed``.

        Ingested server-side events are integrated into Product Analytics to allow users to select and filter
        these events in the event picker, similar to how views or actions are handled.

        **Requirements:**

        * At least one of ``usr`` , ``account`` , or ``session`` must be provided with a valid ID.
        * The ``application.id`` must reference a Product Analytics-enabled application.

        **Custom Attributes:**
        Any additional fields in the payload are flattened and searchable as facets.
        For example, a payload with ``{"customer": {"tier": "premium"}}`` is searchable with
        the syntax ``@customer.tier:premium`` in Datadog.

        The status codes answered by the HTTP API are:

        * 202: Accepted: The request has been accepted for processing
        * 400: Bad request (likely an issue in the payload formatting)
        * 401: Unauthorized (likely a missing API Key)
        * 403: Permission issue (likely using an invalid API Key)
        * 408: Request Timeout, request should be retried after some time
        * 413: Payload too large (batch is above 5MB uncompressed)
        * 429: Too Many Requests, request should be retried after some time
        * 500: Internal Server Error, the server encountered an unexpected condition that prevented it from fulfilling the request, request should be retried after some time
        * 503: Service Unavailable, the server is not ready to handle the request probably because it is overloaded, request should be retried after some time

        :param body: Server-side event to send (JSON format).
        :type body: ProductAnalyticsServerSideEventItem
        :rtype: dict
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._submit_product_analytics_event_endpoint.call_with_http_info(**kwargs)
