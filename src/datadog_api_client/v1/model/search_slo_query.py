# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class SearchSLOQuery(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "denominator": (str,),
            "metrics": ([str], none_type),
            "numerator": (str,),
        }

    attribute_map = {
        "denominator": "denominator",
        "metrics": "metrics",
        "numerator": "numerator",
    }

    def __init__(self_, *args, **kwargs):
        """
        A metric-based SLO. **Required if type is metric**. Note that Datadog only allows the sum by aggregator
        to be used because this will sum up all request counts instead of averaging them, or taking the max or
        min of all of those requests.

        :param denominator: A Datadog metric query for total (valid) events.
        :type denominator: str, optional

        :param metrics: Metric names used in the query's numerator and denominator.
            This field will return null and will be implemented in the next version of this endpoint.
        :type metrics: [str], none_type, optional

        :param numerator: A Datadog metric query for good events.
        :type numerator: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
