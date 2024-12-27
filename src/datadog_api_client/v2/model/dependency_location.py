# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DependencyLocation(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "column_end": (int,),
            "column_start": (int,),
            "file_name": (str,),
            "line_end": (int,),
            "line_start": (int,),
        }

    attribute_map = {
        "column_end": "column_end",
        "column_start": "column_start",
        "file_name": "file_name",
        "line_end": "line_end",
        "line_start": "line_start",
    }

    def __init__(self_, column_end: int, column_start: int, file_name: str, line_end: int, line_start: int, **kwargs):
        """
        Static library vulnerability location.

        :param column_end: Location column end.
        :type column_end: int

        :param column_start: Location column start.
        :type column_start: int

        :param file_name: Location file name.
        :type file_name: str

        :param line_end: Location line end.
        :type line_end: int

        :param line_start: Location line start.
        :type line_start: int
        """
        super().__init__(kwargs)

        self_.column_end = column_end
        self_.column_start = column_start
        self_.file_name = file_name
        self_.line_end = line_end
        self_.line_start = line_start
