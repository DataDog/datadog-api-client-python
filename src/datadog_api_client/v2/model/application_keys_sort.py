# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class ApplicationKeysSort(ModelSimple):

    allowed_values = {
        "value": {
            "CREATED_AT_ASCENDING": "created_at",
            "CREATED_AT_DESCENDING": "-created_at",
            "LAST4_ASCENDING": "last4",
            "LAST4_DESCENDING": "-last4",
            "NAME_ASCENDING": "name",
            "NAME_DESCENDING": "-name",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }

    def __init__(self, *args, **kwargs):
        """
        Sorting options

        Note that value can be passed either in args or in kwargs, but not in both.

        :param value: If omitted defaults to "name". Must be one of ["created_at", "-created_at", "last4", "-last4", "name", "-name"].
        :type value: str
        """
        super().__init__(kwargs)

        if "value" in kwargs:
            value = kwargs.pop("value")
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            value = "name"

        self._check_pos_args(args)

        self.value = value

        self._check_kw_args(kwargs)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""
        return cls(*args, **kwargs)
