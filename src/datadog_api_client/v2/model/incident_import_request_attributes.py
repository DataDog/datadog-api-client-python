# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_import_field_attributes import IncidentImportFieldAttributes
    from datadog_api_client.v2.model.incident_import_visibility import IncidentImportVisibility
    from datadog_api_client.v2.model.incident_import_field_attributes_single_value import (
        IncidentImportFieldAttributesSingleValue,
    )
    from datadog_api_client.v2.model.incident_import_field_attributes_multiple_value import (
        IncidentImportFieldAttributesMultipleValue,
    )


class IncidentImportRequestAttributes(ModelNormal):
    validations = {
        "title": {
            "max_length": 1024,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_import_field_attributes import IncidentImportFieldAttributes
        from datadog_api_client.v2.model.incident_import_visibility import IncidentImportVisibility

        return {
            "declared": (datetime,),
            "detected": (datetime,),
            "fields": ({str: (IncidentImportFieldAttributes,)},),
            "incident_type_uuid": (str,),
            "resolved": (datetime,),
            "title": (str,),
            "visibility": (IncidentImportVisibility,),
        }

    attribute_map = {
        "declared": "declared",
        "detected": "detected",
        "fields": "fields",
        "incident_type_uuid": "incident_type_uuid",
        "resolved": "resolved",
        "title": "title",
        "visibility": "visibility",
    }

    def __init__(
        self_,
        title: str,
        declared: Union[datetime, UnsetType] = unset,
        detected: Union[datetime, UnsetType] = unset,
        fields: Union[
            Dict[
                str,
                Union[
                    IncidentImportFieldAttributes,
                    IncidentImportFieldAttributesSingleValue,
                    IncidentImportFieldAttributesMultipleValue,
                ],
            ],
            UnsetType,
        ] = unset,
        incident_type_uuid: Union[str, UnsetType] = unset,
        resolved: Union[datetime, UnsetType] = unset,
        visibility: Union[IncidentImportVisibility, UnsetType] = unset,
        **kwargs,
    ):
        """
        The incident's attributes for an import request.

        :param declared: Timestamp when the incident was declared.
        :type declared: datetime, optional

        :param detected: Timestamp when the incident was detected.
        :type detected: datetime, optional

        :param fields: A condensed view of the user-defined fields for which to create initial selections.
        :type fields: {str: (IncidentImportFieldAttributes,)}, optional

        :param incident_type_uuid: A unique identifier that represents the incident type. If not provided, the default incident type is used.
        :type incident_type_uuid: str, optional

        :param resolved: Timestamp when the incident was resolved. Can only be set when the state field is set to 'resolved'.
        :type resolved: datetime, optional

        :param title: The title of the incident that summarizes what happened.
        :type title: str

        :param visibility: The visibility of the incident.
        :type visibility: IncidentImportVisibility, optional
        """
        if declared is not unset:
            kwargs["declared"] = declared
        if detected is not unset:
            kwargs["detected"] = detected
        if fields is not unset:
            kwargs["fields"] = fields
        if incident_type_uuid is not unset:
            kwargs["incident_type_uuid"] = incident_type_uuid
        if resolved is not unset:
            kwargs["resolved"] = resolved
        if visibility is not unset:
            kwargs["visibility"] = visibility
        super().__init__(kwargs)

        self_.title = title
