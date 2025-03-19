# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_retention_filters_order_data import RumRetentionFiltersOrderData


class RumRetentionFiltersOrderResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_retention_filters_order_data import RumRetentionFiltersOrderData

        return {
            "data": ([RumRetentionFiltersOrderData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[List[RumRetentionFiltersOrderData], UnsetType] = unset, **kwargs):
        """
        The list of RUM retention filter IDs along with type.

        :param data: A list of RUM retention filter IDs along with type.
        :type data: [RumRetentionFiltersOrderData], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
