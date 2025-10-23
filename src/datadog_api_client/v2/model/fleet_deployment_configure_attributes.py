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


class FleetDeploymentConfigureAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_deployment_operation import FleetDeploymentOperation

        return {
            "config_operations": ([FleetDeploymentOperation],),
            "filter_query": (str,),
        }

    attribute_map = {
        "config_operations": "config_operations",
        "filter_query": "filter_query",
    }

    def __init__(
        self_, config_operations: List[FleetDeploymentOperation], filter_query: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Attributes for creating a new configuration deployment.

        :param config_operations: Ordered list of configuration file operations to perform on the target hosts.
        :type config_operations: [FleetDeploymentOperation]

        :param filter_query: Query used to filter and select target hosts for the deployment. Uses the Datadog query syntax.
        :type filter_query: str, optional
        """
        if filter_query is not unset:
            kwargs["filter_query"] = filter_query
        super().__init__(kwargs)

        self_.config_operations = config_operations
