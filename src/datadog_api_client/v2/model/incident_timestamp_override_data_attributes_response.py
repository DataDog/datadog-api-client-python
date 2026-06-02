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
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_timestamp_type import IncidentTimestampType


class IncidentTimestampOverrideDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_timestamp_type import IncidentTimestampType

        return {
            "created_at": (datetime,),
            "deleted_at": (datetime, none_type),
            "incident_id": (str,),
            "modified_at": (datetime,),
            "timestamp_type": (IncidentTimestampType,),
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
        incident_id: str,
        modified_at: datetime,
        timestamp_type: IncidentTimestampType,
        timestamp_value: datetime,
        deleted_at: Union[datetime, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a timestamp override in a response.

        :param created_at: Timestamp when the override was created.
        :type created_at: datetime

        :param deleted_at: Timestamp when the override was deleted.
        :type deleted_at: datetime, none_type, optional

        :param incident_id: The incident identifier.
        :type incident_id: str

        :param modified_at: Timestamp when the override was last modified.
        :type modified_at: datetime

        :param timestamp_type: The type of timestamp to override.
        :type timestamp_type: IncidentTimestampType

        :param timestamp_value: The overridden timestamp value.
        :type timestamp_value: datetime
        """
        if deleted_at is not unset:
            kwargs["deleted_at"] = deleted_at
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.incident_id = incident_id
        self_.modified_at = modified_at
        self_.timestamp_type = timestamp_type
        self_.timestamp_value = timestamp_value
