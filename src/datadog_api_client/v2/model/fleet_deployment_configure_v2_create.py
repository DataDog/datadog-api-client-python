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
    from datadog_api_client.v2.model.fleet_deployment_configure_v2_attributes import (
        FleetDeploymentConfigureV2Attributes,
    )
    from datadog_api_client.v2.model.fleet_deployment_resource_type import FleetDeploymentResourceType


class FleetDeploymentConfigureV2Create(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_deployment_configure_v2_attributes import (
            FleetDeploymentConfigureV2Attributes,
        )
        from datadog_api_client.v2.model.fleet_deployment_resource_type import FleetDeploymentResourceType

        return {
            "attributes": (FleetDeploymentConfigureV2Attributes,),
            "type": (FleetDeploymentResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: FleetDeploymentConfigureV2Attributes, type: FleetDeploymentResourceType, **kwargs):
        """
        Data for creating a new v2 configuration deployment.

        :param attributes: Attributes for creating a new v2 configuration deployment.
        :type attributes: FleetDeploymentConfigureV2Attributes

        :param type: The type of deployment resource.
        :type type: FleetDeploymentResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
