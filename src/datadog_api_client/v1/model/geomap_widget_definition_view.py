# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class GeomapWidgetDefinitionView(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "focus": (str,),
        }

    attribute_map = {
        "focus": "focus",
    }

    def __init__(self, focus, *args, **kwargs):
        """
        The view of the world that the map should render.

        :param focus: The 2-letter ISO code of a country to focus the map on. Or ``WORLD``.
        :type focus: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.focus = focus

    @classmethod
    def _from_openapi_data(cls, focus, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(GeomapWidgetDefinitionView, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.focus = focus
        return self
