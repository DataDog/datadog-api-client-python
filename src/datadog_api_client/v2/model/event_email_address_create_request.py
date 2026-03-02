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
    from datadog_api_client.v2.model.event_email_address_create_data import EventEmailAddressCreateData


class EventEmailAddressCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event_email_address_create_data import EventEmailAddressCreateData

        return {
            "data": (EventEmailAddressCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: EventEmailAddressCreateData, **kwargs):
        """
        Request body for creating an event email address.

        :param data: Data for creating an event email address.
        :type data: EventEmailAddressCreateData
        """
        super().__init__(kwargs)

        self_.data = data
