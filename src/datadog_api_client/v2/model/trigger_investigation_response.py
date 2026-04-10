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
    from datadog_api_client.v2.model.trigger_investigation_response_data import TriggerInvestigationResponseData


class TriggerInvestigationResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.trigger_investigation_response_data import TriggerInvestigationResponseData

        return {
            "data": (TriggerInvestigationResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: TriggerInvestigationResponseData, **kwargs):
        """
        Response after triggering an investigation.

        :param data: Data for the trigger investigation response.
        :type data: TriggerInvestigationResponseData
        """
        super().__init__(kwargs)

        self_.data = data
