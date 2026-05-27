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
    from datadog_api_client.v2.model.event_email_address_user_data import EventEmailAddressUserData


class EventEmailAddressCreatedByRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event_email_address_user_data import EventEmailAddressUserData

        return {
            "data": (EventEmailAddressUserData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: EventEmailAddressUserData, **kwargs):
        """
        Relationship to the user who created the email address.

        :param data: A user data reference in a relationship.
        :type data: EventEmailAddressUserData
        """
        super().__init__(kwargs)

        self_.data = data
