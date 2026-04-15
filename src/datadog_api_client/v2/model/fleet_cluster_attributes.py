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
    from datadog_api_client.v2.model.fleet_cluster_node_count_by_status import FleetClusterNodeCountByStatus
    from datadog_api_client.v2.model.fleet_cluster_pod_count_by_state import FleetClusterPodCountByState


class FleetClusterAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_cluster_node_count_by_status import FleetClusterNodeCountByStatus
        from datadog_api_client.v2.model.fleet_cluster_pod_count_by_state import FleetClusterPodCountByState

        return {
            "agent_versions": ([str],),
            "api_key_names": ([str],),
            "api_key_uuids": ([str],),
            "cloud_providers": ([str],),
            "cluster_name": (str,),
            "enabled_products": ([str],),
            "envs": ([str],),
            "first_seen_at": (int,),
            "install_method_tool": (str,),
            "node_count": (int,),
            "node_count_by_status": (FleetClusterNodeCountByStatus,),
            "operating_systems": ([str],),
            "otel_collector_distributions": ([str],),
            "otel_collector_versions": ([str],),
            "pod_count_by_state": (FleetClusterPodCountByState,),
            "services": ([str],),
            "teams": ([str],),
        }

    attribute_map = {
        "agent_versions": "agent_versions",
        "api_key_names": "api_key_names",
        "api_key_uuids": "api_key_uuids",
        "cloud_providers": "cloud_providers",
        "cluster_name": "cluster_name",
        "enabled_products": "enabled_products",
        "envs": "envs",
        "first_seen_at": "first_seen_at",
        "install_method_tool": "install_method_tool",
        "node_count": "node_count",
        "node_count_by_status": "node_count_by_status",
        "operating_systems": "operating_systems",
        "otel_collector_distributions": "otel_collector_distributions",
        "otel_collector_versions": "otel_collector_versions",
        "pod_count_by_state": "pod_count_by_state",
        "services": "services",
        "teams": "teams",
    }

    def __init__(
        self_,
        agent_versions: Union[List[str], UnsetType] = unset,
        api_key_names: Union[List[str], UnsetType] = unset,
        api_key_uuids: Union[List[str], UnsetType] = unset,
        cloud_providers: Union[List[str], UnsetType] = unset,
        cluster_name: Union[str, UnsetType] = unset,
        enabled_products: Union[List[str], UnsetType] = unset,
        envs: Union[List[str], UnsetType] = unset,
        first_seen_at: Union[int, UnsetType] = unset,
        install_method_tool: Union[str, UnsetType] = unset,
        node_count: Union[int, UnsetType] = unset,
        node_count_by_status: Union[FleetClusterNodeCountByStatus, UnsetType] = unset,
        operating_systems: Union[List[str], UnsetType] = unset,
        otel_collector_distributions: Union[List[str], UnsetType] = unset,
        otel_collector_versions: Union[List[str], UnsetType] = unset,
        pod_count_by_state: Union[FleetClusterPodCountByState, UnsetType] = unset,
        services: Union[List[str], UnsetType] = unset,
        teams: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Kubernetes cluster in the fleet.

        :param agent_versions: Datadog Agent versions running in the cluster.
        :type agent_versions: [str], optional

        :param api_key_names: API key names used by agents in the cluster.
        :type api_key_names: [str], optional

        :param api_key_uuids: API key UUIDs used by agents in the cluster.
        :type api_key_uuids: [str], optional

        :param cloud_providers: Cloud providers hosting the cluster.
        :type cloud_providers: [str], optional

        :param cluster_name: The name of the Kubernetes cluster.
        :type cluster_name: str, optional

        :param enabled_products: Datadog products enabled in the cluster.
        :type enabled_products: [str], optional

        :param envs: Environments associated with the cluster.
        :type envs: [str], optional

        :param first_seen_at: Timestamp when the cluster was first seen.
        :type first_seen_at: int, optional

        :param install_method_tool: The tool used to install agents in the cluster.
        :type install_method_tool: str, optional

        :param node_count: Total number of nodes in the cluster.
        :type node_count: int, optional

        :param node_count_by_status: Node counts grouped by status.
        :type node_count_by_status: FleetClusterNodeCountByStatus, optional

        :param operating_systems: Operating systems of nodes in the cluster.
        :type operating_systems: [str], optional

        :param otel_collector_distributions: OpenTelemetry collector distributions in the cluster.
        :type otel_collector_distributions: [str], optional

        :param otel_collector_versions: OpenTelemetry collector versions in the cluster.
        :type otel_collector_versions: [str], optional

        :param pod_count_by_state: Pod counts grouped by state.
        :type pod_count_by_state: FleetClusterPodCountByState, optional

        :param services: Services running in the cluster.
        :type services: [str], optional

        :param teams: Teams associated with the cluster.
        :type teams: [str], optional
        """
        if agent_versions is not unset:
            kwargs["agent_versions"] = agent_versions
        if api_key_names is not unset:
            kwargs["api_key_names"] = api_key_names
        if api_key_uuids is not unset:
            kwargs["api_key_uuids"] = api_key_uuids
        if cloud_providers is not unset:
            kwargs["cloud_providers"] = cloud_providers
        if cluster_name is not unset:
            kwargs["cluster_name"] = cluster_name
        if enabled_products is not unset:
            kwargs["enabled_products"] = enabled_products
        if envs is not unset:
            kwargs["envs"] = envs
        if first_seen_at is not unset:
            kwargs["first_seen_at"] = first_seen_at
        if install_method_tool is not unset:
            kwargs["install_method_tool"] = install_method_tool
        if node_count is not unset:
            kwargs["node_count"] = node_count
        if node_count_by_status is not unset:
            kwargs["node_count_by_status"] = node_count_by_status
        if operating_systems is not unset:
            kwargs["operating_systems"] = operating_systems
        if otel_collector_distributions is not unset:
            kwargs["otel_collector_distributions"] = otel_collector_distributions
        if otel_collector_versions is not unset:
            kwargs["otel_collector_versions"] = otel_collector_versions
        if pod_count_by_state is not unset:
            kwargs["pod_count_by_state"] = pod_count_by_state
        if services is not unset:
            kwargs["services"] = services
        if teams is not unset:
            kwargs["teams"] = teams
        super().__init__(kwargs)
