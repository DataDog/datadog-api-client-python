# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class NotebookMarkdownCellAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.notebook_markdown_cell_definition import NotebookMarkdownCellDefinition

        return {
            "definition": (NotebookMarkdownCellDefinition,),
        }

    attribute_map = {
        "definition": "definition",
    }

    def __init__(self, definition, *args, **kwargs):
        """
        The attributes of a notebook ``markdown`` cell.

        :param definition: Text in a notebook is formatted with `Markdown <https://daringfireball.net/projects/markdown/>`_ , which enables the use of headings, subheadings, links, images, lists, and code blocks.
        :type definition: NotebookMarkdownCellDefinition
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.definition = definition

    @classmethod
    def _from_openapi_data(cls, definition, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NotebookMarkdownCellAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.definition = definition
        return self
