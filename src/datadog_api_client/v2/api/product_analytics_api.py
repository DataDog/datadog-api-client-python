# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.product_analytics_server_side_event_item import ProductAnalyticsServerSideEventItem
from datadog_api_client.v2.model.product_analytics_analytics_list_response import ProductAnalyticsAnalyticsListResponse
from datadog_api_client.v2.model.product_analytics_analytics_list_request import ProductAnalyticsAnalyticsListRequest
from datadog_api_client.v2.model.product_analytics_scalar_response import ProductAnalyticsScalarResponse
from datadog_api_client.v2.model.product_analytics_analytics_request import ProductAnalyticsAnalyticsRequest
from datadog_api_client.v2.model.product_analytics_timeseries_response import ProductAnalyticsTimeseriesResponse
from datadog_api_client.v2.model.product_analytics_journey_funnel_response import ProductAnalyticsJourneyFunnelResponse
from datadog_api_client.v2.model.product_analytics_journey_funnel_request import ProductAnalyticsJourneyFunnelRequest
from datadog_api_client.v2.model.product_analytics_journey_list_response import ProductAnalyticsJourneyListResponse
from datadog_api_client.v2.model.product_analytics_journey_list_request import ProductAnalyticsJourneyListRequest
from datadog_api_client.v2.model.product_analytics_journey_scalar_response import ProductAnalyticsJourneyScalarResponse
from datadog_api_client.v2.model.product_analytics_journey_scalar_request import ProductAnalyticsJourneyScalarRequest
from datadog_api_client.v2.model.product_analytics_journey_timeseries_response import (
    ProductAnalyticsJourneyTimeseriesResponse,
)
from datadog_api_client.v2.model.product_analytics_formula_journey_request import ProductAnalyticsFormulaJourneyRequest
from datadog_api_client.v2.model.product_analytics_retention_grid_response import ProductAnalyticsRetentionGridResponse
from datadog_api_client.v2.model.product_analytics_retention_grid_request import ProductAnalyticsRetentionGridRequest
from datadog_api_client.v2.model.product_analytics_retention_list_response import ProductAnalyticsRetentionListResponse
from datadog_api_client.v2.model.product_analytics_retention_list_request import ProductAnalyticsRetentionListRequest
from datadog_api_client.v2.model.product_analytics_formula_retention_request import (
    ProductAnalyticsFormulaRetentionRequest,
)
from datadog_api_client.v2.model.product_analytics_sankey_response import ProductAnalyticsSankeyResponse
from datadog_api_client.v2.model.product_analytics_sankey_request import ProductAnalyticsSankeyRequest


