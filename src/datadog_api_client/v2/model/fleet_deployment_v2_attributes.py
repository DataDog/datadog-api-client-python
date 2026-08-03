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


class FleetDeploymentV2Attributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_deployment_operation import FleetDeploymentOperation

        return {
            "author": (str,),
            "config_operations": ([FleetDeploymentOperation],),
            "duration_seconds": (int,),
            "error_summary": (str,),
            "estimated_finished_at": (int,),
            "finished_at": (int,),
            "is_scheduled": (bool,),
            "query": (str,),
            "schedule_id": (str,),
            "started_at": (int,),
            "status": (str,),
            "target_versions": ([str],),
            "total_hosts": (int,),
            "update_type": (str,),
        }

    attribute_map = {
        "author": "author",
        "config_operations": "config_operations",
        "duration_seconds": "duration_seconds",
        "error_summary": "error_summary",
        "estimated_finished_at": "estimated_finished_at",
        "finished_at": "finished_at",
        "is_scheduled": "is_scheduled",
        "query": "query",
        "schedule_id": "schedule_id",
        "started_at": "started_at",
        "status": "status",
        "target_versions": "target_versions",
        "total_hosts": "total_hosts",
        "update_type": "update_type",
    }

    def __init__(
        self_,
        author: Union[str, UnsetType] = unset,
        config_operations: Union[List[FleetDeploymentOperation], UnsetType] = unset,
        duration_seconds: Union[int, UnsetType] = unset,
        error_summary: Union[str, UnsetType] = unset,
        estimated_finished_at: Union[int, UnsetType] = unset,
        finished_at: Union[int, UnsetType] = unset,
        is_scheduled: Union[bool, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        schedule_id: Union[str, UnsetType] = unset,
        started_at: Union[int, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        target_versions: Union[List[str], UnsetType] = unset,
        total_hosts: Union[int, UnsetType] = unset,
        update_type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a deployment in the v2 API response.

        :param author: Handle of the user who triggered the deployment.
        :type author: str, optional

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

        :param finished_at: Time the deployment finished as a Unix timestamp. Zero if not yet finished.
        :type finished_at: int, optional

        :param is_scheduled: Whether this deployment was triggered by a schedule ( ``schedule_id`` is non-empty).
        :type is_scheduled: bool, optional

        :param query: Query used to filter and select target hosts for the deployment.
        :type query: str, optional

        :param schedule_id: Identifier of the schedule that triggered this deployment. Empty if triggered manually.
        :type schedule_id: str, optional

        :param started_at: Time the deployment started as a Unix timestamp. Zero if not yet started.
        :type started_at: int, optional

        :param status: Current high-level status of the deployment (for example, "pending", "running",
            "completed", "failed").
        :type status: str, optional

        :param target_versions: Package versions targeted by this deployment.
        :type target_versions: [str], optional

        :param total_hosts: Total number of hosts targeted by this deployment.
        :type total_hosts: int, optional

        :param update_type: Type of update operation performed by this deployment
            (for example, "update_config_operations", "update_package").
        :type update_type: str, optional
        """
        if author is not unset:
            kwargs["author"] = author
        if config_operations is not unset:
            kwargs["config_operations"] = config_operations
        if duration_seconds is not unset:
            kwargs["duration_seconds"] = duration_seconds
        if error_summary is not unset:
            kwargs["error_summary"] = error_summary
        if estimated_finished_at is not unset:
            kwargs["estimated_finished_at"] = estimated_finished_at
        if finished_at is not unset:
            kwargs["finished_at"] = finished_at
        if is_scheduled is not unset:
            kwargs["is_scheduled"] = is_scheduled
        if query is not unset:
            kwargs["query"] = query
        if schedule_id is not unset:
            kwargs["schedule_id"] = schedule_id
        if started_at is not unset:
            kwargs["started_at"] = started_at
        if status is not unset:
            kwargs["status"] = status
        if target_versions is not unset:
            kwargs["target_versions"] = target_versions
        if total_hosts is not unset:
            kwargs["total_hosts"] = total_hosts
        if update_type is not unset:
            kwargs["update_type"] = update_type
        super().__init__(kwargs)
