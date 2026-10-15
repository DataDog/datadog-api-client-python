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
    from datadog_api_client.v2.model.saved_filter_condition_operator import SavedFilterConditionOperator


class SavedFilterCondition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.saved_filter_condition_operator import SavedFilterConditionOperator

        return {
            "attribute": (str,),
            "id": (UUID,),
            "operator": (SavedFilterConditionOperator,),
            "value": ([str],),
        }

    attribute_map = {
        "attribute": "attribute",
        "id": "id",
        "operator": "operator",
        "value": "value",
    }

    def __init__(self_, attribute: str, id: UUID, operator: SavedFilterConditionOperator, value: List[str], **kwargs):
        """
        An inline condition in a saved filter targeting rule.

        :param attribute: The attribute evaluated by the condition.
        :type attribute: str

        :param id: The ID of the condition.
        :type id: UUID

        :param operator: The comparison operator used by a saved filter condition.
        :type operator: SavedFilterConditionOperator

        :param value: Values used by the condition operator.
        :type value: [str]
        """
        super().__init__(kwargs)

        self_.attribute = attribute
        self_.id = id
        self_.operator = operator
        self_.value = value
