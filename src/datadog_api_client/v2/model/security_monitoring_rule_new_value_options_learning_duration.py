# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ApiTypeError,
    ModelSimple,
    cached_property,
)


class SecurityMonitoringRuleNewValueOptionsLearningDuration(ModelSimple):
    allowed_values = {
        "value": {
            "ZERO_DAYS": 0,
            "ONE_DAY": 1,
            "SEVEN_DAYS": 7,
        },
    }

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "value": (int,),
        }

    def __init__(self, *args, **kwargs):
        """
        The duration in days during which values are learned, and after which signals will be generated for values that
        weren't learned. If set to 0, a signal will be generated for all new values after the first value is learned.

        Note that value can be passed either in args or in kwargs, but not in both.

        :param value: Must be one of [0, 1, 7].
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
