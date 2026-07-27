# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class TopologyMapWidgetDefinition(ModelComposed):
    def __init__(self, **kwargs):
        """
        This widget displays a topology of nodes and edges for different data sources. It replaces the service map widget.

        :param custom_links: List of custom links.
        :type custom_links: [WidgetCustomLink], optional

        :param description: The description of the widget.
        :type description: str, optional

        :param requests: One Topology request.
        :type requests: [TopologyRequestDataStreams]

        :param time: Time setting for the widget.
        :type time: WidgetTime, optional

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

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v1.model.topology_map_widget_definition_data_streams import (
            TopologyMapWidgetDefinitionDataStreams,
        )
        from datadog_api_client.v1.model.topology_map_widget_definition_service_map import (
            TopologyMapWidgetDefinitionServiceMap,
        )

        return {
            "oneOf": [
                TopologyMapWidgetDefinitionDataStreams,
                TopologyMapWidgetDefinitionServiceMap,
            ],
        }
