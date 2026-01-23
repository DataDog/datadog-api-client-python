# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_handle_attributes_fields import IncidentHandleAttributesFields


class IncidentHandleAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_handle_attributes_fields import IncidentHandleAttributesFields

        return {
            "fields": (IncidentHandleAttributesFields,),
            "name": (str,),
        }

    attribute_map = {
        "fields": "fields",
        "name": "name",
    }

    def __init__(self_, name: str, fields: Union[IncidentHandleAttributesFields, UnsetType] = unset, **kwargs):
        """
        Incident handle attributes for requests

        :param fields: Dynamic fields associated with the handle
        :type fields: IncidentHandleAttributesFields, optional

        :param name: The handle name
        :type name: str
        """
        if fields is not unset:
            kwargs["fields"] = fields
        super().__init__(kwargs)

        self_.name = name
