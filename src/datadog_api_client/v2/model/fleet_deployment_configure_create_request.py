# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.fleet_deployment_configure_create import FleetDeploymentConfigureCreate


class FleetDeploymentConfigureCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_deployment_configure_create import FleetDeploymentConfigureCreate

        return {
            "data": (FleetDeploymentConfigureCreate,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: FleetDeploymentConfigureCreate, **kwargs):
        """
        Request payload for creating a new deployment.

        :param data: Data for creating a new deployment.
        :type data: FleetDeploymentConfigureCreate
        """
        super().__init__(kwargs)

        self_.data = data
