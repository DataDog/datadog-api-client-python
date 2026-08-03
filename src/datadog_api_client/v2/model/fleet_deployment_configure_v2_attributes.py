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
    from datadog_api_client.v2.model.fleet_deployment_configure_v2_package import FleetDeploymentConfigureV2Package


class FleetDeploymentConfigureV2Attributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_deployment_operation import FleetDeploymentOperation
        from datadog_api_client.v2.model.fleet_deployment_configure_v2_package import FleetDeploymentConfigureV2Package

        return {
            "config_operations": ([FleetDeploymentOperation],),
            "dry_run": (bool,),
            "filter_query": (str,),
            "target_packages": ([FleetDeploymentConfigureV2Package],),
        }

    attribute_map = {
        "config_operations": "config_operations",
        "dry_run": "dry_run",
        "filter_query": "filter_query",
        "target_packages": "target_packages",
    }

    def __init__(
        self_,
        config_operations: List[FleetDeploymentOperation],
        filter_query: str,
        dry_run: Union[bool, UnsetType] = unset,
        target_packages: Union[List[FleetDeploymentConfigureV2Package], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating a new v2 configuration deployment.

        :param config_operations: Ordered list of configuration file operations to perform on the target hosts.
        :type config_operations: [FleetDeploymentOperation]

        :param dry_run: Set to ``true`` to validate the configuration and resolve target hosts and packages
            without deploying anything. Returns a 200 with the validation result instead of
            creating and starting a real deployment.
        :type dry_run: bool, optional

        :param filter_query: Query used to filter and select target hosts for the deployment. Uses the Datadog query syntax.
        :type filter_query: str

        :param target_packages: List of packages and their target versions to additionally deploy alongside
            the configuration change.
        :type target_packages: [FleetDeploymentConfigureV2Package], optional
        """
        if dry_run is not unset:
            kwargs["dry_run"] = dry_run
        if target_packages is not unset:
            kwargs["target_packages"] = target_packages
        super().__init__(kwargs)

        self_.config_operations = config_operations
        self_.filter_query = filter_query
