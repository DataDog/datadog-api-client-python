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
    from datadog_api_client.v2.model.rum_product_scales import RUMProductScales


class RUMApplicationListAttributes(ModelNormal):
    validations = {
        "org_id": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_product_scales import RUMProductScales

        return {
            "application_id": (str,),
            "created_at": (int,),
            "created_by_handle": (str,),
            "hash": (str,),
            "is_active": (bool,),
            "name": (str,),
            "org_id": (int,),
            "product_scales": (RUMProductScales,),
            "type": (str,),
            "updated_at": (int,),
            "updated_by_handle": (str,),
        }

    attribute_map = {
        "application_id": "application_id",
        "created_at": "created_at",
        "created_by_handle": "created_by_handle",
        "hash": "hash",
        "is_active": "is_active",
        "name": "name",
        "org_id": "org_id",
        "product_scales": "product_scales",
        "type": "type",
        "updated_at": "updated_at",
        "updated_by_handle": "updated_by_handle",
    }

    def __init__(
        self_,
        application_id: str,
        created_at: int,
        created_by_handle: str,
        name: str,
        org_id: int,
        type: str,
        updated_at: int,
        updated_by_handle: str,
        hash: Union[str, UnsetType] = unset,
        is_active: Union[bool, UnsetType] = unset,
        product_scales: Union[RUMProductScales, UnsetType] = unset,
        **kwargs,
    ):
        """
        RUM application list attributes.

        :param application_id: ID of the RUM application.
        :type application_id: str

        :param created_at: Timestamp in ms of the creation date.
        :type created_at: int

        :param created_by_handle: Handle of the creator user.
        :type created_by_handle: str

        :param hash: Hash of the RUM application. Optional.
        :type hash: str, optional

        :param is_active: Indicates if the RUM application is active.
        :type is_active: bool, optional

        :param name: Name of the RUM application.
        :type name: str

        :param org_id: Org ID of the RUM application.
        :type org_id: int

        :param product_scales: Product Scales configuration for the RUM application.
        :type product_scales: RUMProductScales, optional

        :param type: Type of the RUM application. Supported values are ``browser`` , ``ios`` , ``android`` , ``react-native`` , ``flutter`` , ``roku`` , ``electron`` , ``unity`` , ``kotlin-multiplatform``.
        :type type: str

        :param updated_at: Timestamp in ms of the last update date.
        :type updated_at: int

        :param updated_by_handle: Handle of the updater user.
        :type updated_by_handle: str
        """
        if hash is not unset:
            kwargs["hash"] = hash
        if is_active is not unset:
            kwargs["is_active"] = is_active
        if product_scales is not unset:
            kwargs["product_scales"] = product_scales
        super().__init__(kwargs)

        self_.application_id = application_id
        self_.created_at = created_at
        self_.created_by_handle = created_by_handle
        self_.name = name
        self_.org_id = org_id
        self_.type = type
        self_.updated_at = updated_at
        self_.updated_by_handle = updated_by_handle
