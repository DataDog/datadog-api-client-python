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
    UUID,
)
from datadog_api_client.v2.model.custom_agent_conversation_stream_response import CustomAgentConversationStreamResponse
from datadog_api_client.v2.model.custom_agent_conversation_request import CustomAgentConversationRequest
from datadog_api_client.v2.model.data_transformation_stream_response import DataTransformationStreamResponse
from datadog_api_client.v2.model.data_transformation_request import DataTransformationRequest
from datadog_api_client.v2.model.data_transformation_description_response import DataTransformationDescriptionResponse
from datadog_api_client.v2.model.data_transformation_description_request import DataTransformationDescriptionRequest
from datadog_api_client.v2.model.workflow_description_response import WorkflowDescriptionResponse
from datadog_api_client.v2.model.workflow_description_request import WorkflowDescriptionRequest
from datadog_api_client.v2.model.pick_action_response import PickActionResponse
from datadog_api_client.v2.model.pick_action_request import PickActionRequest
from datadog_api_client.v2.model.pick_remediation_from_investigation_response import (
    PickRemediationFromInvestigationResponse,
)
from datadog_api_client.v2.model.pick_remediation_from_investigation_request import (
    PickRemediationFromInvestigationRequest,
)
from datadog_api_client.v2.model.workflow_scaffold_agentic_stream_response import WorkflowScaffoldAgenticStreamResponse
from datadog_api_client.v2.model.workflow_scaffold_agentic_stream_request import WorkflowScaffoldAgenticStreamRequest
from datadog_api_client.v2.model.create_workflow_response import CreateWorkflowResponse
from datadog_api_client.v2.model.create_workflow_request import CreateWorkflowRequest
from datadog_api_client.v2.model.get_workflow_response import GetWorkflowResponse
from datadog_api_client.v2.model.update_workflow_response import UpdateWorkflowResponse
from datadog_api_client.v2.model.update_workflow_request import UpdateWorkflowRequest
from datadog_api_client.v2.model.workflow_list_instances_response import WorkflowListInstancesResponse
from datadog_api_client.v2.model.workflow_instance_create_response import WorkflowInstanceCreateResponse
from datadog_api_client.v2.model.workflow_instance_create_request import WorkflowInstanceCreateRequest
from datadog_api_client.v2.model.worklflow_get_instance_response import WorklflowGetInstanceResponse
from datadog_api_client.v2.model.worklflow_cancel_instance_response import WorklflowCancelInstanceResponse


