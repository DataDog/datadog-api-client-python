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
    from datadog_api_client.v2.model.fleet_deployment_operation import FleetDeploymentOperation
    from datadog_api_client.v2.model.fleet_deployment_v2_detail_agent import FleetDeploymentV2DetailAgent


class FleetDeploymentV2DetailAttributes(ModelNormal):
    validations = {
        "canceled_hosts": {
            "inclusive_minimum": 0,
        },
        "failed_hosts": {
            "inclusive_minimum": 0,
        },
        "running_hosts": {
            "inclusive_minimum": 0,
        },
        "skipped_hosts": {
            "inclusive_minimum": 0,
        },
        "succeeded_hosts": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_deployment_operation import FleetDeploymentOperation
        from datadog_api_client.v2.model.fleet_deployment_v2_detail_agent import FleetDeploymentV2DetailAgent

        return {
            "author": (str,),
            "canceled_hosts": (int,),
            "config_operations": ([FleetDeploymentOperation],),
            "duration_seconds": (int,),
            "error_summary": (str,),
            "estimated_finished_at": (int,),
            "failed_hosts": (int,),
            "high_level_status": (str,),
            "hosts": ([FleetDeploymentV2DetailAgent],),
            "is_scheduled": (bool,),
            "query": (str,),
            "running_hosts": (int,),
            "schedule_id": (str,),
            "skipped_hosts": (int,),
            "succeeded_hosts": (int,),
            "target_versions": ([str],),
            "total_hosts": (int,),
            "update_type": (str,),
        }

    attribute_map = {
        "author": "author",
        "canceled_hosts": "canceled_hosts",
        "config_operations": "config_operations",
        "duration_seconds": "duration_seconds",
        "error_summary": "error_summary",
        "estimated_finished_at": "estimated_finished_at",
        "failed_hosts": "failed_hosts",
        "high_level_status": "high_level_status",
        "hosts": "hosts",
        "is_scheduled": "is_scheduled",
        "query": "query",
        "running_hosts": "running_hosts",
        "schedule_id": "schedule_id",
        "skipped_hosts": "skipped_hosts",
        "succeeded_hosts": "succeeded_hosts",
        "target_versions": "target_versions",
        "total_hosts": "total_hosts",
        "update_type": "update_type",
    }

    def __init__(
        self_,
        author: Union[str, UnsetType] = unset,
        canceled_hosts: Union[int, UnsetType] = unset,
        config_operations: Union[List[FleetDeploymentOperation], UnsetType] = unset,
        duration_seconds: Union[int, UnsetType] = unset,
        error_summary: Union[str, UnsetType] = unset,
        estimated_finished_at: Union[int, UnsetType] = unset,
        failed_hosts: Union[int, UnsetType] = unset,
        high_level_status: Union[str, UnsetType] = unset,
        hosts: Union[List[FleetDeploymentV2DetailAgent], UnsetType] = unset,
        is_scheduled: Union[bool, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        running_hosts: Union[int, UnsetType] = unset,
        schedule_id: Union[str, UnsetType] = unset,
        skipped_hosts: Union[int, UnsetType] = unset,
        succeeded_hosts: Union[int, UnsetType] = unset,
        target_versions: Union[List[str], UnsetType] = unset,
        total_hosts: Union[int, UnsetType] = unset,
        update_type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a deployment detail response.

        :param author: Handle of the user who triggered the deployment.
        :type author: str, optional

        :param canceled_hosts: Number of hosts on which the deployment was canceled.
        :type canceled_hosts: int, optional

        :param config_operations: Ordered list of configuration file operations applied by this deployment.
            Absent for package deployments, which have no configuration file operations.
        :type config_operations: [FleetDeploymentOperation], optional

        :param duration_seconds: Duration of the deployment in seconds, computed as ``finished_at - started_at``.
            Zero if the deployment has not finished.
        :type duration_seconds: int, optional

        :param error_summary: Top-level error message for the deployment. Populated only when the deployment has failed.
        :type error_summary: str, optional

        :param estimated_finished_at: Estimated completion time of the deployment as a Unix timestamp. Zero if not available.
        :type estimated_finished_at: int, optional

        :param failed_hosts: Number of hosts on which the deployment failed.
        :type failed_hosts: int, optional

        :param high_level_status: Current high-level status of the deployment (for example, "pending", "running",
            "completed", "failed").
        :type high_level_status: str, optional

        :param hosts: Per-host status list for this deployment.
        :type hosts: [FleetDeploymentV2DetailAgent], optional

        :param is_scheduled: Whether this deployment was triggered by a schedule ( ``schedule_id`` is non-empty).
        :type is_scheduled: bool, optional

        :param query: Query used to filter and select target hosts for the deployment.
        :type query: str, optional

        :param running_hosts: Number of hosts on which the deployment is currently running.
        :type running_hosts: int, optional

        :param schedule_id: Identifier of the schedule that triggered this deployment. Empty if triggered manually.
        :type schedule_id: str, optional

        :param skipped_hosts: Number of hosts that were skipped during the deployment.
        :type skipped_hosts: int, optional

        :param succeeded_hosts: Number of hosts on which the deployment succeeded.
        :type succeeded_hosts: int, optional

        :param target_versions: Distinct package versions targeted by this deployment, in first-seen order.
        :type target_versions: [str], optional

        :param total_hosts: Total number of hosts targeted by this deployment.
        :type total_hosts: int, optional

        :param update_type: Type of update operation performed by this deployment
            (for example, "update_config_operations", "update_package").
        :type update_type: str, optional
        """
        if author is not unset:
            kwargs["author"] = author
        if canceled_hosts is not unset:
            kwargs["canceled_hosts"] = canceled_hosts
        if config_operations is not unset:
            kwargs["config_operations"] = config_operations
        if duration_seconds is not unset:
            kwargs["duration_seconds"] = duration_seconds
        if error_summary is not unset:
            kwargs["error_summary"] = error_summary
        if estimated_finished_at is not unset:
            kwargs["estimated_finished_at"] = estimated_finished_at
        if failed_hosts is not unset:
            kwargs["failed_hosts"] = failed_hosts
        if high_level_status is not unset:
            kwargs["high_level_status"] = high_level_status
        if hosts is not unset:
            kwargs["hosts"] = hosts
        if is_scheduled is not unset:
            kwargs["is_scheduled"] = is_scheduled
        if query is not unset:
            kwargs["query"] = query
        if running_hosts is not unset:
            kwargs["running_hosts"] = running_hosts
        if schedule_id is not unset:
            kwargs["schedule_id"] = schedule_id
        if skipped_hosts is not unset:
            kwargs["skipped_hosts"] = skipped_hosts
        if succeeded_hosts is not unset:
            kwargs["succeeded_hosts"] = succeeded_hosts
        if target_versions is not unset:
            kwargs["target_versions"] = target_versions
        if total_hosts is not unset:
            kwargs["total_hosts"] = total_hosts
        if update_type is not unset:
            kwargs["update_type"] = update_type
        super().__init__(kwargs)
