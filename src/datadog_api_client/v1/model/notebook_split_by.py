# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class NotebookSplitBy(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "keys": ([str],),
            "tags": ([str],),
        }

    attribute_map = {
        "keys": "keys",
        "tags": "tags",
    }

    read_only_vars = {}

    def __init__(self, keys, tags, *args, **kwargs):
        """NotebookSplitBy - a model defined in OpenAPI

        Args:
            keys ([str]): Keys to split on.
            tags ([str]): Tags to split on.

        Keyword Args:
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.keys = keys
        self.tags = tags

    @classmethod
    def _from_openapi_data(cls, keys, tags, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NotebookSplitBy, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.keys = keys
        self.tags = tags
        return self
