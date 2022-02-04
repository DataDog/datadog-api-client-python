# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class UsageSyntheticsAPIHour(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "check_calls_count": (int,),
            "hour": (datetime,),
        }

    attribute_map = {
        "check_calls_count": "check_calls_count",
        "hour": "hour",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """UsageSyntheticsAPIHour - a model defined in OpenAPI


        :param check_calls_count: Contains the number of Synthetics API tests run.
        :type check_calls_count: int, optional

        :param hour: The hour for the usage.
        :type hour: datetime, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageSyntheticsAPIHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
