# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    datetime,
    UnsetType,
    unset,
    UUID,
)
from datadog_api_client.v2.model.ai_workflow_response import AIWorkflowResponse
from datadog_api_client.v2.model.create_ai_workflow_request import CreateAIWorkflowRequest
from datadog_api_client.v2.model.list_ai_workflows_response import ListAIWorkflowsResponse
from datadog_api_client.v2.model.update_ai_workflow_request import UpdateAIWorkflowRequest
from datadog_api_client.v2.model.cancel_workflow_executions_response import CancelWorkflowExecutionsResponse
from datadog_api_client.v2.model.create_workflow_executions_response import CreateWorkflowExecutionsResponse
from datadog_api_client.v2.model.list_workflow_instances_response import ListWorkflowInstancesResponse
from datadog_api_client.v2.model.list_pr_outputs_response import ListPROutputsResponse
from datadog_api_client.v2.model.workflow_execution_response import WorkflowExecutionResponse
from datadog_api_client.v2.model.list_execution_steps_response import ListExecutionStepsResponse


class DependencyManagementApi:
    """
    Manage AI-powered dependency upgrade workflows for your organization's repositories.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._cancel_workflow_execution_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dependency-management/workflow-executions/{id}/cancel",
                "operation_id": "cancel_workflow_execution",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._cancel_workflow_executions_endpoint = _Endpoint(
            settings={
                "response_type": (CancelWorkflowExecutionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dependency-management/ai-workflows/{id}/cancel",
                "operation_id": "cancel_workflow_executions",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._create_ai_workflow_endpoint = _Endpoint(
            settings={
                "response_type": (AIWorkflowResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dependency-management/ai-workflow",
                "operation_id": "create_ai_workflow",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateAIWorkflowRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_workflow_execution_endpoint = _Endpoint(
            settings={
                "response_type": (CreateWorkflowExecutionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dependency-management/ai-workflows/{id}/executions",
                "operation_id": "create_workflow_execution",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
                "max_instances": {
                    "validation": {
                        "inclusive_maximum": 30,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "max_instances",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._delete_ai_workflow_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dependency-management/ai-workflows/{id}",
                "operation_id": "delete_ai_workflow",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_workflow_executions_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dependency-management/ai-workflows/{id}/executions",
                "operation_id": "delete_workflow_executions",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_ai_workflow_endpoint = _Endpoint(
            settings={
                "response_type": (AIWorkflowResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dependency-management/ai-workflows/{id}",
                "operation_id": "get_ai_workflow",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_ai_workflow_instances_endpoint = _Endpoint(
            settings={
                "response_type": (ListWorkflowInstancesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dependency-management/ai-workflows/{id}/instances",
                "operation_id": "list_ai_workflow_instances",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_ai_workflows_endpoint = _Endpoint(
            settings={
                "response_type": (ListAIWorkflowsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dependency-management/ai-workflows",
                "operation_id": "list_ai_workflows",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "idp_campaign_id": {
                    "openapi_types": (str,),
                    "attribute": "idp_campaign_id",
                    "location": "query",
                },
                "repository": {
                    "openapi_types": (str,),
                    "attribute": "repository",
                    "location": "query",
                },
                "user": {
                    "openapi_types": (str,),
                    "attribute": "user",
                    "location": "query",
                },
                "completed": {
                    "openapi_types": (bool,),
                    "attribute": "completed",
                    "location": "query",
                },
                "created_after": {
                    "openapi_types": (datetime,),
                    "attribute": "created_after",
                    "location": "query",
                },
                "created_before": {
                    "openapi_types": (datetime,),
                    "attribute": "created_before",
                    "location": "query",
                },
                "limit": {
                    "validation": {
                        "inclusive_maximum": 100,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "limit",
                    "location": "query",
                },
                "offset": {
                    "validation": {
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "offset",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_execution_steps_endpoint = _Endpoint(
            settings={
                "response_type": (ListExecutionStepsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dependency-management/workflow-executions/{id}/steps",
                "operation_id": "list_execution_steps",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_pr_outputs_endpoint = _Endpoint(
            settings={
                "response_type": (ListPROutputsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dependency-management/workflow-executions/{id}/pr-outputs",
                "operation_id": "list_pr_outputs",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._rerun_workflow_execution_endpoint = _Endpoint(
            settings={
                "response_type": (WorkflowExecutionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dependency-management/workflow-executions/{id}/rerun",
                "operation_id": "rerun_workflow_execution",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_ai_workflow_endpoint = _Endpoint(
            settings={
                "response_type": (AIWorkflowResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dependency-management/ai-workflows/{id}",
                "operation_id": "update_ai_workflow",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UpdateAIWorkflowRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def cancel_workflow_execution(
        self,
        id: UUID,
    ) -> None:
        """Cancel a workflow execution.

        Cancel a specific workflow execution instance. Returns 409 if the instance is not currently in a running state.

        :param id: The UUID of the workflow execution.
        :type id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._cancel_workflow_execution_endpoint.call_with_http_info(**kwargs)

    def cancel_workflow_executions(
        self,
        id: UUID,
    ) -> CancelWorkflowExecutionsResponse:
        """Cancel workflow executions.

        Cancel all running workflow execution instances for the given AI workflow.

        :param id: The UUID of the AI workflow.
        :type id: UUID
        :rtype: CancelWorkflowExecutionsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._cancel_workflow_executions_endpoint.call_with_http_info(**kwargs)

    def create_ai_workflow(
        self,
        body: CreateAIWorkflowRequest,
    ) -> AIWorkflowResponse:
        """Create an AI workflow.

        Create a new AI workflow for dependency management. This creates both the workflow definition and initializes its executions.

        :type body: CreateAIWorkflowRequest
        :rtype: AIWorkflowResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_ai_workflow_endpoint.call_with_http_info(**kwargs)

    def create_workflow_execution(
        self,
        id: UUID,
        *,
        max_instances: Union[int, UnsetType] = unset,
    ) -> CreateWorkflowExecutionsResponse:
        """Create workflow executions.

        Create workflow executions for an AI workflow. One execution is created per entity group defined in the workflow.

        :param id: The UUID of the AI workflow.
        :type id: UUID
        :param max_instances: Maximum number of new workflow instances to start. Must be between 1 and 30.
        :type max_instances: int, optional
        :rtype: CreateWorkflowExecutionsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        if max_instances is not unset:
            kwargs["max_instances"] = max_instances

        return self._create_workflow_execution_endpoint.call_with_http_info(**kwargs)

    def delete_ai_workflow(
        self,
        id: UUID,
    ) -> None:
        """Delete an AI workflow.

        Delete a specific AI workflow. This also removes the workflow from Datadog Workflow Automation.

        :param id: The UUID of the AI workflow.
        :type id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._delete_ai_workflow_endpoint.call_with_http_info(**kwargs)

    def delete_workflow_executions(
        self,
        id: UUID,
    ) -> None:
        """Delete workflow executions.

        Delete all workflow executions for a given AI workflow. Running instances are canceled before deletion.

        :param id: The UUID of the AI workflow.
        :type id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._delete_workflow_executions_endpoint.call_with_http_info(**kwargs)

    def get_ai_workflow(
        self,
        id: UUID,
    ) -> AIWorkflowResponse:
        """Get an AI workflow.

        Get details of a specific AI workflow by its ID.

        :param id: The UUID of the AI workflow.
        :type id: UUID
        :rtype: AIWorkflowResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._get_ai_workflow_endpoint.call_with_http_info(**kwargs)

    def list_ai_workflow_instances(
        self,
        id: UUID,
    ) -> ListWorkflowInstancesResponse:
        """List AI workflow instances.

        List all workflow instances for a given AI workflow with their live status from Workflow Automation and entity information.

        :param id: The UUID of the AI workflow.
        :type id: UUID
        :rtype: ListWorkflowInstancesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._list_ai_workflow_instances_endpoint.call_with_http_info(**kwargs)

    def list_ai_workflows(
        self,
        *,
        idp_campaign_id: Union[str, UnsetType] = unset,
        repository: Union[str, UnsetType] = unset,
        user: Union[str, UnsetType] = unset,
        completed: Union[bool, UnsetType] = unset,
        created_after: Union[datetime, UnsetType] = unset,
        created_before: Union[datetime, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        offset: Union[int, UnsetType] = unset,
    ) -> ListAIWorkflowsResponse:
        """List AI workflows.

        List AI workflows for the organization with optional filters.

        :param idp_campaign_id: Filter workflows by IDP campaign ID.
        :type idp_campaign_id: str, optional
        :param repository: Filter workflows by repository name (owner/repo format).
        :type repository: str, optional
        :param user: Filter workflows by the username of the creator.
        :type user: str, optional
        :param completed: Filter workflows by completion status. Use ``true`` to return only completed workflows, ``false`` for incomplete.
        :type completed: bool, optional
        :param created_after: Filter workflows created after this timestamp (RFC3339 format).
        :type created_after: datetime, optional
        :param created_before: Filter workflows created before this timestamp (RFC3339 format).
        :type created_before: datetime, optional
        :param limit: Maximum number of workflows to return. Defaults to 50, maximum 100.
        :type limit: int, optional
        :param offset: Number of workflows to skip for pagination.
        :type offset: int, optional
        :rtype: ListAIWorkflowsResponse
        """
        kwargs: Dict[str, Any] = {}
        if idp_campaign_id is not unset:
            kwargs["idp_campaign_id"] = idp_campaign_id

        if repository is not unset:
            kwargs["repository"] = repository

        if user is not unset:
            kwargs["user"] = user

        if completed is not unset:
            kwargs["completed"] = completed

        if created_after is not unset:
            kwargs["created_after"] = created_after

        if created_before is not unset:
            kwargs["created_before"] = created_before

        if limit is not unset:
            kwargs["limit"] = limit

        if offset is not unset:
            kwargs["offset"] = offset

        return self._list_ai_workflows_endpoint.call_with_http_info(**kwargs)

    def list_execution_steps(
        self,
        id: UUID,
    ) -> ListExecutionStepsResponse:
        """List execution steps.

        Get the real-time step status for a specific workflow execution instance from Datadog Workflow Automation.

        :param id: The UUID of the workflow execution.
        :type id: UUID
        :rtype: ListExecutionStepsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._list_execution_steps_endpoint.call_with_http_info(**kwargs)

    def list_pr_outputs(
        self,
        id: UUID,
    ) -> ListPROutputsResponse:
        """List PR outputs.

        Get the pull request outputs for a specific workflow execution. Includes PR URL, status, and CI status enriched from GitHub.

        :param id: The UUID of the workflow execution.
        :type id: UUID
        :rtype: ListPROutputsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._list_pr_outputs_endpoint.call_with_http_info(**kwargs)

    def rerun_workflow_execution(
        self,
        id: UUID,
    ) -> WorkflowExecutionResponse:
        """Rerun a workflow execution.

        Rerun a failed or canceled workflow execution. This replaces the existing execution with a new one using the same entities.

        :param id: The UUID of the workflow execution.
        :type id: UUID
        :rtype: WorkflowExecutionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._rerun_workflow_execution_endpoint.call_with_http_info(**kwargs)

    def update_ai_workflow(
        self,
        id: UUID,
        body: UpdateAIWorkflowRequest,
    ) -> AIWorkflowResponse:
        """Update an AI workflow.

        Update the configuration of an existing AI workflow. Only the provided fields are updated.

        :param id: The UUID of the AI workflow.
        :type id: UUID
        :type body: UpdateAIWorkflowRequest
        :rtype: AIWorkflowResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["body"] = body

        return self._update_ai_workflow_endpoint.call_with_http_info(**kwargs)
