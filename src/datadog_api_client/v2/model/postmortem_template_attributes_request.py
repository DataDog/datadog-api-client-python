# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.confluence_postmortem_settings import ConfluencePostmortemSettings
    from datadog_api_client.v2.model.google_docs_postmortem_settings import GoogleDocsPostmortemSettings
    from datadog_api_client.v2.model.postmortem_template_location import PostmortemTemplateLocation


class PostmortemTemplateAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.confluence_postmortem_settings import ConfluencePostmortemSettings
        from datadog_api_client.v2.model.google_docs_postmortem_settings import GoogleDocsPostmortemSettings
        from datadog_api_client.v2.model.postmortem_template_location import PostmortemTemplateLocation

        return {
            "confluence_postmortem_settings": (ConfluencePostmortemSettings,),
            "content": (str,),
            "google_docs_postmortem_settings": (GoogleDocsPostmortemSettings,),
            "is_default": (datetime, none_type),
            "location": (PostmortemTemplateLocation,),
            "name": (str,),
        }

    attribute_map = {
        "confluence_postmortem_settings": "confluence_postmortem_settings",
        "content": "content",
        "google_docs_postmortem_settings": "google_docs_postmortem_settings",
        "is_default": "is_default",
        "location": "location",
        "name": "name",
    }

    def __init__(
        self_,
        name: str,
        confluence_postmortem_settings: Union[ConfluencePostmortemSettings, UnsetType] = unset,
        content: Union[str, UnsetType] = unset,
        google_docs_postmortem_settings: Union[GoogleDocsPostmortemSettings, UnsetType] = unset,
        is_default: Union[datetime, none_type, UnsetType] = unset,
        location: Union[PostmortemTemplateLocation, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating or updating a postmortem template.

        :param confluence_postmortem_settings: Settings for a postmortem template stored in Confluence. Required when ``location`` is ``confluence``.
        :type confluence_postmortem_settings: ConfluencePostmortemSettings, optional

        :param content: The templated content of the postmortem, supporting Markdown and incident template variables.
        :type content: str, optional

        :param google_docs_postmortem_settings: Settings for a postmortem template stored in Google Docs. Required when ``location`` is ``google_docs``.
        :type google_docs_postmortem_settings: GoogleDocsPostmortemSettings, optional

        :param is_default: When set, marks this template as a default. The effective default for an incident type is the template with the most recent ``is_default`` timestamp. Set to ``null`` to unset.
        :type is_default: datetime, none_type, optional

        :param location: The location where the postmortem is created and stored.
        :type location: PostmortemTemplateLocation, optional

        :param name: The name of the template.
        :type name: str
        """
        if confluence_postmortem_settings is not unset:
            kwargs["confluence_postmortem_settings"] = confluence_postmortem_settings
        if content is not unset:
            kwargs["content"] = content
        if google_docs_postmortem_settings is not unset:
            kwargs["google_docs_postmortem_settings"] = google_docs_postmortem_settings
        if is_default is not unset:
            kwargs["is_default"] = is_default
        if location is not unset:
            kwargs["location"] = location
        super().__init__(kwargs)

        self_.name = name
