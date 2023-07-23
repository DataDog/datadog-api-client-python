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
    from datadog_api_client.v2.model.incident_response_data import IncidentResponseData
    from datadog_api_client.v2.model.incident_response_included_item import IncidentResponseIncludedItem
    from datadog_api_client.v2.model.incident_response_meta import IncidentResponseMeta
    from datadog_api_client.v2.model.user import User
    from datadog_api_client.v2.model.incident_attachment_data import IncidentAttachmentData
    from datadog_api_client.v2.model.incident_notification_handle import IncidentNotificationHandle
    from datadog_api_client.v2.model.incident_field_attributes import IncidentFieldAttributes
    from datadog_api_client.v2.model.incident_field_attributes_single_value import IncidentFieldAttributesSingleValue
    from datadog_api_client.v2.model.incident_field_attributes_multiple_value import (
        IncidentFieldAttributesMultipleValue,
    )


@dataclass
class IncidentsResponseJSON:
    id: str
    created: Union[datetime, UnsetType] = unset
    customer_impact_duration: Union[int, UnsetType] = unset
    customer_impact_end: Union[datetime, none_type, UnsetType] = unset
    customer_impact_scope: Union[str, none_type, UnsetType] = unset
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
    modified: Union[datetime, UnsetType] = unset
    notification_handles: Union[List[IncidentNotificationHandle], none_type, UnsetType] = unset
    public_id: Union[int, UnsetType] = unset
    resolved: Union[datetime, none_type, UnsetType] = unset
    time_to_detect: Union[int, UnsetType] = unset
    time_to_internal_response: Union[int, UnsetType] = unset
    time_to_repair: Union[int, UnsetType] = unset
    time_to_resolve: Union[int, UnsetType] = unset
    title: Union[str, UnsetType] = unset
    attachments: Union[List[str], UnsetType] = unset
    commander_user: Union[str, none_type, UnsetType] = unset
    created_by_user: Union[str, UnsetType] = unset
    integrations: Union[List[str], UnsetType] = unset
    last_modified_by_user: Union[str, UnsetType] = unset


class IncidentsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_response_data import IncidentResponseData
        from datadog_api_client.v2.model.incident_response_included_item import IncidentResponseIncludedItem
        from datadog_api_client.v2.model.incident_response_meta import IncidentResponseMeta

        return {
            "data": ([IncidentResponseData],),
            "included": ([IncidentResponseIncludedItem],),
            "meta": (IncidentResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "meta": "meta",
    }
    read_only_vars = {
        "included",
        "meta",
    }
    json_api_model = IncidentsResponseJSON

    def __init__(
        self_,
        data: List[IncidentResponseData],
        included: Union[List[Union[IncidentResponseIncludedItem, User, IncidentAttachmentData]], UnsetType] = unset,
        meta: Union[IncidentResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response with a list of incidents.

        :param data: An array of incidents.
        :type data: [IncidentResponseData]

        :param included: Included related resources that the user requested.
        :type included: [IncidentResponseIncludedItem], optional

        :param meta: The metadata object containing pagination metadata.
        :type meta: IncidentResponseMeta, optional
        """
        if included is not unset:
            kwargs["included"] = included
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
