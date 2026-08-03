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
from datadog_api_client.v2.model.fleet_tracers_response import FleetTracersResponse
from datadog_api_client.v2.model.fleet_schedule_response import FleetScheduleResponse
from datadog_api_client.v2.model.fleet_schedule_create_request import FleetScheduleCreateRequest
from datadog_api_client.v2.model.fleet_schedule_patch_request import FleetSchedulePatchRequest
from datadog_api_client.v2.model.fleet_deployment_response import FleetDeploymentResponse
from datadog_api_client.v2.model.fleet_agent_versions_v2_response import FleetAgentVersionsV2Response
from datadog_api_client.v2.model.fleet_agents_v2_response import FleetAgentsV2Response
from datadog_api_client.v2.model.fleet_agent_detail_v2_response import FleetAgentDetailV2Response
from datadog_api_client.v2.model.fleet_deployments_v2_response import FleetDeploymentsV2Response
from datadog_api_client.v2.model.fleet_deployment_configure_v2_dry_run_response import (
    FleetDeploymentConfigureV2DryRunResponse,
)
from datadog_api_client.v2.model.fleet_deployment_configure_v2_create_request import (
    FleetDeploymentConfigureV2CreateRequest,
)
from datadog_api_client.v2.model.fleet_deployment_v2_create_response import FleetDeploymentV2CreateResponse
from datadog_api_client.v2.model.fleet_deployment_package_upgrade_v2_create_request import (
    FleetDeploymentPackageUpgradeV2CreateRequest,
)
from datadog_api_client.v2.model.fleet_deployment_v2_detail_response import FleetDeploymentV2DetailResponse
from datadog_api_client.v2.model.fleet_deployment_v2_cancel_response import FleetDeploymentV2CancelResponse
from datadog_api_client.v2.model.fleet_schedules_v2_response import FleetSchedulesV2Response
from datadog_api_client.v2.model.fleet_schedule_v2_response import FleetScheduleV2Response


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

        self._cancel_fleet_deployment_v2_endpoint = _Endpoint(
            settings={
                "response_type": (FleetDeploymentV2CancelResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/fleet/deployments/{deployment_id}/cancel",
                "operation_id": "cancel_fleet_deployment_v2",
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
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._create_fleet_deployment_configure_v2_endpoint = _Endpoint(
            settings={
                "response_type": (FleetDeploymentConfigureV2DryRunResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/fleet/deployments/configure",
                "operation_id": "create_fleet_deployment_configure_v2",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (FleetDeploymentConfigureV2CreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_fleet_deployment_upgrade_v2_endpoint = _Endpoint(
            settings={
                "response_type": (FleetDeploymentV2CreateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/fleet/deployments/upgrade",
                "operation_id": "create_fleet_deployment_upgrade_v2",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (FleetDeploymentPackageUpgradeV2CreateRequest,),
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

        self._get_fleet_agent_detail_v2_endpoint = _Endpoint(
            settings={
                "response_type": (FleetAgentDetailV2Response,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/fleet/agents/{agent_key}",
                "operation_id": "get_fleet_agent_detail_v2",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "agent_key": {
                    "required": True,
                    "validation": {},
                    "openapi_types": (str,),
                    "attribute": "agent_key",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_fleet_deployment_v2_endpoint = _Endpoint(
            settings={
                "response_type": (FleetDeploymentV2DetailResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/fleet/deployments/{deployment_id}",
                "operation_id": "get_fleet_deployment_v2",
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_fleet_schedule_v2_endpoint = _Endpoint(
            settings={
                "response_type": (FleetScheduleV2Response,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/fleet/schedules/{id}",
                "operation_id": "get_fleet_schedule_v2",
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

        self._list_fleet_agents_v2_endpoint = _Endpoint(
            settings={
                "response_type": (FleetAgentsV2Response,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/fleet/agents",
                "operation_id": "list_fleet_agents_v2",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_number": {
                    "validation": {
                        "inclusive_minimum": 0,
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
                "filter": {
                    "openapi_types": (str,),
                    "attribute": "filter",
                    "location": "query",
                },
                "tags": {
                    "openapi_types": (str,),
                    "attribute": "tags",
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_fleet_agent_tracers_endpoint = _Endpoint(
            settings={
                "response_type": (FleetTracersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/fleet/agents/{agent_key}/tracers",
                "operation_id": "list_fleet_agent_tracers",
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
                "page_number": {
                    "validation": {
                        "inclusive_minimum": 0,
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_fleet_agent_versions_v2_endpoint = _Endpoint(
            settings={
                "response_type": (FleetAgentVersionsV2Response,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/fleet/agent_versions",
                "operation_id": "list_fleet_agent_versions_v2",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_fleet_deployments_v2_endpoint = _Endpoint(
            settings={
                "response_type": (FleetDeploymentsV2Response,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/fleet/deployments",
                "operation_id": "list_fleet_deployments_v2",
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
                "page_number": {
                    "validation": {
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "page_number",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "ascending": {
                    "openapi_types": (bool,),
                    "attribute": "ascending",
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

        self._list_fleet_schedules_v2_endpoint = _Endpoint(
            settings={
                "response_type": (FleetSchedulesV2Response,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/fleet/schedules",
                "operation_id": "list_fleet_schedules_v2",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_fleet_tracers_endpoint = _Endpoint(
            settings={
                "response_type": (FleetTracersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/unstable/fleet/tracers",
                "operation_id": "list_fleet_tracers",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_number": {
                    "validation": {
                        "inclusive_minimum": 0,
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

    def cancel_fleet_deployment_v2(
        self,
        deployment_id: str,
    ) -> FleetDeploymentV2CancelResponse:
        """Cancel a deployment.

        Cancel an active deployment and stop all pending operations.
        When you cancel a deployment:

        * All pending operations on hosts that haven't started yet are stopped.
        * Operations currently in progress on hosts may complete or be interrupted, depending on their current status.
        * Configuration changes or package upgrades already applied to hosts are not rolled back.

        After cancellation, you can view the final state of the deployment using the GET endpoint to see which hosts
        were successfully updated before the cancellation.

        Only deployments with a ``pending`` or ``running`` status can be canceled. Returns a 400 if the deployment is not in a cancelable status. Returns a 404 if no deployment matches the specified ID or if you do not have access to it.

        :param deployment_id: The unique identifier of the deployment to cancel.
        :type deployment_id: str
        :rtype: FleetDeploymentV2CancelResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["deployment_id"] = deployment_id

        return self._cancel_fleet_deployment_v2_endpoint.call_with_http_info(**kwargs)

    def create_fleet_deployment_configure_v2(
        self,
        body: FleetDeploymentConfigureV2CreateRequest,
    ) -> FleetDeploymentConfigureV2DryRunResponse:
        """Create a configuration deployment.

        Create a new deployment to apply configuration changes
        to a fleet of hosts matching the specified filter query.

        This endpoint supports two types of configuration operations:

        * ``merge-patch`` : Merges the provided patch data with the existing configuration file,
          creating the file if it doesn't exist.
        * ``delete`` : Removes the specified configuration file from the target hosts.

        You can optionally use ``target_packages`` to apply the configuration change only to specific package versions.

        The deployment is created and started automatically. You can specify multiple configuration
        operations to execute in order on each target host. Use the filter query to target
        specific hosts using the Datadog query syntax.

        Set ``dry_run`` to ``true`` to validate the configuration and resolve target hosts and packages without deploying anything. A dry run returns a 200 with the validation result instead of creating and starting a deployment.

        Returns a 400 if ``filter_query`` or ``config_operations`` is missing, a target package is missing a name or version or cannot be resolved, the configuration fails validation, or the filter query does not match any host eligible for the deployment.

        :param body: Request payload containing the deployment details.
        :type body: FleetDeploymentConfigureV2CreateRequest
        :rtype: FleetDeploymentConfigureV2DryRunResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_fleet_deployment_configure_v2_endpoint.call_with_http_info(**kwargs)

    def create_fleet_deployment_upgrade_v2(
        self,
        body: FleetDeploymentPackageUpgradeV2CreateRequest,
    ) -> FleetDeploymentV2CreateResponse:
        """Upgrade hosts.

        Create and immediately start a new package upgrade
        on hosts matching the specified filter query.

        This endpoint allows you to upgrade the Datadog Agent to a specific version
        on hosts matching the specified filter query.

        The deployment is created and started automatically. The system:

        #. Identifies all hosts matching the filter query.
        #. Validates that the specified version is available.
        #. Begins rolling out the package upgrade to the target hosts.

        Returns a 400 if ``filter_query`` or ``target_packages`` is missing, a target package is missing a name or version, or the filter query does not match any host eligible for the upgrade. Returns a 409 if a conflicting upgrade is already running on one or more target hosts.

        :param body: Request payload containing the package upgrade details.
        :type body: FleetDeploymentPackageUpgradeV2CreateRequest
        :rtype: FleetDeploymentV2CreateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_fleet_deployment_upgrade_v2_endpoint.call_with_http_info(**kwargs)

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

    def get_fleet_agent_detail_v2(
        self,
        agent_key: str,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> FleetAgentDetailV2Response:
        """Get detailed information about an agent.

        Retrieve detailed information about a specific Datadog Agent.

        By default, only ``agent_infos`` is returned. Use the ``include`` query parameter to
        request additional data: ``integrations`` and/or ``configuration_files``.

        :param agent_key: The unique identifier (Agent key) for the Datadog Agent. Must be a 32-character lowercase hexadecimal string.
        :type agent_key: str
        :param include: Comma-separated list of additional fields to include in the response. Valid values are ``integrations`` and ``configuration_files``. Omitting this parameter returns only ``agent_infos``. Unrecognized values are silently ignored rather than causing an error.
        :type include: str, optional
        :rtype: FleetAgentDetailV2Response
        """
        kwargs: Dict[str, Any] = {}
        kwargs["agent_key"] = agent_key

        if include is not unset:
            kwargs["include"] = include

        return self._get_fleet_agent_detail_v2_endpoint.call_with_http_info(**kwargs)

    def get_fleet_deployment_v2(
        self,
        deployment_id: str,
    ) -> FleetDeploymentV2DetailResponse:
        """Get a deployment by ID.

        Retrieve detailed information about a specific deployment, including its current status,
        configuration operations, and per-host execution status.

        Returns a 404 if no deployment matches the given ID or if you do not have access to it.

        :param deployment_id: The unique identifier of the deployment to retrieve.
        :type deployment_id: str
        :rtype: FleetDeploymentV2DetailResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["deployment_id"] = deployment_id

        return self._get_fleet_deployment_v2_endpoint.call_with_http_info(**kwargs)

    def get_fleet_schedule_v2(
        self,
        id: str,
    ) -> FleetScheduleV2Response:
        """Get a schedule by ID.

        Retrieve detailed information about a specific schedule by its unique identifier.

        :param id: The unique identifier of the schedule to retrieve.
        :type id: str
        :rtype: FleetScheduleV2Response
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._get_fleet_schedule_v2_endpoint.call_with_http_info(**kwargs)

    def list_fleet_agents_v2(
        self,
        *,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
        tags: Union[str, UnsetType] = unset,
        sort_attribute: Union[str, UnsetType] = unset,
        sort_descending: Union[bool, UnsetType] = unset,
    ) -> FleetAgentsV2Response:
        """List all Datadog Agents.

        Retrieve a paginated list of Datadog Agents.

        Returns agents with support for pagination, sorting, and filtering.
        Use ``page_number`` and ``page_size`` to navigate pages, ``filter`` to narrow by field values,
        and ``tags`` to filter by agent tags.

        :param page_number: Page number for pagination, starting at 0.
        :type page_number: int, optional
        :param page_size: Number of agents to return per page. Maximum value is 100. Defaults to 10.
        :type page_size: int, optional
        :param filter: Filter string to narrow down agent results.
        :type filter: str, optional
        :param tags: Comma-separated list of tag keys to select which tags are included in each agent's ``tags`` attribute. Does not filter which agents are returned.
        :type tags: str, optional
        :param sort_attribute: Agent attribute to sort results by. Must be a supported attribute name; unsupported values return a 400 error.
        :type sort_attribute: str, optional
        :param sort_descending: Set to ``true`` to sort results in descending order. Defaults to ascending.
        :type sort_descending: bool, optional
        :rtype: FleetAgentsV2Response
        """
        kwargs: Dict[str, Any] = {}
        if page_number is not unset:
            kwargs["page_number"] = page_number

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if filter is not unset:
            kwargs["filter"] = filter

        if tags is not unset:
            kwargs["tags"] = tags

        if sort_attribute is not unset:
            kwargs["sort_attribute"] = sort_attribute

        if sort_descending is not unset:
            kwargs["sort_descending"] = sort_descending

        return self._list_fleet_agents_v2_endpoint.call_with_http_info(**kwargs)

    def list_fleet_agent_tracers(
        self,
        agent_key: str,
        *,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        sort_attribute: Union[str, UnsetType] = unset,
        sort_descending: Union[bool, UnsetType] = unset,
    ) -> FleetTracersResponse:
        """List tracers for a specific agent.

        Retrieve a paginated list of tracers for a specific agent.

        This endpoint returns tracers associated with a given agent key, identified by the
        agent's hostname. Use this to discover telemetry-derived service names for a particular host.

        :param agent_key: The unique identifier (agent key) for the Datadog Agent.
        :type agent_key: str
        :param page_number: Page number for pagination (starts at 0).
        :type page_number: int, optional
        :param page_size: Number of results per page (must be greater than 0 and less than or equal to 100).
        :type page_size: int, optional
        :param sort_attribute: Attribute to sort by.
        :type sort_attribute: str, optional
        :param sort_descending: Sort order (true for descending, false for ascending).
        :type sort_descending: bool, optional
        :rtype: FleetTracersResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["agent_key"] = agent_key

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if sort_attribute is not unset:
            kwargs["sort_attribute"] = sort_attribute

        if sort_descending is not unset:
            kwargs["sort_descending"] = sort_descending

        return self._list_fleet_agent_tracers_endpoint.call_with_http_info(**kwargs)

    def list_fleet_agent_versions_v2(
        self,
    ) -> FleetAgentVersionsV2Response:
        """List available Datadog Agent versions.

        Retrieve the list of Datadog Agent versions available for deployment.

        Returns ``200`` with an empty ``data`` array if the Agent package exists in the catalog
        but has no available versions, and ``404`` only if the Agent package itself is absent
        from the catalog.

        :rtype: FleetAgentVersionsV2Response
        """
        kwargs: Dict[str, Any] = {}
        return self._list_fleet_agent_versions_v2_endpoint.call_with_http_info(**kwargs)

    def list_fleet_deployments_v2(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        ascending: Union[bool, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
    ) -> FleetDeploymentsV2Response:
        """List all deployments.

        Retrieve a paginated list of all deployments for fleet automation.

        :param page_size: Number of deployments to return per page. Maximum value is 100.
        :type page_size: int, optional
        :param page_number: Page number for pagination, starting at 0.
        :type page_number: int, optional
        :param sort: Field to sort results by (for example, ``start_date`` ). Must be a supported field
            name; unsupported values return a 400 error.
        :type sort: str, optional
        :param ascending: Set to ``true`` to sort in ascending order. This setting has no effect unless ``sort`` is also set.
            Defaults to descending order.
        :type ascending: bool, optional
        :param filter: Query used to filter deployments. Uses the Datadog query syntax. Filtering on an
            unsupported field returns a 400 error. For example:

            * ``status:failed`` or ``status:done_with_errors`` : deployments that need investigation.
            * ``status:running`` : deployments currently in flight.
            * ``update_type:update_package`` or ``update_type:update_config_operations`` : deployments of a given type.
        :type filter: str, optional
        :rtype: FleetDeploymentsV2Response
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if sort is not unset:
            kwargs["sort"] = sort

        if ascending is not unset:
            kwargs["ascending"] = ascending

        if filter is not unset:
            kwargs["filter"] = filter

        return self._list_fleet_deployments_v2_endpoint.call_with_http_info(**kwargs)

    def list_fleet_schedules_v2(
        self,
    ) -> FleetSchedulesV2Response:
        """List all schedules.

        Retrieve all upgrade schedules for the organization.

        Schedules automate package upgrades by defining maintenance windows and recurrence rules.
        Each schedule automatically creates deployments based on its configuration.

        :rtype: FleetSchedulesV2Response
        """
        kwargs: Dict[str, Any] = {}
        return self._list_fleet_schedules_v2_endpoint.call_with_http_info(**kwargs)

    def list_fleet_tracers(
        self,
        *,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        sort_attribute: Union[str, UnsetType] = unset,
        sort_descending: Union[bool, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
    ) -> FleetTracersResponse:
        """List all fleet tracers.

        Retrieve a paginated list of all fleet tracers.

        This endpoint returns telemetry-derived service names from the SDK telemetry pipeline.
        These names may differ from span-derived names in APM and are useful for querying
        service library configurations.
        Use the ``page_number`` and ``page_size`` query parameters to paginate through results.

        :param page_number: Page number for pagination (starts at 0).
        :type page_number: int, optional
        :param page_size: Number of results per page (must be greater than 0 and less than or equal to 100).
        :type page_size: int, optional
        :param sort_attribute: Attribute to sort by.
        :type sort_attribute: str, optional
        :param sort_descending: Sort order (true for descending, false for ascending).
        :type sort_descending: bool, optional
        :param filter: Filter string for narrowing down tracer results.
        :type filter: str, optional
        :rtype: FleetTracersResponse
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

        if filter is not unset:
            kwargs["filter"] = filter

        return self._list_fleet_tracers_endpoint.call_with_http_info(**kwargs)

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
