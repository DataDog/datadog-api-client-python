# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.custom_destination_attribute_tags_restriction_list_type import (
        CustomDestinationAttributeTagsRestrictionListType,
    )
    from datadog_api_client.v2.model.custom_destination_forward_destination import CustomDestinationForwardDestination
    from datadog_api_client.v2.model.custom_destination_forward_destination_http import (
        CustomDestinationForwardDestinationHttp,
    )
    from datadog_api_client.v2.model.custom_destination_forward_destination_splunk import (
        CustomDestinationForwardDestinationSplunk,
    )
    from datadog_api_client.v2.model.custom_destination_forward_destination_elasticsearch import (
        CustomDestinationForwardDestinationElasticsearch,
    )


class CustomDestinationUpdateRequestAttributes(ModelNormal):
    validations = {
        "forward_tags_restriction_list": {
            "max_items": 10,
            "min_items": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_destination_attribute_tags_restriction_list_type import (
            CustomDestinationAttributeTagsRestrictionListType,
        )
        from datadog_api_client.v2.model.custom_destination_forward_destination import (
            CustomDestinationForwardDestination,
        )

        return {
            "enabled": (bool,),
            "forward_tags": (bool,),
            "forward_tags_restriction_list": ([str],),
            "forward_tags_restriction_list_type": (CustomDestinationAttributeTagsRestrictionListType,),
            "forwarder_destination": (CustomDestinationForwardDestination,),
            "name": (str,),
            "query": (str,),
        }

    attribute_map = {
        "enabled": "enabled",
        "forward_tags": "forward_tags",
        "forward_tags_restriction_list": "forward_tags_restriction_list",
        "forward_tags_restriction_list_type": "forward_tags_restriction_list_type",
        "forwarder_destination": "forwarder_destination",
        "name": "name",
        "query": "query",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        forward_tags: Union[bool, UnsetType] = unset,
        forward_tags_restriction_list: Union[List[str], UnsetType] = unset,
        forward_tags_restriction_list_type: Union[CustomDestinationAttributeTagsRestrictionListType, UnsetType] = unset,
        forwarder_destination: Union[
            CustomDestinationForwardDestination,
            CustomDestinationForwardDestinationHttp,
            CustomDestinationForwardDestinationSplunk,
            CustomDestinationForwardDestinationElasticsearch,
            UnsetType,
        ] = unset,
        name: Union[str, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes associated with the custom destination.

        :param enabled: Whether logs matching this custom destination should be forwarded or not.
        :type enabled: bool, optional

        :param forward_tags: Whether tags from the forwarded logs should be forwarded or not.
        :type forward_tags: bool, optional

        :param forward_tags_restriction_list: List of `keys of tags <https://docs.datadoghq.com/getting_started/tagging/#define-tags>`_ to be restricted from being forwarded.
            An empty list represents no restriction is in place and either all or no tags will be forwarded depending on ``forward_tags_restriction_list_type`` parameter.
        :type forward_tags_restriction_list: [str], optional

        :param forward_tags_restriction_list_type: How ``forward_tags_restriction_list`` parameter should be interpreted.
            If ``ALLOW_LIST`` , then only tags whose keys on the forwarded logs match the ones on the restriction list
            are forwarded.

            ``BLOCK_LIST`` works the opposite way. It does not forward the tags matching the ones on the list.
        :type forward_tags_restriction_list_type: CustomDestinationAttributeTagsRestrictionListType, optional

        :param forwarder_destination: A custom destination's location to forward logs.
        :type forwarder_destination: CustomDestinationForwardDestination, optional

        :param name: The custom destination name.
        :type name: str, optional

        :param query: The custom destination query and filter. Logs matching this query are forwarded to the destination.
        :type query: str, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if forward_tags is not unset:
            kwargs["forward_tags"] = forward_tags
        if forward_tags_restriction_list is not unset:
            kwargs["forward_tags_restriction_list"] = forward_tags_restriction_list
        if forward_tags_restriction_list_type is not unset:
            kwargs["forward_tags_restriction_list_type"] = forward_tags_restriction_list_type
        if forwarder_destination is not unset:
            kwargs["forwarder_destination"] = forwarder_destination
        if name is not unset:
            kwargs["name"] = name
        if query is not unset:
            kwargs["query"] = query
        super().__init__(kwargs)
