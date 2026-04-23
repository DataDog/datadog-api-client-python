# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ReviewFlagSuggestionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "comment": (str,),
        }

    attribute_map = {
        "comment": "comment",
    }

    def __init__(self_, comment: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes for reviewing a flag suggestion.

        :param comment: Optional comment from the reviewer.
        :type comment: str, optional
        """
        if comment is not unset:
            kwargs["comment"] = comment
        super().__init__(kwargs)
