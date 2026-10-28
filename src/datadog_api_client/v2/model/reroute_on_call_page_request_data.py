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
    from datadog_api_client.v2.model.reroute_on_call_page_request_data_attributes import (
        RerouteOnCallPageRequestDataAttributes,
    )
    from datadog_api_client.v2.model.reroute_on_call_page_request_data_type import RerouteOnCallPageRequestDataType


class RerouteOnCallPageRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.reroute_on_call_page_request_data_attributes import (
            RerouteOnCallPageRequestDataAttributes,
        )
        from datadog_api_client.v2.model.reroute_on_call_page_request_data_type import RerouteOnCallPageRequestDataType

        return {
            "attributes": (RerouteOnCallPageRequestDataAttributes,),
            "type": (RerouteOnCallPageRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: RerouteOnCallPageRequestDataAttributes, type: RerouteOnCallPageRequestDataType, **kwargs
    ):
        """
        The data for rerouting an On-Call Page, including attributes and resource type.

        :param attributes: Details about where to reroute the On-Call Page.
        :type attributes: RerouteOnCallPageRequestDataAttributes

        :param type: The type of resource used when rerouting an On-Call Page.
        :type type: RerouteOnCallPageRequestDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
