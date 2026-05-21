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
    from datadog_api_client.v2.model.incident_statuspage_preferences_data_attributes import (
        IncidentStatuspagePreferencesDataAttributes,
    )
    from datadog_api_client.v2.model.incident_statuspage_preferences_type import IncidentStatuspagePreferencesType


class IncidentStatuspagePreferencesData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_statuspage_preferences_data_attributes import (
            IncidentStatuspagePreferencesDataAttributes,
        )
        from datadog_api_client.v2.model.incident_statuspage_preferences_type import IncidentStatuspagePreferencesType

        return {
            "attributes": (IncidentStatuspagePreferencesDataAttributes,),
            "id": (str,),
            "type": (IncidentStatuspagePreferencesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentStatuspagePreferencesDataAttributes,
        id: str,
        type: IncidentStatuspagePreferencesType,
        **kwargs,
    ):
        """
        Subscription preferences data.

        :param attributes: Attributes of subscription preferences.
        :type attributes: IncidentStatuspagePreferencesDataAttributes

        :param id: The preferences identifier.
        :type id: str

        :param type: Subscription preferences resource type.
        :type type: IncidentStatuspagePreferencesType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
