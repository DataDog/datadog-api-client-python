# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class SyntheticsTestVersionHistoryMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "next_last_version_number": (int, none_type),
            "retention_period_in_days": (int,),
        }

    attribute_map = {
        "next_last_version_number": "next_last_version_number",
        "retention_period_in_days": "retention_period_in_days",
    }

    def __init__(
        self_,
        next_last_version_number: Union[int, none_type, UnsetType] = unset,
        retention_period_in_days: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Pagination metadata for a version history response.

        :param next_last_version_number: The version number to use as the ``last_version_number`` query parameter
            to fetch the next page. ``null`` indicates there are no more pages.
        :type next_last_version_number: int, none_type, optional

        :param retention_period_in_days: The number of days that version history is retained.
        :type retention_period_in_days: int, optional
        """
        if next_last_version_number is not unset:
            kwargs["next_last_version_number"] = next_last_version_number
        if retention_period_in_days is not unset:
            kwargs["retention_period_in_days"] = retention_period_in_days
        super().__init__(kwargs)
