# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.notebook_resource_type import NotebookResourceType
    from datadog_api_client.v1.model.notebook_response_data_attributes import NotebookResponseDataAttributes

    globals()["NotebookResourceType"] = NotebookResourceType
    globals()["NotebookResponseDataAttributes"] = NotebookResponseDataAttributes


class NotebookResponseData(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "attributes": (NotebookResponseDataAttributes,),
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

    def __init__(self, attributes, type, *args, **kwargs):
        """NotebookResponseData - a model defined in OpenAPI

        Args:
            attributes (NotebookResponseDataAttributes):
            type (NotebookResourceType):

        Keyword Args:
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.type = type

    @classmethod
    def _from_openapi_data(cls, attributes, id, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NotebookResponseData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.id = id
        self.type = type
        return self
