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
    from datadog_api_client.v2.model.fleet_deployment_attributes import FleetDeploymentAttributes
    from datadog_api_client.v2.model.fleet_deployment_resource_type import FleetDeploymentResourceType


class FleetDeployment(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_deployment_attributes import FleetDeploymentAttributes
        from datadog_api_client.v2.model.fleet_deployment_resource_type import FleetDeploymentResourceType

        return {
            "attributes": (FleetDeploymentAttributes,),
            "id": (str,),
            "type": (FleetDeploymentResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: FleetDeploymentAttributes, id: str, type: FleetDeploymentResourceType, **kwargs):
        """
        A deployment that defines automated configuration changes for a fleet of hosts.

        :param attributes: Attributes of a deployment in the response.
        :type attributes: FleetDeploymentAttributes

        :param id: Unique identifier for the deployment.
        :type id: str

        :param type: The type of deployment resource.
        :type type: FleetDeploymentResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
