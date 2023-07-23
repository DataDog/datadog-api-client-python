# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_update_data import IncidentUpdateData
    from datadog_api_client.v2.model.incident_notification_handle import IncidentNotificationHandle
    from datadog_api_client.v2.model.incident_field_attributes import IncidentFieldAttributes
    from datadog_api_client.v2.model.incident_field_attributes_single_value import IncidentFieldAttributesSingleValue
    from datadog_api_client.v2.model.incident_field_attributes_multiple_value import (
        IncidentFieldAttributesMultipleValue,
    )


@dataclass
class IncidentUpdateRequestJSON:
    id: str
    customer_impact_end: Union[datetime, none_type, UnsetType] = unset
    customer_impact_scope: Union[str, UnsetType] = unset
    customer_impact_start: Union[datetime, none_type, UnsetType] = unset
    customer_impacted: Union[bool, UnsetType] = unset
    detected: Union[datetime, none_type, UnsetType] = unset
    fields: Union[
        Dict[
            str,
            Union[IncidentFieldAttributes, IncidentFieldAttributesSingleValue, IncidentFieldAttributesMultipleValue],
        ],
        UnsetType,
    ] = unset
    notification_handles: Union[List[IncidentNotificationHandle], UnsetType] = unset
    title: Union[str, UnsetType] = unset
    commander_user: Union[str, none_type, UnsetType] = unset
    integrations: Union[List[str], UnsetType] = unset
    postmortem: Union[str, UnsetType] = unset


class IncidentUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_update_data import IncidentUpdateData

        return {
            "data": (IncidentUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = IncidentUpdateRequestJSON

    def __init__(self_, data: IncidentUpdateData, **kwargs):
        """
        Update request for an incident.

        :param data: Incident data for an update request.
        :type data: IncidentUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
