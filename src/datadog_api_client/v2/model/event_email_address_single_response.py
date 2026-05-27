# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.event_email_address_data import EventEmailAddressData
    from datadog_api_client.v2.model.event_email_address_included_user import EventEmailAddressIncludedUser


class EventEmailAddressSingleResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event_email_address_data import EventEmailAddressData
        from datadog_api_client.v2.model.event_email_address_included_user import EventEmailAddressIncludedUser

        return {
            "data": (EventEmailAddressData,),
            "included": ([EventEmailAddressIncludedUser],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: EventEmailAddressData,
        included: Union[List[EventEmailAddressIncludedUser], UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing a single event email address.

        :param data: A single event email address resource.
        :type data: EventEmailAddressData

        :param included: Related resources included in the response.
        :type included: [EventEmailAddressIncludedUser], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
