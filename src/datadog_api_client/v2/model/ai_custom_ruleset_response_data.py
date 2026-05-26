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
    from datadog_api_client.v2.model.ai_custom_ruleset_response_attributes import AiCustomRulesetResponseAttributes
    from datadog_api_client.v2.model.ai_custom_ruleset_data_type import AiCustomRulesetDataType


class AiCustomRulesetResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_custom_ruleset_response_attributes import AiCustomRulesetResponseAttributes
        from datadog_api_client.v2.model.ai_custom_ruleset_data_type import AiCustomRulesetDataType

        return {
            "attributes": (AiCustomRulesetResponseAttributes,),
            "id": (str,),
            "type": (AiCustomRulesetDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: AiCustomRulesetResponseAttributes, id: str, type: AiCustomRulesetDataType, **kwargs
    ):
        """
        Response data for an AI custom ruleset.

        :param attributes: Response attributes of an AI custom ruleset.
        :type attributes: AiCustomRulesetResponseAttributes

        :param id: The ruleset identifier.
        :type id: str

        :param type: AI custom ruleset resource type.
        :type type: AiCustomRulesetDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
