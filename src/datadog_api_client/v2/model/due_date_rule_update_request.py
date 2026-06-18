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
    from datadog_api_client.v2.model.due_date_rule_data_create import DueDateRuleDataCreate


class DueDateRuleUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.due_date_rule_data_create import DueDateRuleDataCreate

        return {
            "data": (DueDateRuleDataCreate,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: DueDateRuleDataCreate, **kwargs):
        """
        The body of a due date rule update request.

        :param data: The data object for a due date rule create or update request.
        :type data: DueDateRuleDataCreate
        """
        super().__init__(kwargs)

        self_.data = data
