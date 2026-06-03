# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_metric_update_attributes import RumMetricUpdateAttributes
    from datadog_api_client.v2.model.rum_metric_type import RumMetricType


class RumMetricUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_metric_update_attributes import RumMetricUpdateAttributes
        from datadog_api_client.v2.model.rum_metric_type import RumMetricType

        return {
            "attributes": (RumMetricUpdateAttributes,),
            "id": (str,),
            "type": (RumMetricType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: RumMetricUpdateAttributes, type: RumMetricType, id: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        The new rum-based metric properties.

        :param attributes: The rum-based metric properties that will be updated.
        :type attributes: RumMetricUpdateAttributes

        :param id: The name of the rum-based metric.
        :type id: str, optional

        :param type: The type of the resource. The value should always be rum_metrics.
        :type type: RumMetricType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
