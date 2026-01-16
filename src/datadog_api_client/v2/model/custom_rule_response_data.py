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
    from datadog_api_client.v2.model.custom_rule import CustomRule
    from datadog_api_client.v2.model.custom_rule_data_type import CustomRuleDataType


class CustomRuleResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_rule import CustomRule
        from datadog_api_client.v2.model.custom_rule_data_type import CustomRuleDataType

        return {
            "attributes": (CustomRule,),
            "id": (str,),
            "type": (CustomRuleDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: CustomRule, id: str, type: CustomRuleDataType, **kwargs):
        """


        :param attributes:
        :type attributes: CustomRule

        :param id: Rule identifier
        :type id: str

        :param type: Resource type
        :type type: CustomRuleDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
