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
    from datadog_api_client.v2.model.incident_type_attributes import IncidentTypeAttributes
    from datadog_api_client.v2.model.incident_type_type import IncidentTypeType


class IncidentTypeObject(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_type_attributes import IncidentTypeAttributes
        from datadog_api_client.v2.model.incident_type_type import IncidentTypeType

        return {
            "attributes": (IncidentTypeAttributes,),
            "id": (str,),
            "type": (IncidentTypeType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, id: str, type: IncidentTypeType, attributes: Union[IncidentTypeAttributes, UnsetType] = unset, **kwargs
    ):
        """
        Incident type response data.

        :param attributes: Incident type's attributes.
        :type attributes: IncidentTypeAttributes, optional

        :param id: The incident type's ID.
        :type id: str

        :param type: Incident type resource type.
        :type type: IncidentTypeType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
