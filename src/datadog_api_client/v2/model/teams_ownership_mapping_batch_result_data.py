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
    from datadog_api_client.v2.model.teams_ownership_mapping_batch_result_data_attributes import (
        TeamsOwnershipMappingBatchResultDataAttributes,
    )
    from datadog_api_client.v2.model.teams_ownership_mapping_type import TeamsOwnershipMappingType


class TeamsOwnershipMappingBatchResultData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.teams_ownership_mapping_batch_result_data_attributes import (
            TeamsOwnershipMappingBatchResultDataAttributes,
        )
        from datadog_api_client.v2.model.teams_ownership_mapping_type import TeamsOwnershipMappingType

        return {
            "attributes": (TeamsOwnershipMappingBatchResultDataAttributes,),
            "id": (str,),
            "type": (TeamsOwnershipMappingType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: TeamsOwnershipMappingBatchResultDataAttributes,
        id: str,
        type: TeamsOwnershipMappingType,
        **kwargs,
    ):
        """
        The mapping created by an ``add`` operation.

        :param attributes: The attributes of a mapping created by an ``add`` operation.
        :type attributes: TeamsOwnershipMappingBatchResultDataAttributes

        :param id: The unique identifier of the teams ownership mapping.
        :type id: str

        :param type: The type of the resource. The value should always be teams_ownership_mappings.
        :type type: TeamsOwnershipMappingType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
