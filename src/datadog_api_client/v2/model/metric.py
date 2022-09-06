# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class Metric(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_type import MetricType

        return {
            "id": (str,),
            "type": (MetricType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, *args, **kwargs):
        """
        Object for a single metric tag configuration.

        :param id: The metric name for this resource.
        :type id: str, optional

        :param type: The metric resource type.
        :type type: MetricType, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
