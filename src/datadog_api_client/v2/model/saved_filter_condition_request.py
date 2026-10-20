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
    from datadog_api_client.v2.model.saved_filter_condition_operator import SavedFilterConditionOperator


class SavedFilterConditionRequest(ModelNormal):
    validations = {
        "attribute": {
            "min_length": 1,
        },
        "value": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.saved_filter_condition_operator import SavedFilterConditionOperator

        return {
            "attribute": (str,),
            "operator": (SavedFilterConditionOperator,),
            "value": ([str],),
        }

    attribute_map = {
        "attribute": "attribute",
        "operator": "operator",
        "value": "value",
    }

    def __init__(self_, attribute: str, operator: SavedFilterConditionOperator, value: List[str], **kwargs):
        """
        An inline condition to write in a saved filter. Nested saved-filter references are not supported.

        :param attribute: The attribute evaluated by the condition.
        :type attribute: str

        :param operator: The comparison operator used by a saved filter condition.
        :type operator: SavedFilterConditionOperator

        :param value: Values used by the condition operator. Values must satisfy the selected operator and the organization targeting limits.
        :type value: [str]
        """
        super().__init__(kwargs)

        self_.attribute = attribute
        self_.operator = operator
        self_.value = value
