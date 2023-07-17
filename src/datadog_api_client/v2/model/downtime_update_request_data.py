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
    from datadog_api_client.v2.model.downtime_update_request_attributes import DowntimeUpdateRequestAttributes
    from datadog_api_client.v2.model.downtime_resource_type import DowntimeResourceType


class DowntimeUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.downtime_update_request_attributes import DowntimeUpdateRequestAttributes
        from datadog_api_client.v2.model.downtime_resource_type import DowntimeResourceType

        return {
            "attributes": (DowntimeUpdateRequestAttributes,),
            "id": (str,),
            "type": (DowntimeResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: DowntimeUpdateRequestAttributes, id: str, type: DowntimeResourceType, **kwargs):
        """
        Object to update a downtime.

        :param attributes: Attributes of the downtime to update.
        :type attributes: DowntimeUpdateRequestAttributes

        :param id: ID of this downtime.
        :type id: str

        :param type: Downtime resource type.
        :type type: DowntimeResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
