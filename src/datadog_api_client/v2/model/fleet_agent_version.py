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
    from datadog_api_client.v2.model.fleet_agent_version_attributes import FleetAgentVersionAttributes
    from datadog_api_client.v2.model.fleet_agent_version_resource_type import FleetAgentVersionResourceType


class FleetAgentVersion(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_agent_version_attributes import FleetAgentVersionAttributes
        from datadog_api_client.v2.model.fleet_agent_version_resource_type import FleetAgentVersionResourceType

        return {
            "attributes": (FleetAgentVersionAttributes,),
            "id": (str,),
            "type": (FleetAgentVersionResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: FleetAgentVersionResourceType,
        attributes: Union[FleetAgentVersionAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Represents an available Datadog Agent version.

        :param attributes:
        :type attributes: FleetAgentVersionAttributes, optional

        :param id: Unique identifier for the Agent version (same as version).
        :type id: str

        :param type: The type of Agent version resource.
        :type type: FleetAgentVersionResourceType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
