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
    from datadog_api_client.v2.model.fleet_agent_attributes_tags_items import FleetAgentAttributesTagsItems


class FleetAgentAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_agent_attributes_tags_items import FleetAgentAttributesTagsItems

        return {
            "agent_version": (str,),
            "api_key_name": (str,),
            "api_key_uuid": (str,),
            "cloud_provider": (str,),
            "cluster_name": (str,),
            "datadog_agent_key": (str,),
            "enabled_products": ([str],),
            "envs": ([str],),
            "first_seen_at": (int,),
            "hostname": (str,),
            "ip_addresses": ([str],),
            "is_single_step_instrumentation_enabled": (bool,),
            "last_restart_at": (int,),
            "os": (str,),
            "otel_collector_version": (str,),
            "otel_collector_versions": ([str],),
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
        "datadog_agent_key": "datadog_agent_key",
        "enabled_products": "enabled_products",
        "envs": "envs",
        "first_seen_at": "first_seen_at",
        "hostname": "hostname",
        "ip_addresses": "ip_addresses",
        "is_single_step_instrumentation_enabled": "is_single_step_instrumentation_enabled",
        "last_restart_at": "last_restart_at",
        "os": "os",
        "otel_collector_version": "otel_collector_version",
        "otel_collector_versions": "otel_collector_versions",
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
        datadog_agent_key: Union[str, UnsetType] = unset,
        enabled_products: Union[List[str], UnsetType] = unset,
        envs: Union[List[str], UnsetType] = unset,
        first_seen_at: Union[int, UnsetType] = unset,
        hostname: Union[str, UnsetType] = unset,
        ip_addresses: Union[List[str], UnsetType] = unset,
        is_single_step_instrumentation_enabled: Union[bool, UnsetType] = unset,
        last_restart_at: Union[int, UnsetType] = unset,
        os: Union[str, UnsetType] = unset,
        otel_collector_version: Union[str, UnsetType] = unset,
        otel_collector_versions: Union[List[str], UnsetType] = unset,
        pod_name: Union[str, UnsetType] = unset,
        remote_agent_management: Union[str, UnsetType] = unset,
        remote_config_status: Union[str, UnsetType] = unset,
        services: Union[List[str], UnsetType] = unset,
        tags: Union[List[FleetAgentAttributesTagsItems], UnsetType] = unset,
        team: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Datadog Agent in the list view.

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

        :param datadog_agent_key: The unique agent key identifier.
        :type datadog_agent_key: str, optional

        :param enabled_products: Datadog products enabled on the agent.
        :type enabled_products: [str], optional

        :param envs: Environments the agent is reporting from.
        :type envs: [str], optional

        :param first_seen_at: Timestamp when the agent was first seen.
        :type first_seen_at: int, optional

        :param hostname: The hostname of the agent.
        :type hostname: str, optional

        :param ip_addresses: IP addresses of the agent.
        :type ip_addresses: [str], optional

        :param is_single_step_instrumentation_enabled: Whether single-step instrumentation is enabled.
        :type is_single_step_instrumentation_enabled: bool, optional

        :param last_restart_at: Timestamp of the last agent restart.
        :type last_restart_at: int, optional

        :param os: The operating system.
        :type os: str, optional

        :param otel_collector_version: OpenTelemetry collector version (if applicable).
        :type otel_collector_version: str, optional

        :param otel_collector_versions: List of OpenTelemetry collector versions (if applicable).
        :type otel_collector_versions: [str], optional

        :param pod_name: Kubernetes pod name (if applicable).
        :type pod_name: str, optional

        :param remote_agent_management: Remote agent management status.
        :type remote_agent_management: str, optional

        :param remote_config_status: Remote configuration status.
        :type remote_config_status: str, optional

        :param services: Services running on the agent.
        :type services: [str], optional

        :param tags: Tags associated with the agent.
        :type tags: [FleetAgentAttributesTagsItems], optional

        :param team: Team associated with the agent.
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
        if datadog_agent_key is not unset:
            kwargs["datadog_agent_key"] = datadog_agent_key
        if enabled_products is not unset:
            kwargs["enabled_products"] = enabled_products
        if envs is not unset:
            kwargs["envs"] = envs
        if first_seen_at is not unset:
            kwargs["first_seen_at"] = first_seen_at
        if hostname is not unset:
            kwargs["hostname"] = hostname
        if ip_addresses is not unset:
            kwargs["ip_addresses"] = ip_addresses
        if is_single_step_instrumentation_enabled is not unset:
            kwargs["is_single_step_instrumentation_enabled"] = is_single_step_instrumentation_enabled
        if last_restart_at is not unset:
            kwargs["last_restart_at"] = last_restart_at
        if os is not unset:
            kwargs["os"] = os
        if otel_collector_version is not unset:
            kwargs["otel_collector_version"] = otel_collector_version
        if otel_collector_versions is not unset:
            kwargs["otel_collector_versions"] = otel_collector_versions
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
