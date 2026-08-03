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
    from datadog_api_client.v2.model.fleet_deployment_configure_v2_dry_run import FleetDeploymentConfigureV2DryRun


class FleetDeploymentConfigureV2DryRunResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_deployment_configure_v2_dry_run import FleetDeploymentConfigureV2DryRun

        return {
            "data": (FleetDeploymentConfigureV2DryRun,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: FleetDeploymentConfigureV2DryRun, **kwargs):
        """
        Response containing the result of a configuration deployment dry run.

        :param data: The result of a configuration deployment dry run.
        :type data: FleetDeploymentConfigureV2DryRun
        """
        super().__init__(kwargs)

        self_.data = data
