# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class ExperimentsCreateExperimentV2RequestDataAttributesDecisionMetricsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "is_primary": (bool,),
            "metric_id": (UUID,),
        }

    attribute_map = {
        "is_primary": "is_primary",
        "metric_id": "metric_id",
    }

    def __init__(self_, is_primary: bool, metric_id: UUID, **kwargs):
        """
        Metric used to make an experiment decision, with its primary metric designation.

        :param is_primary: Whether this is the experiment primary metric.
        :type is_primary: bool

        :param metric_id: Decision metric UUID.
        :type metric_id: UUID
        """
        super().__init__(kwargs)

        self_.is_primary = is_primary
        self_.metric_id = metric_id
