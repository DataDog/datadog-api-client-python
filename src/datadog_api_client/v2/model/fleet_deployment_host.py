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
    from datadog_api_client.v2.model.fleet_deployment_host_package import FleetDeploymentHostPackage


class FleetDeploymentHost(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_deployment_host_package import FleetDeploymentHostPackage

        return {
            "error": (str,),
            "hostname": (str,),
            "status": (str,),
            "versions": ([FleetDeploymentHostPackage],),
        }

    attribute_map = {
        "error": "error",
        "hostname": "hostname",
        "status": "status",
        "versions": "versions",
    }

    def __init__(
        self_,
        error: Union[str, UnsetType] = unset,
        hostname: Union[str, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        versions: Union[List[FleetDeploymentHostPackage], UnsetType] = unset,
        **kwargs,
    ):
        """
        A host that is part of a deployment with its current status.

        :param error: Error message if the deployment failed on this host.
        :type error: str, optional

        :param hostname: The hostname of the agent.
        :type hostname: str, optional

        :param status: Current deployment status for this specific host.
        :type status: str, optional

        :param versions: List of packages and their versions currently installed on this host.
        :type versions: [FleetDeploymentHostPackage], optional
        """
        if error is not unset:
            kwargs["error"] = error
        if hostname is not unset:
            kwargs["hostname"] = hostname
        if status is not unset:
            kwargs["status"] = status
        if versions is not unset:
            kwargs["versions"] = versions
        super().__init__(kwargs)
