# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CSMAgentsMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "page_index": (int,),
            "page_size": (int,),
            "total_filtered": (int,),
        }

    attribute_map = {
        "page_index": "page_index",
        "page_size": "page_size",
        "total_filtered": "total_filtered",
    }

    def __init__(
        self_,
        page_index: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        total_filtered: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata related to the paginated response.

        :param page_index: The index of the current page in the paginated results.
        :type page_index: int, optional

        :param page_size: The number of items per page in the paginated results.
        :type page_size: int, optional

        :param total_filtered: Total number of items that match the filter criteria.
        :type total_filtered: int, optional
        """
        if page_index is not unset:
            kwargs["page_index"] = page_index
        if page_size is not unset:
            kwargs["page_size"] = page_size
        if total_filtered is not unset:
            kwargs["total_filtered"] = total_filtered
        super().__init__(kwargs)
