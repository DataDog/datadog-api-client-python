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


class MonthlyResourcesPagination(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "next_record_id": (str, none_type),
        }

    attribute_map = {
        "next_record_id": "next_record_id",
    }

    def __init__(self_, next_record_id: Union[str, none_type, UnsetType] = unset, **kwargs):
        """
        Pagination information for monthly resource usage.

        :param next_record_id: Cursor for the next request. Pass as ``page[next_record_id]`` with the same filters. Null when there are no more results.
        :type next_record_id: str, none_type, optional
        """
        if next_record_id is not unset:
            kwargs["next_record_id"] = next_record_id
        super().__init__(kwargs)
