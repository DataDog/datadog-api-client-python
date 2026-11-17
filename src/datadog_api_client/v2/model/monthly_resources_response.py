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
    from datadog_api_client.v2.model.monthly_resource import MonthlyResource
    from datadog_api_client.v2.model.monthly_resources_metadata import MonthlyResourcesMetadata


class MonthlyResourcesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monthly_resource import MonthlyResource
        from datadog_api_client.v2.model.monthly_resources_metadata import MonthlyResourcesMetadata

        return {
            "data": ([MonthlyResource],),
            "meta": (MonthlyResourcesMetadata,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[MonthlyResource], UnsetType] = unset,
        meta: Union[MonthlyResourcesMetadata, UnsetType] = unset,
        **kwargs,
    ):
        """
        Monthly usage for host and non-host resources.

        :param data: Resource usage records. Empty when no matching resources are available.
        :type data: [MonthlyResource], optional

        :param meta: Metadata for monthly resource usage.
        :type meta: MonthlyResourcesMetadata, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
