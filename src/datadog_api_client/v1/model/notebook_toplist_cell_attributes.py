# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
)


def lazy_import():
    from datadog_api_client.v1.model.notebook_cell_time import NotebookCellTime
    from datadog_api_client.v1.model.notebook_graph_size import NotebookGraphSize
    from datadog_api_client.v1.model.notebook_split_by import NotebookSplitBy
    from datadog_api_client.v1.model.toplist_widget_definition import ToplistWidgetDefinition

    globals()["NotebookCellTime"] = NotebookCellTime
    globals()["NotebookGraphSize"] = NotebookGraphSize
    globals()["NotebookSplitBy"] = NotebookSplitBy
    globals()["ToplistWidgetDefinition"] = ToplistWidgetDefinition


class NotebookToplistCellAttributes(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "definition": (ToplistWidgetDefinition,),
            "graph_size": (NotebookGraphSize,),
            "split_by": (NotebookSplitBy,),
            "time": (NotebookCellTime,),
        }

    attribute_map = {
        "definition": "definition",
        "graph_size": "graph_size",
        "split_by": "split_by",
        "time": "time",
    }

    read_only_vars = {}

    def __init__(self, definition, *args, **kwargs):
        """NotebookToplistCellAttributes - a model defined in OpenAPI

        Args:
            definition (ToplistWidgetDefinition):

        Keyword Args:
            graph_size (NotebookGraphSize): [optional]
            split_by (NotebookSplitBy): [optional]
            time (NotebookCellTime): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.definition = definition

    @classmethod
    def _from_openapi_data(cls, definition, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NotebookToplistCellAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.definition = definition
        return self
