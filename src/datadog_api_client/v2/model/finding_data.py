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
    from datadog_api_client.v2.model.finding_data_type import FindingDataType


class FindingData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.finding_data_type import FindingDataType

        return {
            "id": (str,),
            "type": (FindingDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: FindingDataType, **kwargs):
        """


        :param id: Unique identifier of the security finding.
        :type id: str

        :param type: Security findings resource type.
        :type type: FindingDataType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
