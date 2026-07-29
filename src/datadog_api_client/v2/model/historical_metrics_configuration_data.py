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
    from datadog_api_client.v2.model.historical_metrics_configuration_attributes import (
        HistoricalMetricsConfigurationAttributes,
    )
    from datadog_api_client.v2.model.historical_metrics_configuration_type import HistoricalMetricsConfigurationType


class HistoricalMetricsConfigurationData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.historical_metrics_configuration_attributes import (
            HistoricalMetricsConfigurationAttributes,
        )
        from datadog_api_client.v2.model.historical_metrics_configuration_type import HistoricalMetricsConfigurationType

        return {
            "attributes": (HistoricalMetricsConfigurationAttributes,),
            "id": (str,),
            "type": (HistoricalMetricsConfigurationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[HistoricalMetricsConfigurationAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[HistoricalMetricsConfigurationType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A historical metrics configuration resource object. Existence of this resource means historical metrics ingestion is enabled for the metric; there is no separate enabled attribute.

        :param attributes: Attributes of a historical metrics configuration.
        :type attributes: HistoricalMetricsConfigurationAttributes, optional

        :param id: The metric name, used as the resource ID.
        :type id: str, optional

        :param type: The historical metrics configuration resource type.
        :type type: HistoricalMetricsConfigurationType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
