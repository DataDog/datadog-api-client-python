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
from datadog_api_client.v2.model.governance_insights_response import GovernanceInsightsResponse


class GovernanceInsightsApi:
    """
    Governance Insights surface key usage, configuration, and best-practice signals for an
    organization within the Governance Console. Each insight reports a current value (and,
    optionally, a previous value for comparison) along with the query used to compute it, so
    that the Console can render trends and highlight areas that need attention.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._list_governance_insights_endpoint = _Endpoint(
            settings={
                "response_type": (GovernanceInsightsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/governance/insights",
                "operation_id": "list_governance_insights",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "with_values": {
                    "openapi_types": (bool,),
                    "attribute": "withValues",
                    "location": "query",
                },
                "org_uuid": {
                    "openapi_types": (str,),
                    "attribute": "orgUuid",
                    "location": "query",
                },
                "filter_product": {
                    "openapi_types": ([str],),
                    "attribute": "filter[product]",
                    "location": "query",
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def list_governance_insights(
        self,
        *,
        with_values: Union[bool, UnsetType] = unset,
        org_uuid: Union[str, UnsetType] = unset,
        filter_product: Union[List[str], UnsetType] = unset,
    ) -> GovernanceInsightsResponse:
        """List governance insights.

        Retrieve the list of governance insights available to the organization. By default, only
        insight metadata is returned; pass ``withValues=true`` to also compute and include each
        insight's current and previous values. Insights can be filtered by product.

        :param with_values: Whether to compute and include the current and previous value of each insight.
            Defaults to ``false`` , in which case only insight metadata is returned.
        :type with_values: bool, optional
        :param org_uuid: The UUID of the organization to compute insights for. Defaults to the organization of
            the authenticated user. Used to retrieve insights for a child organization from a
            parent organization.
        :type org_uuid: str, optional
        :param filter_product: Restrict the results to insights belonging to the given products. May be repeated to
            filter by multiple products. Matching is case-insensitive.
        :type filter_product: [str], optional
        :rtype: GovernanceInsightsResponse
        """
        kwargs: Dict[str, Any] = {}
        if with_values is not unset:
            kwargs["with_values"] = with_values

        if org_uuid is not unset:
            kwargs["org_uuid"] = org_uuid

        if filter_product is not unset:
            kwargs["filter_product"] = filter_product

        return self._list_governance_insights_endpoint.call_with_http_info(**kwargs)
