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
    from datadog_api_client.v1_20270101.model.text_formatting_rule_replace_any_of_any_of_item_type import (
        TextFormattingRuleReplaceAnyOfAnyOfItemType,
    )


class TextFormattingRule20270101ReplaceOneOf(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.text_formatting_rule_replace_any_of_any_of_item_type import (
            TextFormattingRuleReplaceAnyOfAnyOfItemType,
        )

        return {
            "substring": (str,),
            "type": (TextFormattingRuleReplaceAnyOfAnyOfItemType,),
            "_with": (str,),
        }

    attribute_map = {
        "substring": "substring",
        "type": "type",
        "_with": "with",
    }

    def __init__(self_, substring: str, type: TextFormattingRuleReplaceAnyOfAnyOfItemType, _with: str, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param substring: Test-only generated schema for the dashboard versioning proof of concept.
        :type substring: str

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: TextFormattingRuleReplaceAnyOfAnyOfItemType

        :param _with: Test-only generated schema for the dashboard versioning proof of concept.
        :type _with: str
        """
        super().__init__(kwargs)

        self_.substring = substring
        self_.type = type
        self_._with = _with
