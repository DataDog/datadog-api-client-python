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


class SuggestionMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "variant_id": (str,),
        }

    attribute_map = {
        "variant_id": "variant_id",
    }

    def __init__(self_, variant_id: Union[str, UnsetType] = unset, **kwargs):
        """
        Optional metadata for a suggestion.

        :param variant_id: Variant ID for variant delete suggestions.
        :type variant_id: str, optional
        """
        if variant_id is not unset:
            kwargs["variant_id"] = variant_id
        super().__init__(kwargs)
