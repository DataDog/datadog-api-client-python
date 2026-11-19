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
    from datadog_api_client.v2.model.metric_metadata_attributes import MetricMetadataAttributes
    from datadog_api_client.v2.model.metric_metadata_type import MetricMetadataType


class MetricMetadataData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_metadata_attributes import MetricMetadataAttributes
        from datadog_api_client.v2.model.metric_metadata_type import MetricMetadataType

        return {
            "attributes": (MetricMetadataAttributes,),
            "id": (str,),
            "type": (MetricMetadataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: MetricMetadataAttributes, id: str, type: MetricMetadataType, **kwargs):
        """
        Metadata for one requested metric.

        :param attributes: Metadata for one metric. Every attribute is always present. A value that is unknown or not set is ``null``.
        :type attributes: MetricMetadataAttributes

        :param id: The metric name.
        :type id: str

        :param type: The metric metadata resource type.
        :type type: MetricMetadataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
