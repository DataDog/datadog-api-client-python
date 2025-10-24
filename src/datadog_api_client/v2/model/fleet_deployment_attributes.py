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


class FleetDeploymentAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_deployment_operation import FleetDeploymentOperation

        return {
            "config_operations": ([FleetDeploymentOperation],),
            "estimated_end_time_unix": (int,),
            "filter_query": (str,),
            "high_level_status": (str,),
            "total_hosts": (int,),
        }

    attribute_map = {
        "config_operations": "config_operations",
        "estimated_end_time_unix": "estimated_end_time_unix",
        "filter_query": "filter_query",
        "high_level_status": "high_level_status",
        "total_hosts": "total_hosts",
    }

    def __init__(
        self_,
        config_operations: Union[List[FleetDeploymentOperation], UnsetType] = unset,
        estimated_end_time_unix: Union[int, UnsetType] = unset,
        filter_query: Union[str, UnsetType] = unset,
        high_level_status: Union[str, UnsetType] = unset,
        total_hosts: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a deployment in the response.

        :param config_operations: Ordered list of configuration file operations to perform on the target hosts.
        :type config_operations: [FleetDeploymentOperation], optional

        :param estimated_end_time_unix: Estimated completion time of the deployment as a Unix timestamp (seconds since epoch).
        :type estimated_end_time_unix: int, optional

        :param filter_query: Query used to filter and select target hosts for the deployment. Uses the Datadog query syntax.
        :type filter_query: str, optional

        :param high_level_status: Current high-level status of the deployment (for example, "pending", "running", "completed", "failed").
        :type high_level_status: str, optional

        :param total_hosts: Total number of hosts targeted by this deployment.
        :type total_hosts: int, optional
        """
        if config_operations is not unset:
            kwargs["config_operations"] = config_operations
        if estimated_end_time_unix is not unset:
            kwargs["estimated_end_time_unix"] = estimated_end_time_unix
        if filter_query is not unset:
            kwargs["filter_query"] = filter_query
        if high_level_status is not unset:
            kwargs["high_level_status"] = high_level_status
        if total_hosts is not unset:
            kwargs["total_hosts"] = total_hosts
        super().__init__(kwargs)
