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
    from datadog_api_client.v2.model.experiments_bandit_refresh_v2_dto_data_attributes import (
        ExperimentsBanditRefreshV2DTODataAttributes,
    )
    from datadog_api_client.v2.model.experiments_bandit_refresh_v2_dto_data_type import (
        ExperimentsBanditRefreshV2DTODataType,
    )


class ExperimentsBanditRefreshV2DTOData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_bandit_refresh_v2_dto_data_attributes import (
            ExperimentsBanditRefreshV2DTODataAttributes,
        )
        from datadog_api_client.v2.model.experiments_bandit_refresh_v2_dto_data_type import (
            ExperimentsBanditRefreshV2DTODataType,
        )

        return {
            "attributes": (ExperimentsBanditRefreshV2DTODataAttributes,),
            "id": (UUID,),
            "type": (ExperimentsBanditRefreshV2DTODataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ExperimentsBanditRefreshV2DTODataAttributes,
        id: UUID,
        type: ExperimentsBanditRefreshV2DTODataType,
        **kwargs,
    ):
        """
        The refresh that started.

        :param attributes: The bandit being refreshed.
        :type attributes: ExperimentsBanditRefreshV2DTODataAttributes

        :param id: The refresh ID. The bandit reports it as ``latest_refresh``.
        :type id: UUID

        :param type: Bandit refresh resource type.
        :type type: ExperimentsBanditRefreshV2DTODataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
