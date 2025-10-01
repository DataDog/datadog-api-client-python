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
    from datadog_api_client.v2.model.incident_create_page_attributes import IncidentCreatePageAttributes
    from datadog_api_client.v2.model.incident_page_type import IncidentPageType


class IncidentCreatePageFromIncidentData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_create_page_attributes import IncidentCreatePageAttributes
        from datadog_api_client.v2.model.incident_page_type import IncidentPageType

        return {
            "attributes": (IncidentCreatePageAttributes,),
            "type": (IncidentPageType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: IncidentCreatePageAttributes, type: IncidentPageType, **kwargs):
        """
        Data for creating a page from an incident.

        :param attributes: Attributes for creating a page from an incident.
        :type attributes: IncidentCreatePageAttributes

        :param type: Incident page type.
        :type type: IncidentPageType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
