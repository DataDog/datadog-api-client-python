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
    from datadog_api_client.v2.model.default_rulesets_per_language_data import DefaultRulesetsPerLanguageData


class DefaultRulesetsPerLanguageResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.default_rulesets_per_language_data import DefaultRulesetsPerLanguageData

        return {
            "data": (DefaultRulesetsPerLanguageData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: DefaultRulesetsPerLanguageData, **kwargs):
        """
        The response payload containing the default ruleset names for a programming language.

        :param data: The primary data object in the default rulesets per language response.
        :type data: DefaultRulesetsPerLanguageData
        """
        super().__init__(kwargs)

        self_.data = data
