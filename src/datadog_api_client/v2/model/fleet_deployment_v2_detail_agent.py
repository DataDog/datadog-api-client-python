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


class FleetDeploymentV2DetailAgent(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_deployment_host_package import FleetDeploymentHostPackage

        return {
            "error": (str,),
            "hostname": (str,),
            "running_step": (str,),
            "status": (str,),
            "status_details": (str,),
            "versions": ([FleetDeploymentHostPackage],),
        }

    attribute_map = {
        "error": "error",
        "hostname": "hostname",
        "running_step": "running_step",
        "status": "status",
        "status_details": "status_details",
        "versions": "versions",
    }

    def __init__(
        self_,
        error: Union[str, UnsetType] = unset,
        hostname: Union[str, UnsetType] = unset,
        running_step: Union[str, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        status_details: Union[str, UnsetType] = unset,
        versions: Union[List[FleetDeploymentHostPackage], UnsetType] = unset,
        **kwargs,
    ):
        """
        Per-host status entry for a deployment.

        :param error: Error message if the deployment failed on this host.
        :type error: str, optional

        :param hostname: Hostname of the agent.
        :type hostname: str, optional

        :param running_step: Name of the step currently executing on this host.
        :type running_step: str, optional

        :param status: Deployment status for this host (for example, "pending", "running", "succeeded", "failed").
        :type status: str, optional

        :param status_details: Additional details about the current deployment status on this host.
        :type status_details: str, optional

        :param versions: Package version details for this host.
        :type versions: [FleetDeploymentHostPackage], optional
        """
        if error is not unset:
            kwargs["error"] = error
        if hostname is not unset:
            kwargs["hostname"] = hostname
        if running_step is not unset:
            kwargs["running_step"] = running_step
        if status is not unset:
            kwargs["status"] = status
        if status_details is not unset:
            kwargs["status_details"] = status_details
        if versions is not unset:
            kwargs["versions"] = versions
        super().__init__(kwargs)
