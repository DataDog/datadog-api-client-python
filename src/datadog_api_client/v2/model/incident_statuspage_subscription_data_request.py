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
    from datadog_api_client.v2.model.incident_statuspage_subscription_data_attributes_request import (
        IncidentStatuspageSubscriptionDataAttributesRequest,
    )
    from datadog_api_client.v2.model.incident_statuspage_subscription_type import IncidentStatuspageSubscriptionType


class IncidentStatuspageSubscriptionDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_statuspage_subscription_data_attributes_request import (
            IncidentStatuspageSubscriptionDataAttributesRequest,
        )
        from datadog_api_client.v2.model.incident_statuspage_subscription_type import IncidentStatuspageSubscriptionType

        return {
            "attributes": (IncidentStatuspageSubscriptionDataAttributesRequest,),
            "type": (IncidentStatuspageSubscriptionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentStatuspageSubscriptionDataAttributesRequest,
        type: IncidentStatuspageSubscriptionType,
        **kwargs,
    ):
        """
        Subscription data for a request.

        :param attributes: Attributes for creating an email subscription.
        :type attributes: IncidentStatuspageSubscriptionDataAttributesRequest

        :param type: Statuspage email subscription resource type.
        :type type: IncidentStatuspageSubscriptionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
