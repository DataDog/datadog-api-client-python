# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.review_flag_suggestion_attributes import ReviewFlagSuggestionAttributes
    from datadog_api_client.v2.model.flag_suggestion_event_data_type import FlagSuggestionEventDataType


class ReviewFlagSuggestionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.review_flag_suggestion_attributes import ReviewFlagSuggestionAttributes
        from datadog_api_client.v2.model.flag_suggestion_event_data_type import FlagSuggestionEventDataType

        return {
            "attributes": (ReviewFlagSuggestionAttributes,),
            "type": (FlagSuggestionEventDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: FlagSuggestionEventDataType,
        attributes: Union[ReviewFlagSuggestionAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for reviewing a flag suggestion.

        :param attributes: Attributes for reviewing a flag suggestion.
        :type attributes: ReviewFlagSuggestionAttributes, optional

        :param type: Flag suggestion events resource type.
        :type type: FlagSuggestionEventDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
