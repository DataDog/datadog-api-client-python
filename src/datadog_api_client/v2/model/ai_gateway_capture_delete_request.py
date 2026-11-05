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
    from datadog_api_client.v2.model.ai_gateway_capture_delete_request_data import AiGatewayCaptureDeleteRequestData


class AiGatewayCaptureDeleteRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_capture_delete_request_data import AiGatewayCaptureDeleteRequestData

        return {
            "data": (AiGatewayCaptureDeleteRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: AiGatewayCaptureDeleteRequestData, **kwargs):
        """
        Request body for deleting a scoped data capture override.

        :param data: Override identifier, revisions, and confirmation required for deletion.
        :type data: AiGatewayCaptureDeleteRequestData
        """
        super().__init__(kwargs)

        self_.data = data
