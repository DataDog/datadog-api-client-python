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
    from datadog_api_client.v2.model.severity_modifier_rule_data_update import SeverityModifierRuleDataUpdate


class SeverityModifierRuleUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.severity_modifier_rule_data_update import SeverityModifierRuleDataUpdate

        return {
            "data": (SeverityModifierRuleDataUpdate,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SeverityModifierRuleDataUpdate, **kwargs):
        """
        The body of a severity modifier rule update request.

        :param data: The data object for a severity modifier rule update request. The ``id`` must match the ``rule_id`` path parameter.
        :type data: SeverityModifierRuleDataUpdate
        """
        super().__init__(kwargs)

        self_.data = data
