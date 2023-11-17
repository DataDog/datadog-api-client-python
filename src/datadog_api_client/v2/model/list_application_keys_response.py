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
    from datadog_api_client.v2.model.partial_application_key import PartialApplicationKey
    from datadog_api_client.v2.model.application_key_response_included_item import ApplicationKeyResponseIncludedItem
    from datadog_api_client.v2.model.application_key_response_meta import ApplicationKeyResponseMeta
    from datadog_api_client.v2.model.user import User
    from datadog_api_client.v2.model.role import Role


class ListApplicationKeysResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.partial_application_key import PartialApplicationKey
        from datadog_api_client.v2.model.application_key_response_included_item import (
            ApplicationKeyResponseIncludedItem,
        )
        from datadog_api_client.v2.model.application_key_response_meta import ApplicationKeyResponseMeta

        return {
            "data": ([PartialApplicationKey],),
            "included": ([ApplicationKeyResponseIncludedItem],),
            "meta": (ApplicationKeyResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[PartialApplicationKey], UnsetType] = unset,
        included: Union[List[Union[ApplicationKeyResponseIncludedItem, User, Role]], UnsetType] = unset,
        meta: Union[ApplicationKeyResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response for a list of application keys.

        :param data: Array of application keys.
        :type data: [PartialApplicationKey], optional

        :param included: Array of objects related to the application key.
        :type included: [ApplicationKeyResponseIncludedItem], optional

        :param meta: Additional information related to the application key response.
        :type meta: ApplicationKeyResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
