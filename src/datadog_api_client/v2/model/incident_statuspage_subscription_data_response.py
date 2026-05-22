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
    from datadog_api_client.v2.model.incident_statuspage_subscription_data_attributes_response import (
        IncidentStatuspageSubscriptionDataAttributesResponse,
    )
    from datadog_api_client.v2.model.incident_statuspage_subscription_type import IncidentStatuspageSubscriptionType


class IncidentStatuspageSubscriptionDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_statuspage_subscription_data_attributes_response import (
            IncidentStatuspageSubscriptionDataAttributesResponse,
        )
        from datadog_api_client.v2.model.incident_statuspage_subscription_type import IncidentStatuspageSubscriptionType

        return {
            "attributes": (IncidentStatuspageSubscriptionDataAttributesResponse,),
            "id": (str,),
            "type": (IncidentStatuspageSubscriptionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentStatuspageSubscriptionDataAttributesResponse,
        id: str,
        type: IncidentStatuspageSubscriptionType,
        **kwargs,
    ):
        """
        Email subscription data in a response.

        :param attributes: Attributes of an email subscription.
        :type attributes: IncidentStatuspageSubscriptionDataAttributesResponse

        :param id: The subscription identifier.
        :type id: str

        :param type: Statuspage email subscription resource type.
        :type type: IncidentStatuspageSubscriptionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
