# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.model_utils import (
    datetime,
)
from datadog_api_client.v2.model.cost_by_org_response import CostByOrgResponse
from datadog_api_client.v2.model.usage_observability_pipelines_response import UsageObservabilityPipelinesResponse


class UsageMeteringApi:
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

    def get_cost_by_org(self, start_month, **kwargs):
        """Get Cost Across Multi-Org Account.

        Get Cost Across Multi-Org Account.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_cost_by_org(start_month, async_req=True)
        >>> result = thread.get()

        :param start_month: Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for cost beginning this month.
        :type start_month: datetime
        :param end_month: Datetime in ISO-8601 format, UTC, precise to month: `[YYYY-MM]` for cost ending this month.
        :type end_month: datetime, optional
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: CostByOrgResponse
        """
        kwargs = self._get_cost_by_org_endpoint.default_arguments(kwargs)
        kwargs["start_month"] = start_month

        return self._get_cost_by_org_endpoint.call_with_http_info(**kwargs)

    def get_usage_observability_pipelines(self, start_hr, **kwargs):
        """Get hourly usage for Observability Pipelines.

        Get hourly usage for Observability Pipelines.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_usage_observability_pipelines(start_hr, async_req=True)
        >>> result = thread.get()

        :param start_hr: Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage beginning at this hour.
        :type start_hr: datetime
        :param end_hr: Datetime in ISO-8601 format, UTC, precise to hour: `[YYYY-MM-DDThh]` for usage ending
            **before** this hour.
        :type end_hr: datetime, optional
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: UsageObservabilityPipelinesResponse
        """
        kwargs = self._get_usage_observability_pipelines_endpoint.default_arguments(kwargs)
        kwargs["start_hr"] = start_hr

        return self._get_usage_observability_pipelines_endpoint.call_with_http_info(**kwargs)
