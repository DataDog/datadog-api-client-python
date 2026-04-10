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
    from datadog_api_client.v2.model.trigger_investigation_request_data_attributes import (
        TriggerInvestigationRequestDataAttributes,
    )
    from datadog_api_client.v2.model.trigger_investigation_request_type import TriggerInvestigationRequestType


class TriggerInvestigationRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.trigger_investigation_request_data_attributes import (
            TriggerInvestigationRequestDataAttributes,
        )
        from datadog_api_client.v2.model.trigger_investigation_request_type import TriggerInvestigationRequestType

        return {
            "attributes": (TriggerInvestigationRequestDataAttributes,),
            "type": (TriggerInvestigationRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: TriggerInvestigationRequestDataAttributes, type: TriggerInvestigationRequestType, **kwargs
    ):
        """
        Data for the trigger investigation request.

        :param attributes: Attributes for the trigger investigation request.
        :type attributes: TriggerInvestigationRequestDataAttributes

        :param type: The resource type for trigger investigation requests.
        :type type: TriggerInvestigationRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
