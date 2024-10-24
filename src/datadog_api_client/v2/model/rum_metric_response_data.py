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
    from datadog_api_client.v2.model.rum_metric_response_attributes import RumMetricResponseAttributes
    from datadog_api_client.v2.model.rum_metric_type import RumMetricType


class RumMetricResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_metric_response_attributes import RumMetricResponseAttributes
        from datadog_api_client.v2.model.rum_metric_type import RumMetricType

        return {
            "attributes": (RumMetricResponseAttributes,),
            "id": (str,),
            "type": (RumMetricType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[RumMetricResponseAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[RumMetricType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The rum-based metric properties.

        :param attributes: The object describing a Datadog rum-based metric.
        :type attributes: RumMetricResponseAttributes, optional

        :param id: The name of the rum-based metric.
        :type id: str, optional

        :param type: The type of the resource. The value should always be rum_metrics.
        :type type: RumMetricType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
