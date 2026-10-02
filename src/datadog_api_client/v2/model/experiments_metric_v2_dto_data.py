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
    from datadog_api_client.v2.model.experiments_metric_v2_dto_data_attributes import (
        ExperimentsMetricV2DTODataAttributes,
    )
    from datadog_api_client.v2.model.metric_type import MetricType


class ExperimentsMetricV2DTOData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_metric_v2_dto_data_attributes import (
            ExperimentsMetricV2DTODataAttributes,
        )
        from datadog_api_client.v2.model.metric_type import MetricType

        return {
            "attributes": (ExperimentsMetricV2DTODataAttributes,),
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
        id: UUID,
        type: MetricType,
        attributes: Union[ExperimentsMetricV2DTODataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON:API resource containing the metric identity and fields.

        :param attributes: Details of the metric.
        :type attributes: ExperimentsMetricV2DTODataAttributes, optional

        :param id: ID of the metric.
        :type id: UUID

        :param type: The metric resource type.
        :type type: MetricType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
