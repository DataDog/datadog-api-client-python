# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IFrameWidgetDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.i_frame_widget_definition_type import IFrameWidgetDefinitionType

        return {
            "type": (IFrameWidgetDefinitionType,),
            "url": (str,),
        }

    attribute_map = {
        "type": "type",
        "url": "url",
    }

    def __init__(self, type, url, *args, **kwargs):
        """
        The iframe widget allows you to embed a portion of any other web page on your dashboard. Only available on FREE layout dashboards.

        :param type: Type of the iframe widget.
        :type type: IFrameWidgetDefinitionType

        :param url: URL of the iframe.
        :type url: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.type = type
        self.url = url

    @classmethod
    def _from_openapi_data(cls, type, url, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IFrameWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.type = type
        self.url = url
        return self
