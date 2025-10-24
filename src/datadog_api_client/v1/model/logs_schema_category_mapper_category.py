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
    from datadog_api_client.v1.model.logs_filter import LogsFilter


class LogsSchemaCategoryMapperCategory(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_filter import LogsFilter

        return {
            "filter": (LogsFilter,),
            "id": (int,),
            "name": (str,),
        }

    attribute_map = {
        "filter": "filter",
        "id": "id",
        "name": "name",
    }

    def __init__(self_, filter: LogsFilter, id: int, name: str, **kwargs):
        """
        Object describing the logs filter with corresponding category ID and name assignment.

        :param filter: Filter for logs.
        :type filter: LogsFilter

        :param id: ID to inject into the category.
        :type id: int

        :param name: Value to assign to target schema field.
        :type name: str
        """
        super().__init__(kwargs)

        self_.filter = filter
        self_.id = id
        self_.name = name
