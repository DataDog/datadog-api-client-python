# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class NotebookCellUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.notebook_cell_update_request_attributes import (
            NotebookCellUpdateRequestAttributes,
        )
        from datadog_api_client.v1.model.notebook_cell_resource_type import NotebookCellResourceType

        return {
            "attributes": (NotebookCellUpdateRequestAttributes,),
            "id": (str,),
            "type": (NotebookCellResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self, attributes, id, type, *args, **kwargs):
        """
        The description of a notebook cell update request.

        :param attributes: The attributes of a notebook cell in update cell request. Valid cell types are ``markdown`` , ``timeseries`` , ``toplist`` , ``heatmap`` , ``distribution`` ,
            ``log_stream``. `More information on each graph visualization type. <https://docs.datadoghq.com/dashboards/widgets/>`_
        :type attributes: NotebookCellUpdateRequestAttributes

        :param id: Notebook cell ID.
        :type id: str

        :param type: Type of the Notebook Cell resource.
        :type type: NotebookCellResourceType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.id = id
        self.type = type

    @classmethod
    def _from_openapi_data(cls, attributes, id, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NotebookCellUpdateRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.id = id
        self.type = type
        return self
