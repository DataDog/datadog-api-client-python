# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.remediation_deployment_rollout_state import RemediationDeploymentRolloutState


class RemediationWorkloadSummary(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.remediation_deployment_rollout_state import RemediationDeploymentRolloutState

        return {
            "deployment_rollout_state": (RemediationDeploymentRolloutState,),
            "desired_count": (str,),
            "failed_count": (str,),
            "failed_percent": (str,),
            "pending_count": (str,),
            "previous_task_definition": (str,),
            "running_count": (str,),
        }

    attribute_map = {
        "deployment_rollout_state": "deployment_rollout_state",
        "desired_count": "desired_count",
        "failed_count": "failed_count",
        "failed_percent": "failed_percent",
        "pending_count": "pending_count",
        "previous_task_definition": "previous_task_definition",
        "running_count": "running_count",
    }

    def __init__(
        self_,
        deployment_rollout_state: Union[RemediationDeploymentRolloutState, UnsetType] = unset,
        desired_count: Union[str, UnsetType] = unset,
        failed_count: Union[str, UnsetType] = unset,
        failed_percent: Union[str, UnsetType] = unset,
        pending_count: Union[str, UnsetType] = unset,
        previous_task_definition: Union[str, UnsetType] = unset,
        running_count: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Aggregated health across all tasks in a workload (service or daemon).

        :param deployment_rollout_state: ECS deployment state, populated only for deployment failures.
        :type deployment_rollout_state: RemediationDeploymentRolloutState, optional

        :param desired_count: Expected task count (64-bit integer encoded as a string).
        :type desired_count: str, optional

        :param failed_count: Tasks in a problematic state (64-bit integer encoded as a string).
        :type failed_count: str, optional

        :param failed_percent: Percentage of desired count that is failed (64-bit integer encoded as a string).
        :type failed_percent: str, optional

        :param pending_count: Tasks currently pending (64-bit integer encoded as a string).
        :type pending_count: str, optional

        :param previous_task_definition: Previous deployment's task definition, as family:revision or a full task definition ARN. Empty when no rollback target is visible.
        :type previous_task_definition: str, optional

        :param running_count: Tasks currently running (64-bit integer encoded as a string).
        :type running_count: str, optional
        """
        if deployment_rollout_state is not unset:
            kwargs["deployment_rollout_state"] = deployment_rollout_state
        if desired_count is not unset:
            kwargs["desired_count"] = desired_count
        if failed_count is not unset:
            kwargs["failed_count"] = failed_count
        if failed_percent is not unset:
            kwargs["failed_percent"] = failed_percent
        if pending_count is not unset:
            kwargs["pending_count"] = pending_count
        if previous_task_definition is not unset:
            kwargs["previous_task_definition"] = previous_task_definition
        if running_count is not unset:
            kwargs["running_count"] = running_count
        super().__init__(kwargs)
