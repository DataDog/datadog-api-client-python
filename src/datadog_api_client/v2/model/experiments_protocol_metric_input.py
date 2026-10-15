# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class ExperimentsProtocolMetricInput(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "metric_id": (UUID,),
        }

    attribute_map = {
        "metric_id": "metric_id",
    }

    def __init__(self_, metric_id: UUID, **kwargs):
        """
        A metric included in a protocol. Select the primary metric with ``primary_metric_id`` , not ``is_primary``.

        :param metric_id: Metric UUID.
        :type metric_id: UUID
        """
        super().__init__(kwargs)

        self_.metric_id = metric_id
