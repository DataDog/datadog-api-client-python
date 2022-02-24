# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.notebooks_response_data_attributes import NotebooksResponseDataAttributes
    from datadog_api_client.v1.model.notebook_resource_type import NotebookResourceType

    globals()["NotebooksResponseDataAttributes"] = NotebooksResponseDataAttributes
    globals()["NotebookResourceType"] = NotebookResourceType


class NotebooksResponseData(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "attributes": (NotebooksResponseDataAttributes,),
            "id": (int,),
            "type": (NotebookResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    read_only_vars = {
        "id",
    }

    def __init__(self, attributes, id, type, *args, **kwargs):
        """
        The data for a notebook in get all response.

        :param attributes: The attributes of a notebook in get all response.
        :type attributes: NotebooksResponseDataAttributes

        :param id: Unique notebook ID, assigned when you create the notebook.
        :type id: int

        :param type: Type of the Notebook resource.
        :type type: NotebookResourceType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.id = id
        self.type = type

    @classmethod
    def _from_openapi_data(cls, attributes, id, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NotebooksResponseData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.id = id
        self.type = type
        return self
