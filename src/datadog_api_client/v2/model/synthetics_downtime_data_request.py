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
    from datadog_api_client.v2.model.synthetics_downtime_data_attributes_request import (
        SyntheticsDowntimeDataAttributesRequest,
    )
    from datadog_api_client.v2.model.synthetics_downtime_resource_type import SyntheticsDowntimeResourceType


class SyntheticsDowntimeDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_downtime_data_attributes_request import (
            SyntheticsDowntimeDataAttributesRequest,
        )
        from datadog_api_client.v2.model.synthetics_downtime_resource_type import SyntheticsDowntimeResourceType

        return {
            "attributes": (SyntheticsDowntimeDataAttributesRequest,),
            "type": (SyntheticsDowntimeResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: SyntheticsDowntimeDataAttributesRequest, type: SyntheticsDowntimeResourceType, **kwargs
    ):
        """
        The data object for a Synthetics downtime create or update request.

        :param attributes: Attributes for creating or updating a Synthetics downtime.
        :type attributes: SyntheticsDowntimeDataAttributesRequest

        :param type: The resource type for a Synthetics downtime.
        :type type: SyntheticsDowntimeResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
