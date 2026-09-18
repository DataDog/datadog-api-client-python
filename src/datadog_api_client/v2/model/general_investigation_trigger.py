# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.general_investigation_attributes import GeneralInvestigationAttributes
    from datadog_api_client.v2.model.general_investigation_trigger_type import GeneralInvestigationTriggerType
    from datadog_api_client.v2.model.general_investigation_attributes_without_time_bounds import (
        GeneralInvestigationAttributesWithoutTimeBounds,
    )
    from datadog_api_client.v2.model.general_investigation_attributes_with_time_bounds import (
        GeneralInvestigationAttributesWithTimeBounds,
    )


class GeneralInvestigationTrigger(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.general_investigation_attributes import GeneralInvestigationAttributes
        from datadog_api_client.v2.model.general_investigation_trigger_type import GeneralInvestigationTriggerType

        return {
            "general_investigation": (GeneralInvestigationAttributes,),
            "type": (GeneralInvestigationTriggerType,),
        }

    attribute_map = {
        "general_investigation": "general_investigation",
        "type": "type",
    }

    def __init__(
        self_,
        general_investigation: Union[
            GeneralInvestigationAttributes,
            GeneralInvestigationAttributesWithoutTimeBounds,
            GeneralInvestigationAttributesWithTimeBounds,
        ],
        type: GeneralInvestigationTriggerType,
        **kwargs,
    ):
        """
        A trigger created from a general investigation request.

        :param general_investigation: Attributes for a general investigation, not tied to a specific monitor alert.
        :type general_investigation: GeneralInvestigationAttributes

        :param type: The type of general investigation trigger.
        :type type: GeneralInvestigationTriggerType
        """
        super().__init__(kwargs)

        self_.general_investigation = general_investigation
        self_.type = type
