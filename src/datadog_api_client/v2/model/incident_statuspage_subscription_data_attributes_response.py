# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class IncidentStatuspageSubscriptionDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "confirmed": (bool,),
            "created_at": (datetime,),
            "email": (str,),
        }

    attribute_map = {
        "confirmed": "confirmed",
        "created_at": "created_at",
        "email": "email",
    }

    def __init__(self_, confirmed: bool, created_at: datetime, email: str, **kwargs):
        """
        Attributes of an email subscription.

        :param confirmed: Whether the subscription has been confirmed.
        :type confirmed: bool

        :param created_at: Timestamp when the subscription was created.
        :type created_at: datetime

        :param email: The subscribed email address.
        :type email: str
        """
        super().__init__(kwargs)

        self_.confirmed = confirmed
        self_.created_at = created_at
        self_.email = email
