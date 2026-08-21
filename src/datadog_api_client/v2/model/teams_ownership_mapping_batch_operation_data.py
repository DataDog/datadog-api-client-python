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
    from datadog_api_client.v2.model.teams_ownership_mapping_batch_operation_data_attributes import (
        TeamsOwnershipMappingBatchOperationDataAttributes,
    )
    from datadog_api_client.v2.model.teams_ownership_mapping_type import TeamsOwnershipMappingType


class TeamsOwnershipMappingBatchOperationData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.teams_ownership_mapping_batch_operation_data_attributes import (
            TeamsOwnershipMappingBatchOperationDataAttributes,
        )
        from datadog_api_client.v2.model.teams_ownership_mapping_type import TeamsOwnershipMappingType

        return {
            "attributes": (TeamsOwnershipMappingBatchOperationDataAttributes,),
            "type": (TeamsOwnershipMappingType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: TeamsOwnershipMappingBatchOperationDataAttributes, type: TeamsOwnershipMappingType, **kwargs
    ):
        """
        The mapping to add. Required when ``op`` is ``add``.

        :param attributes: The attributes of the mapping to add. ``team_handle`` and ``view_name`` are required
            when ``op`` is ``add``. At least one of ``service`` or ``application_id`` must be provided.
        :type attributes: TeamsOwnershipMappingBatchOperationDataAttributes

        :param type: The type of the resource. The value should always be teams_ownership_mappings.
        :type type: TeamsOwnershipMappingType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
