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
    from datadog_api_client.v2.model.fleet_deployment_hosts_page import FleetDeploymentHostsPage


class FleetDeploymentResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_deployment_hosts_page import FleetDeploymentHostsPage

        return {
            "hosts": (FleetDeploymentHostsPage,),
        }

    attribute_map = {
        "hosts": "hosts",
    }

    def __init__(self_, hosts: Union[FleetDeploymentHostsPage, UnsetType] = unset, **kwargs):
        """
        Metadata for a single deployment response, including pagination information for hosts.

        :param hosts: Pagination details for the list of hosts in a deployment.
        :type hosts: FleetDeploymentHostsPage, optional
        """
        if hosts is not unset:
            kwargs["hosts"] = hosts
        super().__init__(kwargs)
