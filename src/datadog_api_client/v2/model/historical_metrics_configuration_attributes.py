# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class HistoricalMetricsConfigurationAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
        }

    attribute_map = {
        "created_at": "created_at",
    }
    read_only_vars = {
        "created_at",
    }

    def __init__(self_, created_at: Union[datetime, UnsetType] = unset, **kwargs):
        """
        Attributes of a historical metrics configuration.

        :param created_at: Timestamp when historical metrics ingestion was enabled for the metric.
        :type created_at: datetime, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        super().__init__(kwargs)
