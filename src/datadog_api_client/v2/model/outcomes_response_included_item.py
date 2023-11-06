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
    from datadog_api_client.v2.model.outcomes_response_included_rule_attributes import (
        OutcomesResponseIncludedRuleAttributes,
    )
    from datadog_api_client.v2.model.rule_type import RuleType


class OutcomesResponseIncludedItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.outcomes_response_included_rule_attributes import (
            OutcomesResponseIncludedRuleAttributes,
        )
        from datadog_api_client.v2.model.rule_type import RuleType

        return {
            "attributes": (OutcomesResponseIncludedRuleAttributes,),
            "id": (str,),
            "type": (RuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[OutcomesResponseIncludedRuleAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[RuleType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the included rule.

        :param attributes: Details of a rule.
        :type attributes: OutcomesResponseIncludedRuleAttributes, optional

        :param id: The unique ID for a scorecard rule.
        :type id: str, optional

        :param type: The JSON:API type for scorecard rules.
        :type type: RuleType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
