# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_on_call_event_email_address_request_data_attributes import (
        CreateOnCallEventEmailAddressRequestDataAttributes,
    )
    from datadog_api_client.v2.model.event_emails_type import EventEmailsType


class CreateOnCallEventEmailAddressRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_on_call_event_email_address_request_data_attributes import (
            CreateOnCallEventEmailAddressRequestDataAttributes,
        )
        from datadog_api_client.v2.model.event_emails_type import EventEmailsType

        return {
            "attributes": (CreateOnCallEventEmailAddressRequestDataAttributes,),
            "type": (EventEmailsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: EventEmailsType,
        attributes: Union[CreateOnCallEventEmailAddressRequestDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: CreateOnCallEventEmailAddressRequestDataAttributes, optional

        :param type: Event emails resource type.
        :type type: EventEmailsType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
