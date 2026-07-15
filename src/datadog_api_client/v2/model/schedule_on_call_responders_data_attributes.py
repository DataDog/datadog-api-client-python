# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class ScheduleOnCallRespondersDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "scheduled_at": (datetime,),
        }

    attribute_map = {
        "scheduled_at": "scheduled_at",
    }

    def __init__(self_, scheduled_at: Union[datetime, UnsetType] = unset, **kwargs):
        """
        Attributes for a schedule's on-call responders lookup.

        :param scheduled_at: The timestamp the responders were resolved at.
        :type scheduled_at: datetime, optional
        """
        if scheduled_at is not unset:
            kwargs["scheduled_at"] = scheduled_at
        super().__init__(kwargs)