class ProductAnalyticsApi:
    """
    Send server-side events to Product Analytics. Server-Side Events Ingestion allows you to collect custom events
    from any server-side source, and retains events for 15 months. Server-side events are helpful for understanding
    causes of a funnel drop-off which are external to the client-side (for example, payment processing error).

    **Note** : Sending server-side events impacts billing. Review the `pricing page <https://www.datadoghq.com/pricing/?product=product-analytics#products>`_
    and contact your Customer Success Manager for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._query_product_analytics_journey_funnel_endpoint = _Endpoint(
            settings={
                "response_type": (ProductAnalyticsJourneyFunnelResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/product-analytics/journey/funnel",
                "operation_id": "query_product_analytics_journey_funnel",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ProductAnalyticsJourneyFunnelRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._query_product_analytics_journey_list_endpoint = _Endpoint(
            settings={
                "response_type": (ProductAnalyticsJourneyListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/product-analytics/journey/list",
                "operation_id": "query_product_analytics_journey_list",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ProductAnalyticsJourneyListRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._query_product_analytics_journey_scalar_endpoint = _Endpoint(
            settings={
                "response_type": (ProductAnalyticsJourneyScalarResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/product-analytics/journey/scalar",
                "operation_id": "query_product_analytics_journey_scalar",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ProductAnalyticsJourneyScalarRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._query_product_analytics_journey_timeseries_endpoint = _Endpoint(
            settings={
                "response_type": (ProductAnalyticsJourneyTimeseriesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/product-analytics/journey/timeseries",
                "operation_id": "query_product_analytics_journey_timeseries",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ProductAnalyticsFormulaJourneyRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._query_product_analytics_list_endpoint = _Endpoint(
            settings={
                "response_type": (ProductAnalyticsAnalyticsListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/product-analytics/analytics/list",
                "operation_id": "query_product_analytics_list",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ProductAnalyticsAnalyticsListRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._query_product_analytics_retention_grid_endpoint = _Endpoint(
            settings={
                "response_type": (ProductAnalyticsRetentionGridResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/product-analytics/retention/grid",
                "operation_id": "query_product_analytics_retention_grid",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ProductAnalyticsRetentionGridRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._query_product_analytics_retention_list_endpoint = _Endpoint(
            settings={
                "response_type": (ProductAnalyticsRetentionListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/product-analytics/retention/list",
                "operation_id": "query_product_analytics_retention_list",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ProductAnalyticsRetentionListRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._query_product_analytics_retention_scalar_endpoint = _Endpoint(
            settings={
                "response_type": (ProductAnalyticsScalarResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/product-analytics/retention/scalar",
                "operation_id": "query_product_analytics_retention_scalar",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ProductAnalyticsFormulaRetentionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._query_product_analytics_retention_timeseries_endpoint = _Endpoint(
            settings={
                "response_type": (ProductAnalyticsTimeseriesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/product-analytics/retention/timeseries",
                "operation_id": "query_product_analytics_retention_timeseries",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ProductAnalyticsFormulaRetentionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._query_product_analytics_sankey_endpoint = _Endpoint(
            settings={
                "response_type": (ProductAnalyticsSankeyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/product-analytics/sankey",
                "operation_id": "query_product_analytics_sankey",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ProductAnalyticsSankeyRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._query_product_analytics_scalar_endpoint = _Endpoint(
            settings={
                "response_type": (ProductAnalyticsScalarResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/product-analytics/analytics/scalar",
                "operation_id": "query_product_analytics_scalar",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ProductAnalyticsAnalyticsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._query_product_analytics_timeseries_endpoint = _Endpoint(
            settings={
                "response_type": (ProductAnalyticsTimeseriesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/product-analytics/analytics/timeseries",
                "operation_id": "query_product_analytics_timeseries",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ProductAnalyticsAnalyticsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

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
                        "url": "https://{site}",
                        "variables": {
                            "site": {
                                "description": "The intake domain for the regional site.",
                                "default_value": "browser-intake-datadoghq.com",
                                "enum_values": [
                                    "browser-intake-datadoghq.com",
                                    "browser-intake-us3-datadoghq.com",
                                    "browser-intake-us5-datadoghq.com",
                                    "browser-intake-ap1-datadoghq.com",
                                    "browser-intake-ap2-datadoghq.com",
                                    "browser-intake-datadoghq.eu",
                                ],
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
                                "default_value": "api",
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

    def query_product_analytics_journey_funnel(
        self,
        body: ProductAnalyticsJourneyFunnelRequest,
    ) -> ProductAnalyticsJourneyFunnelResponse:
        """Compute journey funnel analysis.

        Compute a funnel over an ordered sequence of Product Analytics events.
        Returns the per-step conversion counts, conversion rates, and elapsed times,
        optionally segmented by group-by facets.

        :type body: ProductAnalyticsJourneyFunnelRequest
        :rtype: ProductAnalyticsJourneyFunnelResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._query_product_analytics_journey_funnel_endpoint.call_with_http_info(**kwargs)

    def query_product_analytics_journey_list(
        self,
        body: ProductAnalyticsJourneyListRequest,
    ) -> ProductAnalyticsJourneyListResponse:
        """List journey entities.

        Return the individual sessions that reached, or dropped off at, a given step of the journey.
        Each row contains the identity join key, the event timestamp, and the columns requested
        in ``entity_columns``.

        :type body: ProductAnalyticsJourneyListRequest
        :rtype: ProductAnalyticsJourneyListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._query_product_analytics_journey_list_endpoint.call_with_http_info(**kwargs)

    def query_product_analytics_journey_scalar(
        self,
        body: ProductAnalyticsJourneyScalarRequest,
    ) -> ProductAnalyticsJourneyScalarResponse:
        """Compute journey scalar analytics.

        Compute scalar results for a journey query, such as the conversion count,
        the conversion rate, or the time to convert, optionally segmented by group-by facets.

        :type body: ProductAnalyticsJourneyScalarRequest
        :rtype: ProductAnalyticsJourneyScalarResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._query_product_analytics_journey_scalar_endpoint.call_with_http_info(**kwargs)

    def query_product_analytics_journey_timeseries(
        self,
        body: ProductAnalyticsFormulaJourneyRequest,
    ) -> ProductAnalyticsJourneyTimeseriesResponse:
        """Compute journey timeseries analytics.

        Compute timeseries results for a journey query.
        Returns one series per group-by combination, bucketed by the requested interval.

        :type body: ProductAnalyticsFormulaJourneyRequest
        :rtype: ProductAnalyticsJourneyTimeseriesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._query_product_analytics_journey_timeseries_endpoint.call_with_http_info(**kwargs)

    def query_product_analytics_list(
        self,
        body: ProductAnalyticsAnalyticsListRequest,
    ) -> ProductAnalyticsAnalyticsListResponse:
        """List analytics events.

        List the individual event records matching an analytics query.
        Use ``columns`` to choose the attributes returned on each row, ``sort`` to order the rows,
        and ``limit`` to cap how many are returned.

        :type body: ProductAnalyticsAnalyticsListRequest
        :rtype: ProductAnalyticsAnalyticsListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._query_product_analytics_list_endpoint.call_with_http_info(**kwargs)

    def query_product_analytics_retention_grid(
        self,
        body: ProductAnalyticsRetentionGridRequest,
    ) -> ProductAnalyticsRetentionGridResponse:
        """Compute a retention grid.

        Compute a retention grid, showing how much of each cohort came back over each subsequent period.
        Rows are cohorts, columns are return periods, and each cell holds the count and rate of entities that returned.

        :param body: The retention grid query.
        :type body: ProductAnalyticsRetentionGridRequest
        :rtype: ProductAnalyticsRetentionGridResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._query_product_analytics_retention_grid_endpoint.call_with_http_info(**kwargs)

    def query_product_analytics_retention_list(
        self,
        body: ProductAnalyticsRetentionListRequest,
    ) -> ProductAnalyticsRetentionListResponse:
        """List the entities behind a retention cell.

        List the individual users or accounts counted in one cell of the retention grid.
        Set ``computation_scope`` to the cohort and return period you want to examine.

        :param body: The retention list query.
        :type body: ProductAnalyticsRetentionListRequest
        :rtype: ProductAnalyticsRetentionListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._query_product_analytics_retention_list_endpoint.call_with_http_info(**kwargs)

    def query_product_analytics_retention_scalar(
        self,
        body: ProductAnalyticsFormulaRetentionRequest,
    ) -> ProductAnalyticsScalarResponse:
        """Compute retention scalar values.

        Compute retention as a single value per group, suitable for a query value or top list widget.

        :param body: The retention scalar query.
        :type body: ProductAnalyticsFormulaRetentionRequest
        :rtype: ProductAnalyticsScalarResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._query_product_analytics_retention_scalar_endpoint.call_with_http_info(**kwargs)

    def query_product_analytics_retention_timeseries(
        self,
        body: ProductAnalyticsFormulaRetentionRequest,
    ) -> ProductAnalyticsTimeseriesResponse:
        """Compute retention timeseries.

        Compute retention as a series of values over time, using the same query definition as the
        retention grid.

        :param body: The retention timeseries query.
        :type body: ProductAnalyticsFormulaRetentionRequest
        :rtype: ProductAnalyticsTimeseriesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._query_product_analytics_retention_timeseries_endpoint.call_with_http_info(**kwargs)

    def query_product_analytics_sankey(
        self,
        body: ProductAnalyticsSankeyRequest,
    ) -> ProductAnalyticsSankeyResponse:
        """Compute a Sankey diagram.

        Compute a Sankey diagram of how sessions flow between the values of two facets,
        showing where users continue and where they drop off at each step.

        :param body: The Sankey diagram query.
        :type body: ProductAnalyticsSankeyRequest
        :rtype: ProductAnalyticsSankeyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._query_product_analytics_sankey_endpoint.call_with_http_info(**kwargs)

    def query_product_analytics_scalar(
        self,
        body: ProductAnalyticsAnalyticsRequest,
    ) -> ProductAnalyticsScalarResponse:
        """Compute scalar analytics.

        Compute scalar analytics results for Product Analytics data.
        Returns aggregated values (counts, averages, percentiles) optionally grouped by facets.

        :type body: ProductAnalyticsAnalyticsRequest
        :rtype: ProductAnalyticsScalarResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._query_product_analytics_scalar_endpoint.call_with_http_info(**kwargs)

    def query_product_analytics_timeseries(
        self,
        body: ProductAnalyticsAnalyticsRequest,
    ) -> ProductAnalyticsTimeseriesResponse:
        """Compute timeseries analytics.

        Compute timeseries analytics results for Product Analytics data.
        Returns time-bucketed values for charts and trend analysis.
        The ``compute.interval`` field (milliseconds) is required for time bucketing.

        :type body: ProductAnalyticsAnalyticsRequest
        :rtype: ProductAnalyticsTimeseriesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._query_product_analytics_timeseries_endpoint.call_with_http_info(**kwargs)

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
