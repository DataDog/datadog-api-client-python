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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_patch_bandit_v2_request_data_attributes import (
        ExperimentsPatchBanditV2RequestDataAttributes,
    )
    from datadog_api_client.v2.model.experiments_bandit_v2_dto_data_type import ExperimentsBanditV2DTODataType


class ExperimentsPatchBanditV2RequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_bandit_v2_request_data_attributes import (
            ExperimentsPatchBanditV2RequestDataAttributes,
        )
        from datadog_api_client.v2.model.experiments_bandit_v2_dto_data_type import ExperimentsBanditV2DTODataType

        return {
            "attributes": (ExperimentsPatchBanditV2RequestDataAttributes,),
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
        attributes: ExperimentsPatchBanditV2RequestDataAttributes,
        type: ExperimentsBanditV2DTODataType,
        id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        Bandit resource with the attributes to change.

        :param attributes: The attributes to change. Omitted attributes are unchanged. Which ones can change depends on the bandit's status.
        :type attributes: ExperimentsPatchBanditV2RequestDataAttributes

        :param id: The bandit ID. When present, it must match the path.
        :type id: UUID, optional

        :param type: Bandit resource type.
        :type type: ExperimentsBanditV2DTODataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
