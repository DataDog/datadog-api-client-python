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
    from datadog_api_client.v2.model.trigger_attributes import TriggerAttributes


class TriggerInvestigationRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.trigger_attributes import TriggerAttributes

        return {
            "trigger": (TriggerAttributes,),
        }

    attribute_map = {
        "trigger": "trigger",
    }

    def __init__(self_, trigger: TriggerAttributes, **kwargs):
        """
        Attributes for the trigger investigation request.

        :param trigger: The trigger definition for starting an investigation.
        :type trigger: TriggerAttributes
        """
        super().__init__(kwargs)

        self_.trigger = trigger
