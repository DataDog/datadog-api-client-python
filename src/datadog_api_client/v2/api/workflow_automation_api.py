# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.workflow_list_instances_response import WorkflowListInstancesResponse
from datadog_api_client.v2.model.workflow_instance_create_response import WorkflowInstanceCreateResponse
from datadog_api_client.v2.model.workflow_instance_create_request import WorkflowInstanceCreateRequest
from datadog_api_client.v2.model.worklflow_get_instance_response import WorklflowGetInstanceResponse
from datadog_api_client.v2.model.worklflow_cancel_instance_response import WorklflowCancelInstanceResponse


class WorkflowAutomationApi:
    """
    Automate your teams operational processes with Datadog Workflow Automation.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._cancel_workflow_instance_endpoint = _Endpoint(
            settings={
                "response_type": (WorklflowCancelInstanceResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/workflows/{workflow_id}/instances/{instance_id}/cancel",
                "operation_id": "cancel_workflow_instance",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "workflow_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "workflow_id",
                    "location": "path",
                },
                "instance_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "instance_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._create_workflow_instance_endpoint = _Endpoint(
            settings={
                "response_type": (WorkflowInstanceCreateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/workflows/{workflow_id}/instances",
                "operation_id": "create_workflow_instance",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "workflow_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "workflow_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (WorkflowInstanceCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_workflow_instance_endpoint = _Endpoint(
            settings={
                "response_type": (WorklflowGetInstanceResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/workflows/{workflow_id}/instances/{instance_id}",
                "operation_id": "get_workflow_instance",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "workflow_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "workflow_id",
                    "location": "path",
                },
                "instance_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "instance_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_workflow_instances_endpoint = _Endpoint(
            settings={
                "response_type": (WorkflowListInstancesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/workflows/{workflow_id}/instances",
                "operation_id": "list_workflow_instances",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "workflow_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "workflow_id",
                    "location": "path",
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def cancel_workflow_instance(
        self,
        workflow_id: str,
        instance_id: str,
    ) -> WorklflowCancelInstanceResponse:
        """Cancel a workflow instance.

        Cancels a specific execution of a given workflow. This API requires an application key scoped with the workflows_run permission.

        :param workflow_id: The ID of the workflow.
        :type workflow_id: str
        :param instance_id: The ID of the workflow instance.
        :type instance_id: str
        :rtype: WorklflowCancelInstanceResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["workflow_id"] = workflow_id

        kwargs["instance_id"] = instance_id

        return self._cancel_workflow_instance_endpoint.call_with_http_info(**kwargs)

    def create_workflow_instance(
        self,
        workflow_id: str,
        body: WorkflowInstanceCreateRequest,
    ) -> WorkflowInstanceCreateResponse:
        """Execute a workflow.

        Execute the given workflow. This API requires an application key scoped with the workflows_run permission.

        :param workflow_id: The ID of the workflow.
        :type workflow_id: str
        :type body: WorkflowInstanceCreateRequest
        :rtype: WorkflowInstanceCreateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["workflow_id"] = workflow_id

        kwargs["body"] = body

        return self._create_workflow_instance_endpoint.call_with_http_info(**kwargs)

    def get_workflow_instance(
        self,
        workflow_id: str,
        instance_id: str,
    ) -> WorklflowGetInstanceResponse:
        """Get a workflow instance.

        Get a specific execution of a given workflow. This API requires an application key scoped with the workflows_read permission.

        :param workflow_id: The ID of the workflow.
        :type workflow_id: str
        :param instance_id: The ID of the workflow instance.
        :type instance_id: str
        :rtype: WorklflowGetInstanceResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["workflow_id"] = workflow_id

        kwargs["instance_id"] = instance_id

        return self._get_workflow_instance_endpoint.call_with_http_info(**kwargs)

    def list_workflow_instances(
        self,
        workflow_id: str,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
    ) -> WorkflowListInstancesResponse:
        """List workflow instances.

        List all instances of a given workflow. This API requires an application key scoped with the workflows_read permission.

        :param workflow_id: The ID of the workflow.
        :type workflow_id: str
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :rtype: WorkflowListInstancesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["workflow_id"] = workflow_id

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        return self._list_workflow_instances_endpoint.call_with_http_info(**kwargs)
