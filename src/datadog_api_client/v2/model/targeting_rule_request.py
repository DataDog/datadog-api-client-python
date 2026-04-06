# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.condition_request import ConditionRequest


class TargetingRuleRequest(ModelNormal):
    validations = {
        "conditions": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.condition_request import ConditionRequest

        return {
            "conditions": ([ConditionRequest],),
        }

    attribute_map = {
        "conditions": "conditions",
    }

    def __init__(self_, conditions: List[ConditionRequest], **kwargs):
        """
        Targeting rule request payload.

        :param conditions: Conditions that must match for this rule.
        :type conditions: [ConditionRequest]
        """
        super().__init__(kwargs)

        self_.conditions = conditions
