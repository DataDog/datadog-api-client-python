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
    from datadog_api_client.v2.model.incident_handle_attributes_fields import IncidentHandleAttributesFields


class IncidentHandleAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_handle_attributes_fields import IncidentHandleAttributesFields

        return {
            "created_at": (datetime,),
            "fields": (IncidentHandleAttributesFields,),
            "modified_at": (datetime,),
            "name": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "fields": "fields",
        "modified_at": "modified_at",
        "name": "name",
    }

    def __init__(
        self_, created_at: datetime, fields: IncidentHandleAttributesFields, modified_at: datetime, name: str, **kwargs
    ):
        """
        Incident handle attributes for responses

        :param created_at: Timestamp when the handle was created
        :type created_at: datetime

        :param fields: Dynamic fields associated with the handle
        :type fields: IncidentHandleAttributesFields

        :param modified_at: Timestamp when the handle was last modified
        :type modified_at: datetime

        :param name: The handle name
        :type name: str
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.fields = fields
        self_.modified_at = modified_at
        self_.name = name
