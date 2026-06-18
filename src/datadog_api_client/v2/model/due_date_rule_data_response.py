# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.due_date_rule_attributes_response import DueDateRuleAttributesResponse
    from datadog_api_client.v2.model.due_date_rule_type import DueDateRuleType


class DueDateRuleDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.due_date_rule_attributes_response import DueDateRuleAttributesResponse
        from datadog_api_client.v2.model.due_date_rule_type import DueDateRuleType

        return {
            "attributes": (DueDateRuleAttributesResponse,),
            "id": (UUID,),
            "type": (DueDateRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: DueDateRuleAttributesResponse, id: UUID, type: DueDateRuleType, **kwargs):
        """
        The data object for a due date rule returned by the API.

        :param attributes: Attributes of a due date rule returned by the API.
        :type attributes: DueDateRuleAttributesResponse

        :param id: The ID of the due date rule.
        :type id: UUID

        :param type: The JSON:API type for due date rules.
        :type type: DueDateRuleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
