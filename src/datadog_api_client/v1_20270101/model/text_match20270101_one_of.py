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
    from datadog_api_client.v1_20270101.model.text_match_any_of_any_of_item_type import TextMatchAnyOfAnyOfItemType


class TextMatch20270101OneOf(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.text_match_any_of_any_of_item_type import TextMatchAnyOfAnyOfItemType

        return {
            "type": (TextMatchAnyOfAnyOfItemType,),
            "value": (str,),
        }

    attribute_map = {
        "type": "type",
        "value": "value",
    }

    def __init__(self_, type: TextMatchAnyOfAnyOfItemType, value: str, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: TextMatchAnyOfAnyOfItemType

        :param value: Test-only generated schema for the dashboard versioning proof of concept.
        :type value: str
        """
        super().__init__(kwargs)

        self_.type = type
        self_.value = value
