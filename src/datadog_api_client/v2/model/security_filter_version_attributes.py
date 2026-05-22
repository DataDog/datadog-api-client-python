# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_filter_version_entry import SecurityFilterVersionEntry


class SecurityFilterVersionAttributes(ModelNormal):
    validations = {
        "version": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_filter_version_entry import SecurityFilterVersionEntry

        return {
            "date": (int,),
            "filters": ([SecurityFilterVersionEntry],),
            "version": (int,),
        }

    attribute_map = {
        "date": "date",
        "filters": "filters",
        "version": "version",
    }

    def __init__(self_, date: int, filters: List[SecurityFilterVersionEntry], version: int, **kwargs):
        """
        The attributes describing a single security filter configuration version.

        :param date: The Unix timestamp in milliseconds at which this configuration version was applied.
        :type date: int

        :param filters: The set of security filters at this configuration version.
        :type filters: [SecurityFilterVersionEntry]

        :param version: The configuration version number.
        :type version: int
        """
        super().__init__(kwargs)

        self_.date = date
        self_.filters = filters
        self_.version = version
