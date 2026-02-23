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
    from datadog_api_client.v2.model.incident_timestamp_override_create_attributes import (
        IncidentTimestampOverrideCreateAttributes,
    )
    from datadog_api_client.v2.model.incidents_timestamp_overrides_type import IncidentsTimestampOverridesType


class IncidentTimestampOverrideCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_timestamp_override_create_attributes import (
            IncidentTimestampOverrideCreateAttributes,
        )
        from datadog_api_client.v2.model.incidents_timestamp_overrides_type import IncidentsTimestampOverridesType

        return {
            "attributes": (IncidentTimestampOverrideCreateAttributes,),
            "type": (IncidentsTimestampOverridesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: IncidentTimestampOverrideCreateAttributes, type: IncidentsTimestampOverridesType, **kwargs
    ):
        """
        Data for creating an incident timestamp override.

        :param attributes: Attributes for creating an incident timestamp override.
        :type attributes: IncidentTimestampOverrideCreateAttributes

        :param type: The JSON:API type for timestamp overrides.
        :type type: IncidentsTimestampOverridesType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
