# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SensitiveDataScannerIncludedKeywordConfiguration(ModelNormal):
    validations = {
        "character_count": {
            "inclusive_maximum": 50,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "character_count": (int,),
            "keywords": ([str],),
            "use_recommended_keywords": (bool,),
        }

    attribute_map = {
        "character_count": "character_count",
        "keywords": "keywords",
        "use_recommended_keywords": "use_recommended_keywords",
    }

    def __init__(
        self_,
        character_count: int,
        keywords: List[str],
        use_recommended_keywords: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object defining a set of keywords and a number of characters that help reduce noise.
        You can provide a list of keywords you would like to check within a defined proximity of the matching pattern.
        If any of the keywords are found within the proximity check, the match is kept.
        If none are found, the match is discarded.

        :param character_count: The number of characters behind a match detected by Sensitive Data Scanner to look for the keywords defined.
            ``character_count`` should be greater than the maximum length of a keyword defined for a rule.
        :type character_count: int

        :param keywords: Keyword list that will be checked during scanning in order to validate a match.
            The number of keywords in the list must be less than or equal to 30.
        :type keywords: [str]

        :param use_recommended_keywords: Should the rule use the underlying standard pattern keyword configuration. If set to ``true`` , the rule must be tied
            to a standard pattern. If set to ``false`` , the specified keywords and ``character_count`` are applied.
        :type use_recommended_keywords: bool, optional
        """
        if use_recommended_keywords is not unset:
            kwargs["use_recommended_keywords"] = use_recommended_keywords
        super().__init__(kwargs)

        self_.character_count = character_count
        self_.keywords = keywords
