# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ApiTypeError,
    ModelSimple,
    cached_property,
)


class SecurityMonitoringRuleNewValueOptionsForgetAfter(ModelSimple):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    allowed_values = {
        "value": {
            "ONE_DAY": 1,
            "TWO_DAYS": 2,
            "ONE_WEEK": 7,
            "TWO_WEEKS": 14,
            "THREE_WEEKS": 21,
            "FOUR_WEEKS": 28,
        },
    }

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "value": (int,),
        }

    def __init__(self, *args, **kwargs):
        """SecurityMonitoringRuleNewValueOptionsForgetAfter - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.
        :param value: The duration in days after which a learned value is forgotten. Must be one of [1, 2, 7, 14, 21, 28].
        :type value: int
        """
        super().__init__(kwargs)

        if "value" in kwargs:
            value = kwargs.pop("value")
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=self._path_to_item,
                valid_classes=(self.__class__,),
            )

        self._check_pos_args(args)

        self.value = value

        self._check_kw_args(kwargs)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""
        return cls(*args, **kwargs)
