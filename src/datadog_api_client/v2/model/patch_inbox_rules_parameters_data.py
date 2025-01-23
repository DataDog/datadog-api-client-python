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
    from datadog_api_client.v2.model.patch_inbox_rules_parameters_data_attributes import (
        PatchInboxRulesParametersDataAttributes,
    )
    from datadog_api_client.v2.model.inbox_rules_type import InboxRulesType


class PatchInboxRulesParametersData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_inbox_rules_parameters_data_attributes import (
            PatchInboxRulesParametersDataAttributes,
        )
        from datadog_api_client.v2.model.inbox_rules_type import InboxRulesType

        return {
            "attributes": (PatchInboxRulesParametersDataAttributes,),
            "id": (UUID,),
            "type": (InboxRulesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: PatchInboxRulesParametersDataAttributes, id: UUID, type: InboxRulesType, **kwargs):
        """
        Data of the inbox rule patch request: the rule UUID, the rule type, and the rule attributes. All fields are required.

        :param attributes: Attributes of the inbox rule patch request: the rule name, the rule details, the associated action, and the enabled field.
        :type attributes: PatchInboxRulesParametersDataAttributes

        :param id: The ID of a pipeline rule
        :type id: UUID

        :param type: The pipeline rule type associated to inbox rules
        :type type: InboxRulesType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
