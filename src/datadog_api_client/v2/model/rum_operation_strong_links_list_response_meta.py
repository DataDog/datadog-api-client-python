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


class RUMOperationStrongLinksListResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "limit": (int,),
            "offset": (int,),
            "total": (int,),
        }

    attribute_map = {
        "limit": "limit",
        "offset": "offset",
        "total": "total",
    }

    def __init__(
        self_,
        limit: Union[int, UnsetType] = unset,
        offset: Union[int, UnsetType] = unset,
        total: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata for a list of RUM operation strong links.

        :param limit: The pagination limit.
        :type limit: int, optional

        :param offset: The current offset.
        :type offset: int, optional

        :param total: The total number of strong links matching the request.
        :type total: int, optional
        """
        if limit is not unset:
            kwargs["limit"] = limit
        if offset is not unset:
            kwargs["offset"] = offset
        if total is not unset:
            kwargs["total"] = total
        super().__init__(kwargs)
