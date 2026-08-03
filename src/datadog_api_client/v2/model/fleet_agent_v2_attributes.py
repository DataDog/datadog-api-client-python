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
    from datadog_api_client.v2.model.fleet_agent_v2_attributes_instrumentation_status import (
        FleetAgentV2AttributesInstrumentationStatus,
    )
    from datadog_api_client.v2.model.fleet_agent_attributes_tags_items import FleetAgentAttributesTagsItems


class FleetAgentV2Attributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_agent_v2_attributes_instrumentation_status import (
            FleetAgentV2AttributesInstrumentationStatus,
        )
        from datadog_api_client.v2.model.fleet_agent_attributes_tags_items import FleetAgentAttributesTagsItems

        return {
            "agent_version": (str,),
            "api_key_name": (str,),
            "api_key_uuid": (str,),
            "cloud_provider": (str,),
            "cluster_name": (str,),
            "datadog_data_center": (str,),
            "ecs_fargate_cluster_name": (str,),
            "ecs_fargate_task_arn": (str,),
            "enabled_products": ([str],),
            "env": ([str],),
            "first_seen_at": (int,),
            "fleet_policies": ([str],),
            "hostname": (str,),
            "instrumentation_error_counts": (int,),
            "instrumentation_status": (FleetAgentV2AttributesInstrumentationStatus,),
            "integrations": ([str],),
            "ip_addresses": ([str],),
            "is_single_step_instrumentation_enabled": (bool,),
            "last_restart_at": (int,),
            "os": (str,),
            "otel_collector_deployment_types": ([str],),
            "otel_collector_distributions": ([str],),
            "otel_collector_version": (str,),
            "otel_collector_versions": ([str],),
            "otel_resource_attributes": ([str],),
            "pod_name": (str,),
            "remote_agent_management": (str,),
            "remote_config_status": (str,),
            "services": ([str],),
            "tags": ([FleetAgentAttributesTagsItems],),
            "team": (str,),
        }

    attribute_map = {
        "agent_version": "agent_version",
        "api_key_name": "api_key_name",
        "api_key_uuid": "api_key_uuid",
        "cloud_provider": "cloud_provider",
        "cluster_name": "cluster_name",
        "datadog_data_center": "datadog_data_center",
        "ecs_fargate_cluster_name": "ecs_fargate_cluster_name",
        "ecs_fargate_task_arn": "ecs_fargate_task_arn",
        "enabled_products": "enabled_products",
        "env": "env",
        "first_seen_at": "first_seen_at",
        "fleet_policies": "fleet_policies",
        "hostname": "hostname",
        "instrumentation_error_counts": "instrumentation_error_counts",
        "instrumentation_status": "instrumentation_status",
        "integrations": "integrations",
        "ip_addresses": "ip_addresses",
        "is_single_step_instrumentation_enabled": "is_single_step_instrumentation_enabled",
        "last_restart_at": "last_restart_at",
        "os": "os",
        "otel_collector_deployment_types": "otel_collector_deployment_types",
        "otel_collector_distributions": "otel_collector_distributions",
        "otel_collector_version": "otel_collector_version",
        "otel_collector_versions": "otel_collector_versions",
        "otel_resource_attributes": "otel_resource_attributes",
        "pod_name": "pod_name",
        "remote_agent_management": "remote_agent_management",
        "remote_config_status": "remote_config_status",
        "services": "services",
        "tags": "tags",
        "team": "team",
    }

    def __init__(
        self_,
        agent_version: Union[str, UnsetType] = unset,
        api_key_name: Union[str, UnsetType] = unset,
        api_key_uuid: Union[str, UnsetType] = unset,
        cloud_provider: Union[str, UnsetType] = unset,
        cluster_name: Union[str, UnsetType] = unset,
        datadog_data_center: Union[str, UnsetType] = unset,
        ecs_fargate_cluster_name: Union[str, UnsetType] = unset,
        ecs_fargate_task_arn: Union[str, UnsetType] = unset,
        enabled_products: Union[List[str], UnsetType] = unset,
        env: Union[List[str], UnsetType] = unset,
        first_seen_at: Union[int, UnsetType] = unset,
        fleet_policies: Union[List[str], UnsetType] = unset,
        hostname: Union[str, UnsetType] = unset,
        instrumentation_error_counts: Union[int, UnsetType] = unset,
        instrumentation_status: Union[FleetAgentV2AttributesInstrumentationStatus, UnsetType] = unset,
        integrations: Union[List[str], UnsetType] = unset,
        ip_addresses: Union[List[str], UnsetType] = unset,
        is_single_step_instrumentation_enabled: Union[bool, UnsetType] = unset,
        last_restart_at: Union[int, UnsetType] = unset,
        os: Union[str, UnsetType] = unset,
        otel_collector_deployment_types: Union[List[str], UnsetType] = unset,
        otel_collector_distributions: Union[List[str], UnsetType] = unset,
        otel_collector_version: Union[str, UnsetType] = unset,
        otel_collector_versions: Union[List[str], UnsetType] = unset,
        otel_resource_attributes: Union[List[str], UnsetType] = unset,
        pod_name: Union[str, UnsetType] = unset,
        remote_agent_management: Union[str, UnsetType] = unset,
        remote_config_status: Union[str, UnsetType] = unset,
        services: Union[List[str], UnsetType] = unset,
        tags: Union[List[FleetAgentAttributesTagsItems], UnsetType] = unset,
        team: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Datadog Agent in the v2 list response.

        :param agent_version: The Datadog Agent version.
        :type agent_version: str, optional

        :param api_key_name: The name of the API key used by the agent, if available and not redacted.
        :type api_key_name: str, optional

        :param api_key_uuid: The UUID of the API key used by the agent.
        :type api_key_uuid: str, optional

        :param cloud_provider: The cloud provider where the agent is running.
        :type cloud_provider: str, optional

        :param cluster_name: The Kubernetes cluster name, if the agent runs in a cluster.
        :type cluster_name: str, optional

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

        :param first_seen_at: Unix timestamp when the agent was first seen.
        :type first_seen_at: int, optional

        :param fleet_policies: Identifiers of fleet policies applied to the agent.
        :type fleet_policies: [str], optional

        :param hostname: The hostname of the agent.
        :type hostname: str, optional

        :param instrumentation_error_counts: Number of instrumentation errors on the agent. Absent from the response when the count is zero.
        :type instrumentation_error_counts: int, optional

        :param instrumentation_status: The single-step instrumentation status of the Agent.
        :type instrumentation_status: FleetAgentV2AttributesInstrumentationStatus, optional

        :param integrations: Names of integrations configured on the agent.
        :type integrations: [str], optional

        :param ip_addresses: IP addresses of the agent host.
        :type ip_addresses: [str], optional

        :param is_single_step_instrumentation_enabled: Whether single-step instrumentation is enabled on the agent.
        :type is_single_step_instrumentation_enabled: bool, optional

        :param last_restart_at: Unix timestamp of the last agent restart.
        :type last_restart_at: int, optional

        :param os: The operating system of the host.
        :type os: str, optional

        :param otel_collector_deployment_types: OpenTelemetry collector deployment types associated with the agent.
        :type otel_collector_deployment_types: [str], optional

        :param otel_collector_distributions: OpenTelemetry collector distributions associated with the agent.
        :type otel_collector_distributions: [str], optional

        :param otel_collector_version: The primary OpenTelemetry collector version, if applicable.
        :type otel_collector_version: str, optional

        :param otel_collector_versions: All OpenTelemetry collector versions associated with the agent.
        :type otel_collector_versions: [str], optional

        :param otel_resource_attributes: OpenTelemetry resource attributes reported by the agent.
        :type otel_resource_attributes: [str], optional

        :param pod_name: The Kubernetes pod name, if the agent runs as a pod.
        :type pod_name: str, optional

        :param remote_agent_management: The remote agent management status.
        :type remote_agent_management: str, optional

        :param remote_config_status: The remote configuration connection status of the agent.
        :type remote_config_status: str, optional

        :param services: Services running on the agent.
        :type services: [str], optional

        :param tags: Tags associated with the agent. Returned as an empty array when the agent has no tags.
        :type tags: [FleetAgentAttributesTagsItems], optional

        :param team: The team associated with the agent.
        :type team: str, optional
        """
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
        if fleet_policies is not unset:
            kwargs["fleet_policies"] = fleet_policies
        if hostname is not unset:
            kwargs["hostname"] = hostname
        if instrumentation_error_counts is not unset:
            kwargs["instrumentation_error_counts"] = instrumentation_error_counts
        if instrumentation_status is not unset:
            kwargs["instrumentation_status"] = instrumentation_status
        if integrations is not unset:
            kwargs["integrations"] = integrations
        if ip_addresses is not unset:
            kwargs["ip_addresses"] = ip_addresses
        if is_single_step_instrumentation_enabled is not unset:
            kwargs["is_single_step_instrumentation_enabled"] = is_single_step_instrumentation_enabled
        if last_restart_at is not unset:
            kwargs["last_restart_at"] = last_restart_at
        if os is not unset:
            kwargs["os"] = os
        if otel_collector_deployment_types is not unset:
            kwargs["otel_collector_deployment_types"] = otel_collector_deployment_types
        if otel_collector_distributions is not unset:
            kwargs["otel_collector_distributions"] = otel_collector_distributions
        if otel_collector_version is not unset:
            kwargs["otel_collector_version"] = otel_collector_version
        if otel_collector_versions is not unset:
            kwargs["otel_collector_versions"] = otel_collector_versions
        if otel_resource_attributes is not unset:
            kwargs["otel_resource_attributes"] = otel_resource_attributes
        if pod_name is not unset:
            kwargs["pod_name"] = pod_name
        if remote_agent_management is not unset:
            kwargs["remote_agent_management"] = remote_agent_management
        if remote_config_status is not unset:
            kwargs["remote_config_status"] = remote_config_status
        if services is not unset:
            kwargs["services"] = services
        if tags is not unset:
            kwargs["tags"] = tags
        if team is not unset:
            kwargs["team"] = team
        super().__init__(kwargs)
