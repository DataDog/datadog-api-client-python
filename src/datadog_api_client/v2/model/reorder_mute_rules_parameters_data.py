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
    from datadog_api_client.v2.model.mute_rules_type import MuteRulesType


class ReorderMuteRulesParametersData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.mute_rules_type import MuteRulesType

        return {
            "id": (UUID,),
            "type": (MuteRulesType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: UUID, type: MuteRulesType, **kwargs):
        """
        Data of the mute rule reorder request: a rule UUID and its type. All fields are required.

        :param id: The ID of a pipeline rule
        :type id: UUID

        :param type: The pipeline rule type associated to mute rules
        :type type: MuteRulesType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
