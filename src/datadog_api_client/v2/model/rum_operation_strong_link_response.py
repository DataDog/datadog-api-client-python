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
    from datadog_api_client.v2.model.rum_operation_strong_link_response_data import RUMOperationStrongLinkResponseData


class RUMOperationStrongLinkResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_operation_strong_link_response_data import (
            RUMOperationStrongLinkResponseData,
        )

        return {
            "data": (RUMOperationStrongLinkResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: RUMOperationStrongLinkResponseData, **kwargs):
        """
        The response for a single RUM operation strong link.

        :param data: The data object in a RUM operation strong link response.
        :type data: RUMOperationStrongLinkResponseData
        """
        super().__init__(kwargs)

        self_.data = data
