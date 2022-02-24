# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.notebook_cell_create_request_attributes import NotebookCellCreateRequestAttributes
    from datadog_api_client.v1.model.notebook_cell_resource_type import NotebookCellResourceType

    globals()["NotebookCellCreateRequestAttributes"] = NotebookCellCreateRequestAttributes
    globals()["NotebookCellResourceType"] = NotebookCellResourceType


class NotebookCellCreateRequest(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "attributes": (NotebookCellCreateRequestAttributes,),
            "type": (NotebookCellResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, attributes, type, *args, **kwargs):
        """
        The description of a notebook cell create request.

        :param attributes: The attributes of a notebook cell in create cell request. Valid cell types are `markdown`, `timeseries`, `toplist`, `heatmap`, `distribution`,
            `log_stream`. [More information on each graph visualization type.](https://docs.datadoghq.com/dashboards/widgets/)
        :type attributes: NotebookCellCreateRequestAttributes

        :param type: Type of the Notebook Cell resource.
        :type type: NotebookCellResourceType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.type = type

    @classmethod
    def _from_openapi_data(cls, attributes, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NotebookCellCreateRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.type = type
        return self
