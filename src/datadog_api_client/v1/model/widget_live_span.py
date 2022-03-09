# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ApiTypeError,
    ModelSimple,
    cached_property,
)


class WidgetLiveSpan(ModelSimple):

    allowed_values = {
        "value": {
            "PAST_ONE_MINUTE": "1m",
            "PAST_FIVE_MINUTES": "5m",
            "PAST_TEN_MINUTES": "10m",
            "PAST_FIFTEEN_MINUTES": "15m",
            "PAST_THIRTY_MINUTES": "30m",
            "PAST_ONE_HOUR": "1h",
            "PAST_FOUR_HOURS": "4h",
            "PAST_ONE_DAY": "1d",
            "PAST_TWO_DAYS": "2d",
            "PAST_ONE_WEEK": "1w",
            "PAST_ONE_MONTH": "1mo",
            "PAST_THREE_MONTHS": "3mo",
            "PAST_SIX_MONTHS": "6mo",
            "PAST_ONE_YEAR": "1y",
            "ALERT": "alert",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }

    def __init__(self, *args, **kwargs):
        """
        The available timeframes depend on the widget you are using.

        Note that value can be passed either in args or in kwargs, but not in both.

        :param value: Must be one of ["1m", "5m", "10m", "15m", "30m", "1h", "4h", "1d", "2d", "1w", "1mo", "3mo", "6mo", "1y", "alert"].
        :type value: str
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
