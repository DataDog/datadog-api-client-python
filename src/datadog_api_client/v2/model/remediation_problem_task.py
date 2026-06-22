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
    from datadog_api_client.v2.model.remediation_problem_container import RemediationProblemContainer
    from datadog_api_client.v2.model.remediation_launch_type import RemediationLaunchType


class RemediationProblemTask(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.remediation_problem_container import RemediationProblemContainer
        from datadog_api_client.v2.model.remediation_launch_type import RemediationLaunchType

        return {
            "availability_zone": (str,),
            "container_instance_arn": (str,),
            "containers": ([RemediationProblemContainer],),
            "cpu_units": (str,),
            "desired_status": (str,),
            "execution_role_arn": (str,),
            "health_status": (str,),
            "issue_start_time": (str,),
            "issue_type": (str,),
            "last_status": (str,),
            "launch_type": (RemediationLaunchType,),
            "memory_mib": (str,),
            "stop_code": (str,),
            "stopped_reason": (str,),
            "tags": ([str],),
            "task_arn": (str,),
            "task_definition_arn": (str,),
            "task_role_arn": (str,),
        }

    attribute_map = {
        "availability_zone": "availability_zone",
        "container_instance_arn": "container_instance_arn",
        "containers": "containers",
        "cpu_units": "cpu_units",
        "desired_status": "desired_status",
        "execution_role_arn": "execution_role_arn",
        "health_status": "health_status",
        "issue_start_time": "issue_start_time",
        "issue_type": "issue_type",
        "last_status": "last_status",
        "launch_type": "launch_type",
        "memory_mib": "memory_mib",
        "stop_code": "stop_code",
        "stopped_reason": "stopped_reason",
        "tags": "tags",
        "task_arn": "task_arn",
        "task_definition_arn": "task_definition_arn",
        "task_role_arn": "task_role_arn",
    }

    def __init__(
        self_,
        availability_zone: Union[str, UnsetType] = unset,
        container_instance_arn: Union[str, UnsetType] = unset,
        containers: Union[List[RemediationProblemContainer], UnsetType] = unset,
        cpu_units: Union[str, UnsetType] = unset,
        desired_status: Union[str, UnsetType] = unset,
        execution_role_arn: Union[str, UnsetType] = unset,
        health_status: Union[str, UnsetType] = unset,
        issue_start_time: Union[str, UnsetType] = unset,
        issue_type: Union[str, UnsetType] = unset,
        last_status: Union[str, UnsetType] = unset,
        launch_type: Union[RemediationLaunchType, UnsetType] = unset,
        memory_mib: Union[str, UnsetType] = unset,
        stop_code: Union[str, UnsetType] = unset,
        stopped_reason: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        task_arn: Union[str, UnsetType] = unset,
        task_definition_arn: Union[str, UnsetType] = unset,
        task_role_arn: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        An individual ECS task in a problematic state.

        :param availability_zone: Availability zone where the task is running.
        :type availability_zone: str, optional

        :param container_instance_arn: Container instance ARN (EC2 launch type only).
        :type container_instance_arn: str, optional

        :param containers: Problematic containers within the task.
        :type containers: [RemediationProblemContainer], optional

        :param cpu_units: CPU units allocated to the task (64-bit integer encoded as a string).
        :type cpu_units: str, optional

        :param desired_status: Desired task status.
        :type desired_status: str, optional

        :param execution_role_arn: IAM role used by ECS to pull images and fetch secrets.
        :type execution_role_arn: str, optional

        :param health_status: Task-level health status.
        :type health_status: str, optional

        :param issue_start_time: When this task's issue started, epoch milliseconds (64-bit integer encoded as a string).
        :type issue_start_time: str, optional

        :param issue_type: Issue type for this specific task.
        :type issue_type: str, optional

        :param last_status: Current task status.
        :type last_status: str, optional

        :param launch_type: ECS launch type.
        :type launch_type: RemediationLaunchType, optional

        :param memory_mib: Memory in MiB allocated to the task (64-bit integer encoded as a string).
        :type memory_mib: str, optional

        :param stop_code: Stop code if the task was stopped.
        :type stop_code: str, optional

        :param stopped_reason: Stop reason if the task was stopped.
        :type stopped_reason: str, optional

        :param tags: Task-level tags.
        :type tags: [str], optional

        :param task_arn: Full task ARN.
        :type task_arn: str, optional

        :param task_definition_arn: Task definition ARN with revision.
        :type task_definition_arn: str, optional

        :param task_role_arn: IAM role used by the task at runtime.
        :type task_role_arn: str, optional
        """
        if availability_zone is not unset:
            kwargs["availability_zone"] = availability_zone
        if container_instance_arn is not unset:
            kwargs["container_instance_arn"] = container_instance_arn
        if containers is not unset:
            kwargs["containers"] = containers
        if cpu_units is not unset:
            kwargs["cpu_units"] = cpu_units
        if desired_status is not unset:
            kwargs["desired_status"] = desired_status
        if execution_role_arn is not unset:
            kwargs["execution_role_arn"] = execution_role_arn
        if health_status is not unset:
            kwargs["health_status"] = health_status
        if issue_start_time is not unset:
            kwargs["issue_start_time"] = issue_start_time
        if issue_type is not unset:
            kwargs["issue_type"] = issue_type
        if last_status is not unset:
            kwargs["last_status"] = last_status
        if launch_type is not unset:
            kwargs["launch_type"] = launch_type
        if memory_mib is not unset:
            kwargs["memory_mib"] = memory_mib
        if stop_code is not unset:
            kwargs["stop_code"] = stop_code
        if stopped_reason is not unset:
            kwargs["stopped_reason"] = stopped_reason
        if tags is not unset:
            kwargs["tags"] = tags
        if task_arn is not unset:
            kwargs["task_arn"] = task_arn
        if task_definition_arn is not unset:
            kwargs["task_definition_arn"] = task_definition_arn
        if task_role_arn is not unset:
            kwargs["task_role_arn"] = task_role_arn
        super().__init__(kwargs)
