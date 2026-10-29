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
    validations = {
        "id": {
            "max_length": 200,
        },
    }

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
        The RUM-based metric properties to update. ``id`` is required by the API and must match the ``metric_id`` path parameter.

        :param attributes: The RUM-based metric properties that will be updated. Omitted properties keep their current value.
        :type attributes: RumMetricUpdateAttributes

        :param id: The name of the RUM-based metric.
            On creation, it must be 1 to 200 characters long, contain only ASCII letters, digits, underscores, and periods, start with a letter, and not start with ``rum.measure`` or ``rum.investigate``.
            It cannot be changed after creation.
        :type id: str, optional

        :param type: The type of the resource. The value must be ``rum_metrics``.
        :type type: RumMetricType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
