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
    from datadog_api_client.v2.model.rum_config_update_data import RumConfigUpdateData


class RumConfigUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_config_update_data import RumConfigUpdateData

        return {
            "data": (RumConfigUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: RumConfigUpdateData, **kwargs):
        """
        Request body for updating the RUM configuration.

        :param data: Object describing the RUM configuration to update.
        :type data: RumConfigUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
