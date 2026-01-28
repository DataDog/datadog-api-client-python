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
    from datadog_api_client.v2.model.create_status_page_request_data_attributes import (
        CreateStatusPageRequestDataAttributes,
    )
    from datadog_api_client.v2.model.status_page_data_type import StatusPageDataType


class CreateStatusPageRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_status_page_request_data_attributes import (
            CreateStatusPageRequestDataAttributes,
        )
        from datadog_api_client.v2.model.status_page_data_type import StatusPageDataType

        return {
            "attributes": (CreateStatusPageRequestDataAttributes,),
            "type": (StatusPageDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: CreateStatusPageRequestDataAttributes, type: StatusPageDataType, **kwargs):
        """


        :param attributes: The supported attributes for creating a status page.
        :type attributes: CreateStatusPageRequestDataAttributes

        :param type: Status pages resource type.
        :type type: StatusPageDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
