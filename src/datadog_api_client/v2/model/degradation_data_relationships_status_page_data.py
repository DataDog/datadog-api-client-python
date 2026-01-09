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
    from datadog_api_client.v2.model.status_page_data_type import StatusPageDataType


class DegradationDataRelationshipsStatusPageData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.status_page_data_type import StatusPageDataType

        return {
            "id": (str,),
            "type": (StatusPageDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: StatusPageDataType, **kwargs):
        """


        :param id:
        :type id: str

        :param type: Status pages resource type.
        :type type: StatusPageDataType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
