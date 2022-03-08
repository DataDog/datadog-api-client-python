# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ApiTypeError,
    ModelSimple,
    cached_property,
)


class WidgetTimeWindows(ModelSimple):

    allowed_values = {
        "value": {
            "SEVEN_DAYS": "7d",
            "THIRTY_DAYS": "30d",
            "NINETY_DAYS": "90d",
            "WEEK_TO_DATE": "week_to_date",
            "PREVIOUS_WEEK": "previous_week",
            "MONTH_TO_DATE": "month_to_date",
            "PREVIOUS_MONTH": "previous_month",
            "GLOBAL_TIME": "global_time",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }

    def __init__(self, *args, **kwargs):
        """
        Define a time window.

        Note that value can be passed either in args or in kwargs, but not in both.

        :param value: Must be one of ["7d", "30d", "90d", "week_to_date", "previous_week", "month_to_date", "previous_month", "global_time"].
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
