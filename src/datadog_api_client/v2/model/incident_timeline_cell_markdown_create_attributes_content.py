# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentTimelineCellMarkdownCreateAttributesContent(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "content": (str,),
        }

    attribute_map = {
        "content": "content",
    }

    def __init__(self_, *args, **kwargs):
        """
        The Markdown timeline cell contents.

        :param content: The Markdown content of the cell.
        :type content: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
