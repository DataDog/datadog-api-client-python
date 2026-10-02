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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_update_metric_v2_request_data_attributes import (
        ExperimentsUpdateMetricV2RequestDataAttributes,
    )
    from datadog_api_client.v2.model.metric_type import MetricType


class ExperimentsUpdateMetricV2RequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_update_metric_v2_request_data_attributes import (
            ExperimentsUpdateMetricV2RequestDataAttributes,
        )
        from datadog_api_client.v2.model.metric_type import MetricType

        return {
            "attributes": (ExperimentsUpdateMetricV2RequestDataAttributes,),
            "id": (UUID,),
            "type": (MetricType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: MetricType,
        attributes: Union[ExperimentsUpdateMetricV2RequestDataAttributes, UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON:API resource containing the metric identity and fields.

        :param attributes: Fields supplied to update the metric. Every attribute is optional; omit an attribute to leave it unchanged.
        :type attributes: ExperimentsUpdateMetricV2RequestDataAttributes, optional

        :param id: ID of the metric.
        :type id: UUID, optional

        :param type: The metric resource type.
        :type type: MetricType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
