# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.notebook_markdown_cell_definition_type import NotebookMarkdownCellDefinitionType

    globals()["NotebookMarkdownCellDefinitionType"] = NotebookMarkdownCellDefinitionType


class NotebookMarkdownCellDefinition(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "text": (str,),
            "type": (NotebookMarkdownCellDefinitionType,),
        }

    attribute_map = {
        "text": "text",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, text, type, *args, **kwargs):
        """
        Text in a notebook is formatted with [Markdown](https://daringfireball.net/projects/markdown/), which enables the use of headings, subheadings, links, images, lists, and code blocks.

        :param text: The markdown content.
        :type text: str

        :param type: Type of the markdown cell.
        :type type: NotebookMarkdownCellDefinitionType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.text = text
        self.type = type

    @classmethod
    def _from_openapi_data(cls, text, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NotebookMarkdownCellDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.text = text
        self.type = type
        return self
