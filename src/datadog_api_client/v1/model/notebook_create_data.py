# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.notebook_create_data_attributes import NotebookCreateDataAttributes
    from datadog_api_client.v1.model.notebook_resource_type import NotebookResourceType

    globals()["NotebookCreateDataAttributes"] = NotebookCreateDataAttributes
    globals()["NotebookResourceType"] = NotebookResourceType


class NotebookCreateData(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "attributes": (NotebookCreateDataAttributes,),
            "type": (NotebookResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, attributes, type, *args, **kwargs):
        """
        The data for a notebook create request.

        :param attributes: The data attributes of a notebook.
        :type attributes: NotebookCreateDataAttributes

        :param type: Type of the Notebook resource.
        :type type: NotebookResourceType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.type = type

    @classmethod
    def _from_openapi_data(cls, attributes, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NotebookCreateData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.type = type
        return self
