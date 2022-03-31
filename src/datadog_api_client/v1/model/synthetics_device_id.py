# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ApiTypeError,
    ModelSimple,
    cached_property,
)


class SyntheticsDeviceID(ModelSimple):

    allowed_values = {
        "value": {
            "LAPTOP_LARGE": "laptop_large",
            "TABLET": "tablet",
            "MOBILE_SMALL": "mobile_small",
            "CHROME_LAPTOP_LARGE": "chrome.laptop_large",
            "CHROME_TABLET": "chrome.tablet",
            "CHROME_MOBILE_SMALL": "chrome.mobile_small",
            "FIREFOX_LAPTOP_LARGE": "firefox.laptop_large",
            "FIREFOX_TABLET": "firefox.tablet",
            "FIREFOX_MOBILE_SMALL": "firefox.mobile_small",
            "EDGE_LAPTOP_LARGE": "edge.laptop_large",
            "EDGE_TABLET": "edge.tablet",
            "EDGE_MOBILE_SMALL": "edge.mobile_small",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }

    def __init__(self, *args, **kwargs):
        """
        The device ID.

        Note that value can be passed either in args or in kwargs, but not in both.

        :param value: Must be one of ["laptop_large", "tablet", "mobile_small", "chrome.laptop_large", "chrome.tablet", "chrome.mobile_small", "firefox.laptop_large", "firefox.tablet", "firefox.mobile_small", "edge.laptop_large", "edge.tablet", "edge.mobile_small"].
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
