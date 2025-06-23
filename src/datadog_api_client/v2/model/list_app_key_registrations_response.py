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
    from datadog_api_client.v2.model.app_key_registration_data import AppKeyRegistrationData
    from datadog_api_client.v2.model.list_app_key_registrations_response_meta import ListAppKeyRegistrationsResponseMeta


class ListAppKeyRegistrationsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.app_key_registration_data import AppKeyRegistrationData
        from datadog_api_client.v2.model.list_app_key_registrations_response_meta import (
            ListAppKeyRegistrationsResponseMeta,
        )

        return {
            "data": ([AppKeyRegistrationData],),
            "meta": (ListAppKeyRegistrationsResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[AppKeyRegistrationData], UnsetType] = unset,
        meta: Union[ListAppKeyRegistrationsResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        A paginated list of app key registrations.

        :param data: An array of app key registrations.
        :type data: [AppKeyRegistrationData], optional

        :param meta: The definition of ``ListAppKeyRegistrationsResponseMeta`` object.
        :type meta: ListAppKeyRegistrationsResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
