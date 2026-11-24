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
    from datadog_api_client.v2.model.rum_metric_response_attributes import RUMMetricResponseAttributes
    from datadog_api_client.v2.model.rum_metric_type import RUMMetricType


class RUMMetricResponseData(ModelNormal):
    validations = {
        "id": {
            "max_length": 200,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_metric_response_attributes import RUMMetricResponseAttributes
        from datadog_api_client.v2.model.rum_metric_type import RUMMetricType

        return {
            "attributes": (RUMMetricResponseAttributes,),
            "id": (str,),
            "type": (RUMMetricType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[RUMMetricResponseAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[RUMMetricType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The RUM-based metric properties.

        :param attributes: The object describing a Datadog RUM-based metric.
        :type attributes: RUMMetricResponseAttributes, optional

        :param id: The name of the RUM-based metric.
            On creation, it must be 1 to 200 characters long, contain only ASCII letters, digits, underscores, and periods, start with a letter, and not start with ``rum.measure`` or ``rum.investigate``.
            It cannot be changed after creation.
        :type id: str, optional

        :param type: The type of the resource. The value must be ``rum_metrics``.
        :type type: RUMMetricType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
