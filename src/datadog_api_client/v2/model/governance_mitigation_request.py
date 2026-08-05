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
    from datadog_api_client.v2.model.governance_mitigation_request_data import GovernanceMitigationRequestData


class GovernanceMitigationRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_mitigation_request_data import GovernanceMitigationRequestData

        return {
            "data": (GovernanceMitigationRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: GovernanceMitigationRequestData, **kwargs):
        """
        A request to mitigate a set of governance detections.

        :param data: The data of a governance mitigation request.
        :type data: GovernanceMitigationRequestData
        """
        super().__init__(kwargs)

        self_.data = data
