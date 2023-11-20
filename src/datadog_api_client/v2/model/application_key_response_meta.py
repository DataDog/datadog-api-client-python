# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.application_key_response_meta_page import ApplicationKeyResponseMetaPage


class ApplicationKeyResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_key_response_meta_page import ApplicationKeyResponseMetaPage

        return {
            "max_allowed_per_user": (int,),
            "page": (ApplicationKeyResponseMetaPage,),
        }

    attribute_map = {
        "max_allowed_per_user": "max_allowed_per_user",
        "page": "page",
    }

    def __init__(
        self_,
        max_allowed_per_user: Union[int, UnsetType] = unset,
        page: Union[ApplicationKeyResponseMetaPage, UnsetType] = unset,
        **kwargs,
    ):
        """
        Additional information related to the application key response.

        :param max_allowed_per_user: Max allowed number of application keys per user.
        :type max_allowed_per_user: int, optional

        :param page: Additional information related to the application key response.
        :type page: ApplicationKeyResponseMetaPage, optional
        """
        if max_allowed_per_user is not unset:
            kwargs["max_allowed_per_user"] = max_allowed_per_user
        if page is not unset:
            kwargs["page"] = page
        super().__init__(kwargs)
