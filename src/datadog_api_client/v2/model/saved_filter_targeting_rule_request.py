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
    from datadog_api_client.v2.model.saved_filter_condition_request import SavedFilterConditionRequest


class SavedFilterTargetingRuleRequest(ModelNormal):
    validations = {
        "conditions": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.saved_filter_condition_request import SavedFilterConditionRequest

        return {
            "conditions": ([SavedFilterConditionRequest],),
        }

    attribute_map = {
        "conditions": "conditions",
    }

    def __init__(self_, conditions: List[SavedFilterConditionRequest], **kwargs):
        """
        A replacement saved filter targeting rule.

        :param conditions: Inline conditions combined with AND. Must contain at least one condition.
        :type conditions: [SavedFilterConditionRequest]
        """
        super().__init__(kwargs)

        self_.conditions = conditions
