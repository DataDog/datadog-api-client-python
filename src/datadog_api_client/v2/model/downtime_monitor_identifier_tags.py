# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


class DowntimeMonitorIdentifierTags(ModelNormal):
    validations = {
        "monitor_tags": {
            "min_items": 1,
        },
    }

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
            "monitor_tags": ([str],),
        }

    attribute_map = {
        "monitor_tags": "monitor_tags",
    }

    def __init__(self_, monitor_tags: List[str], **kwargs):
        """
        Object of the monitor tags.

        :param monitor_tags: A list of monitor tags. For example, tags that are applied directly to monitors,
            not tags that are used in monitor queries (which are filtered by the scope parameter), to which the downtime applies.
            The resulting downtime applies to monitors that match **all** provided monitor tags. Setting ``monitor_tags``
            to ``[*]`` configures the downtime to mute all monitors for the given scope.
        :type monitor_tags: [str]
        """
        super().__init__(kwargs)

        self_.monitor_tags = monitor_tags
