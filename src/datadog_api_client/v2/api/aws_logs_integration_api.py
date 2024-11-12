# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.aws_logs_services_response import AWSLogsServicesResponse


class AWSLogsIntegrationApi:
    """
    Configure your Datadog-AWS-Logs integration directly through Datadog API.
    For more information, see the `AWS integration page <https://docs.datadoghq.com/integrations/amazon_web_services/#log-collection>`_.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._list_aws_logs_services_endpoint = _Endpoint(
            settings={
                "response_type": (AWSLogsServicesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/aws/logs/services",
                "operation_id": "list_aws_logs_services",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def list_aws_logs_services(
        self,
    ) -> AWSLogsServicesResponse:
        """Get list of AWS log ready services.

        Get a list of AWS services that can send logs to Datadog.

        :rtype: AWSLogsServicesResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_aws_logs_services_endpoint.call_with_http_info(**kwargs)
