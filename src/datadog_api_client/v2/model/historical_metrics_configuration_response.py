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
    from datadog_api_client.v2.model.historical_metrics_configuration_data import HistoricalMetricsConfigurationData


class HistoricalMetricsConfigurationResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.historical_metrics_configuration_data import HistoricalMetricsConfigurationData

        return {
            "data": (HistoricalMetricsConfigurationData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[HistoricalMetricsConfigurationData, UnsetType] = unset, **kwargs):
        """
        Response containing a historical metrics configuration.

        :param data: A historical metrics configuration resource object. Existence of this resource means historical metrics ingestion is enabled for the metric; there is no separate enabled attribute.
        :type data: HistoricalMetricsConfigurationData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
