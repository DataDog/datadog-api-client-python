# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.timestamp_type import TimestampType


class IncidentTimestampOverrideAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timestamp_type import TimestampType

        return {
            "created_at": (datetime,),
            "deleted_at": (datetime, none_type),
            "incident_id": (UUID,),
            "modified_at": (datetime,),
            "timestamp_type": (TimestampType,),
            "timestamp_value": (datetime,),
        }

    attribute_map = {
        "created_at": "created_at",
        "deleted_at": "deleted_at",
        "incident_id": "incident_id",
        "modified_at": "modified_at",
        "timestamp_type": "timestamp_type",
        "timestamp_value": "timestamp_value",
    }

    def __init__(
        self_,
        created_at: datetime,
        deleted_at: Union[datetime, none_type],
        incident_id: UUID,
        modified_at: datetime,
        timestamp_type: TimestampType,
        timestamp_value: datetime,
        **kwargs,
    ):
        """
        Attributes of an incident timestamp override.

        :param created_at: Timestamp of when the override was created.
        :type created_at: datetime

        :param deleted_at: Timestamp of when the override was deleted (soft delete).
        :type deleted_at: datetime, none_type

        :param incident_id: The UUID of the incident.
        :type incident_id: UUID

        :param modified_at: Timestamp of when the override was last modified.
        :type modified_at: datetime

        :param timestamp_type: The type of timestamp being overridden.
        :type timestamp_type: TimestampType

        :param timestamp_value: The timestamp value for the override.
        :type timestamp_value: datetime
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.deleted_at = deleted_at
        self_.incident_id = incident_id
        self_.modified_at = modified_at
        self_.timestamp_type = timestamp_type
        self_.timestamp_value = timestamp_value
