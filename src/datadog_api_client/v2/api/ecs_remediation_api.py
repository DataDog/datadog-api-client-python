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
from datadog_api_client.v2.model.remediation_execute_response import RemediationExecuteResponse
from datadog_api_client.v2.model.remediation_execute_request import RemediationExecuteRequest
from datadog_api_client.v2.model.remediation_get_investigation_response import RemediationGetInvestigationResponse
from datadog_api_client.v2.model.remediation_list_investigations_response import RemediationListInvestigationsResponse


class ECSRemediationApi:
    """
    Manage ECS remediation investigations and execute proposed remediation plans.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._execute_remediation_endpoint = _Endpoint(
            settings={
                "response_type": (RemediationExecuteResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/ui/orchestration/ecs_remediation/execute",
                "operation_id": "execute_remediation",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (RemediationExecuteRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_ecs_remediation_investigation_endpoint = _Endpoint(
            settings={
                "response_type": (RemediationGetInvestigationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/ui/orchestration/ecs_remediation/investigation",
                "operation_id": "get_ecs_remediation_investigation",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_ecs_remediation_investigations_endpoint = _Endpoint(
            settings={
                "response_type": (RemediationListInvestigationsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/ui/orchestration/ecs_remediation/investigations",
                "operation_id": "list_ecs_remediation_investigations",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "cluster_arn": {
                    "openapi_types": (str,),
                    "attribute": "cluster_arn",
                    "location": "query",
                },
                "cluster_name": {
                    "openapi_types": (str,),
                    "attribute": "cluster_name",
                    "location": "query",
                },
                "service_arn": {
                    "openapi_types": (str,),
                    "attribute": "service_arn",
                    "location": "query",
                },
                "task_arn": {
                    "openapi_types": (str,),
                    "attribute": "task_arn",
                    "location": "query",
                },
                "resource_arn": {
                    "openapi_types": (str,),
                    "attribute": "resource_arn",
                    "location": "query",
                },
                "status": {
                    "openapi_types": ([str],),
                    "attribute": "status",
                    "location": "query",
                    "collection_format": "multi",
                },
                "issue_type": {
                    "openapi_types": (str,),
                    "attribute": "issue_type",
                    "location": "query",
                },
                "since_ms": {
                    "openapi_types": (int,),
                    "attribute": "since_ms",
                    "location": "query",
                },
                "until_ms": {
                    "openapi_types": (int,),
                    "attribute": "until_ms",
                    "location": "query",
                },
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 200,
                    },
                    "openapi_types": (int,),
                    "attribute": "page_size",
                    "location": "query",
                },
                "page_token": {
                    "openapi_types": (str,),
                    "attribute": "page_token",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def execute_remediation(
        self,
        body: RemediationExecuteRequest,
    ) -> RemediationExecuteResponse:
        """Execute an ECS remediation.

        Trigger execution of the proposed remediation for an investigation through the configured AWS connection. The investigation must belong to the caller's organization.

        :param body: The investigation to remediate and the AWS connection to use.
        :type body: RemediationExecuteRequest
        :rtype: RemediationExecuteResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._execute_remediation_endpoint.call_with_http_info(**kwargs)

    def get_ecs_remediation_investigation(
        self,
        id: str,
    ) -> RemediationGetInvestigationResponse:
        """Get an ECS remediation investigation.

        Get a single ECS remediation investigation by ID, including its proposed plan, history, and ECS workload metadata.

        :param id: The investigation ID.
        :type id: str
        :rtype: RemediationGetInvestigationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._get_ecs_remediation_investigation_endpoint.call_with_http_info(**kwargs)

    def list_ecs_remediation_investigations(
        self,
        *,
        cluster_arn: Union[str, UnsetType] = unset,
        cluster_name: Union[str, UnsetType] = unset,
        service_arn: Union[str, UnsetType] = unset,
        task_arn: Union[str, UnsetType] = unset,
        resource_arn: Union[str, UnsetType] = unset,
        status: Union[List[str], UnsetType] = unset,
        issue_type: Union[str, UnsetType] = unset,
        since_ms: Union[int, UnsetType] = unset,
        until_ms: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_token: Union[str, UnsetType] = unset,
    ) -> RemediationListInvestigationsResponse:
        """List ECS remediation investigations.

        List ECS remediation investigations for the caller's organization. All filters are optional and applied together. Results are returned in pages.

        :param cluster_arn: Filter by ECS cluster ARN.
        :type cluster_arn: str, optional
        :param cluster_name: Filter by ECS cluster name.
        :type cluster_name: str, optional
        :param service_arn: Filter by ECS service ARN.
        :type service_arn: str, optional
        :param task_arn: Filter by ECS task ARN.
        :type task_arn: str, optional
        :param resource_arn: Filter by resource ARN. Matches services, daemons, and standalone tasks.
        :type resource_arn: str, optional
        :param status: Filter by investigation status. Repeatable. Accepted values: open, approval_required, executing, succeeded, failed. Unknown values are ignored.
        :type status: [str], optional
        :param issue_type: Filter by issue type.
        :type issue_type: str, optional
        :param since_ms: Start of the created-at time range, in epoch milliseconds.
        :type since_ms: int, optional
        :param until_ms: End of the created-at time range, in epoch milliseconds.
        :type until_ms: int, optional
        :param page_size: Maximum number of investigations to return. Clamped to 200.
        :type page_size: int, optional
        :param page_token: Pagination token returned by a previous call.
        :type page_token: str, optional
        :rtype: RemediationListInvestigationsResponse
        """
        kwargs: Dict[str, Any] = {}
        if cluster_arn is not unset:
            kwargs["cluster_arn"] = cluster_arn

        if cluster_name is not unset:
            kwargs["cluster_name"] = cluster_name

        if service_arn is not unset:
            kwargs["service_arn"] = service_arn

        if task_arn is not unset:
            kwargs["task_arn"] = task_arn

        if resource_arn is not unset:
            kwargs["resource_arn"] = resource_arn

        if status is not unset:
            kwargs["status"] = status

        if issue_type is not unset:
            kwargs["issue_type"] = issue_type

        if since_ms is not unset:
            kwargs["since_ms"] = since_ms

        if until_ms is not unset:
            kwargs["until_ms"] = until_ms

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_token is not unset:
            kwargs["page_token"] = page_token

        return self._list_ecs_remediation_investigations_endpoint.call_with_http_info(**kwargs)
