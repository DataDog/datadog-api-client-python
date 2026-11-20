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
    from datadog_api_client.v2.model.rum_exclusion_filter_create_data import RUMExclusionFilterCreateData


class RUMExclusionFilterCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_exclusion_filter_create_data import RUMExclusionFilterCreateData

        return {
            "data": (RUMExclusionFilterCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: RUMExclusionFilterCreateData, **kwargs):
        """
        The exclusion filter body to create.

        :param data: The new exclusion filter properties to create.
        :type data: RUMExclusionFilterCreateData
        """
        super().__init__(kwargs)

        self_.data = data
