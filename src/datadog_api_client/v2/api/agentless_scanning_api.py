# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.aws_scan_options_list_response import AwsScanOptionsListResponse
from datadog_api_client.v2.model.aws_scan_options_response import AwsScanOptionsResponse
from datadog_api_client.v2.model.aws_scan_options_create_request import AwsScanOptionsCreateRequest
from datadog_api_client.v2.model.aws_scan_options_update_request import AwsScanOptionsUpdateRequest
from datadog_api_client.v2.model.aws_on_demand_list_response import AwsOnDemandListResponse
from datadog_api_client.v2.model.aws_on_demand_response import AwsOnDemandResponse
from datadog_api_client.v2.model.aws_on_demand_create_request import AwsOnDemandCreateRequest


class AgentlessScanningApi:
    """
    Datadog Agentless Scanning provides visibility into risks and vulnerabilities
    within your hosts, running containers, and serverless functions—all without
    requiring teams to install Agents on every host or where Agents cannot be installed.
    Agentless offers also Sensitive Data Scanning capabilities on your storage.
    Go to https://www.datadoghq.com/blog/agentless-scanning/ to learn more.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_aws_on_demand_task_endpoint = _Endpoint(
            settings={
                "response_type": (AwsOnDemandResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/agentless_scanning/ondemand/aws",
                "operation_id": "create_aws_on_demand_task",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AwsOnDemandCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_aws_scan_options_endpoint = _Endpoint(
            settings={
                "response_type": (AwsScanOptionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/agentless_scanning/accounts/aws",
                "operation_id": "create_aws_scan_options",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AwsScanOptionsCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_aws_scan_options_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/agentless_scanning/accounts/aws/{account_id}",
                "operation_id": "delete_aws_scan_options",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "account_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_aws_on_demand_task_endpoint = _Endpoint(
            settings={
                "response_type": (AwsOnDemandResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/agentless_scanning/ondemand/aws/{task_id}",
                "operation_id": "get_aws_on_demand_task",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "task_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "task_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_aws_on_demand_tasks_endpoint = _Endpoint(
            settings={
                "response_type": (AwsOnDemandListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/agentless_scanning/ondemand/aws",
                "operation_id": "list_aws_on_demand_tasks",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_aws_scan_options_endpoint = _Endpoint(
            settings={
                "response_type": (AwsScanOptionsListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/agentless_scanning/accounts/aws",
                "operation_id": "list_aws_scan_options",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_aws_scan_options_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/agentless_scanning/accounts/aws/{account_id}",
                "operation_id": "update_aws_scan_options",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "account_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AwsScanOptionsUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_aws_on_demand_task(
        self,
        body: AwsOnDemandCreateRequest,
    ) -> AwsOnDemandResponse:
        """Post an AWS on demand task.

        Trigger the scan of an AWS resource with a high priority. Agentless scanning must be activated for the AWS account containing the resource to scan.

        :param body: The definition of the on demand task.
        :type body: AwsOnDemandCreateRequest
        :rtype: AwsOnDemandResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_aws_on_demand_task_endpoint.call_with_http_info(**kwargs)

    def create_aws_scan_options(
        self,
        body: AwsScanOptionsCreateRequest,
    ) -> AwsScanOptionsResponse:
        """Post AWS Scan Options.

        Activate Agentless scan options for an AWS account.

        :param body: The definition of the new scan options.
        :type body: AwsScanOptionsCreateRequest
        :rtype: AwsScanOptionsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_aws_scan_options_endpoint.call_with_http_info(**kwargs)

    def delete_aws_scan_options(
        self,
        account_id: str,
    ) -> None:
        """Delete AWS Scan Options.

        Delete Agentless scan options for an AWS account.

        :param account_id: The ID of an AWS account.
        :type account_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._delete_aws_scan_options_endpoint.call_with_http_info(**kwargs)

    def get_aws_on_demand_task(
        self,
        task_id: str,
    ) -> AwsOnDemandResponse:
        """Get AWS On Demand task by id.

        Fetch the data of a specific on demand task.

        :param task_id: The UUID of the task.
        :type task_id: str
        :rtype: AwsOnDemandResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["task_id"] = task_id

        return self._get_aws_on_demand_task_endpoint.call_with_http_info(**kwargs)

    def list_aws_on_demand_tasks(
        self,
    ) -> AwsOnDemandListResponse:
        """Get AWS On Demand tasks.

        Fetches the most recent 1000 AWS on demand tasks.

        :rtype: AwsOnDemandListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_aws_on_demand_tasks_endpoint.call_with_http_info(**kwargs)

    def list_aws_scan_options(
        self,
    ) -> AwsScanOptionsListResponse:
        """Get AWS Scan Options.

        Fetches the scan options configured for AWS accounts.

        :rtype: AwsScanOptionsListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_aws_scan_options_endpoint.call_with_http_info(**kwargs)

    def update_aws_scan_options(
        self,
        account_id: str,
        body: AwsScanOptionsUpdateRequest,
    ) -> None:
        """Patch AWS Scan Options.

        Update the Agentless scan options for an activated account.

        :param account_id: The ID of an AWS account.
        :type account_id: str
        :param body: New definition of the scan options.
        :type body: AwsScanOptionsUpdateRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        kwargs["body"] = body

        return self._update_aws_scan_options_endpoint.call_with_http_info(**kwargs)
