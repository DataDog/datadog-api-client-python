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
    from datadog_api_client.v2.model.remediation_launch_type import RemediationLaunchType
    from datadog_api_client.v2.model.remediation_problem_task import RemediationProblemTask
    from datadog_api_client.v2.model.remediation_workload_summary import RemediationWorkloadSummary
    from datadog_api_client.v2.model.remediation_workload_type import RemediationWorkloadType


class RemediationEcsMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.remediation_launch_type import RemediationLaunchType
        from datadog_api_client.v2.model.remediation_problem_task import RemediationProblemTask
        from datadog_api_client.v2.model.remediation_workload_summary import RemediationWorkloadSummary
        from datadog_api_client.v2.model.remediation_workload_type import RemediationWorkloadType

        return {
            "account_id": (str,),
            "capacity_providers": ([str],),
            "cluster_arn": (str,),
            "cluster_name": (str,),
            "impact_score": (str,),
            "issue_start_time": (str,),
            "launch_type": (RemediationLaunchType,),
            "region": (str,),
            "task_arns": ([str],),
            "task_definition_family": (str,),
            "task_definition_revision": (int,),
            "tasks": ([RemediationProblemTask],),
            "total_cpu_units": (str,),
            "total_memory_mib": (str,),
            "update_timestamp": (str,),
            "workload_summary": (RemediationWorkloadSummary,),
            "workload_type": (RemediationWorkloadType,),
        }

    attribute_map = {
        "account_id": "account_id",
        "capacity_providers": "capacity_providers",
        "cluster_arn": "cluster_arn",
        "cluster_name": "cluster_name",
        "impact_score": "impact_score",
        "issue_start_time": "issue_start_time",
        "launch_type": "launch_type",
        "region": "region",
        "task_arns": "task_arns",
        "task_definition_family": "task_definition_family",
        "task_definition_revision": "task_definition_revision",
        "tasks": "tasks",
        "total_cpu_units": "total_cpu_units",
        "total_memory_mib": "total_memory_mib",
        "update_timestamp": "update_timestamp",
        "workload_summary": "workload_summary",
        "workload_type": "workload_type",
    }

    def __init__(
        self_,
        account_id: Union[str, UnsetType] = unset,
        capacity_providers: Union[List[str], UnsetType] = unset,
        cluster_arn: Union[str, UnsetType] = unset,
        cluster_name: Union[str, UnsetType] = unset,
        impact_score: Union[str, UnsetType] = unset,
        issue_start_time: Union[str, UnsetType] = unset,
        launch_type: Union[RemediationLaunchType, UnsetType] = unset,
        region: Union[str, UnsetType] = unset,
        task_arns: Union[List[str], UnsetType] = unset,
        task_definition_family: Union[str, UnsetType] = unset,
        task_definition_revision: Union[int, UnsetType] = unset,
        tasks: Union[List[RemediationProblemTask], UnsetType] = unset,
        total_cpu_units: Union[str, UnsetType] = unset,
        total_memory_mib: Union[str, UnsetType] = unset,
        update_timestamp: Union[str, UnsetType] = unset,
        workload_summary: Union[RemediationWorkloadSummary, UnsetType] = unset,
        workload_type: Union[RemediationWorkloadType, UnsetType] = unset,
        **kwargs,
    ):
        """
        ECS-specific context for the investigation.

        :param account_id: AWS account ID.
        :type account_id: str, optional

        :param capacity_providers: Associated capacity providers.
        :type capacity_providers: [str], optional

        :param cluster_arn: ECS cluster ARN.
        :type cluster_arn: str, optional

        :param cluster_name: ECS cluster name.
        :type cluster_name: str, optional

        :param impact_score: Computed impact score for ranking (64-bit integer encoded as a string).
        :type impact_score: str, optional

        :param issue_start_time: When the issue was first detected, epoch milliseconds (64-bit integer encoded as a string).
        :type issue_start_time: str, optional

        :param launch_type: ECS launch type.
        :type launch_type: RemediationLaunchType, optional

        :param region: AWS region.
        :type region: str, optional

        :param task_arns: All affected task ARNs, for filtering.
        :type task_arns: [str], optional

        :param task_definition_family: Task definition family name.
        :type task_definition_family: str, optional

        :param task_definition_revision: Current task definition revision.
        :type task_definition_revision: int, optional

        :param tasks: Individual tasks exhibiting issues. Capped at 50 most recent.
        :type tasks: [RemediationProblemTask], optional

        :param total_cpu_units: Sum of CPU units across affected tasks (64-bit integer encoded as a string).
        :type total_cpu_units: str, optional

        :param total_memory_mib: Sum of memory (MiB) across affected tasks (64-bit integer encoded as a string).
        :type total_memory_mib: str, optional

        :param update_timestamp: When this metadata was last updated, epoch milliseconds (64-bit integer encoded as a string).
        :type update_timestamp: str, optional

        :param workload_summary: Aggregated health across all tasks in a workload (service or daemon).
        :type workload_summary: RemediationWorkloadSummary, optional

        :param workload_type: The kind of ECS workload that owns the problematic tasks.
        :type workload_type: RemediationWorkloadType, optional
        """
        if account_id is not unset:
            kwargs["account_id"] = account_id
        if capacity_providers is not unset:
            kwargs["capacity_providers"] = capacity_providers
        if cluster_arn is not unset:
            kwargs["cluster_arn"] = cluster_arn
        if cluster_name is not unset:
            kwargs["cluster_name"] = cluster_name
        if impact_score is not unset:
            kwargs["impact_score"] = impact_score
        if issue_start_time is not unset:
            kwargs["issue_start_time"] = issue_start_time
        if launch_type is not unset:
            kwargs["launch_type"] = launch_type
        if region is not unset:
            kwargs["region"] = region
        if task_arns is not unset:
            kwargs["task_arns"] = task_arns
        if task_definition_family is not unset:
            kwargs["task_definition_family"] = task_definition_family
        if task_definition_revision is not unset:
            kwargs["task_definition_revision"] = task_definition_revision
        if tasks is not unset:
            kwargs["tasks"] = tasks
        if total_cpu_units is not unset:
            kwargs["total_cpu_units"] = total_cpu_units
        if total_memory_mib is not unset:
            kwargs["total_memory_mib"] = total_memory_mib
        if update_timestamp is not unset:
            kwargs["update_timestamp"] = update_timestamp
        if workload_summary is not unset:
            kwargs["workload_summary"] = workload_summary
        if workload_type is not unset:
            kwargs["workload_type"] = workload_type
        super().__init__(kwargs)
