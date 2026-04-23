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
    from datadog_api_client.v2.model.create_flag_suggestion_attributes import CreateFlagSuggestionAttributes
    from datadog_api_client.v2.model.flag_suggestion_data_type import FlagSuggestionDataType


class CreateFlagSuggestionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_flag_suggestion_attributes import CreateFlagSuggestionAttributes
        from datadog_api_client.v2.model.flag_suggestion_data_type import FlagSuggestionDataType

        return {
            "attributes": (CreateFlagSuggestionAttributes,),
            "type": (FlagSuggestionDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: CreateFlagSuggestionAttributes, type: FlagSuggestionDataType, **kwargs):
        """
        Data for creating a flag suggestion.

        :param attributes: Attributes for creating a flag suggestion.
        :type attributes: CreateFlagSuggestionAttributes

        :param type: Flag suggestions resource type.
        :type type: FlagSuggestionDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
