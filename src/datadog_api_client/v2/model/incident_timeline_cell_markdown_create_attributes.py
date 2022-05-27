# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentTimelineCellMarkdownCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_timeline_cell_markdown_content_type import (
            IncidentTimelineCellMarkdownContentType,
        )
        from datadog_api_client.v2.model.incident_timeline_cell_markdown_create_attributes_content import (
            IncidentTimelineCellMarkdownCreateAttributesContent,
        )

        return {
            "cell_type": (IncidentTimelineCellMarkdownContentType,),
            "content": (IncidentTimelineCellMarkdownCreateAttributesContent,),
            "important": (bool,),
        }

    attribute_map = {
        "cell_type": "cell_type",
        "content": "content",
        "important": "important",
    }

    def __init__(self, cell_type, content, *args, **kwargs):
        """
        Timeline cell data for Markdown timeline cells for a create request.

        :param cell_type: Type of the Markdown timeline cell.
        :type cell_type: IncidentTimelineCellMarkdownContentType

        :param content: The Markdown timeline cell contents.
        :type content: IncidentTimelineCellMarkdownCreateAttributesContent

        :param important: A flag indicating whether the timeline cell is important and should be highlighted.
        :type important: bool, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.cell_type = cell_type
        self.content = content

    @classmethod
    def _from_openapi_data(cls, cell_type, content, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IncidentTimelineCellMarkdownCreateAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.cell_type = cell_type
        self.content = content
        return self
