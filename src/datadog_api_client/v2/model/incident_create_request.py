# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.incident_timeline_cell_create_attributes import IncidentTimelineCellCreateAttributes
from datadog_api_client.v2.model.incident_notification_handle import IncidentNotificationHandle
from datadog_api_client.v2.model.incident_field_attributes import IncidentFieldAttributes
from datadog_api_client.v2.model.incident_field_attributes_single_value import IncidentFieldAttributesSingleValue
from datadog_api_client.v2.model.incident_field_attributes_multiple_value import IncidentFieldAttributesMultipleValue
from datadog_api_client.v2.model.incident_timeline_cell_create_attributes import IncidentTimelineCellCreateAttributes
from datadog_api_client.v2.model.incident_timeline_cell_markdown_create_attributes import (
    IncidentTimelineCellMarkdownCreateAttributes,
)
from datadog_api_client.v2.model.incident_notification_handle import IncidentNotificationHandle

if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_create_data import IncidentCreateData


@dataclass
class IncidentCreateRequestJSON:
    commander_user: Union[str, none_type]
    customer_impact_scope: Union[str, UnsetType] = unset
    customer_impacted: Union[bool, UnsetType] = unset
    fields: Union[
        Dict[
            str,
            Union[IncidentFieldAttributes, IncidentFieldAttributesSingleValue, IncidentFieldAttributesMultipleValue],
        ],
        UnsetType,
    ] = unset
    initial_cells: Union[
        List[Union[IncidentTimelineCellCreateAttributes, IncidentTimelineCellMarkdownCreateAttributes]], UnsetType
    ] = unset
    notification_handles: Union[List[IncidentNotificationHandle], UnsetType] = unset
    title: Union[str, UnsetType] = unset


class IncidentCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_create_data import IncidentCreateData

        return {
            "data": (IncidentCreateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = IncidentCreateRequestJSON

    def __init__(self_, data: IncidentCreateData, **kwargs):
        """
        Create request for an incident.

        :param data: Incident data for a create request.
        :type data: IncidentCreateData
        """
        super().__init__(kwargs)

        self_.data = data
