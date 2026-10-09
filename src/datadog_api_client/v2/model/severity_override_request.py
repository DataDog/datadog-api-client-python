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
    from datadog_api_client.v2.model.severity_override_request_data import SeverityOverrideRequestData


class SeverityOverrideRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.severity_override_request_data import SeverityOverrideRequestData

        return {
            "data": (SeverityOverrideRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SeverityOverrideRequestData, **kwargs):
        """
        Request to set or clear the manual severity override of security findings.

        :param data: Data of the severity override request.
        :type data: SeverityOverrideRequestData
        """
        super().__init__(kwargs)

        self_.data = data
