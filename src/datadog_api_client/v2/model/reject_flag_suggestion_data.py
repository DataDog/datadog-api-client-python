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
    from datadog_api_client.v2.model.reject_flag_suggestion_attributes import RejectFlagSuggestionAttributes
    from datadog_api_client.v2.model.review_flag_suggestion_data_type import ReviewFlagSuggestionDataType


class RejectFlagSuggestionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.reject_flag_suggestion_attributes import RejectFlagSuggestionAttributes
        from datadog_api_client.v2.model.review_flag_suggestion_data_type import ReviewFlagSuggestionDataType

        return {
            "attributes": (RejectFlagSuggestionAttributes,),
            "type": (ReviewFlagSuggestionDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: RejectFlagSuggestionAttributes, type: ReviewFlagSuggestionDataType, **kwargs):
        """
        The rejection event to create.

        :param attributes: Rejection options for the suggestion.
        :type attributes: RejectFlagSuggestionAttributes

        :param type: The resource type for reviewing feature flag suggestions.
        :type type: ReviewFlagSuggestionDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
