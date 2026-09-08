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
    from datadog_api_client.v2.model.custom_rule_attributes import CustomRuleAttributes
    from datadog_api_client.v2.model.custom_rule_data_type import CustomRuleDataType


class CustomRuleResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_rule_attributes import CustomRuleAttributes
        from datadog_api_client.v2.model.custom_rule_data_type import CustomRuleDataType

        return {
            "attributes": (CustomRuleAttributes,),
            "id": (str,),
            "type": (CustomRuleDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: CustomRuleAttributes, id: str, type: CustomRuleDataType, **kwargs):
        """
        Data object returned in a custom rule response, including its ID, type, and attributes.

        :param attributes: Attributes of a custom static analysis rule, including its most recent revision and revision history.
        :type attributes: CustomRuleAttributes

        :param id: Rule identifier
        :type id: str

        :param type: Resource type
        :type type: CustomRuleDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
