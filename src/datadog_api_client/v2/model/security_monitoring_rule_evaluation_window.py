# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ApiTypeError,
    ModelSimple,
    cached_property,
)


class SecurityMonitoringRuleEvaluationWindow(ModelSimple):

    allowed_values = {
        "value": {
            "ZERO_MINUTES": 0,
            "ONE_MINUTE": 60,
            "FIVE_MINUTES": 300,
            "TEN_MINUTES": 600,
            "FIFTEEN_MINUTES": 900,
            "THIRTY_MINUTES": 1800,
            "ONE_HOUR": 3600,
            "TWO_HOURS": 7200,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (int,),
        }

    def __init__(self, *args, **kwargs):
        """
        A time window is specified to match when at least one of the cases matches true. This is a sliding window
        and evaluates in real time.

        Note that value can be passed either in args or in kwargs, but not in both.

        :param value: Must be one of [0, 60, 300, 600, 900, 1800, 3600, 7200].
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
