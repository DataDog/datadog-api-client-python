# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.service_map_widget_definition_type import ServiceMapWidgetDefinitionType
    from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

    globals()["ServiceMapWidgetDefinitionType"] = ServiceMapWidgetDefinitionType
    globals()["WidgetCustomLink"] = WidgetCustomLink
    globals()["WidgetTextAlign"] = WidgetTextAlign


class ServiceMapWidgetDefinition(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {
        "filters": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "custom_links": ([WidgetCustomLink],),
            "filters": ([str],),
            "service": (str,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (ServiceMapWidgetDefinitionType,),
        }

    attribute_map = {
        "filters": "filters",
        "service": "service",
        "type": "type",
        "custom_links": "custom_links",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
    }

    read_only_vars = {}

    def __init__(self, filters, service, type, *args, **kwargs):
        """ServiceMapWidgetDefinition - a model defined in OpenAPI


        :param filters: Your environment and primary tag (or * if enabled for your account).
        :type filters: [str]

        :param service: The ID of the service you want to map.
        :type service: str

        :type type: ServiceMapWidgetDefinitionType

        :param custom_links: List of custom links.
        :type custom_links: [WidgetCustomLink], optional

        :param title: The title of your widget.
        :type title: str, optional

        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.filters = filters
        self.service = service
        self.type = type

    @classmethod
    def _from_openapi_data(cls, filters, service, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ServiceMapWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.filters = filters
        self.service = service
        self.type = type
        return self
