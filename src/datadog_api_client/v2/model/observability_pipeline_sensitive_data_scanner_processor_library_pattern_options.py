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


class ObservabilityPipelineSensitiveDataScannerProcessorLibraryPatternOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "use_recommended_keywords": (bool,),
        }

    attribute_map = {
        "id": "id",
        "use_recommended_keywords": "use_recommended_keywords",
    }

    def __init__(self_, id: str, use_recommended_keywords: Union[bool, UnsetType] = unset, **kwargs):
        """
        Options for selecting a predefined library pattern and enabling keyword support.

        :param id: Identifier for a predefined pattern from the sensitive data scanner pattern library.
        :type id: str

        :param use_recommended_keywords: Whether to augment the pattern with recommended keywords (optional).
        :type use_recommended_keywords: bool, optional
        """
        if use_recommended_keywords is not unset:
            kwargs["use_recommended_keywords"] = use_recommended_keywords
        super().__init__(kwargs)

        self_.id = id
