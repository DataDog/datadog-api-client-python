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
from datadog_api_client.v2.model.security_entity_risk_scores_response import SecurityEntityRiskScoresResponse


class EntityRiskScoresApi:
    """
    Retrieves security risk scores for entities in your organization.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._list_entity_risk_scores_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityEntityRiskScoresResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security-entities/risk-scores",
                "operation_id": "list_entity_risk_scores",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "_from": {
                    "openapi_types": (int,),
                    "attribute": "from",
                    "location": "query",
                },
                "to": {
                    "openapi_types": (int,),
                    "attribute": "to",
                    "location": "query",
                },
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "page_query_id": {
                    "openapi_types": (str,),
                    "attribute": "page[queryId]",
                    "location": "query",
                },
                "filter_sort": {
                    "openapi_types": (str,),
                    "attribute": "filter[sort]",
                    "location": "query",
                },
                "filter_query": {
                    "openapi_types": (str,),
                    "attribute": "filter[query]",
                    "location": "query",
                },
                "entity_type": {
                    "openapi_types": ([str],),
                    "attribute": "entityType",
                    "location": "query",
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def list_entity_risk_scores(
        self,
        *,
        _from: Union[int, UnsetType] = unset,
        to: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        page_query_id: Union[str, UnsetType] = unset,
        filter_sort: Union[str, UnsetType] = unset,
        filter_query: Union[str, UnsetType] = unset,
        entity_type: Union[List[str], UnsetType] = unset,
    ) -> SecurityEntityRiskScoresResponse:
        """List Entity Risk Scores.

        Get a list of entity risk scores for your organization. Entity risk scores provide security risk assessment for entities like cloud resources, identities, or services based on detected signals, misconfigurations, and identity risks.

        :param _from: Start time for the query in Unix timestamp (milliseconds). Defaults to 2 weeks ago.
        :type _from: int, optional
        :param to: End time for the query in Unix timestamp (milliseconds). Defaults to now.
        :type to: int, optional
        :param page_size: Size of the page to return. Maximum is 1000.
        :type page_size: int, optional
        :param page_number: Page number to return (1-indexed).
        :type page_number: int, optional
        :param page_query_id: Query ID for pagination consistency.
        :type page_query_id: str, optional
        :param filter_sort: Sort order for results. Format: ``field:direction`` where direction is ``asc`` or ``desc``.
            Supported fields: ``riskScore`` , ``lastDetected`` , ``firstDetected`` , ``entityName`` , ``signalsDetected``.
        :type filter_sort: str, optional
        :param filter_query: Supports filtering by entity attributes, risk scores, severity, and more.
            Example: ``severity:critical AND entityType:aws_iam_user``
        :type filter_query: str, optional
        :param entity_type: Filter by entity type(s). Can specify multiple values.
        :type entity_type: [str], optional
        :rtype: SecurityEntityRiskScoresResponse
        """
        kwargs: Dict[str, Any] = {}
        if _from is not unset:
            kwargs["_from"] = _from

        if to is not unset:
            kwargs["to"] = to

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if page_query_id is not unset:
            kwargs["page_query_id"] = page_query_id

        if filter_sort is not unset:
            kwargs["filter_sort"] = filter_sort

        if filter_query is not unset:
            kwargs["filter_query"] = filter_query

        if entity_type is not unset:
            kwargs["entity_type"] = entity_type

        return self._list_entity_risk_scores_endpoint.call_with_http_info(**kwargs)
