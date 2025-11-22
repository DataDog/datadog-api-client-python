# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.get_cohort_response import GetCohortResponse
from datadog_api_client.v2.model.get_cohort_request import GetCohortRequest
from datadog_api_client.v2.model.get_cohort_users_response import GetCohortUsersResponse
from datadog_api_client.v2.model.get_cohort_users_request import GetCohortUsersRequest


class CohortApi:
    """
    API for Cohort.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_rum_cohort_endpoint = _Endpoint(
            settings={
                "response_type": (GetCohortResponse,),
                "auth": [],
                "endpoint_path": "/api/v2/rum/cohort",
                "operation_id": "get_rum_cohort",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (GetCohortRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_rum_cohort_users_endpoint = _Endpoint(
            settings={
                "response_type": (GetCohortUsersResponse,),
                "auth": [],
                "endpoint_path": "/api/v2/rum/cohort/users",
                "operation_id": "get_rum_cohort_users",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (GetCohortUsersRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def get_rum_cohort(
        self,
        body: GetCohortRequest,
    ) -> GetCohortResponse:
        """Get rum cohort.

        Analyze user cohorts for retention and conversion analysis

        :type body: GetCohortRequest
        :rtype: GetCohortResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._get_rum_cohort_endpoint.call_with_http_info(**kwargs)

    def get_rum_cohort_users(
        self,
        body: GetCohortUsersRequest,
    ) -> GetCohortUsersResponse:
        """Get rum cohort users.

        Get users within a specific cohort for retention analysis

        :type body: GetCohortUsersRequest
        :rtype: GetCohortUsersResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._get_rum_cohort_users_endpoint.call_with_http_info(**kwargs)
