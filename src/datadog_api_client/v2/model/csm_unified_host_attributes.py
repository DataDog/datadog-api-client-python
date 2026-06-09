# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.csm_cloud_provider import CsmCloudProvider
    from datadog_api_client.v2.model.csm_agentless_host_resource_type import CsmAgentlessHostResourceType
    from datadog_api_client.v2.model.csm_unified_host_source import CsmUnifiedHostSource


class CsmUnifiedHostAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.csm_cloud_provider import CsmCloudProvider
        from datadog_api_client.v2.model.csm_agentless_host_resource_type import CsmAgentlessHostResourceType
        from datadog_api_client.v2.model.csm_unified_host_source import CsmUnifiedHostSource

        return {
            "account_id": (str, none_type),
            "agent_csm_vm_containers_enabled": (bool, none_type),
            "agent_csm_vm_hosts_enabled": (bool, none_type),
            "agent_cws_enabled": (bool, none_type),
            "agent_posture_management": (bool, none_type),
            "agent_version": (str, none_type),
            "agentless_posture_management": (bool, none_type),
            "agentless_vulnerability_scanning": (bool, none_type),
            "cloud_provider": (CsmCloudProvider,),
            "cluster_name": (str, none_type),
            "datadog_agent_key": (str, none_type),
            "env": ([str], none_type),
            "host_id": (int, none_type),
            "install_method_tool": (str, none_type),
            "os": (str, none_type),
            "resource_type": (CsmAgentlessHostResourceType,),
            "source": (CsmUnifiedHostSource,),
        }

    attribute_map = {
        "account_id": "account_id",
        "agent_csm_vm_containers_enabled": "agent_csm_vm_containers_enabled",
        "agent_csm_vm_hosts_enabled": "agent_csm_vm_hosts_enabled",
        "agent_cws_enabled": "agent_cws_enabled",
        "agent_posture_management": "agent_posture_management",
        "agent_version": "agent_version",
        "agentless_posture_management": "agentless_posture_management",
        "agentless_vulnerability_scanning": "agentless_vulnerability_scanning",
        "cloud_provider": "cloud_provider",
        "cluster_name": "cluster_name",
        "datadog_agent_key": "datadog_agent_key",
        "env": "env",
        "host_id": "host_id",
        "install_method_tool": "install_method_tool",
        "os": "os",
        "resource_type": "resource_type",
        "source": "source",
    }

    def __init__(
        self_,
        source: CsmUnifiedHostSource,
        account_id: Union[str, none_type, UnsetType] = unset,
        agent_csm_vm_containers_enabled: Union[bool, none_type, UnsetType] = unset,
        agent_csm_vm_hosts_enabled: Union[bool, none_type, UnsetType] = unset,
        agent_cws_enabled: Union[bool, none_type, UnsetType] = unset,
        agent_posture_management: Union[bool, none_type, UnsetType] = unset,
        agent_version: Union[str, none_type, UnsetType] = unset,
        agentless_posture_management: Union[bool, none_type, UnsetType] = unset,
        agentless_vulnerability_scanning: Union[bool, none_type, UnsetType] = unset,
        cloud_provider: Union[CsmCloudProvider, UnsetType] = unset,
        cluster_name: Union[str, none_type, UnsetType] = unset,
        datadog_agent_key: Union[str, none_type, UnsetType] = unset,
        env: Union[List[str], none_type, UnsetType] = unset,
        host_id: Union[int, none_type, UnsetType] = unset,
        install_method_tool: Union[str, none_type, UnsetType] = unset,
        os: Union[str, none_type, UnsetType] = unset,
        resource_type: Union[CsmAgentlessHostResourceType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a unified host, combining data from agent and agentless sources.

        :param account_id: The ID of the cloud account that the host belongs to. Present only when the host was discovered through agentless scanning.
        :type account_id: str, none_type, optional

        :param agent_csm_vm_containers_enabled: Whether CSM Vulnerabilities is enabled for containers through the Datadog Agent. ``true`` if enabled; ``false`` if disabled.
        :type agent_csm_vm_containers_enabled: bool, none_type, optional

        :param agent_csm_vm_hosts_enabled: Whether CSM Vulnerabilities is enabled for hosts through the Datadog Agent. ``true`` if enabled; ``false`` if disabled.
        :type agent_csm_vm_hosts_enabled: bool, none_type, optional

        :param agent_cws_enabled: Whether CSM Threats is enabled for this host through the Datadog Agent. ``true`` if enabled; ``false`` if disabled.
        :type agent_cws_enabled: bool, none_type, optional

        :param agent_posture_management: Whether CSM Misconfigurations is enabled for this host through the Datadog Agent. ``true`` if enabled; ``false`` if disabled.
        :type agent_posture_management: bool, none_type, optional

        :param agent_version: The version of the Datadog Agent running on this host.
        :type agent_version: str, none_type, optional

        :param agentless_posture_management: Whether CSM Misconfigurations is enabled for this host via agentless scanning. ``true`` if enabled; ``false`` if disabled.
        :type agentless_posture_management: bool, none_type, optional

        :param agentless_vulnerability_scanning: Whether CSM Vulnerabilities is enabled for this host via agentless scanning. ``true`` if enabled; ``false`` if disabled.
        :type agentless_vulnerability_scanning: bool, none_type, optional

        :param cloud_provider: The cloud provider of a host resource.
        :type cloud_provider: CsmCloudProvider, optional

        :param cluster_name: The name of the Kubernetes cluster the host belongs to, if applicable.
        :type cluster_name: str, none_type, optional

        :param datadog_agent_key: The Datadog Agent key associated with this host. Present only for agent-sourced hosts.
        :type datadog_agent_key: str, none_type, optional

        :param env: The list of environment tags associated with this host.
        :type env: [str], none_type, optional

        :param host_id: The internal Datadog host identifier. Present only for agent-sourced hosts.
        :type host_id: int, none_type, optional

        :param install_method_tool: The tool used to install the Datadog Agent on this host.
        :type install_method_tool: str, none_type, optional

        :param os: The operating system of the host. Present only for agent-sourced hosts.
        :type os: str, none_type, optional

        :param resource_type: The type of cloud resource for an agentless host.
        :type resource_type: CsmAgentlessHostResourceType, optional

        :param source: The source of a unified host entry, indicating whether it was discovered via agent, agentless scanning, or both.
        :type source: CsmUnifiedHostSource
        """
        if account_id is not unset:
            kwargs["account_id"] = account_id
        if agent_csm_vm_containers_enabled is not unset:
            kwargs["agent_csm_vm_containers_enabled"] = agent_csm_vm_containers_enabled
        if agent_csm_vm_hosts_enabled is not unset:
            kwargs["agent_csm_vm_hosts_enabled"] = agent_csm_vm_hosts_enabled
        if agent_cws_enabled is not unset:
            kwargs["agent_cws_enabled"] = agent_cws_enabled
        if agent_posture_management is not unset:
            kwargs["agent_posture_management"] = agent_posture_management
        if agent_version is not unset:
            kwargs["agent_version"] = agent_version
        if agentless_posture_management is not unset:
            kwargs["agentless_posture_management"] = agentless_posture_management
        if agentless_vulnerability_scanning is not unset:
            kwargs["agentless_vulnerability_scanning"] = agentless_vulnerability_scanning
        if cloud_provider is not unset:
            kwargs["cloud_provider"] = cloud_provider
        if cluster_name is not unset:
            kwargs["cluster_name"] = cluster_name
        if datadog_agent_key is not unset:
            kwargs["datadog_agent_key"] = datadog_agent_key
        if env is not unset:
            kwargs["env"] = env
        if host_id is not unset:
            kwargs["host_id"] = host_id
        if install_method_tool is not unset:
            kwargs["install_method_tool"] = install_method_tool
        if os is not unset:
            kwargs["os"] = os
        if resource_type is not unset:
            kwargs["resource_type"] = resource_type
        super().__init__(kwargs)

        self_.source = source
