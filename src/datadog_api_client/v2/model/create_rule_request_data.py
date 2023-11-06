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
    from datadog_api_client.v2.model.rule_attributes import RuleAttributes
    from datadog_api_client.v2.model.rule_type import RuleType


class CreateRuleRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rule_attributes import RuleAttributes
        from datadog_api_client.v2.model.rule_type import RuleType

        return {
            "attributes": (RuleAttributes,),
            "type": (RuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: Union[RuleAttributes, UnsetType] = unset, type: Union[RuleType, UnsetType] = unset, **kwargs
    ):
        """
        Scorecard create rule request data.

        :param attributes: Details of a rule.
        :type attributes: RuleAttributes, optional

        :param type: The JSON:API type for scorecard rules.
        :type type: RuleType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
