# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.notebook_cell_resource_type import NotebookCellResourceType
    from datadog_api_client.v1.model.notebook_cell_update_request_attributes import NotebookCellUpdateRequestAttributes

    globals()["NotebookCellResourceType"] = NotebookCellResourceType
    globals()["NotebookCellUpdateRequestAttributes"] = NotebookCellUpdateRequestAttributes


class NotebookCellUpdateRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
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

    read_only_vars = {}

    def __init__(self, attributes, id, type, *args, **kwargs):
        """NotebookCellUpdateRequest - a model defined in OpenAPI

        Args:
            attributes (NotebookCellUpdateRequestAttributes):
            id (str): Notebook cell ID.
            type (NotebookCellResourceType):

        Keyword Args:
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
