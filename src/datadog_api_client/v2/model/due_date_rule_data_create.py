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
    from datadog_api_client.v2.model.due_date_rule_attributes_create import DueDateRuleAttributesCreate
    from datadog_api_client.v2.model.due_date_rule_type import DueDateRuleType


class DueDateRuleDataCreate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.due_date_rule_attributes_create import DueDateRuleAttributesCreate
        from datadog_api_client.v2.model.due_date_rule_type import DueDateRuleType

        return {
            "attributes": (DueDateRuleAttributesCreate,),
            "type": (DueDateRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: DueDateRuleAttributesCreate, type: DueDateRuleType, **kwargs):
        """
        The data object for a due date rule create or update request.

        :param attributes: Attributes for creating or updating a due date rule.
        :type attributes: DueDateRuleAttributesCreate

        :param type: The JSON:API type for due date rules.
        :type type: DueDateRuleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
