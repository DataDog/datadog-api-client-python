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
    from datadog_api_client.v2.model.inbox_rule_attributes_create import InboxRuleAttributesCreate
    from datadog_api_client.v2.model.inbox_rule_type import InboxRuleType


class InboxRuleDataUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.inbox_rule_attributes_create import InboxRuleAttributesCreate
        from datadog_api_client.v2.model.inbox_rule_type import InboxRuleType

        return {
            "attributes": (InboxRuleAttributesCreate,),
            "id": (UUID,),
            "type": (InboxRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: InboxRuleAttributesCreate, id: UUID, type: InboxRuleType, **kwargs):
        """
        The data object for an inbox rule update request. The ``id`` must match the ``rule_id`` path parameter.

        :param attributes: Attributes for creating or updating an inbox rule.
        :type attributes: InboxRuleAttributesCreate

        :param id: The ID of the inbox rule to update.
        :type id: UUID

        :param type: The JSON:API type for inbox rules.
        :type type: InboxRuleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
