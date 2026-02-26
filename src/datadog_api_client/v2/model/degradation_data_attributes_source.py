# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.degradation_data_attributes_source_type import DegradationDataAttributesSourceType


class DegradationDataAttributesSource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.degradation_data_attributes_source_type import (
            DegradationDataAttributesSourceType,
        )

        return {
            "created_at": (datetime,),
            "source_id": (str,),
            "type": (DegradationDataAttributesSourceType,),
        }

    attribute_map = {
        "created_at": "created_at",
        "source_id": "source_id",
        "type": "type",
    }

    def __init__(self_, created_at: datetime, source_id: str, type: DegradationDataAttributesSourceType, **kwargs):
        """
        The source of the degradation.

        :param created_at: Timestamp of when the source was created.
        :type created_at: datetime

        :param source_id: The ID of the source.
        :type source_id: str

        :param type: The type of the source.
        :type type: DegradationDataAttributesSourceType
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.source_id = source_id
        self_.type = type
