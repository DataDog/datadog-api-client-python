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
    from datadog_api_client.v2.model.downtime_create_request_attributes import DowntimeCreateRequestAttributes
    from datadog_api_client.v2.model.downtime_resource_type import DowntimeResourceType


class DowntimeCreateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.downtime_create_request_attributes import DowntimeCreateRequestAttributes
        from datadog_api_client.v2.model.downtime_resource_type import DowntimeResourceType

        return {
            "attributes": (DowntimeCreateRequestAttributes,),
            "type": (DowntimeResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: DowntimeCreateRequestAttributes, type: DowntimeResourceType, **kwargs):
        """
        Object to create a downtime.

        :param attributes: Downtime details.
        :type attributes: DowntimeCreateRequestAttributes

        :param type: Downtime resource type.
        :type type: DowntimeResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
