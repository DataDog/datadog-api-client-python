# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.links_described_by import LinksDescribedBy
    from datadog_api_client.v2.model.links_first import LinksFirst
    from datadog_api_client.v2.model.links_last import LinksLast
    from datadog_api_client.v2.model.links_next import LinksNext
    from datadog_api_client.v2.model.links_prev import LinksPrev
    from datadog_api_client.v2.model.links_related import LinksRelated
    from datadog_api_client.v2.model.links_self import LinksSelf
    from datadog_api_client.v2.model.link_object import LinkObject


class WidgetLinks(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.links_described_by import LinksDescribedBy
        from datadog_api_client.v2.model.links_first import LinksFirst
        from datadog_api_client.v2.model.links_last import LinksLast
        from datadog_api_client.v2.model.links_next import LinksNext
        from datadog_api_client.v2.model.links_prev import LinksPrev
        from datadog_api_client.v2.model.links_related import LinksRelated
        from datadog_api_client.v2.model.links_self import LinksSelf

        return {
            "described_by": (LinksDescribedBy,),
            "first": (LinksFirst,),
            "last": (LinksLast,),
            "next": (LinksNext,),
            "prev": (LinksPrev,),
            "related": (LinksRelated,),
            "self": (LinksSelf,),
        }

    attribute_map = {
        "described_by": "describedBy",
        "first": "first",
        "last": "last",
        "next": "next",
        "prev": "prev",
        "related": "related",
        "self": "self",
    }

    def __init__(
        self_,
        described_by: Union[Union[LinksDescribedBy, str, LinkObject], none_type, UnsetType] = unset,
        first: Union[Union[LinksFirst, str, LinkObject], none_type, UnsetType] = unset,
        last: Union[Union[LinksLast, str, LinkObject], none_type, UnsetType] = unset,
        next: Union[Union[LinksNext, str, LinkObject], none_type, UnsetType] = unset,
        prev: Union[Union[LinksPrev, str, LinkObject], none_type, UnsetType] = unset,
        related: Union[Union[LinksRelated, str, LinkObject], none_type, UnsetType] = unset,
        self: Union[Union[LinksSelf, str, LinkObject], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        A JSON:API "links" member
        See: https://jsonapi.org/format/#document-links

        :param described_by:
        :type described_by: LinksDescribedBy, none_type, optional

        :param first:
        :type first: LinksFirst, none_type, optional

        :param last:
        :type last: LinksLast, none_type, optional

        :param next:
        :type next: LinksNext, none_type, optional

        :param prev:
        :type prev: LinksPrev, none_type, optional

        :param related:
        :type related: LinksRelated, none_type, optional

        :param self:
        :type self: LinksSelf, none_type, optional
        """
        if described_by is not unset:
            kwargs["described_by"] = described_by
        if first is not unset:
            kwargs["first"] = first
        if last is not unset:
            kwargs["last"] = last
        if next is not unset:
            kwargs["next"] = next
        if prev is not unset:
            kwargs["prev"] = prev
        if related is not unset:
            kwargs["related"] = related
        if self is not unset:
            kwargs["self"] = self
        super().__init__(kwargs)
