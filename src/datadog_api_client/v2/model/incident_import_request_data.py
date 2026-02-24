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
    from datadog_api_client.v2.model.incident_import_request_attributes import IncidentImportRequestAttributes
    from datadog_api_client.v2.model.incident_import_relationships import IncidentImportRelationships
    from datadog_api_client.v2.model.incident_type import IncidentType


class IncidentImportRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_import_request_attributes import IncidentImportRequestAttributes
        from datadog_api_client.v2.model.incident_import_relationships import IncidentImportRelationships
        from datadog_api_client.v2.model.incident_type import IncidentType

        return {
            "attributes": (IncidentImportRequestAttributes,),
            "relationships": (IncidentImportRelationships,),
            "type": (IncidentType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentImportRequestAttributes,
        type: IncidentType,
        relationships: Union[IncidentImportRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Incident data for an import request.

        :param attributes: The incident's attributes for an import request.
        :type attributes: IncidentImportRequestAttributes

        :param relationships: The relationships for an incident import request.
        :type relationships: IncidentImportRelationships, optional

        :param type: Incident resource type.
        :type type: IncidentType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
