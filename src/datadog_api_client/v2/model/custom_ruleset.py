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
    from datadog_api_client.v2.model.custom_ruleset_attributes import CustomRulesetAttributes
    from datadog_api_client.v2.model.custom_ruleset_data_type import CustomRulesetDataType


class CustomRuleset(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_ruleset_attributes import CustomRulesetAttributes
        from datadog_api_client.v2.model.custom_ruleset_data_type import CustomRulesetDataType

        return {
            "attributes": (CustomRulesetAttributes,),
            "id": (str,),
            "type": (CustomRulesetDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: CustomRulesetAttributes, id: str, type: CustomRulesetDataType, **kwargs):
        """


        :param attributes:
        :type attributes: CustomRulesetAttributes

        :param id: Ruleset identifier
        :type id: str

        :param type: Resource type
        :type type: CustomRulesetDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
