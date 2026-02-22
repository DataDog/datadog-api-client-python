# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.timestamp_type import TimestampType


class IncidentTimestampOverrideCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timestamp_type import TimestampType

        return {
            "timestamp_type": (TimestampType,),
            "timestamp_value": (datetime,),
        }

    attribute_map = {
        "timestamp_type": "timestamp_type",
        "timestamp_value": "timestamp_value",
    }

    def __init__(self_, timestamp_type: TimestampType, timestamp_value: datetime, **kwargs):
        """
        Attributes for creating an incident timestamp override.

        :param timestamp_type: The type of timestamp being overridden.
        :type timestamp_type: TimestampType

        :param timestamp_value: The timestamp value for the override.
        :type timestamp_value: datetime
        """
        super().__init__(kwargs)

        self_.timestamp_type = timestamp_type
        self_.timestamp_value = timestamp_value
