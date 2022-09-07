# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricPayload(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_series import MetricSeries

        return {
            "series": ([MetricSeries],),
        }

    attribute_map = {
        "series": "series",
    }

    def __init__(self_, series, *args, **kwargs):
        """
        The metrics' payload.

        :param series: A list of time series to submit to Datadog.
        :type series: [MetricSeries]
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.series = series
