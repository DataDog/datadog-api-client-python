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
    from datadog_api_client.v2.model.change_request_create_attributes import ChangeRequestCreateAttributes
    from datadog_api_client.v2.model.change_request_resource_type import ChangeRequestResourceType


class ChangeRequestCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_request_create_attributes import ChangeRequestCreateAttributes
        from datadog_api_client.v2.model.change_request_resource_type import ChangeRequestResourceType

        return {
            "attributes": (ChangeRequestCreateAttributes,),
            "type": (ChangeRequestResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: ChangeRequestCreateAttributes, type: ChangeRequestResourceType, **kwargs):
        """
        Data object to create a change request.

        :param attributes: Attributes for creating a change request.
        :type attributes: ChangeRequestCreateAttributes

        :param type: Change request resource type.
        :type type: ChangeRequestResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
