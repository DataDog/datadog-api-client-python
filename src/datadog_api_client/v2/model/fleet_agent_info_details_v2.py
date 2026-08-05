# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.fleet_otel_collector import FleetOtelCollector


class FleetAgentInfoDetailsV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_otel_collector import FleetOtelCollector

        return {
            "active_ha_agent": (str,),
            "agent_version": (str,),
            "api_key_name": (str,),
            "api_key_uuid": (str,),
            "cloud_provider": (str,),
            "cluster_name": (str,),
            "config_id": (str,),
            "datadog_agent_key": (str,),
            "datadog_data_center": (str,),
            "ecs_fargate_cluster_name": (str,),
            "ecs_fargate_task_arn": (str,),
            "enabled_products": ([str],),
            "env": ([str],),
            "first_seen_at": (int,),
            "ha_agent_hosts": ([str],),
            "ha_agent_state": (str,),
            "hostname": (str,),
            "hostname_aliases": ([str],),
            "install_method_installer_version": (str,),
            "install_method_tool": (str,),
            "ip_addresses": ([str],),
            "is_single_step_instrumentation_enabled": (bool,),
            "last_restart_at": (int,),
            "os": (str,),
            "os_version": (str,),
            "otel_collector_deployment_types": ([str],),
            "otel_collector_distributions": ([str],),
            "otel_collector_versions": ([str],),
            "otel_collectors": ([FleetOtelCollector],),
            "otel_resource_attributes": ([str],),
            "pod_name": (str,),
            "preferred_ha_active_agent": (str,),
            "python_version": (str,),
            "region": ([str],),
            "remote_agent_management": (str,),
            "remote_config_status": (str,),
            "services": ([str],),
            "support_agent_upgrade": (bool,),
            "tags": ([str],),
            "team": (str,),
        }

    attribute_map = {
        "active_ha_agent": "active_ha_agent",
        "agent_version": "agent_version",
        "api_key_name": "api_key_name",
        "api_key_uuid": "api_key_uuid",
        "cloud_provider": "cloud_provider",
        "cluster_name": "cluster_name",
        "config_id": "config_id",
        "datadog_agent_key": "datadog_agent_key",
        "datadog_data_center": "datadog_data_center",
        "ecs_fargate_cluster_name": "ecs_fargate_cluster_name",
        "ecs_fargate_task_arn": "ecs_fargate_task_arn",
        "enabled_products": "enabled_products",
        "env": "env",
        "first_seen_at": "first_seen_at",
        "ha_agent_hosts": "ha_agent_hosts",
        "ha_agent_state": "ha_agent_state",
        "hostname": "hostname",
        "hostname_aliases": "hostname_aliases",
        "install_method_installer_version": "install_method_installer_version",
        "install_method_tool": "install_method_tool",
        "ip_addresses": "ip_addresses",
        "is_single_step_instrumentation_enabled": "is_single_step_instrumentation_enabled",
        "last_restart_at": "last_restart_at",
        "os": "os",
        "os_version": "os_version",
        "otel_collector_deployment_types": "otel_collector_deployment_types",
        "otel_collector_distributions": "otel_collector_distributions",
        "otel_collector_versions": "otel_collector_versions",
        "otel_collectors": "otel_collectors",
        "otel_resource_attributes": "otel_resource_attributes",
        "pod_name": "pod_name",
        "preferred_ha_active_agent": "preferred_ha_active_agent",
        "python_version": "python_version",
        "region": "region",
        "remote_agent_management": "remote_agent_management",
        "remote_config_status": "remote_config_status",
        "services": "services",
        "support_agent_upgrade": "support_agent_upgrade",
        "tags": "tags",
        "team": "team",
    }

    def __init__(
        self_,
        active_ha_agent: Union[str, UnsetType] = unset,
        agent_version: Union[str, UnsetType] = unset,
        api_key_name: Union[str, UnsetType] = unset,
        api_key_uuid: Union[str, UnsetType] = unset,
        cloud_provider: Union[str, UnsetType] = unset,
        cluster_name: Union[str, UnsetType] = unset,
        config_id: Union[str, UnsetType] = unset,
        datadog_agent_key: Union[str, UnsetType] = unset,
        datadog_data_center: Union[str, UnsetType] = unset,
        ecs_fargate_cluster_name: Union[str, UnsetType] = unset,
        ecs_fargate_task_arn: Union[str, UnsetType] = unset,
        enabled_products: Union[List[str], UnsetType] = unset,
        env: Union[List[str], UnsetType] = unset,
        first_seen_at: Union[int, UnsetType] = unset,
        ha_agent_hosts: Union[List[str], UnsetType] = unset,
        ha_agent_state: Union[str, UnsetType] = unset,
        hostname: Union[str, UnsetType] = unset,
        hostname_aliases: Union[List[str], UnsetType] = unset,
        install_method_installer_version: Union[str, UnsetType] = unset,
        install_method_tool: Union[str, UnsetType] = unset,
        ip_addresses: Union[List[str], UnsetType] = unset,
        is_single_step_instrumentation_enabled: Union[bool, UnsetType] = unset,
        last_restart_at: Union[int, UnsetType] = unset,
        os: Union[str, UnsetType] = unset,
        os_version: Union[str, UnsetType] = unset,
        otel_collector_deployment_types: Union[List[str], UnsetType] = unset,
        otel_collector_distributions: Union[List[str], UnsetType] = unset,
        otel_collector_versions: Union[List[str], UnsetType] = unset,
        otel_collectors: Union[List[FleetOtelCollector], UnsetType] = unset,
        otel_resource_attributes: Union[List[str], UnsetType] = unset,
        pod_name: Union[str, UnsetType] = unset,
        preferred_ha_active_agent: Union[str, UnsetType] = unset,
        python_version: Union[str, UnsetType] = unset,
        region: Union[List[str], UnsetType] = unset,
        remote_agent_management: Union[str, UnsetType] = unset,
        remote_config_status: Union[str, UnsetType] = unset,
        services: Union[List[str], UnsetType] = unset,
        support_agent_upgrade: Union[bool, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        team: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Detailed information about a Datadog Agent.

        :param active_ha_agent: The currently active agent in the high-availability group.
        :type active_ha_agent: str, optional

        :param agent_version: The Datadog Agent version.
        :type agent_version: str, optional

        :param api_key_name: The API key name (if available and not redacted).
        :type api_key_name: str, optional

        :param api_key_uuid: The API key UUID.
        :type api_key_uuid: str, optional

        :param cloud_provider: The cloud provider where the agent is running.
        :type cloud_provider: str, optional

        :param cluster_name: Kubernetes cluster name (if applicable).
        :type cluster_name: str, optional

        :param config_id: The configuration identifier applied to the agent.
        :type config_id: str, optional

        :param datadog_agent_key: The unique agent key identifier.
        :type datadog_agent_key: str, optional

        :param datadog_data_center: The Datadog data center the agent reports to.
        :type datadog_data_center: str, optional

        :param ecs_fargate_cluster_name: The ECS Fargate cluster name, if the agent runs in an ECS Fargate environment.
        :type ecs_fargate_cluster_name: str, optional

        :param ecs_fargate_task_arn: The ECS Fargate task ARN, if the agent runs in an ECS Fargate environment.
        :type ecs_fargate_task_arn: str, optional

        :param enabled_products: Datadog products enabled on the agent.
        :type enabled_products: [str], optional

        :param env: Environments the agent is reporting from.
        :type env: [str], optional

        :param first_seen_at: Timestamp when the agent was first seen.
        :type first_seen_at: int, optional

        :param ha_agent_hosts: Hosts participating in the agent's high-availability group.
        :type ha_agent_hosts: [str], optional

        :param ha_agent_state: The high-availability state of the agent.
        :type ha_agent_state: str, optional

        :param hostname: The hostname of the agent.
        :type hostname: str, optional

        :param hostname_aliases: Alternative hostname list for the agent.
        :type hostname_aliases: [str], optional

        :param install_method_installer_version: The version of the installer used.
        :type install_method_installer_version: str, optional

        :param install_method_tool: The tool used to install the agent.
        :type install_method_tool: str, optional

        :param ip_addresses: IP addresses of the agent.
        :type ip_addresses: [str], optional

        :param is_single_step_instrumentation_enabled: Whether single-step instrumentation is enabled.
        :type is_single_step_instrumentation_enabled: bool, optional

        :param last_restart_at: Timestamp of the last agent restart.
        :type last_restart_at: int, optional

        :param os: The operating system.
        :type os: str, optional

        :param os_version: The operating system version.
        :type os_version: str, optional

        :param otel_collector_deployment_types: OpenTelemetry collector deployment types associated with the agent.
        :type otel_collector_deployment_types: [str], optional

        :param otel_collector_distributions: OpenTelemetry collector distributions associated with the agent.
        :type otel_collector_distributions: [str], optional

        :param otel_collector_versions: List of OpenTelemetry collector versions (if applicable).
        :type otel_collector_versions: [str], optional

        :param otel_collectors: OpenTelemetry collectors associated with the agent (if applicable).
        :type otel_collectors: [FleetOtelCollector], optional

        :param otel_resource_attributes: OpenTelemetry resource attributes reported by the agent.
        :type otel_resource_attributes: [str], optional

        :param pod_name: Kubernetes pod name (if applicable).
        :type pod_name: str, optional

        :param preferred_ha_active_agent: The preferred active agent in the high-availability group.
        :type preferred_ha_active_agent: str, optional

        :param python_version: The Python version used by the agent.
        :type python_version: str, optional

        :param region: Regions where the agent is running.
        :type region: [str], optional

        :param remote_agent_management: Remote agent management status.
        :type remote_agent_management: str, optional

        :param remote_config_status: Remote configuration status.
        :type remote_config_status: str, optional

        :param services: Services running on the agent.
        :type services: [str], optional

        :param support_agent_upgrade: Whether the agent supports remote agent upgrade.
        :type support_agent_upgrade: bool, optional

        :param tags: Tags associated with the agent.
        :type tags: [str], optional

        :param team: Team associated with the agent.
        :type team: str, optional
        """
        if active_ha_agent is not unset:
            kwargs["active_ha_agent"] = active_ha_agent
        if agent_version is not unset:
            kwargs["agent_version"] = agent_version
        if api_key_name is not unset:
            kwargs["api_key_name"] = api_key_name
        if api_key_uuid is not unset:
            kwargs["api_key_uuid"] = api_key_uuid
        if cloud_provider is not unset:
            kwargs["cloud_provider"] = cloud_provider
        if cluster_name is not unset:
            kwargs["cluster_name"] = cluster_name
        if config_id is not unset:
            kwargs["config_id"] = config_id
        if datadog_agent_key is not unset:
            kwargs["datadog_agent_key"] = datadog_agent_key
        if datadog_data_center is not unset:
            kwargs["datadog_data_center"] = datadog_data_center
        if ecs_fargate_cluster_name is not unset:
            kwargs["ecs_fargate_cluster_name"] = ecs_fargate_cluster_name
        if ecs_fargate_task_arn is not unset:
            kwargs["ecs_fargate_task_arn"] = ecs_fargate_task_arn
        if enabled_products is not unset:
            kwargs["enabled_products"] = enabled_products
        if env is not unset:
            kwargs["env"] = env
        if first_seen_at is not unset:
            kwargs["first_seen_at"] = first_seen_at
        if ha_agent_hosts is not unset:
            kwargs["ha_agent_hosts"] = ha_agent_hosts
        if ha_agent_state is not unset:
            kwargs["ha_agent_state"] = ha_agent_state
        if hostname is not unset:
            kwargs["hostname"] = hostname
        if hostname_aliases is not unset:
            kwargs["hostname_aliases"] = hostname_aliases
        if install_method_installer_version is not unset:
            kwargs["install_method_installer_version"] = install_method_installer_version
        if install_method_tool is not unset:
            kwargs["install_method_tool"] = install_method_tool
        if ip_addresses is not unset:
            kwargs["ip_addresses"] = ip_addresses
        if is_single_step_instrumentation_enabled is not unset:
            kwargs["is_single_step_instrumentation_enabled"] = is_single_step_instrumentation_enabled
        if last_restart_at is not unset:
            kwargs["last_restart_at"] = last_restart_at
        if os is not unset:
            kwargs["os"] = os
        if os_version is not unset:
            kwargs["os_version"] = os_version
        if otel_collector_deployment_types is not unset:
            kwargs["otel_collector_deployment_types"] = otel_collector_deployment_types
        if otel_collector_distributions is not unset:
            kwargs["otel_collector_distributions"] = otel_collector_distributions
        if otel_collector_versions is not unset:
            kwargs["otel_collector_versions"] = otel_collector_versions
        if otel_collectors is not unset:
            kwargs["otel_collectors"] = otel_collectors
        if otel_resource_attributes is not unset:
            kwargs["otel_resource_attributes"] = otel_resource_attributes
        if pod_name is not unset:
            kwargs["pod_name"] = pod_name
        if preferred_ha_active_agent is not unset:
            kwargs["preferred_ha_active_agent"] = preferred_ha_active_agent
        if python_version is not unset:
            kwargs["python_version"] = python_version
        if region is not unset:
            kwargs["region"] = region
        if remote_agent_management is not unset:
            kwargs["remote_agent_management"] = remote_agent_management
        if remote_config_status is not unset:
            kwargs["remote_config_status"] = remote_config_status
        if services is not unset:
            kwargs["services"] = services
        if support_agent_upgrade is not unset:
            kwargs["support_agent_upgrade"] = support_agent_upgrade
        if tags is not unset:
            kwargs["tags"] = tags
        if team is not unset:
            kwargs["team"] = team
        super().__init__(kwargs)
