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
    from datadog_api_client.v2.model.incident_timestamp_override_data_attributes_request import (
        IncidentTimestampOverrideDataAttributesRequest,
    )
    from datadog_api_client.v2.model.incident_timestamp_override_type import IncidentTimestampOverrideType


class IncidentTimestampOverrideDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_timestamp_override_data_attributes_request import (
            IncidentTimestampOverrideDataAttributesRequest,
        )
        from datadog_api_client.v2.model.incident_timestamp_override_type import IncidentTimestampOverrideType

        return {
            "attributes": (IncidentTimestampOverrideDataAttributesRequest,),
            "type": (IncidentTimestampOverrideType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: IncidentTimestampOverrideDataAttributesRequest, type: IncidentTimestampOverrideType, **kwargs
    ):
        """
        Timestamp override data in a create request.

        :param attributes: Attributes for creating a timestamp override.
        :type attributes: IncidentTimestampOverrideDataAttributesRequest

        :param type: Incident timestamp override resource type.
        :type type: IncidentTimestampOverrideType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
