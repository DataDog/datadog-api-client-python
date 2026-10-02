# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ExperimentsExperimentMetricGroupMutationV2DataAttributesMetricsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "is_primary": (bool,),
            "metric_id": (str,),
            "metric_name": (str,),
        }

    attribute_map = {
        "is_primary": "is_primary",
        "metric_id": "metric_id",
        "metric_name": "metric_name",
    }

    def __init__(self_, is_primary: bool, metric_id: str, metric_name: str, **kwargs):
        """
        Metric in an experiment metric group, with its name and primary metric designation.

        :param is_primary: Whether this is the experiment primary metric.
        :type is_primary: bool

        :param metric_id: Identifier of the metric in the group.
        :type metric_id: str

        :param metric_name: Display name of the metric in the group.
        :type metric_name: str
        """
        super().__init__(kwargs)

        self_.is_primary = is_primary
        self_.metric_id = metric_id
        self_.metric_name = metric_name
