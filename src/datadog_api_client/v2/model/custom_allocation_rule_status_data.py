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
    from datadog_api_client.v2.model.custom_allocation_rule_status_attributes import (
        CustomAllocationRuleStatusAttributes,
    )
    from datadog_api_client.v2.model.custom_allocation_rule_status_type import CustomAllocationRuleStatusType


class CustomAllocationRuleStatusData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_allocation_rule_status_attributes import (
            CustomAllocationRuleStatusAttributes,
        )
        from datadog_api_client.v2.model.custom_allocation_rule_status_type import CustomAllocationRuleStatusType

        return {
            "attributes": (CustomAllocationRuleStatusAttributes,),
            "id": (str,),
            "type": (CustomAllocationRuleStatusType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: CustomAllocationRuleStatusAttributes, id: str, type: CustomAllocationRuleStatusType, **kwargs
    ):
        """
        Custom allocation rule status data.

        :param attributes: Attributes for a custom allocation rule status.
        :type attributes: CustomAllocationRuleStatusAttributes

        :param id: The unique identifier of the custom allocation rule.
        :type id: str

        :param type: Custom allocation rule status resource type.
        :type type: CustomAllocationRuleStatusType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
