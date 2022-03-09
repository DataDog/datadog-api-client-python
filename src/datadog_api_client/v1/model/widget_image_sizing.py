# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ApiTypeError,
    ModelSimple,
    cached_property,
)


class WidgetImageSizing(ModelSimple):

    allowed_values = {
        "value": {
            "FILL": "fill",
            "CONTAIN": "contain",
            "COVER": "cover",
            "NONE": "none",
            "SCALEDOWN": "scale-down",
            "ZOOM": "zoom",
            "FIT": "fit",
            "CENTER": "center",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }

    def __init__(self, *args, **kwargs):
        """
        How to size the image on the widget. The values are based on the image `object-fit` CSS properties.
        **Note**: `zoom`, `fit` and `center` values are deprecated.

        Note that value can be passed either in args or in kwargs, but not in both.

        :param value: Must be one of ["fill", "contain", "cover", "none", "scale-down", "zoom", "fit", "center"].
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
