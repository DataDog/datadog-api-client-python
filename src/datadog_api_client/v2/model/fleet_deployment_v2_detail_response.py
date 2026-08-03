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
    from datadog_api_client.v2.model.fleet_deployment_v2_detail import FleetDeploymentV2Detail


class FleetDeploymentV2DetailResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_deployment_v2_detail import FleetDeploymentV2Detail

        return {
            "data": (FleetDeploymentV2Detail,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: FleetDeploymentV2Detail, **kwargs):
        """
        Response containing detailed information about a single deployment.

        :param data: Detailed information about a deployment.
        :type data: FleetDeploymentV2Detail
        """
        super().__init__(kwargs)

        self_.data = data
