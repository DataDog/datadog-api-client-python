# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class WidgetCustomLink(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "is_hidden": (bool,),
            "label": (str,),
            "link": (str,),
            "override_label": (str,),
        }

    attribute_map = {
        "is_hidden": "is_hidden",
        "label": "label",
        "link": "link",
        "override_label": "override_label",
    }

    def __init__(self, *args, **kwargs):
        """
        Custom links help you connect a data value to a URL, like a Datadog page or your AWS console.

        :param is_hidden: The flag for toggling context menu link visibility.
        :type is_hidden: bool, optional

        :param label: The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables.
        :type label: str, optional

        :param link: The URL of the custom link. URL must include ``http`` or ``https``. A relative URL must start with ``/``.
        :type link: str, optional

        :param override_label: The label ID that refers to a context menu link. Can be ``logs`` , ``hosts`` , ``traces`` , ``profiles`` , ``processes`` , ``containers`` , or ``rum``.
        :type override_label: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(WidgetCustomLink, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
