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
    from datadog_api_client.v2.model.flag_suggestion_attributes import FlagSuggestionAttributes
    from datadog_api_client.v2.model.flag_suggestion_data_type import FlagSuggestionDataType


class FlagSuggestion(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.flag_suggestion_attributes import FlagSuggestionAttributes
        from datadog_api_client.v2.model.flag_suggestion_data_type import FlagSuggestionDataType

        return {
            "attributes": (FlagSuggestionAttributes,),
            "id": (UUID,),
            "type": (FlagSuggestionDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: FlagSuggestionAttributes, id: UUID, type: FlagSuggestionDataType, **kwargs):
        """
        A flag change suggestion.

        :param attributes: Attributes of a flag suggestion.
        :type attributes: FlagSuggestionAttributes

        :param id: Unique identifier for the suggestion.
        :type id: UUID

        :param type: Flag suggestions resource type.
        :type type: FlagSuggestionDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
