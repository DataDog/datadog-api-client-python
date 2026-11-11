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
    from datadog_api_client.v2.model.feature_flag_suggestion_attributes import FeatureFlagSuggestionAttributes
    from datadog_api_client.v2.model.feature_flag_suggestion_data_type import FeatureFlagSuggestionDataType


class FeatureFlagSuggestion(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.feature_flag_suggestion_attributes import FeatureFlagSuggestionAttributes
        from datadog_api_client.v2.model.feature_flag_suggestion_data_type import FeatureFlagSuggestionDataType

        return {
            "attributes": (FeatureFlagSuggestionAttributes,),
            "id": (UUID,),
            "type": (FeatureFlagSuggestionDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: FeatureFlagSuggestionAttributes, id: UUID, type: FeatureFlagSuggestionDataType, **kwargs
    ):
        """
        A proposed feature flag change and its approval lifecycle.

        :param attributes: Attributes of a feature flag change suggestion.
        :type attributes: FeatureFlagSuggestionAttributes

        :param id: The unique identifier of the suggestion.
        :type id: UUID

        :param type: The resource type for feature flag suggestions.
        :type type: FeatureFlagSuggestionDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
