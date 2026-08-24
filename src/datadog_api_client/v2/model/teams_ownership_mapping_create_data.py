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
    from datadog_api_client.v2.model.teams_ownership_mapping_create_data_attributes import (
        TeamsOwnershipMappingCreateDataAttributes,
    )
    from datadog_api_client.v2.model.teams_ownership_mapping_type import TeamsOwnershipMappingType


class TeamsOwnershipMappingCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.teams_ownership_mapping_create_data_attributes import (
            TeamsOwnershipMappingCreateDataAttributes,
        )
        from datadog_api_client.v2.model.teams_ownership_mapping_type import TeamsOwnershipMappingType

        return {
            "attributes": (TeamsOwnershipMappingCreateDataAttributes,),
            "type": (TeamsOwnershipMappingType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: TeamsOwnershipMappingCreateDataAttributes, type: TeamsOwnershipMappingType, **kwargs
    ):
        """
        The JSON:API data envelope for a teams ownership mapping create request.

        :param attributes: The attributes of the teams ownership mapping to create.
        :type attributes: TeamsOwnershipMappingCreateDataAttributes

        :param type: The type of the resource. The value should always be teams_ownership_mappings.
        :type type: TeamsOwnershipMappingType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
