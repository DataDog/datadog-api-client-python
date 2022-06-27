# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.model_utils import (
    datetime,
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.usage_application_security_monitoring_response import (
    UsageApplicationSecurityMonitoringResponse,
)
from datadog_api_client.v2.model.cost_by_org_response import CostByOrgResponse
from datadog_api_client.v2.model.usage_lambda_traced_invocations_response import UsageLambdaTracedInvocationsResponse
from datadog_api_client.v2.model.usage_observability_pipelines_response import UsageObservabilityPipelinesResponse


class UsageMeteringApi:
    """
    The usage metering API allows you to get hourly, daily, and
    monthly usage across multiple facets of Datadog.
    This API is available to all Pro and Enterprise customers.
    Usage is only accessible for `parent-level organizations <https://docs.datadoghq.com/account_management/multi_organization/>`_.

    **Note** : Usage data is delayed by up to 72 hours from when it was incurred.
    It is retained for 15 months.

    You can retrieve up to 24 hours of hourly usage data for multiple organizations,
    and up to two months of hourly usage data for a single organization in one request.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._get_cost_by_org_endpoint = _Endpoint(
            settings={
                "response_type": (CostByOrgResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/usage/cost_by_org",
                "operation_id": "get_cost_by_org",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "start_month": {
                    "required": True,
                    "openapi_types": (datetime,),
                    "attribute": "start_month",
                    "location": "query",
                },
                "end_month": {
                    "openapi_types": (datetime,),
                    "attribute": "end_month",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json;datetime-format=rfc3339"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_estimated_cost_by_org_endpoint = _Endpoint(
            settings={
                "response_type": (CostByOrgResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/usage/estimated_cost_by_org",
                "operation_id": "get_estimated_cost_by_org",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "start_month": {
                    "openapi_types": (datetime,),
                    "attribute": "start_month",
                    "location": "query",
                },
                "end_month": {
                    "openapi_types": (datetime,),
                    "attribute": "end_month",
                    "location": "query",
                },
                "start_date": {
                    "openapi_types": (datetime,),
                    "attribute": "start_date",
                    "location": "query",
                },
                "end_date": {
                    "openapi_types": (datetime,),
                    "attribute": "end_date",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json;datetime-format=rfc3339"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_usage_application_security_monitoring_endpoint = _Endpoint(
            settings={
                "response_type": (UsageApplicationSecurityMonitoringResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/usage/application_security",
                "operation_id": "get_usage_application_security_monitoring",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "start_hr": {
                    "required": True,
                    "openapi_types": (datetime,),
                    "attribute": "start_hr",
                    "location": "query",
                },
                "end_hr": {
                    "openapi_types": (datetime,),
                    "attribute": "end_hr",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json;datetime-format=rfc3339"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_usage_lambda_traced_invocations_endpoint = _Endpoint(
            settings={
                "response_type": (UsageLambdaTracedInvocationsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/usage/lambda_traced_invocations",
                "operation_id": "get_usage_lambda_traced_invocations",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "start_hr": {
                    "required": True,
                    "openapi_types": (datetime,),
                    "attribute": "start_hr",
                    "location": "query",
                },
                "end_hr": {
                    "openapi_types": (datetime,),
                    "attribute": "end_hr",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json;datetime-format=rfc3339"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_usage_observability_pipelines_endpoint = _Endpoint(
            settings={
                "response_type": (UsageObservabilityPipelinesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/usage/observability_pipelines",
                "operation_id": "get_usage_observability_pipelines",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "start_hr": {
                    "required": True,
                    "openapi_types": (datetime,),
                    "attribute": "start_hr",
                    "location": "query",
                },
                "end_hr": {
                    "openapi_types": (datetime,),
                    "attribute": "end_hr",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json;datetime-format=rfc3339"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def get_cost_by_org(
        self,
        start_month: datetime,
        *,
        end_month: Union[datetime, UnsetType] = unset,
    ) -> CostByOrgResponse:
        """Get cost across multi-org account.

        Get cost across multi-org account. Cost by org data for a given month becomes available no later than the 16th of the following month.

        :param start_month: Datetime in ISO-8601 format, UTC, precise to month: ``[YYYY-MM]`` for cost beginning this month.
        :type start_month: datetime
        :param end_month: Datetime in ISO-8601 format, UTC, precise to month: ``[YYYY-MM]`` for cost ending this month.
        :type end_month: datetime, optional
        :rtype: CostByOrgResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["start_month"] = start_month

        if end_month is not unset:
            kwargs["end_month"] = end_month

        return self._get_cost_by_org_endpoint.call_with_http_info(**kwargs)

    def get_estimated_cost_by_org(
        self,
        *,
        start_month: Union[datetime, UnsetType] = unset,
        end_month: Union[datetime, UnsetType] = unset,
        start_date: Union[datetime, UnsetType] = unset,
        end_date: Union[datetime, UnsetType] = unset,
    ) -> CostByOrgResponse:
        """Get estimated cost across multi-org account.

        Get estimated cost across multi-org account.

        :param start_month: Datetime in ISO-8601 format, UTC, precise to month: ``[YYYY-MM]`` for cost beginning this month. Either start_month or start_date should be specified, but not both.
        :type start_month: datetime, optional
        :param end_month: Datetime in ISO-8601 format, UTC, precise to month: ``[YYYY-MM]`` for cost ending this month.
        :type end_month: datetime, optional
        :param start_date: Datetime in ISO-8601 format, UTC, precise to day: ``[YYYY-MM-DD]`` for cost beginning this day. Either start_month or start_date should be specified, but not both.
        :type start_date: datetime, optional
        :param end_date: Datetime in ISO-8601 format, UTC, precise to day: ``[YYYY-MM-DD]`` for cost ending this day.
        :type end_date: datetime, optional
        :rtype: CostByOrgResponse
        """
        kwargs: Dict[str, Any] = {}
        if start_month is not unset:
            kwargs["start_month"] = start_month

        if end_month is not unset:
            kwargs["end_month"] = end_month

        if start_date is not unset:
            kwargs["start_date"] = start_date

        if end_date is not unset:
            kwargs["end_date"] = end_date

        return self._get_estimated_cost_by_org_endpoint.call_with_http_info(**kwargs)

    def get_usage_application_security_monitoring(
        self,
        start_hr: datetime,
        *,
        end_hr: Union[datetime, UnsetType] = unset,
    ) -> UsageApplicationSecurityMonitoringResponse:
        """Get hourly usage for Application Security.

        Get hourly usage for Application Security .

        :param start_hr: Datetime in ISO-8601 format, UTC, precise to hour: ``[YYYY-MM-DDThh]`` for usage beginning at this hour.
        :type start_hr: datetime
        :param end_hr: Datetime in ISO-8601 format, UTC, precise to hour: ``[YYYY-MM-DDThh]`` for usage ending
            **before** this hour.
        :type end_hr: datetime, optional
        :rtype: UsageApplicationSecurityMonitoringResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["start_hr"] = start_hr

        if end_hr is not unset:
            kwargs["end_hr"] = end_hr

        return self._get_usage_application_security_monitoring_endpoint.call_with_http_info(**kwargs)

    def get_usage_lambda_traced_invocations(
        self,
        start_hr: datetime,
        *,
        end_hr: Union[datetime, UnsetType] = unset,
    ) -> UsageLambdaTracedInvocationsResponse:
        """Get hourly usage for Lambda Traced Invocations.

        Get hourly usage for Lambda Traced Invocations.

        :param start_hr: Datetime in ISO-8601 format, UTC, precise to hour: ``[YYYY-MM-DDThh]`` for usage beginning at this hour.
        :type start_hr: datetime
        :param end_hr: Datetime in ISO-8601 format, UTC, precise to hour: ``[YYYY-MM-DDThh]`` for usage ending
            **before** this hour.
        :type end_hr: datetime, optional
        :rtype: UsageLambdaTracedInvocationsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["start_hr"] = start_hr

        if end_hr is not unset:
            kwargs["end_hr"] = end_hr

        return self._get_usage_lambda_traced_invocations_endpoint.call_with_http_info(**kwargs)

    def get_usage_observability_pipelines(
        self,
        start_hr: datetime,
        *,
        end_hr: Union[datetime, UnsetType] = unset,
    ) -> UsageObservabilityPipelinesResponse:
        """Get hourly usage for Observability Pipelines.

        Get hourly usage for Observability Pipelines.

        :param start_hr: Datetime in ISO-8601 format, UTC, precise to hour: ``[YYYY-MM-DDThh]`` for usage beginning at this hour.
        :type start_hr: datetime
        :param end_hr: Datetime in ISO-8601 format, UTC, precise to hour: ``[YYYY-MM-DDThh]`` for usage ending
            **before** this hour.
        :type end_hr: datetime, optional
        :rtype: UsageObservabilityPipelinesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["start_hr"] = start_hr

        if end_hr is not unset:
            kwargs["end_hr"] = end_hr

        return self._get_usage_observability_pipelines_endpoint.call_with_http_info(**kwargs)