class WorkflowAutomationApi:
    """
    Datadog Workflow Automation allows you to automate your end-to-end processes by connecting Datadog with the rest of your tech stack. Build workflows to auto-remediate your alerts, streamline your incident and security processes, and reduce manual toil. Workflow Automation supports over 1,000+ OOTB actions, including AWS, JIRA, ServiceNow, GitHub, and OpenAI. Learn more in our Workflow Automation docs `here <https://docs.datadoghq.com/service_management/workflows/>`_.
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

        self._create_custom_agent_conversation_endpoint = _Endpoint(
            settings={
                "response_type": (CustomAgentConversationStreamResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/actions/agents/{custom_agent_id}/conversation",
                "operation_id": "create_custom_agent_conversation",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "custom_agent_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "custom_agent_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CustomAgentConversationRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["text/event-stream", "application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_data_transformation_endpoint = _Endpoint(
            settings={
                "response_type": (DataTransformationStreamResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/workflow_generation/data_transformation",
                "operation_id": "create_data_transformation",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DataTransformationRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["text/event-stream", "application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_data_transformation_description_endpoint = _Endpoint(
            settings={
                "response_type": (DataTransformationDescriptionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/workflow_generation/data_transformation/description",
                "operation_id": "create_data_transformation_description",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DataTransformationDescriptionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_pick_action_endpoint = _Endpoint(
            settings={
                "response_type": (PickActionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/workflow_generation/pick_action",
                "operation_id": "create_pick_action",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (PickActionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_pick_remediation_from_investigation_endpoint = _Endpoint(
            settings={
                "response_type": (PickRemediationFromInvestigationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/workflow_generation/pick_remediation_from_investigation",
                "operation_id": "create_pick_remediation_from_investigation",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (PickRemediationFromInvestigationRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_workflow_endpoint = _Endpoint(
            settings={
                "response_type": (CreateWorkflowResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/workflows",
                "operation_id": "create_workflow",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateWorkflowRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_workflow_description_endpoint = _Endpoint(
            settings={
                "response_type": (WorkflowDescriptionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/workflow_generation/description",
                "operation_id": "create_workflow_description",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (WorkflowDescriptionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_workflow_instance_endpoint = _Endpoint(
            settings={
                "response_type": (WorkflowInstanceCreateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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

        self._create_workflow_scaffold_agentic_stream_endpoint = _Endpoint(
            settings={
                "response_type": (WorkflowScaffoldAgenticStreamResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/workflow_generation/scaffold_agentic_stream",
                "operation_id": "create_workflow_scaffold_agentic_stream",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (WorkflowScaffoldAgenticStreamRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["text/event-stream", "application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_workflow_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/workflows/{workflow_id}",
                "operation_id": "delete_workflow",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "workflow_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "workflow_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_workflow_endpoint = _Endpoint(
            settings={
                "response_type": (GetWorkflowResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/workflows/{workflow_id}",
                "operation_id": "get_workflow",
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
            },
            headers_map={
                "accept": ["application/json"],
            },
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

        self._update_workflow_endpoint = _Endpoint(
            settings={
                "response_type": (UpdateWorkflowResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/workflows/{workflow_id}",
                "operation_id": "update_workflow",
                "http_method": "PATCH",
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
                    "openapi_types": (UpdateWorkflowRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def cancel_workflow_instance(
        self,
        workflow_id: str,
        instance_id: str,
    ) -> WorklflowCancelInstanceResponse:
        """Cancel a workflow instance.

        Cancels a specific execution of a given workflow. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_. Alternatively, you can configure these permissions `in the UI <https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access>`_.

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

    def create_custom_agent_conversation(
        self,
        custom_agent_id: UUID,
        body: CustomAgentConversationRequest,
    ) -> CustomAgentConversationStreamResponse:
        """Create a custom agent conversation.

        Initiates or continues a conversation with a custom agent. Supports streaming responses.

        :param custom_agent_id: The ID of the custom agent.
        :type custom_agent_id: UUID
        :type body: CustomAgentConversationRequest
        :rtype: CustomAgentConversationStreamResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["custom_agent_id"] = custom_agent_id

        kwargs["body"] = body

        return self._create_custom_agent_conversation_endpoint.call_with_http_info(**kwargs)

    def create_data_transformation(
        self,
        body: DataTransformationRequest,
    ) -> DataTransformationStreamResponse:
        """Generate data transformation code.

        Generates data transformation code (JavaScript or Python) based on user prompt and context.

        :type body: DataTransformationRequest
        :rtype: DataTransformationStreamResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_data_transformation_endpoint.call_with_http_info(**kwargs)

    def create_data_transformation_description(
        self,
        body: DataTransformationDescriptionRequest,
    ) -> DataTransformationDescriptionResponse:
        """Generate data transformation description.

        Generates a summary and detailed description for data transformation code.

        :type body: DataTransformationDescriptionRequest
        :rtype: DataTransformationDescriptionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_data_transformation_description_endpoint.call_with_http_info(**kwargs)

    def create_pick_action(
        self,
        body: PickActionRequest,
    ) -> PickActionResponse:
        """Pick relevant actions.

        Finds similar actions based on a user prompt using vector search.

        :type body: PickActionRequest
        :rtype: PickActionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_pick_action_endpoint.call_with_http_info(**kwargs)

    def create_pick_remediation_from_investigation(
        self,
        body: PickRemediationFromInvestigationRequest,
    ) -> PickRemediationFromInvestigationResponse:
        """Pick remediation actions from investigation.

        Generates keywords from an investigation and finds relevant remediation actions.

        :type body: PickRemediationFromInvestigationRequest
        :rtype: PickRemediationFromInvestigationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_pick_remediation_from_investigation_endpoint.call_with_http_info(**kwargs)

    def create_workflow(
        self,
        body: CreateWorkflowRequest,
    ) -> CreateWorkflowResponse:
        """Create a Workflow.

        Create a new workflow, returning the workflow ID. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_. Alternatively, you can configure these permissions `in the UI <https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access>`_.

        :type body: CreateWorkflowRequest
        :rtype: CreateWorkflowResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_workflow_endpoint.call_with_http_info(**kwargs)

    def create_workflow_description(
        self,
        body: WorkflowDescriptionRequest,
    ) -> WorkflowDescriptionResponse:
        """Generate workflow description.

        Generates a description and summary for a workflow based on its specification.

        :type body: WorkflowDescriptionRequest
        :rtype: WorkflowDescriptionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_workflow_description_endpoint.call_with_http_info(**kwargs)

    def create_workflow_instance(
        self,
        workflow_id: str,
        body: WorkflowInstanceCreateRequest,
    ) -> WorkflowInstanceCreateResponse:
        """Execute a workflow.

        Execute the given workflow. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_. Alternatively, you can configure these permissions `in the UI <https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access>`_.

        :param workflow_id: The ID of the workflow.
        :type workflow_id: str
        :type body: WorkflowInstanceCreateRequest
        :rtype: WorkflowInstanceCreateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["workflow_id"] = workflow_id

        kwargs["body"] = body

        return self._create_workflow_instance_endpoint.call_with_http_info(**kwargs)

    def create_workflow_scaffold_agentic_stream(
        self,
        body: WorkflowScaffoldAgenticStreamRequest,
    ) -> WorkflowScaffoldAgenticStreamResponse:
        """Generate workflow scaffold with agentic stream.

        Generates or updates a workflow scaffold using agentic streaming based on user prompts.

        :type body: WorkflowScaffoldAgenticStreamRequest
        :rtype: WorkflowScaffoldAgenticStreamResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_workflow_scaffold_agentic_stream_endpoint.call_with_http_info(**kwargs)

    def delete_workflow(
        self,
        workflow_id: str,
    ) -> None:
        """Delete an existing Workflow.

        Delete a workflow by ID. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_. Alternatively, you can configure these permissions `in the UI <https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access>`_.

        :param workflow_id: The ID of the workflow.
        :type workflow_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["workflow_id"] = workflow_id

        return self._delete_workflow_endpoint.call_with_http_info(**kwargs)

    def get_workflow(
        self,
        workflow_id: str,
    ) -> GetWorkflowResponse:
        """Get an existing Workflow.

        Get a workflow by ID. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_. Alternatively, you can configure these permissions `in the UI <https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access>`_.

        :param workflow_id: The ID of the workflow.
        :type workflow_id: str
        :rtype: GetWorkflowResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["workflow_id"] = workflow_id

        return self._get_workflow_endpoint.call_with_http_info(**kwargs)

    def get_workflow_instance(
        self,
        workflow_id: str,
        instance_id: str,
    ) -> WorklflowGetInstanceResponse:
        """Get a workflow instance.

        Get a specific execution of a given workflow. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_. Alternatively, you can configure these permissions `in the UI <https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access>`_.

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

        List all instances of a given workflow. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_. Alternatively, you can configure these permissions `in the UI <https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access>`_.

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

    def update_workflow(
        self,
        workflow_id: str,
        body: UpdateWorkflowRequest,
    ) -> UpdateWorkflowResponse:
        """Update an existing Workflow.

        Update a workflow by ID. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_. Alternatively, you can configure these permissions `in the UI <https://docs.datadoghq.com/account_management/api-app-keys/#actions-api-access>`_.

        :param workflow_id: The ID of the workflow.
        :type workflow_id: str
        :type body: UpdateWorkflowRequest
        :rtype: UpdateWorkflowResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["workflow_id"] = workflow_id

        kwargs["body"] = body

        return self._update_workflow_endpoint.call_with_http_info(**kwargs)
