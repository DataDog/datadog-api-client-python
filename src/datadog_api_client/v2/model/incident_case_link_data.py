# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_case_link_data_attributes import IncidentCaseLinkDataAttributes
    from datadog_api_client.v2.model.incident_case_link_type import IncidentCaseLinkType


class IncidentCaseLinkData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_case_link_data_attributes import IncidentCaseLinkDataAttributes
        from datadog_api_client.v2.model.incident_case_link_type import IncidentCaseLinkType

        return {
            "attributes": (IncidentCaseLinkDataAttributes,),
            "id": (str,),
            "type": (IncidentCaseLinkType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: IncidentCaseLinkDataAttributes, id: str, type: IncidentCaseLinkType, **kwargs):
        """
        Case link data.

        :param attributes: Attributes of a case link.
        :type attributes: IncidentCaseLinkDataAttributes

        :param id: The case link identifier.
        :type id: str

        :param type: Case link resource type.
        :type type: IncidentCaseLinkType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
