# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class UsageSyntheticsBrowserHour(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "browser_check_calls_count": (int,),
            "hour": (datetime,),
        }

    attribute_map = {
        "browser_check_calls_count": "browser_check_calls_count",
        "hour": "hour",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """UsageSyntheticsBrowserHour - a model defined in OpenAPI


        :param browser_check_calls_count: Contains the number of Synthetics Browser tests run.
        :type browser_check_calls_count: int, optional

        :param hour: The hour for the usage.
        :type hour: datetime, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageSyntheticsBrowserHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
