# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsExclusionFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "query": (str,),
            "sample_rate": (float,),
        }

    attribute_map = {
        "query": "query",
        "sample_rate": "sample_rate",
    }

    def __init__(self, sample_rate, *args, **kwargs):
        """
        Exclusion filter is defined by a query, a sampling rule, and a active/inactive toggle.

        :param query: Default query is ``*`` , meaning all logs flowing in the index would be excluded.
            Scope down exclusion filter to only a subset of logs with a log query.
        :type query: str, optional

        :param sample_rate: Sample rate to apply to logs going through this exclusion filter,
            a value of 1.0 excludes all logs matching the query.
        :type sample_rate: float
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.sample_rate = sample_rate

    @classmethod
    def _from_openapi_data(cls, sample_rate, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsExclusionFilter, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.sample_rate = sample_rate
        return self
