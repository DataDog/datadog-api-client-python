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
    from datadog_api_client.v2.model.on_call_event_email_address_create_data import OnCallEventEmailAddressCreateData


class OnCallEventEmailAddressCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_event_email_address_create_data import (
            OnCallEventEmailAddressCreateData,
        )

        return {
            "data": (OnCallEventEmailAddressCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: OnCallEventEmailAddressCreateData, **kwargs):
        """
        Request body for creating an on-call event email address.

        :param data: Data for creating an on-call event email address.
        :type data: OnCallEventEmailAddressCreateData
        """
        super().__init__(kwargs)

        self_.data = data
