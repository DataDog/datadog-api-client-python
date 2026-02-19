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
    from datadog_api_client.v2.model.default_rule_response_attributes import DefaultRuleResponseAttributes
    from datadog_api_client.v2.model.default_rule_type import DefaultRuleType


class DefaultRuleResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.default_rule_response_attributes import DefaultRuleResponseAttributes
        from datadog_api_client.v2.model.default_rule_type import DefaultRuleType

        return {
            "attributes": (DefaultRuleResponseAttributes,),
            "id": (str,),
            "type": (DefaultRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: DefaultRuleResponseAttributes, id: str, type: DefaultRuleType, **kwargs):
        """
        Default rule data.

        :param attributes: Default rule attributes.
        :type attributes: DefaultRuleResponseAttributes

        :param id: The unique ID of the default rule.
        :type id: str

        :param type: The JSON:API type for default rules.
        :type type: DefaultRuleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
