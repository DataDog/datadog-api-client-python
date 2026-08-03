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
    from datadog_api_client.v2.model.fleet_deployment_configure_v2_dry_run_attributes import (
        FleetDeploymentConfigureV2DryRunAttributes,
    )
    from datadog_api_client.v2.model.fleet_deployment_resource_type import FleetDeploymentResourceType


class FleetDeploymentConfigureV2DryRun(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_deployment_configure_v2_dry_run_attributes import (
            FleetDeploymentConfigureV2DryRunAttributes,
        )
        from datadog_api_client.v2.model.fleet_deployment_resource_type import FleetDeploymentResourceType

        return {
            "attributes": (FleetDeploymentConfigureV2DryRunAttributes,),
            "id": (str,),
            "type": (FleetDeploymentResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: FleetDeploymentConfigureV2DryRunAttributes,
        id: str,
        type: FleetDeploymentResourceType,
        **kwargs,
    ):
        """
        The result of a configuration deployment dry run.

        :param attributes: Attributes of a configuration deployment dry-run response.
        :type attributes: FleetDeploymentConfigureV2DryRunAttributes

        :param id: Always ``"dry-run"`` for a dry-run response. Does not identify a real deployment
            and cannot be used to fetch a deployment by ID.
        :type id: str

        :param type: The type of deployment resource.
        :type type: FleetDeploymentResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
