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
    from datadog_api_client.v2.model.retention_filter_create_attributes import RetentionFilterCreateAttributes
    from datadog_api_client.v2.model.apm_retention_filter_type import ApmRetentionFilterType


class RetentionFilterCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.retention_filter_create_attributes import RetentionFilterCreateAttributes
        from datadog_api_client.v2.model.apm_retention_filter_type import ApmRetentionFilterType

        return {
            "attributes": (RetentionFilterCreateAttributes,),
            "type": (ApmRetentionFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: RetentionFilterCreateAttributes, type: ApmRetentionFilterType, **kwargs):
        """
        The body of the retention filter to be created.

        :param attributes: The object describing the configuration of the retention filter to create/update.
        :type attributes: RetentionFilterCreateAttributes

        :param type: The type of the resource.
        :type type: ApmRetentionFilterType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
