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
    from datadog_api_client.v2.model.fleet_deployment_package import FleetDeploymentPackage


class FleetDeploymentPackageUpgradeAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_deployment_package import FleetDeploymentPackage

        return {
            "filter_query": (str,),
            "target_packages": ([FleetDeploymentPackage],),
        }

    attribute_map = {
        "filter_query": "filter_query",
        "target_packages": "target_packages",
    }

    def __init__(
        self_, target_packages: List[FleetDeploymentPackage], filter_query: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Attributes for creating a new package upgrade deployment.

        :param filter_query: Query used to filter and select target hosts for the deployment. Uses the Datadog query syntax.
        :type filter_query: str, optional

        :param target_packages: List of packages and their target versions to deploy to the selected hosts.
        :type target_packages: [FleetDeploymentPackage]
        """
        if filter_query is not unset:
            kwargs["filter_query"] = filter_query
        super().__init__(kwargs)

        self_.target_packages = target_packages
