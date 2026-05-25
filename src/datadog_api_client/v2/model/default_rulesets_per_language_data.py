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
    from datadog_api_client.v2.model.default_rulesets_per_language_data_attributes import (
        DefaultRulesetsPerLanguageDataAttributes,
    )
    from datadog_api_client.v2.model.default_rulesets_per_language_data_type import DefaultRulesetsPerLanguageDataType


class DefaultRulesetsPerLanguageData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.default_rulesets_per_language_data_attributes import (
            DefaultRulesetsPerLanguageDataAttributes,
        )
        from datadog_api_client.v2.model.default_rulesets_per_language_data_type import (
            DefaultRulesetsPerLanguageDataType,
        )

        return {
            "attributes": (DefaultRulesetsPerLanguageDataAttributes,),
            "id": (str,),
            "type": (DefaultRulesetsPerLanguageDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: DefaultRulesetsPerLanguageDataAttributes,
        id: str,
        type: DefaultRulesetsPerLanguageDataType,
        **kwargs,
    ):
        """
        The primary data object in the default rulesets per language response.

        :param attributes: The attributes of the default rulesets per language response, containing the list of default ruleset names.
        :type attributes: DefaultRulesetsPerLanguageDataAttributes

        :param id: The language identifier used as the resource identifier.
        :type id: str

        :param type: Default rulesets per language resource type.
        :type type: DefaultRulesetsPerLanguageDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
