# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.event_email_address_response_data import EventEmailAddressResponseData


class EventEmailAddressResponseArray(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event_email_address_response_data import EventEmailAddressResponseData

        return {
            "data": ([EventEmailAddressResponseData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[EventEmailAddressResponseData], **kwargs):
        """


        :param data:
        :type data: [EventEmailAddressResponseData]
        """
        super().__init__(kwargs)

        self_.data = data
