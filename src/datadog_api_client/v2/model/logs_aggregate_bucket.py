# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsAggregateBucket(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_aggregate_bucket_value import LogsAggregateBucketValue

        return {
            "by": ({str: (str,)},),
            "computes": ({str: (LogsAggregateBucketValue,)},),
        }

    attribute_map = {
        "by": "by",
        "computes": "computes",
    }

    def __init__(self, *args, **kwargs):
        """
        A bucket values

        :param by: The key, value pairs for each group by
        :type by: {str: (str,)}, optional

        :param computes: A map of the metric name -> value for regular compute or list of values for a timeseries
        :type computes: {str: (LogsAggregateBucketValue,)}, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsAggregateBucket, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
