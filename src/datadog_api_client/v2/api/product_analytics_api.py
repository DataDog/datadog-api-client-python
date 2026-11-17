# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
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
from datadog_api_client.v2.model.product_analytics_launches_response import ProductAnalyticsLaunchesResponse
from datadog_api_client.v2.model.product_analytics_launch_list_scope import ProductAnalyticsLaunchListScope
from datadog_api_client.v2.model.product_analytics_launch_phase import ProductAnalyticsLaunchPhase
from datadog_api_client.v2.model.product_analytics_launch_response import ProductAnalyticsLaunchResponse
from datadog_api_client.v2.model.product_analytics_launch_create_request import ProductAnalyticsLaunchCreateRequest
from datadog_api_client.v2.model.product_analytics_launch_patch_request import ProductAnalyticsLaunchPatchRequest
from datadog_api_client.v2.model.product_analytics_monitor_list_response import ProductAnalyticsMonitorListResponse
from datadog_api_client.v2.model.product_analytics_monitor_response import ProductAnalyticsMonitorResponse
from datadog_api_client.v2.model.product_analytics_monitor_create_request import ProductAnalyticsMonitorCreateRequest
from datadog_api_client.v2.model.product_analytics_monitor_update_request import ProductAnalyticsMonitorUpdateRequest
from datadog_api_client.v2.model.product_analytics_monitor_unlink_request import ProductAnalyticsMonitorUnlinkRequest
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

        self._create_product_analytics_launch_endpoint = _Endpoint(
            settings={
                "response_type": (ProductAnalyticsLaunchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-analytics/launches",
                "operation_id": "create_product_analytics_launch",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ProductAnalyticsLaunchCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_product_analytics_monitor_endpoint = _Endpoint(
            settings={
                "response_type": (ProductAnalyticsMonitorResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/product-analytics/monitors",
                "operation_id": "create_product_analytics_monitor",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ProductAnalyticsMonitorCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_product_analytics_launch_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-analytics/launches/{id}",
                "operation_id": "delete_product_analytics_launch",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_product_analytics_monitor_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/product-analytics/monitors/{monitor_id}",
                "operation_id": "delete_product_analytics_monitor",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "monitor_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "monitor_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_product_analytics_launch_endpoint = _Endpoint(
            settings={
                "response_type": (ProductAnalyticsLaunchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-analytics/launches/{id}",
                "operation_id": "get_product_analytics_launch",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_product_analytics_monitor_endpoint = _Endpoint(
            settings={
                "response_type": (ProductAnalyticsMonitorResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/product-analytics/monitors/{monitor_id}",
                "operation_id": "get_product_analytics_monitor",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "monitor_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "monitor_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_product_analytics_launches_endpoint = _Endpoint(
            settings={
                "response_type": (ProductAnalyticsLaunchesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-analytics/launches",
                "operation_id": "list_product_analytics_launches",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "scope": {
                    "openapi_types": (ProductAnalyticsLaunchListScope,),
                    "attribute": "scope",
                    "location": "query",
                },
                "phase": {
                    "openapi_types": ([ProductAnalyticsLaunchPhase],),
                    "attribute": "phase",
                    "location": "query",
                    "collection_format": "multi",
                },
                "application_id": {
                    "openapi_types": (str,),
                    "attribute": "application_id",
                    "location": "query",
                },
                "name": {
                    "openapi_types": (str,),
                    "attribute": "name",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_product_analytics_monitors_endpoint = _Endpoint(
            settings={
                "response_type": (ProductAnalyticsMonitorListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/product-analytics/monitors",
                "operation_id": "list_product_analytics_monitors",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 1000,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "validation": {
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "chart_id": {
                    "openapi_types": (str,),
                    "attribute": "chart_id",
                    "location": "query",
                },
                "dashboard_id": {
                    "openapi_types": (str,),
                    "attribute": "dashboard_id",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._query_product_analytics_journey_funnel_endpoint = _Endpoint(
            settings={
                "response_type": (ProductAnalyticsJourneyFunnelResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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

        self._remove_chart_from_product_analytics_monitor_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/product-analytics/monitors/{monitor_id}/unlink",
                "operation_id": "remove_chart_from_product_analytics_monitor",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "monitor_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "monitor_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ProductAnalyticsMonitorUnlinkRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
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
                                    "browser-intake-uk1-datadoghq.com",
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

        self._update_product_analytics_launch_endpoint = _Endpoint(
            settings={
                "response_type": (ProductAnalyticsLaunchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-analytics/launches/{id}",
                "operation_id": "update_product_analytics_launch",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ProductAnalyticsLaunchPatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_product_analytics_monitor_endpoint = _Endpoint(
            settings={
                "response_type": (ProductAnalyticsMonitorResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/product-analytics/monitors/{monitor_id}",
                "operation_id": "update_product_analytics_monitor",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "monitor_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "monitor_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ProductAnalyticsMonitorUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_product_analytics_launch(
        self,
        body: ProductAnalyticsLaunchCreateRequest,
    ) -> ProductAnalyticsLaunchResponse:
        """Create a Product Analytics launch.

        Create a Product Analytics launch and its tracking plan.
        The tracking plan lists the events and event properties to instrument. Events can only reference properties
        and KPIs defined in the launch.

        :type body: ProductAnalyticsLaunchCreateRequest
        :rtype: ProductAnalyticsLaunchResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_product_analytics_launch_endpoint.call_with_http_info(**kwargs)

    def create_product_analytics_monitor(
        self,
        body: ProductAnalyticsMonitorCreateRequest,
    ) -> ProductAnalyticsMonitorResponse:
        """Create a Product Analytics monitor.

        Create a Product Analytics monitor that alerts on a Product Analytics query, such as a funnel conversion rate.
        Link it to the chart it was created from with the ``chart_id`` and ``dashboard_id`` tags.

        :type body: ProductAnalyticsMonitorCreateRequest
        :rtype: ProductAnalyticsMonitorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_product_analytics_monitor_endpoint.call_with_http_info(**kwargs)

    def delete_product_analytics_launch(
        self,
        id: str,
    ) -> None:
        """Delete a Product Analytics launch.

        Delete a Product Analytics launch and its tracking plan.

        :param id: UUID of the launch.
        :type id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._delete_product_analytics_launch_endpoint.call_with_http_info(**kwargs)

    def delete_product_analytics_monitor(
        self,
        monitor_id: str,
    ) -> None:
        """Delete a Product Analytics monitor.

        Delete a Product Analytics monitor.

        :param monitor_id: Numeric ID of the monitor.
        :type monitor_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["monitor_id"] = monitor_id

        return self._delete_product_analytics_monitor_endpoint.call_with_http_info(**kwargs)

    def get_product_analytics_launch(
        self,
        id: str,
    ) -> ProductAnalyticsLaunchResponse:
        """Get a Product Analytics launch.

        Get a Product Analytics launch and its tracking plan by UUID.

        :param id: UUID of the launch.
        :type id: str
        :rtype: ProductAnalyticsLaunchResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._get_product_analytics_launch_endpoint.call_with_http_info(**kwargs)

    def get_product_analytics_monitor(
        self,
        monitor_id: str,
    ) -> ProductAnalyticsMonitorResponse:
        """Get a Product Analytics monitor.

        Get a Product Analytics monitor by its ID.

        :param monitor_id: Numeric ID of the monitor.
        :type monitor_id: str
        :rtype: ProductAnalyticsMonitorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["monitor_id"] = monitor_id

        return self._get_product_analytics_monitor_endpoint.call_with_http_info(**kwargs)

    def list_product_analytics_launches(
        self,
        *,
        sort: Union[str, UnsetType] = unset,
        scope: Union[ProductAnalyticsLaunchListScope, UnsetType] = unset,
        phase: Union[List[ProductAnalyticsLaunchPhase], UnsetType] = unset,
        application_id: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
    ) -> ProductAnalyticsLaunchesResponse:
        """List Product Analytics launches.

        List the Product Analytics launches of your organization. A launch tracks a feature release with its phase,
        KPIs, and tracking plan.
        Results are sorted by ``-created_at`` by default.

        :param sort: Comma-separated fields to sort by: ``id`` , ``phase`` , ``feature_flag_id`` , ``name`` , ``application_id`` ,
            ``description`` , ``created_by`` , ``created_at`` , ``updated_by`` , or ``updated_at``. Prefix a field with ``-`` to sort
            in descending order.
        :type sort: str, optional
        :param scope: Set to ``liftoffs`` to leave out launches in the ``plan`` phase.
        :type scope: ProductAnalyticsLaunchListScope, optional
        :param phase: Return only launches in these phases. Repeat the parameter to pass several phases.
        :type phase: [ProductAnalyticsLaunchPhase], optional
        :param application_id: Return only launches of this RUM application UUID.
        :type application_id: str, optional
        :param name: Return only launches whose name contains this value, ignoring case.
        :type name: str, optional
        :rtype: ProductAnalyticsLaunchesResponse
        """
        kwargs: Dict[str, Any] = {}
        if sort is not unset:
            kwargs["sort"] = sort

        if scope is not unset:
            kwargs["scope"] = scope

        if phase is not unset:
            kwargs["phase"] = phase

        if application_id is not unset:
            kwargs["application_id"] = application_id

        if name is not unset:
            kwargs["name"] = name

        return self._list_product_analytics_launches_endpoint.call_with_http_info(**kwargs)

    def list_product_analytics_monitors(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        chart_id: Union[str, UnsetType] = unset,
        dashboard_id: Union[str, UnsetType] = unset,
    ) -> ProductAnalyticsMonitorListResponse:
        """List Product Analytics monitors.

        List the Product Analytics monitors of your organization, one page at a time.
        When ``chart_id`` is set, optionally with ``dashboard_id`` , the response includes every monitor linked to that
        chart, without pagination.
        With ``chart_id`` alone, monitors created from a dashboard widget are not returned.
        Monitors created in the last few seconds may be missing.

        :param page_size: Maximum number of monitors per page, from 1 to 1000. Ignored when ``chart_id`` is set.
        :type page_size: int, optional
        :param page_number: Page number, starting at 1. Ignored when ``chart_id`` is set.
        :type page_number: int, optional
        :param chart_id: Return only the monitors linked to this chart. Turns off pagination.
        :type chart_id: str, optional
        :param dashboard_id: Return only the monitors linked to this dashboard. Requires ``chart_id``.
        :type dashboard_id: str, optional
        :rtype: ProductAnalyticsMonitorListResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if chart_id is not unset:
            kwargs["chart_id"] = chart_id

        if dashboard_id is not unset:
            kwargs["dashboard_id"] = dashboard_id

        return self._list_product_analytics_monitors_endpoint.call_with_http_info(**kwargs)

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

    def remove_chart_from_product_analytics_monitor(
        self,
        monitor_id: str,
        body: ProductAnalyticsMonitorUnlinkRequest,
    ) -> None:
        """Unlink a Product Analytics monitor from its chart.

        Remove the ``chart_id`` and ``dashboard_id`` tags from a Product Analytics monitor. The monitor and the rest of
        its configuration are kept.
        The request must name the stored link exactly. A monitor with no link is left unchanged.

        :param monitor_id: Numeric ID of the monitor.
        :type monitor_id: str
        :type body: ProductAnalyticsMonitorUnlinkRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["monitor_id"] = monitor_id

        kwargs["body"] = body

        return self._remove_chart_from_product_analytics_monitor_endpoint.call_with_http_info(**kwargs)

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

    def update_product_analytics_launch(
        self,
        id: str,
        body: ProductAnalyticsLaunchPatchRequest,
    ) -> ProductAnalyticsLaunchResponse:
        """Update a Product Analytics launch.

        Update some fields of a Product Analytics launch. Fields that are not set are left unchanged. The ``id`` in
        the body must match the one in the path.
        Setting ``steps.tracking_plan`` replaces the whole stored tracking plan, not only the fields you send.
        Returns ``409`` when the launch changed during the update; fetch it again and retry.

        :param id: UUID of the launch.
        :type id: str
        :type body: ProductAnalyticsLaunchPatchRequest
        :rtype: ProductAnalyticsLaunchResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["body"] = body

        return self._update_product_analytics_launch_endpoint.call_with_http_info(**kwargs)

    def update_product_analytics_monitor(
        self,
        monitor_id: str,
        body: ProductAnalyticsMonitorUpdateRequest,
    ) -> ProductAnalyticsMonitorResponse:
        """Update a Product Analytics monitor.

        Update a Product Analytics monitor. Fields that are not set are left unchanged, and at least one field
        must be set. When set, ``tags`` replaces the monitor tags except ``chart_id`` and ``dashboard_id`` , which this
        endpoint ignores. To remove them, use the unlink endpoint.

        :param monitor_id: Numeric ID of the monitor.
        :type monitor_id: str
        :type body: ProductAnalyticsMonitorUpdateRequest
        :rtype: ProductAnalyticsMonitorResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["monitor_id"] = monitor_id

        kwargs["body"] = body

        return self._update_product_analytics_monitor_endpoint.call_with_http_info(**kwargs)
