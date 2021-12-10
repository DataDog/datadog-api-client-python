# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import re  # noqa: F401

from datadog_api_client.v1.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model_utils import (  # noqa: F401
    date,
    datetime,
    file_type,
    none_type,
)
from datadog_api_client.v1.model.api_error_response import APIErrorResponse
from datadog_api_client.v1.model.ip_ranges import IPRanges


class IPRangesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._get_ip_ranges_endpoint = _Endpoint(
            settings={
                "response_type": (IPRanges,),
                "auth": [],
                "endpoint_path": "/",
                "operation_id": "get_ip_ranges",
                "http_method": "GET",
                "servers": [
                    {
                        "url": "https://{subdomain}.{site}",
                        "description": "No description provided",
                        "variables": {
                            "site": {
                                "description": "The regional site for our customers.",
                                "default_value": "datadoghq.com",
                                "enum_values": [
                                    "datadoghq.com",
                                    "us3.datadoghq.com",
                                    "us5.datadoghq.com",
                                    "datadoghq.eu",
                                    "ddog-gov.com",
                                ],
                            },
                            "subdomain": {
                                "description": "The subdomain where the API is deployed.",
                                "default_value": "ip-ranges",
                            },
                        },
                    },
                    {
                        "url": "{protocol}://{name}",
                        "description": "No description provided",
                        "variables": {
                            "name": {
                                "description": "Full site DNS name.",
                                "default_value": "ip-ranges.datadoghq.com",
                            },
                            "protocol": {
                                "description": "The protocol for accessing the API.",
                                "default_value": "https",
                            },
                        },
                    },
                    {
                        "url": "https://{subdomain}.datadoghq.com",
                        "description": "No description provided",
                        "variables": {
                            "subdomain": {
                                "description": "The subdomain where the API is deployed.",
                                "default_value": "ip-ranges",
                            }
                        },
                    },
                ],
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def get_ip_ranges(self, **kwargs):
        """List IP Ranges

        Get information about Datadog IP ranges.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_ip_ranges(async_req=True)
        >>> result = thread.get()

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            IPRanges
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._get_ip_ranges_endpoint.default_arguments(kwargs)
        return self._get_ip_ranges_endpoint.call_with_http_info(**kwargs)
