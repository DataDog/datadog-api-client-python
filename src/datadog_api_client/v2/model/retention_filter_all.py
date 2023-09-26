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
    from datadog_api_client.v2.model.retention_filter_all_attributes import RetentionFilterAllAttributes
    from datadog_api_client.v2.model.apm_retention_filter_type import ApmRetentionFilterType


class RetentionFilterAll(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.retention_filter_all_attributes import RetentionFilterAllAttributes
        from datadog_api_client.v2.model.apm_retention_filter_type import ApmRetentionFilterType

        return {
            "attributes": (RetentionFilterAllAttributes,),
            "id": (str,),
            "type": (ApmRetentionFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: RetentionFilterAllAttributes, id: str, type: ApmRetentionFilterType, **kwargs):
        """
        The definition of the retention filter.

        :param attributes: The attributes of the retention filter.
        :type attributes: RetentionFilterAllAttributes

        :param id: The ID of the retention filter.
        :type id: str

        :param type: The type of the resource.
        :type type: ApmRetentionFilterType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
