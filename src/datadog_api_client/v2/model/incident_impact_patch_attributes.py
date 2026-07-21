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
    from datadog_api_client.v2.model.incident_impact_fields_object import IncidentImpactFieldsObject


class IncidentImpactPatchAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_impact_fields_object import IncidentImpactFieldsObject

        return {
            "description": (str,),
            "end_at": (datetime, none_type),
            "fields": (IncidentImpactFieldsObject,),
            "start_at": (datetime,),
        }

    attribute_map = {
        "description": "description",
        "end_at": "end_at",
        "fields": "fields",
        "start_at": "start_at",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        end_at: Union[datetime, none_type, UnsetType] = unset,
        fields: Union[IncidentImpactFieldsObject, UnsetType] = unset,
        start_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        The incident impact's attributes for a patch request. All fields are optional.

        :param description: Description of the impact.
        :type description: str, optional

        :param end_at: Timestamp when the impact ended.
        :type end_at: datetime, none_type, optional

        :param fields: An object mapping impact field names to field values.
        :type fields: IncidentImpactFieldsObject, optional

        :param start_at: Timestamp when the impact started.
        :type start_at: datetime, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if end_at is not unset:
            kwargs["end_at"] = end_at
        if fields is not unset:
            kwargs["fields"] = fields
        if start_at is not unset:
            kwargs["start_at"] = start_at
        super().__init__(kwargs)
