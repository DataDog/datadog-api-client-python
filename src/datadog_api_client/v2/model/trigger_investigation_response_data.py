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
    from datadog_api_client.v2.model.trigger_investigation_response_data_attributes import (
        TriggerInvestigationResponseDataAttributes,
    )
    from datadog_api_client.v2.model.trigger_investigation_response_type import TriggerInvestigationResponseType


class TriggerInvestigationResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.trigger_investigation_response_data_attributes import (
            TriggerInvestigationResponseDataAttributes,
        )
        from datadog_api_client.v2.model.trigger_investigation_response_type import TriggerInvestigationResponseType

        return {
            "attributes": (TriggerInvestigationResponseDataAttributes,),
            "id": (str,),
            "type": (TriggerInvestigationResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: TriggerInvestigationResponseDataAttributes,
        id: str,
        type: TriggerInvestigationResponseType,
        **kwargs,
    ):
        """
        Data for the trigger investigation response.

        :param attributes: Attributes for the trigger investigation response.
        :type attributes: TriggerInvestigationResponseDataAttributes

        :param id: Unique identifier for the trigger response.
        :type id: str

        :param type: The resource type for trigger investigation responses.
        :type type: TriggerInvestigationResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
