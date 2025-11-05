# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class FleetDeploymentHostPackage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "current_version": (str,),
            "initial_version": (str,),
            "package_name": (str,),
            "target_version": (str,),
        }

    attribute_map = {
        "current_version": "current_version",
        "initial_version": "initial_version",
        "package_name": "package_name",
        "target_version": "target_version",
    }

    def __init__(
        self_,
        current_version: Union[str, UnsetType] = unset,
        initial_version: Union[str, UnsetType] = unset,
        package_name: Union[str, UnsetType] = unset,
        target_version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Package version information for a host, showing the initial version before deployment,
        the target version to deploy, and the current version on the host.

        :param current_version: The current version of the package on the host.
        :type current_version: str, optional

        :param initial_version: The initial version of the package on the host before the deployment started.
        :type initial_version: str, optional

        :param package_name: The name of the package.
        :type package_name: str, optional

        :param target_version: The target version that the deployment is attempting to install.
        :type target_version: str, optional
        """
        if current_version is not unset:
            kwargs["current_version"] = current_version
        if initial_version is not unset:
            kwargs["initial_version"] = initial_version
        if package_name is not unset:
            kwargs["package_name"] = package_name
        if target_version is not unset:
            kwargs["target_version"] = target_version
        super().__init__(kwargs)
