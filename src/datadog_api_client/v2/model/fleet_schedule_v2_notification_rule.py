# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class FleetScheduleV2NotificationRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "handles": ([str],),
            "tags": ([str],),
        }

    attribute_map = {
        "handles": "handles",
        "tags": "tags",
    }

    def __init__(
        self_, handles: Union[List[str], UnsetType] = unset, tags: Union[List[str], UnsetType] = unset, **kwargs
    ):
        """
        Notification configuration attached to a schedule.

        Included when available. If the notification rule cannot be retrieved, this field is
        omitted and the schedule is still returned. If the notification rule is retrieved but its
        handles cannot be resolved, it is still included with an empty ``handles`` array.

        :param handles: Notification handles (for example, Slack channels or PagerDuty integrations).
        :type handles: [str], optional

        :param tags: Tags associated with the notification rule.
        :type tags: [str], optional
        """
        if handles is not unset:
            kwargs["handles"] = handles
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
