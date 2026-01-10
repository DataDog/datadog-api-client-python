# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v1.model.tag_to_hosts import TagToHosts
from datadog_api_client.v1.model.host_tags import HostTags


class TagsApi:
    """
    The tag endpoint allows you to assign tags to hosts,
    for example: ``role:database``. Those tags are applied to
    all metrics sent by the host. Refer to hosts by name
    ( ``yourhost.example.com`` ) when fetching and applying
    tags to a particular host.

    The component of your infrastructure responsible for a tag is identified
    by a source. For example, some valid sources include nagios, hudson, jenkins,
    users, feed, chef, puppet, git, bitbucket, fabric, capistrano, etc. Find a complete list of source type names under `API Source Attributes <https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value>`_.

    Read more about tags on `Getting Started with Tags <https://docs.datadoghq.com/getting_started/tagging/>`_.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_host_tags_endpoint = _Endpoint(
            settings={
                "response_type": (HostTags,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/tags/hosts/{host_name}",
                "operation_id": "create_host_tags",
                "http_method": "POST",
                "version": "v1",
            },
            params_map={
                "host_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "host_name",
                    "location": "path",
                },
                "source": {
                    "openapi_types": (str,),
                    "attribute": "source",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (HostTags,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_host_tags_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/tags/hosts/{host_name}",
                "operation_id": "delete_host_tags",
                "http_method": "DELETE",
                "version": "v1",
            },
            params_map={
                "host_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "host_name",
                    "location": "path",
                },
                "source": {
                    "openapi_types": (str,),
                    "attribute": "source",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_host_tags_endpoint = _Endpoint(
            settings={
                "response_type": (HostTags,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/tags/hosts/{host_name}",
                "operation_id": "get_host_tags",
                "http_method": "GET",
                "version": "v1",
            },
            params_map={
                "host_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "host_name",
                    "location": "path",
                },
                "source": {
                    "openapi_types": (str,),
                    "attribute": "source",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_host_tags_endpoint = _Endpoint(
            settings={
                "response_type": (TagToHosts,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/tags/hosts",
                "operation_id": "list_host_tags",
                "http_method": "GET",
                "version": "v1",
            },
            params_map={
                "source": {
                    "openapi_types": (str,),
                    "attribute": "source",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_host_tags_endpoint = _Endpoint(
            settings={
                "response_type": (HostTags,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/tags/hosts/{host_name}",
                "operation_id": "update_host_tags",
                "http_method": "PUT",
                "version": "v1",
            },
            params_map={
                "host_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "host_name",
                    "location": "path",
                },
                "source": {
                    "openapi_types": (str,),
                    "attribute": "source",
                    "location": "query",
                },
                "body": {
                    "required": True,
                    "openapi_types": (HostTags,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_host_tags(
        self,
        host_name: str,
        body: HostTags,
        *,
        source: Union[str, UnsetType] = unset,
    ) -> HostTags:
        """Add tags to a host.

        This endpoint allows you to add new tags to a host,
        optionally specifying what source these tags come from. If tags already exist, appends new tags to the tag list. If no source is specified, defaults to "user".

        :param host_name: Specified host name to add new tags
        :type host_name: str
        :param body: Update host tags request body.
        :type body: HostTags
        :param source: Source to add tags. `Complete list of source attribute values <https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value>`_. Use "user" source for custom-defined tags. If no source is specified, defaults to "user".
        :type source: str, optional
        :rtype: HostTags
        """
        kwargs: Dict[str, Any] = {}
        kwargs["host_name"] = host_name

        if source is not unset:
            kwargs["source"] = source

        kwargs["body"] = body

        return self._create_host_tags_endpoint.call_with_http_info(**kwargs)

    def delete_host_tags(
        self,
        host_name: str,
        *,
        source: Union[str, UnsetType] = unset,
    ) -> None:
        """Remove host tags.

        This endpoint allows you to remove all tags
        for a single host. If no source is specified, only deletes from the source "User".

        :param host_name: Specified host name to delete tags
        :type host_name: str
        :param source: Source of the tags to be deleted. `Complete list of source attribute values <https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value>`_. Use "user" source for custom-defined tags.
        :type source: str, optional
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["host_name"] = host_name

        if source is not unset:
            kwargs["source"] = source

        return self._delete_host_tags_endpoint.call_with_http_info(**kwargs)

    def get_host_tags(
        self,
        host_name: str,
        *,
        source: Union[str, UnsetType] = unset,
    ) -> HostTags:
        """Get Host Tags.

        Return the list of tags that apply to a given host.

        :param host_name: Name of the host to retrieve tags for
        :type host_name: str
        :param source: Source to filter. `Complete list of source attribute values <https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value>`_. Use "user" source for custom-defined tags.
        :type source: str, optional
        :rtype: HostTags
        """
        kwargs: Dict[str, Any] = {}
        kwargs["host_name"] = host_name

        if source is not unset:
            kwargs["source"] = source

        return self._get_host_tags_endpoint.call_with_http_info(**kwargs)

    def list_host_tags(
        self,
        *,
        source: Union[str, UnsetType] = unset,
    ) -> TagToHosts:
        """Get All Host Tags.

        Returns a mapping of tags to hosts. For each tag, the response returns a list of host names that contain this tag. There is a restriction of 10k total host names from the org that can be attached to tags and returned.

        :param source: Source to filter. `Complete list of source attribute values <https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value>`_. Use "user" source for custom-defined tags.
        :type source: str, optional
        :rtype: TagToHosts
        """
        kwargs: Dict[str, Any] = {}
        if source is not unset:
            kwargs["source"] = source

        return self._list_host_tags_endpoint.call_with_http_info(**kwargs)

    def update_host_tags(
        self,
        host_name: str,
        body: HostTags,
        *,
        source: Union[str, UnsetType] = unset,
    ) -> HostTags:
        """Update host tags.

        This endpoint allows you to update/replace all tags in
        an integration source with those supplied in the request.

        :param host_name: Specified host name to change tags
        :type host_name: str
        :param body: Add tags to host
        :type body: HostTags
        :param source: Source to update tags. `Complete list of source attribute values <https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value>`_. Use "user" source for custom-defined tags. If no source specified, defaults to "user".
        :type source: str, optional
        :rtype: HostTags
        """
        kwargs: Dict[str, Any] = {}
        kwargs["host_name"] = host_name

        if source is not unset:
            kwargs["source"] = source

        kwargs["body"] = body

        return self._update_host_tags_endpoint.call_with_http_info(**kwargs)
