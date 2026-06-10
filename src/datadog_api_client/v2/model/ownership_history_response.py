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
    from datadog_api_client.v2.model.ownership_history_data import OwnershipHistoryData


class OwnershipHistoryResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ownership_history_data import OwnershipHistoryData

        return {
            "data": (OwnershipHistoryData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: OwnershipHistoryData, **kwargs):
        """
        The response returned when listing the inference history for a resource.

        :param data: The data wrapper for an ownership history response.
        :type data: OwnershipHistoryData
        """
        super().__init__(kwargs)

        self_.data = data
