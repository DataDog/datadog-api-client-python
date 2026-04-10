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
    from datadog_api_client.v2.model.trigger_investigation_request_data import TriggerInvestigationRequestData


class TriggerInvestigationRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.trigger_investigation_request_data import TriggerInvestigationRequestData

        return {
            "data": (TriggerInvestigationRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: TriggerInvestigationRequestData, **kwargs):
        """
        Request to trigger a new investigation.

        :param data: Data for the trigger investigation request.
        :type data: TriggerInvestigationRequestData
        """
        super().__init__(kwargs)

        self_.data = data
