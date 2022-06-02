# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class TreeMapWidgetDefinition(ModelNormal):
    validations = {
        "requests": {
            "max_items": 1,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.tree_map_color_by import TreeMapColorBy
        from datadog_api_client.v1.model.tree_map_group_by import TreeMapGroupBy
        from datadog_api_client.v1.model.tree_map_widget_request import TreeMapWidgetRequest
        from datadog_api_client.v1.model.tree_map_size_by import TreeMapSizeBy
        from datadog_api_client.v1.model.tree_map_widget_definition_type import TreeMapWidgetDefinitionType

        return {
            "color_by": (TreeMapColorBy,),
            "group_by": (TreeMapGroupBy,),
            "requests": ([TreeMapWidgetRequest],),
            "size_by": (TreeMapSizeBy,),
            "title": (str,),
            "type": (TreeMapWidgetDefinitionType,),
        }

    attribute_map = {
        "color_by": "color_by",
        "group_by": "group_by",
        "requests": "requests",
        "size_by": "size_by",
        "title": "title",
        "type": "type",
    }

    def __init__(self, requests, type, *args, **kwargs):
        """
        The treemap visualization found on the Host Dashboards comes from the output of ``ps auxww``. This is not continuously run on your hosts. Instead, it’s run once on Agent start/restart. The treemap is only supported for process data on a single host dashboard — this may not be reused in other dashboards or for other metrics.

        :param color_by: The attribute used to determine color in the widget.
        :type color_by: TreeMapColorBy, optional

        :param group_by: The attribute used to group elements in the widget.
        :type group_by: TreeMapGroupBy, optional

        :param requests: List of top list widget requests.
        :type requests: [TreeMapWidgetRequest]

        :param size_by: The attribute used to determine size in the widget.
        :type size_by: TreeMapSizeBy, optional

        :param title: Title of your widget.
        :type title: str, optional

        :param type: Type of the treemap widget.
        :type type: TreeMapWidgetDefinitionType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.type = type

    @classmethod
    def _from_openapi_data(cls, requests, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(TreeMapWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.type = type
        return self
