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
    from datadog_api_client.v2.model.ai_custom_rule_revision_response_attributes import (
        AiCustomRuleRevisionResponseAttributes,
    )
    from datadog_api_client.v2.model.ai_custom_rule_revision_data_type import AiCustomRuleRevisionDataType


class AiCustomRuleRevisionResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_custom_rule_revision_response_attributes import (
            AiCustomRuleRevisionResponseAttributes,
        )
        from datadog_api_client.v2.model.ai_custom_rule_revision_data_type import AiCustomRuleRevisionDataType

        return {
            "attributes": (AiCustomRuleRevisionResponseAttributes,),
            "id": (str,),
            "type": (AiCustomRuleRevisionDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: AiCustomRuleRevisionResponseAttributes, id: str, type: AiCustomRuleRevisionDataType, **kwargs
    ):
        """
        Response data for an AI custom rule revision.

        :param attributes: Response attributes of an AI custom rule revision.
        :type attributes: AiCustomRuleRevisionResponseAttributes

        :param id: The revision identifier.
        :type id: str

        :param type: AI custom rule revision resource type.
        :type type: AiCustomRuleRevisionDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
