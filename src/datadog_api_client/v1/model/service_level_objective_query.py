# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ServiceLevelObjectiveQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "denominator": (str,),
            "numerator": (str,),
        }

    attribute_map = {
        "denominator": "denominator",
        "numerator": "numerator",
    }

    def __init__(self, denominator, numerator, *args, **kwargs):
        """
        A metric-based SLO. **Required if type is metric**. Note that Datadog only allows the sum by aggregator
        to be used because this will sum up all request counts instead of averaging them, or taking the max or
        min of all of those requests.

        :param denominator: A Datadog metric query for total (valid) events.
        :type denominator: str

        :param numerator: A Datadog metric query for good events.
        :type numerator: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.denominator = denominator
        self.numerator = numerator

    @classmethod
    def _from_openapi_data(cls, denominator, numerator, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ServiceLevelObjectiveQuery, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.denominator = denominator
        self.numerator = numerator
        return self
