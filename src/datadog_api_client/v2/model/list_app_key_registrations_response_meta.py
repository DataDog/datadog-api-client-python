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


class ListAppKeyRegistrationsResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "total": (int,),
            "total_filtered": (int,),
        }

    attribute_map = {
        "total": "total",
        "total_filtered": "total_filtered",
    }

    def __init__(self_, total: Union[int, UnsetType] = unset, total_filtered: Union[int, UnsetType] = unset, **kwargs):
        """
        The definition of ``ListAppKeyRegistrationsResponseMeta`` object.

        :param total: The total number of app key registrations.
        :type total: int, optional

        :param total_filtered: The total number of app key registrations that match the specified filters.
        :type total_filtered: int, optional
        """
        if total is not unset:
            kwargs["total"] = total
        if total_filtered is not unset:
            kwargs["total_filtered"] = total_filtered
        super().__init__(kwargs)
