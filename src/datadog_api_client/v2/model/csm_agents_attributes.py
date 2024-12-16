# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class CsmAgentsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "agent_version": (str,),
            "aws_fargate": (str,),
            "cluster_name": ([str],),
            "datadog_agent": (str,),
            "ecs_fargate_task_arn": (str,),
            "envs": ([str], none_type),
            "host_id": (int,),
            "hostname": (str,),
            "install_method_installer_version": (str,),
            "install_method_tool": (str,),
            "is_csm_vm_containers_enabled": (bool, none_type),
            "is_csm_vm_hosts_enabled": (bool, none_type),
            "is_cspm_enabled": (bool, none_type),
            "is_cws_enabled": (bool, none_type),
            "is_cws_remote_configuration_enabled": (bool, none_type),
            "is_remote_configuration_enabled": (bool, none_type),
            "os": (str,),
        }

    attribute_map = {
        "agent_version": "agent_version",
        "aws_fargate": "aws_fargate",
        "cluster_name": "cluster_name",
        "datadog_agent": "datadog_agent",
        "ecs_fargate_task_arn": "ecs_fargate_task_arn",
        "envs": "envs",
        "host_id": "host_id",
        "hostname": "hostname",
        "install_method_installer_version": "install_method_installer_version",
        "install_method_tool": "install_method_tool",
        "is_csm_vm_containers_enabled": "is_csm_vm_containers_enabled",
        "is_csm_vm_hosts_enabled": "is_csm_vm_hosts_enabled",
        "is_cspm_enabled": "is_cspm_enabled",
        "is_cws_enabled": "is_cws_enabled",
        "is_cws_remote_configuration_enabled": "is_cws_remote_configuration_enabled",
        "is_remote_configuration_enabled": "is_remote_configuration_enabled",
        "os": "os",
    }

    def __init__(
        self_,
        agent_version: Union[str, UnsetType] = unset,
        aws_fargate: Union[str, UnsetType] = unset,
        cluster_name: Union[List[str], UnsetType] = unset,
        datadog_agent: Union[str, UnsetType] = unset,
        ecs_fargate_task_arn: Union[str, UnsetType] = unset,
        envs: Union[List[str], none_type, UnsetType] = unset,
        host_id: Union[int, UnsetType] = unset,
        hostname: Union[str, UnsetType] = unset,
        install_method_installer_version: Union[str, UnsetType] = unset,
        install_method_tool: Union[str, UnsetType] = unset,
        is_csm_vm_containers_enabled: Union[bool, none_type, UnsetType] = unset,
        is_csm_vm_hosts_enabled: Union[bool, none_type, UnsetType] = unset,
        is_cspm_enabled: Union[bool, none_type, UnsetType] = unset,
        is_cws_enabled: Union[bool, none_type, UnsetType] = unset,
        is_cws_remote_configuration_enabled: Union[bool, none_type, UnsetType] = unset,
        is_remote_configuration_enabled: Union[bool, none_type, UnsetType] = unset,
        os: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A CSM Agent returned by the API.

        :param agent_version: Version of the Datadog Agent.
        :type agent_version: str, optional

        :param aws_fargate: AWS Fargate details.
        :type aws_fargate: str, optional

        :param cluster_name: List of cluster names associated with the Agent.
        :type cluster_name: [str], optional

        :param datadog_agent: Unique identifier for the Datadog Agent.
        :type datadog_agent: str, optional

        :param ecs_fargate_task_arn: ARN of the ECS Fargate task.
        :type ecs_fargate_task_arn: str, optional

        :param envs: List of environments associated with the Agent.
        :type envs: [str], none_type, optional

        :param host_id: ID of the host.
        :type host_id: int, optional

        :param hostname: Name of the host.
        :type hostname: str, optional

        :param install_method_installer_version: Version of the installer used for installing the Datadog Agent.
        :type install_method_installer_version: str, optional

        :param install_method_tool: Tool used for installing the Datadog Agent.
        :type install_method_tool: str, optional

        :param is_csm_vm_containers_enabled: Indicates if CSM VM Containers is enabled.
        :type is_csm_vm_containers_enabled: bool, none_type, optional

        :param is_csm_vm_hosts_enabled: Indicates if CSM VM Hosts is enabled.
        :type is_csm_vm_hosts_enabled: bool, none_type, optional

        :param is_cspm_enabled: Indicates if CSPM is enabled.
        :type is_cspm_enabled: bool, none_type, optional

        :param is_cws_enabled: Indicates if CWS is enabled.
        :type is_cws_enabled: bool, none_type, optional

        :param is_cws_remote_configuration_enabled: Indicates if CWS Remote Configuration is enabled.
        :type is_cws_remote_configuration_enabled: bool, none_type, optional

        :param is_remote_configuration_enabled: Indicates if Remote Configuration is enabled.
        :type is_remote_configuration_enabled: bool, none_type, optional

        :param os: Operating system of the host.
        :type os: str, optional
        """
        if agent_version is not unset:
            kwargs["agent_version"] = agent_version
        if aws_fargate is not unset:
            kwargs["aws_fargate"] = aws_fargate
        if cluster_name is not unset:
            kwargs["cluster_name"] = cluster_name
        if datadog_agent is not unset:
            kwargs["datadog_agent"] = datadog_agent
        if ecs_fargate_task_arn is not unset:
            kwargs["ecs_fargate_task_arn"] = ecs_fargate_task_arn
        if envs is not unset:
            kwargs["envs"] = envs
        if host_id is not unset:
            kwargs["host_id"] = host_id
        if hostname is not unset:
            kwargs["hostname"] = hostname
        if install_method_installer_version is not unset:
            kwargs["install_method_installer_version"] = install_method_installer_version
        if install_method_tool is not unset:
            kwargs["install_method_tool"] = install_method_tool
        if is_csm_vm_containers_enabled is not unset:
            kwargs["is_csm_vm_containers_enabled"] = is_csm_vm_containers_enabled
        if is_csm_vm_hosts_enabled is not unset:
            kwargs["is_csm_vm_hosts_enabled"] = is_csm_vm_hosts_enabled
        if is_cspm_enabled is not unset:
            kwargs["is_cspm_enabled"] = is_cspm_enabled
        if is_cws_enabled is not unset:
            kwargs["is_cws_enabled"] = is_cws_enabled
        if is_cws_remote_configuration_enabled is not unset:
            kwargs["is_cws_remote_configuration_enabled"] = is_cws_remote_configuration_enabled
        if is_remote_configuration_enabled is not unset:
            kwargs["is_remote_configuration_enabled"] = is_remote_configuration_enabled
        if os is not unset:
            kwargs["os"] = os
        super().__init__(kwargs)
