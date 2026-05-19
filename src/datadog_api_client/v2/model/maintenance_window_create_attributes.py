# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class MaintenanceWindowCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "end_at": (datetime,),
            "name": (str,),
            "query": (str,),
            "start_at": (datetime,),
        }

    attribute_map = {
        "end_at": "end_at",
        "name": "name",
        "query": "query",
        "start_at": "start_at",
    }

    def __init__(self_, end_at: datetime, name: str, query: str, start_at: datetime, **kwargs):
        """
        Attributes required to create a maintenance window.

        :param end_at: The end time of the maintenance window.
        :type end_at: datetime

        :param name: The name of the maintenance window.
        :type name: str

        :param query: The query to filter event management cases for this maintenance window.
        :type query: str

        :param start_at: The start time of the maintenance window.
        :type start_at: datetime
        """
        super().__init__(kwargs)

        self_.end_at = end_at
        self_.name = name
        self_.query = query
        self_.start_at = start_at
