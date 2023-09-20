# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


class DowntimeMonitorIdentifierId(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return (
            bool,
            date,
            datetime,
            dict,
            float,
            int,
            list,
            str,
            UUID,
            none_type,
        )

    @cached_property
    def openapi_types(_):
        return {
            "monitor_id": (int,),
        }

    attribute_map = {
        "monitor_id": "monitor_id",
    }

    def __init__(self_, monitor_id: int, **kwargs):
        """
        Object of the monitor identifier.

        :param monitor_id: ID of the monitor to prevent notifications.
        :type monitor_id: int
        """
        super().__init__(kwargs)

        self_.monitor_id = monitor_id
