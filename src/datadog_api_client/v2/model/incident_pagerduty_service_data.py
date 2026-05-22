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
    from datadog_api_client.v2.model.incident_pagerduty_service_data_attributes import (
        IncidentPagerdutyServiceDataAttributes,
    )
    from datadog_api_client.v2.model.incident_pagerduty_service_type import IncidentPagerdutyServiceType


class IncidentPagerdutyServiceData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_pagerduty_service_data_attributes import (
            IncidentPagerdutyServiceDataAttributes,
        )
        from datadog_api_client.v2.model.incident_pagerduty_service_type import IncidentPagerdutyServiceType

        return {
            "attributes": (IncidentPagerdutyServiceDataAttributes,),
            "id": (str,),
            "type": (IncidentPagerdutyServiceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: IncidentPagerdutyServiceDataAttributes, id: str, type: IncidentPagerdutyServiceType, **kwargs
    ):
        """
        PagerDuty service data.

        :param attributes: Attributes of a PagerDuty service.
        :type attributes: IncidentPagerdutyServiceDataAttributes

        :param id: The PagerDuty service identifier.
        :type id: str

        :param type: PagerDuty service resource type.
        :type type: IncidentPagerdutyServiceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
