# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageTopAvgMetricsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.usage_top_avg_metrics_metadata import UsageTopAvgMetricsMetadata
        from datadog_api_client.v1.model.usage_top_avg_metrics_hour import UsageTopAvgMetricsHour

        return {
            "metadata": (UsageTopAvgMetricsMetadata,),
            "usage": ([UsageTopAvgMetricsHour],),
        }

    attribute_map = {
        "metadata": "metadata",
        "usage": "usage",
    }

    def __init__(self, *args, **kwargs):
        """
        Response containing the number of hourly recorded custom metrics for a given organization.

        :param metadata: The object containing document metadata.
        :type metadata: UsageTopAvgMetricsMetadata, optional

        :param usage: Number of hourly recorded custom metrics for a given organization.
        :type usage: [UsageTopAvgMetricsHour], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageTopAvgMetricsResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
