# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_bandit_v2_list_dto_data_attributes import (
        ExperimentsBanditV2ListDTODataAttributes,
    )
    from datadog_api_client.v2.model.experiments_bandit_v2_dto_data_type import ExperimentsBanditV2DTODataType


class ExperimentsBanditV2ListDTOData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_bandit_v2_list_dto_data_attributes import (
            ExperimentsBanditV2ListDTODataAttributes,
        )
        from datadog_api_client.v2.model.experiments_bandit_v2_dto_data_type import ExperimentsBanditV2DTODataType

        return {
            "attributes": (ExperimentsBanditV2ListDTODataAttributes,),
            "id": (UUID,),
            "type": (ExperimentsBanditV2DTODataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ExperimentsBanditV2ListDTODataAttributes,
        id: UUID,
        type: ExperimentsBanditV2DTODataType,
        **kwargs,
    ):
        """
        JSON:API resource containing a bandit summary.

        :param attributes: Summary of a bandit. Use Get bandit for its setup, active policy, and latest refresh.
        :type attributes: ExperimentsBanditV2ListDTODataAttributes

        :param id: The bandit ID.
        :type id: UUID

        :param type: Bandit resource type.
        :type type: ExperimentsBanditV2DTODataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
