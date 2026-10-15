# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.saved_filter_condition import SavedFilterCondition


class SavedFilterTargetingRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.saved_filter_condition import SavedFilterCondition

        return {
            "conditions": ([SavedFilterCondition],),
            "id": (UUID,),
        }

    attribute_map = {
        "conditions": "conditions",
        "id": "id",
    }

    def __init__(self_, conditions: List[SavedFilterCondition], id: UUID, **kwargs):
        """
        A targeting rule in a saved filter. A rule matches when all its conditions match.

        :param conditions: Conditions combined with AND within this targeting rule.
        :type conditions: [SavedFilterCondition]

        :param id: The ID of the targeting rule.
        :type id: UUID
        """
        super().__init__(kwargs)

        self_.conditions = conditions
        self_.id = id
