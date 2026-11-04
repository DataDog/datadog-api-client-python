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
    from datadog_api_client.v2.model.rum_metric_create_attributes import RumMetricCreateAttributes
    from datadog_api_client.v2.model.rum_metric_type import RumMetricType


class RumMetricCreateData(ModelNormal):
    validations = {
        "id": {
            "max_length": 200,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_metric_create_attributes import RumMetricCreateAttributes
        from datadog_api_client.v2.model.rum_metric_type import RumMetricType

        return {
            "attributes": (RumMetricCreateAttributes,),
            "id": (str,),
            "type": (RumMetricType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: RumMetricCreateAttributes, id: str, type: RumMetricType, **kwargs):
        """
        The new RUM-based metric properties.

        :param attributes: The object describing the Datadog RUM-based metric to create.
        :type attributes: RumMetricCreateAttributes

        :param id: The name of the RUM-based metric.
            On creation, it must be 1 to 200 characters long, contain only ASCII letters, digits, underscores, and periods, start with a letter, and not start with ``rum.measure`` or ``rum.investigate``.
            It cannot be changed after creation.
        :type id: str

        :param type: The type of the resource. The value must be ``rum_metrics``.
        :type type: RumMetricType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
