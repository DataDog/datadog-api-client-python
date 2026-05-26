# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringDatasetColumn(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "column": (str,),
            "type": (str,),
        }

    attribute_map = {
        "column": "column",
        "type": "type",
    }

    def __init__(self_, column: str, type: str, **kwargs):
        """
        A column exposed by an event platform dataset.

        :param column: The name of the column.
        :type column: str

        :param type: The type of the column value.
        :type type: str
        """
        super().__init__(kwargs)

        self_.column = column
        self_.type = type
