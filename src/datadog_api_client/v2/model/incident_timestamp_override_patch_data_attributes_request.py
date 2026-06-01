# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_timestamp_type import IncidentTimestampType


class IncidentTimestampOverridePatchDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_timestamp_type import IncidentTimestampType

        return {
            "timestamp_type": (IncidentTimestampType,),
            "timestamp_value": (datetime,),
        }

    attribute_map = {
        "timestamp_type": "timestamp_type",
        "timestamp_value": "timestamp_value",
    }

    def __init__(
        self_,
        timestamp_type: Union[IncidentTimestampType, UnsetType] = unset,
        timestamp_value: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for patching a timestamp override. All fields are optional.

        :param timestamp_type: The type of timestamp to override.
        :type timestamp_type: IncidentTimestampType, optional

        :param timestamp_value: The overridden timestamp value.
        :type timestamp_value: datetime, optional
        """
        if timestamp_type is not unset:
            kwargs["timestamp_type"] = timestamp_type
        if timestamp_value is not unset:
            kwargs["timestamp_value"] = timestamp_value
        super().__init__(kwargs)
