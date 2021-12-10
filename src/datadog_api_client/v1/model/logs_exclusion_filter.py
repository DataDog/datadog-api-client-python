# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
)


class LogsExclusionFilter(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "query": (str,),
            "sample_rate": (float,),
        }

    attribute_map = {
        "sample_rate": "sample_rate",
        "query": "query",
    }

    read_only_vars = {}

    def __init__(self, sample_rate, *args, **kwargs):
        """LogsExclusionFilter - a model defined in OpenAPI

        Args:
            sample_rate (float): Sample rate to apply to logs going through this exclusion filter, a value of 1.0 excludes all logs matching the query.

        Keyword Args:
            query (str): [optional] Default query is `*`, meaning all logs flowing in the index would be excluded. Scope down exclusion filter to only a subset of logs with a log query.
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
