# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RUMBucketResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_aggregate_bucket_value import RUMAggregateBucketValue

        return {
            "by": ({str: (str,)},),
            "computes": ({str: (RUMAggregateBucketValue,)},),
        }

    attribute_map = {
        "by": "by",
        "computes": "computes",
    }

    def __init__(self, *args, **kwargs):
        """
        Bucket values.

        :param by: The key-value pairs for each group-by.
        :type by: {str: (str,)}, optional

        :param computes: A map of the metric name to value for regular compute, or a list of values for a timeseries.
        :type computes: {str: (RUMAggregateBucketValue,)}, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(RUMBucketResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
