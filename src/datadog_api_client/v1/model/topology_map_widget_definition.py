# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class TopologyMapWidgetDefinition(ModelNormal):
    validations = {
        "requests": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1.model.topology_request import TopologyRequest
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.topology_map_widget_definition_type import TopologyMapWidgetDefinitionType

        return {
            "custom_links": ([WidgetCustomLink],),
            "requests": ([TopologyRequest],),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (TopologyMapWidgetDefinitionType,),
        }

    attribute_map = {
        "custom_links": "custom_links",
        "requests": "requests",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(self_, requests, type, *args, **kwargs):
        """
        This widget displays a topology of nodes and edges for different data sources. It replaces the service map widget.

        :param custom_links: List of custom links.
        :type custom_links: [WidgetCustomLink], optional

        :param requests: One or more Topology requests.
        :type requests: [TopologyRequest]

        :param title: Title of your widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional

        :param type: Type of the topology map widget.
        :type type: TopologyMapWidgetDefinitionType
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.requests = requests
        self_.type = type
