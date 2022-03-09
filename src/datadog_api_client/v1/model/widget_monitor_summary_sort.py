# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ApiTypeError,
    ModelSimple,
    cached_property,
)


class WidgetMonitorSummarySort(ModelSimple):

    allowed_values = {
        "value": {
            "NAME": "name",
            "GROUP": "group",
            "STATUS": "status",
            "TAGS": "tags",
            "TRIGGERED": "triggered",
            "GROUP_ASCENDING": "group,asc",
            "GROUP_DESCENDING": "group,desc",
            "NAME_ASCENDING": "name,asc",
            "NAME_DESCENDING": "name,desc",
            "STATUS_ASCENDING": "status,asc",
            "STATUS_DESCENDING": "status,desc",
            "TAGS_ASCENDING": "tags,asc",
            "TAGS_DESCENDING": "tags,desc",
            "TRIGGERED_ASCENDING": "triggered,asc",
            "TRIGGERED_DESCENDING": "triggered,desc",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }

    def __init__(self, *args, **kwargs):
        """
        Widget sorting methods.

        Note that value can be passed either in args or in kwargs, but not in both.

        :param value: Must be one of ["name", "group", "status", "tags", "triggered", "group,asc", "group,desc", "name,asc", "name,desc", "status,asc", "status,desc", "tags,asc", "tags,desc", "triggered,asc", "triggered,desc"].
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
