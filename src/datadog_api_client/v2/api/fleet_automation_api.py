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
from datadog_api_client.v2.model.fleet_agent_versions_response import FleetAgentVersionsResponse
from datadog_api_client.v2.model.fleet_agents_response import FleetAgentsResponse
from datadog_api_client.v2.model.fleet_agent_info_response import FleetAgentInfoResponse
from datadog_api_client.v2.model.fleet_deployments_response import FleetDeploymentsResponse
from datadog_api_client.v2.model.fleet_deployment_response import FleetDeploymentResponse
from datadog_api_client.v2.model.fleet_deployment_configure_create_request import FleetDeploymentConfigureCreateRequest
from datadog_api_client.v2.model.fleet_deployment_package_upgrade_create_request import (
    FleetDeploymentPackageUpgradeCreateRequest,
)
from datadog_api_client.v2.model.fleet_schedules_response import FleetSchedulesResponse
from datadog_api_client.v2.model.fleet_schedule_response import FleetScheduleResponse
from datadog_api_client.v2.model.fleet_schedule_create_request import FleetScheduleCreateRequest
from datadog_api_client.v2.model.fleet_schedule_patch_request import FleetSchedulePatchRequest


class FleetAutomationApi:
    """
    Manage automated deployments across your fleet of hosts.

    Fleet Automation provides two types of deployments:

    Configuration Deployments ( ``/configure`` ):

    * Apply configuration file changes to target hosts
    * Support merge-patch operations to update specific configuration fields
    * Support delete operations to remove configuration files
    * Useful for updating Datadog Agent settings, integration configs, and more

    Package Upgrade Deployments ( ``/upgrade`` ):

    * Upgrade the Datadog Agent to specific versions
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._cancel_fleet_deployment_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/fleet/deployments/{deployment_id}/cancel",
                "operation_id": "cancel_fleet_deployment",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "deployment_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "deployment_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._create_fleet_deployment_configure_endpoint = _Endpoint(
            settings={
                "response_type": (FleetDeploymentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/fleet/deployments/configure",
                "operation_id": "create_fleet_deployment_configure",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (FleetDeploymentConfigureCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_fleet_deployment_upgrade_endpoint = _Endpoint(
            settings={
                "response_type": (FleetDeploymentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/fleet/deployments/upgrade",
                "operation_id": "create_fleet_deployment_upgrade",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (FleetDeploymentPackageUpgradeCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_fleet_schedule_endpoint = _Endpoint(
            settings={
                "response_type": (FleetScheduleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/fleet/schedules",
                "operation_id": "create_fleet_schedule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (FleetScheduleCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_fleet_schedule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/fleet/schedules/{id}",
                "operation_id": "delete_fleet_schedule",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_fleet_agent_info_endpoint = _Endpoint(
            settings={
                "response_type": (FleetAgentInfoResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/fleet/agents/{agent_key}",
                "operation_id": "get_fleet_agent_info",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "agent_key": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "agent_key",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_fleet_deployment_endpoint = _Endpoint(
            settings={
                "response_type": (FleetDeploymentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/fleet/deployments/{deployment_id}",
                "operation_id": "get_fleet_deployment",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "deployment_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "deployment_id",
                    "location": "path",
                },
                "limit": {
                    "validation": {
                        "inclusive_maximum": 100,
                    },
                    "openapi_types": (int,),
                    "attribute": "limit",
                    "location": "query",
                },
                "page": {
                    "openapi_types": (int,),
                    "attribute": "page",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_fleet_schedule_endpoint = _Endpoint(
            settings={
                "response_type": (FleetScheduleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/fleet/schedules/{id}",
                "operation_id": "get_fleet_schedule",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_fleet_agents_endpoint = _Endpoint(
            settings={
                "response_type": (FleetAgentsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/fleet/agents",
                "operation_id": "list_fleet_agents",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_number": {
                    "validation": {
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page_number",
                    "location": "query",
                },
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 100,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page_size",
                    "location": "query",
                },
                "sort_attribute": {
                    "openapi_types": (str,),
                    "attribute": "sort_attribute",
                    "location": "query",
                },
                "sort_descending": {
                    "openapi_types": (bool,),
                    "attribute": "sort_descending",
                    "location": "query",
                },
                "tags": {
                    "openapi_types": (str,),
                    "attribute": "tags",
                    "location": "query",
                },
                "filter": {
                    "openapi_types": (str,),
                    "attribute": "filter",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_fleet_agent_versions_endpoint = _Endpoint(
            settings={
                "response_type": (FleetAgentVersionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/fleet/agent_versions",
                "operation_id": "list_fleet_agent_versions",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_fleet_deployments_endpoint = _Endpoint(
            settings={
                "response_type": (FleetDeploymentsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/fleet/deployments",
                "operation_id": "list_fleet_deployments",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 100,
                    },
                    "openapi_types": (int,),
                    "attribute": "page_size",
                    "location": "query",
                },
                "page_offset": {
                    "openapi_types": (int,),
                    "attribute": "page_offset",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_fleet_schedules_endpoint = _Endpoint(
            settings={
                "response_type": (FleetSchedulesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/fleet/schedules",
                "operation_id": "list_fleet_schedules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._trigger_fleet_schedule_endpoint = _Endpoint(
            settings={
                "response_type": (FleetDeploymentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/fleet/schedules/{id}/trigger",
                "operation_id": "trigger_fleet_schedule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_fleet_schedule_endpoint = _Endpoint(
            settings={
                "response_type": (FleetScheduleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/fleet/schedules/{id}",
                "operation_id": "update_fleet_schedule",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (FleetSchedulePatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def cancel_fleet_deployment(
        self,
        deployment_id: str,
    ) -> None:
        """Cancel a deployment.

        Cancel an active deployment and stop all pending operations.
        When you cancel a deployment:

        * All pending operations on hosts that haven't started yet are stopped
        * Operations currently in progress on hosts may complete or be interrupted, depending on their current state
        * Configuration changes or package upgrades already applied to hosts are not rolled back

        After cancellation, you can view the final state of the deployment using the GET endpoint to see which hosts
        were successfully updated before the cancellation.

        :param deployment_id: The unique identifier of the deployment to cancel.
        :type deployment_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["deployment_id"] = deployment_id

        return self._cancel_fleet_deployment_endpoint.call_with_http_info(**kwargs)

    def create_fleet_deployment_configure(
        self,
        body: FleetDeploymentConfigureCreateRequest,
    ) -> FleetDeploymentResponse:
        """Create a configuration deployment.

        Create a new deployment to apply configuration changes
        to a fleet of hosts matching the specified filter query.

        This endpoint supports two types of configuration operations:

        * ``merge-patch`` : Merges the provided patch data with the existing configuration file,
          creating the file if it doesn't exist
        * ``delete`` : Removes the specified configuration file from the target hosts

        The deployment is created and started automatically. You can specify multiple configuration
        operations that will be executed in order on each target host. Use the filter query to target
        specific hosts using the Datadog query syntax.

        :param body: Request payload containing the deployment details.
        :type body: FleetDeploymentConfigureCreateRequest
        :rtype: FleetDeploymentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_fleet_deployment_configure_endpoint.call_with_http_info(**kwargs)

    def create_fleet_deployment_upgrade(
        self,
        body: FleetDeploymentPackageUpgradeCreateRequest,
    ) -> FleetDeploymentResponse:
        """Upgrade hosts.

        Create and immediately start a new package upgrade
        on hosts matching the specified filter query.

        This endpoint allows you to upgrade the Datadog Agent to a specific version
        on hosts matching the specified filter query.

        The deployment is created and started automatically. The system will:

        #. Identify all hosts matching the filter query
        #. Validate that the specified version is available
        #. Begin rolling out the package upgrade to the target hosts

        :param body: Request payload containing the package upgrade details.
        :type body: FleetDeploymentPackageUpgradeCreateRequest
        :rtype: FleetDeploymentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_fleet_deployment_upgrade_endpoint.call_with_http_info(**kwargs)

    def create_fleet_schedule(
        self,
        body: FleetScheduleCreateRequest,
    ) -> FleetScheduleResponse:
        """Create a schedule.

        Create a new schedule for automated package upgrades.

        Schedules define when and how often to automatically deploy package upgrades to a fleet
        of hosts. Each schedule includes:

        * A filter query to select target hosts
        * A recurrence rule defining maintenance windows
        * A version strategy (e.g., always latest, or N versions behind latest)

        When the schedule triggers during a maintenance window, it automatically creates a
        deployment that upgrades the Datadog Agent to the specified version on all matching hosts.

        :param body: Request payload containing the schedule details.
        :type body: FleetScheduleCreateRequest
        :rtype: FleetScheduleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_fleet_schedule_endpoint.call_with_http_info(**kwargs)

    def delete_fleet_schedule(
        self,
        id: str,
    ) -> None:
        """Delete a schedule.

        Delete a schedule permanently.

        When you delete a schedule:

        * The schedule is permanently removed and will no longer create deployments
        * Any deployments already created by this schedule are not affected
        * This action cannot be undone

        If you want to temporarily stop a schedule from creating deployments, consider
        updating its status to "inactive" instead of deleting it.

        :param id: The unique identifier of the schedule to delete.
        :type id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._delete_fleet_schedule_endpoint.call_with_http_info(**kwargs)

    def get_fleet_agent_info(
        self,
        agent_key: str,
    ) -> FleetAgentInfoResponse:
        """Get detailed information about an agent.

        Retrieve detailed information about a specific Datadog Agent.
        This endpoint returns comprehensive information about an agent including:

        * Agent details and metadata
        * Configured integrations organized by status (working, warning, error, missing)
        * Detected integrations
        * Configuration files and layers

        :param agent_key: The unique identifier (agent key) for the Datadog Agent.
        :type agent_key: str
        :rtype: FleetAgentInfoResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["agent_key"] = agent_key

        return self._get_fleet_agent_info_endpoint.call_with_http_info(**kwargs)

    def get_fleet_deployment(
        self,
        deployment_id: str,
        *,
        limit: Union[int, UnsetType] = unset,
        page: Union[int, UnsetType] = unset,
    ) -> FleetDeploymentResponse:
        """Get a configuration deployment by ID.

        Retrieve detailed information about a specific deployment using its unique identifier.
        This endpoint returns comprehensive information about a deployment, including:

        * Deployment metadata (ID, type, filter query)
        * Total number of target hosts
        * Current high-level status (pending, running, succeeded, failed)
        * Estimated completion time
        * Configuration operations that were or are being applied
        * Detailed host list: A paginated array of hosts included in this deployment with individual
          host status, current package versions, and any errors

        The host list provides visibility into the per-host execution status, allowing you to:

        * Monitor which hosts have completed successfully
        * Identify hosts that are still in progress
        * Investigate failures on specific hosts
        * View current package versions installed on each host (including initial, target, and current
          versions for each package)

        Pagination: Use the ``limit`` and ``page`` query parameters to paginate through hosts. The response
        includes pagination metadata in the ``meta.hosts`` field with information about the current page,
        total pages, and total host count. The default page size is 50 hosts, with a maximum of 100.

        :param deployment_id: The unique identifier of the deployment to retrieve.
        :type deployment_id: str
        :param limit: Maximum number of hosts to return per page. Default is 50, maximum is 100.
        :type limit: int, optional
        :param page: Page index for pagination (zero-based). Use this to retrieve subsequent pages of hosts.
        :type page: int, optional
        :rtype: FleetDeploymentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["deployment_id"] = deployment_id

        if limit is not unset:
            kwargs["limit"] = limit

        if page is not unset:
            kwargs["page"] = page

        return self._get_fleet_deployment_endpoint.call_with_http_info(**kwargs)

    def get_fleet_schedule(
        self,
        id: str,
    ) -> FleetScheduleResponse:
        """Get a schedule by ID.

        Retrieve detailed information about a specific schedule using its unique identifier.

        This endpoint returns comprehensive information about a schedule, including:

        * Schedule metadata (ID, name, creation/update timestamps)
        * Filter query for selecting target hosts
        * Recurrence rule defining when deployments are triggered
        * Version strategy for package upgrades
        * Current status (active or inactive)

        :param id: The unique identifier of the schedule to retrieve.
        :type id: str
        :rtype: FleetScheduleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._get_fleet_schedule_endpoint.call_with_http_info(**kwargs)

    def list_fleet_agents(
        self,
        *,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        sort_attribute: Union[str, UnsetType] = unset,
        sort_descending: Union[bool, UnsetType] = unset,
        tags: Union[str, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
    ) -> FleetAgentsResponse:
        """List all Datadog Agents.

        Retrieve a paginated list of all Datadog Agents.
        This endpoint returns a paginated list of all Datadog Agents with support for pagination, sorting, and filtering.
        Use the ``page_number`` and ``page_size`` query parameters to paginate through results.

        :param page_number: Page number for pagination (must be greater than 0).
        :type page_number: int, optional
        :param page_size: Number of results per page (must be greater than 0 and less than or equal to 100).
        :type page_size: int, optional
        :param sort_attribute: Attribute to sort by.
        :type sort_attribute: str, optional
        :param sort_descending: Sort order (true for descending, false for ascending).
        :type sort_descending: bool, optional
        :param tags: Comma-separated list of tags to filter agents.
        :type tags: str, optional
        :param filter: Filter string for narrowing down agent results.
        :type filter: str, optional
        :rtype: FleetAgentsResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_number is not unset:
            kwargs["page_number"] = page_number

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if sort_attribute is not unset:
            kwargs["sort_attribute"] = sort_attribute

        if sort_descending is not unset:
            kwargs["sort_descending"] = sort_descending

        if tags is not unset:
            kwargs["tags"] = tags

        if filter is not unset:
            kwargs["filter"] = filter

        return self._list_fleet_agents_endpoint.call_with_http_info(**kwargs)

    def list_fleet_agent_versions(
        self,
    ) -> FleetAgentVersionsResponse:
        """List all available Agent versions.

        Retrieve a list of all available Datadog Agent versions.

        This endpoint returns the available Agent versions that can be deployed to your fleet.
        These versions are used when creating deployments or configuring schedules for
        automated Agent upgrades.

        :rtype: FleetAgentVersionsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_fleet_agent_versions_endpoint.call_with_http_info(**kwargs)

    def list_fleet_deployments(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
    ) -> FleetDeploymentsResponse:
        """List all deployments.

        Retrieve a list of all deployments for fleet automation.
        Use the ``page_size`` and ``page_offset`` parameters to paginate results.

        :param page_size: Number of deployments to return per page. Maximum value is 100.
        :type page_size: int, optional
        :param page_offset: Index of the first deployment to return. Use this with ``page_size`` to paginate through results.
        :type page_offset: int, optional
        :rtype: FleetDeploymentsResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        return self._list_fleet_deployments_endpoint.call_with_http_info(**kwargs)

    def list_fleet_schedules(
        self,
    ) -> FleetSchedulesResponse:
        """List all schedules.

        Retrieve a list of all schedules for automated fleet deployments.

        Schedules allow you to automate package upgrades by defining maintenance windows
        and recurrence rules. Each schedule automatically creates deployments based on its
        configuration.

        :rtype: FleetSchedulesResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_fleet_schedules_endpoint.call_with_http_info(**kwargs)

    def trigger_fleet_schedule(
        self,
        id: str,
    ) -> FleetDeploymentResponse:
        """Trigger a schedule deployment.

        Manually trigger a schedule to immediately create and start a deployment.

        This endpoint allows you to manually initiate a deployment using the schedule's
        configuration, without waiting for the next scheduled maintenance window. This is
        useful for:

        * Testing a schedule before it runs automatically
        * Performing an emergency update outside the regular maintenance window
        * Creating an ad-hoc deployment with the same settings as a schedule

        The deployment is created immediately with:

        * The same filter query as the schedule
        * The package version determined by the schedule's version strategy
        * All matching hosts as targets

        The manually triggered deployment is independent of the schedule and does not
        affect the schedule's normal recurrence pattern.

        :param id: The unique identifier of the schedule to trigger.
        :type id: str
        :rtype: FleetDeploymentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._trigger_fleet_schedule_endpoint.call_with_http_info(**kwargs)

    def update_fleet_schedule(
        self,
        id: str,
        body: FleetSchedulePatchRequest,
    ) -> FleetScheduleResponse:
        """Update a schedule.

        Partially update a schedule by providing only the fields you want to change.

        This endpoint allows you to modify specific attributes of a schedule without
        affecting other fields. Common use cases include:

        * Changing the schedule status between active and inactive
        * Updating the maintenance window times
        * Modifying the filter query to target different hosts
        * Adjusting the version strategy

        Only include the fields you want to update in the request body. All fields
        are optional in a PATCH request.

        :param id: The unique identifier of the schedule to update.
        :type id: str
        :param body: Request payload containing the fields to update.
        :type body: FleetSchedulePatchRequest
        :rtype: FleetScheduleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["body"] = body

        return self._update_fleet_schedule_endpoint.call_with_http_info(**kwargs)
