# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SLOListWidgetDefinition(ModelNormal):
    validations = {
        "requests": {
            "max_items": 1,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_list_widget_request import SLOListWidgetRequest
        from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1.model.slo_list_widget_definition_type import SLOListWidgetDefinitionType

        return {
            "requests": ([SLOListWidgetRequest],),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (SLOListWidgetDefinitionType,),
        }

    attribute_map = {
        "requests": "requests",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(self_, requests, type, *args, **kwargs):
        """
        Use the SLO List widget to track your SLOs (Service Level Objectives) on dashboards.

        :param requests: Array of one request object to display in the widget.
        :type requests: [SLOListWidgetRequest]

        :param title: Title of the widget.
        :type title: str, optional

        :param title_align: How to align the text on the widget.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional

        :param type: Type of the SLO List widget.
        :type type: SLOListWidgetDefinitionType
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.requests = requests
        self_.type = type