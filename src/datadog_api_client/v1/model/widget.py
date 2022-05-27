# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class Widget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_definition import WidgetDefinition
        from datadog_api_client.v1.model.widget_layout import WidgetLayout

        return {
            "definition": (WidgetDefinition,),
            "id": (int,),
            "layout": (WidgetLayout,),
        }

    attribute_map = {
        "definition": "definition",
        "id": "id",
        "layout": "layout",
    }

    def __init__(self, definition, *args, **kwargs):
        """
        Information about widget.

        **Note** : The ``layout`` property is required for widgets in dashboards with ``free`` ``layout_type``.
              For the **new dashboard layout** , the ``layout`` property depends on the ``reflow_type`` of the dashboard.

        .. code-block::

             - If `reflow_type` is `fixed`, `layout` is required.
             - If `reflow_type` is `auto`, `layout` should not be set.

        :param definition: `Definition of the widget <https://docs.datadoghq.com/dashboards/widgets/>`_.
        :type definition: WidgetDefinition

        :param id: ID of the widget.
        :type id: int, optional

        :param layout: The layout for a widget on a ``free`` or **new dashboard layout** dashboard.
        :type layout: WidgetLayout, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.definition = definition

    @classmethod
    def _from_openapi_data(cls, definition, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(Widget, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.definition = definition
        return self
