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
    from datadog_api_client.v2.model.rum_exclusion_filter_data import RUMExclusionFilterData


class RUMExclusionFiltersResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_exclusion_filter_data import RUMExclusionFilterData

        return {
            "data": ([RUMExclusionFilterData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[List[RUMExclusionFilterData], UnsetType] = unset, **kwargs):
        """
        All exclusion filters for a RUM application.

        :param data: A list of exclusion filters.
        :type data: [RUMExclusionFilterData], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
