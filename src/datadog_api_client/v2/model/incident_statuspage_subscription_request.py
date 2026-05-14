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
    from datadog_api_client.v2.model.incident_statuspage_subscription_data_request import (
        IncidentStatuspageSubscriptionDataRequest,
    )


class IncidentStatuspageSubscriptionRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_statuspage_subscription_data_request import (
            IncidentStatuspageSubscriptionDataRequest,
        )

        return {
            "data": (IncidentStatuspageSubscriptionDataRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IncidentStatuspageSubscriptionDataRequest, **kwargs):
        """
        Request to create an email subscription.

        :param data: Subscription data for a request.
        :type data: IncidentStatuspageSubscriptionDataRequest
        """
        super().__init__(kwargs)

        self_.data = data
