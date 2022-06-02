# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricsAndMetricTagConfigurationsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metrics_and_metric_tag_configurations import MetricsAndMetricTagConfigurations

        return {
            "data": ([MetricsAndMetricTagConfigurations],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self, *args, **kwargs):
        """
        Response object that includes metrics and metric tag configurations.

        :param data: Array of metrics and metric tag configurations.
        :type data: [MetricsAndMetricTagConfigurations], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricsAndMetricTagConfigurationsResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
