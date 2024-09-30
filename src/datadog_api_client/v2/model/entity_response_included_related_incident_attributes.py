# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class EntityResponseIncludedRelatedIncidentAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "html_url": (str,),
            "provider": (str,),
            "status": (str,),
            "title": (str,),
        }

    attribute_map = {
        "created_at": "createdAt",
        "html_url": "htmlURL",
        "provider": "provider",
        "status": "status",
        "title": "title",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        html_url: Union[str, UnsetType] = unset,
        provider: Union[str, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Incident attributes.

        :param created_at: Incident creation time.
        :type created_at: datetime, optional

        :param html_url: Incident URL.
        :type html_url: str, optional

        :param provider: Incident provider.
        :type provider: str, optional

        :param status: Incident status.
        :type status: str, optional

        :param title: Incident title.
        :type title: str, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if html_url is not unset:
            kwargs["html_url"] = html_url
        if provider is not unset:
            kwargs["provider"] = provider
        if status is not unset:
            kwargs["status"] = status
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)
