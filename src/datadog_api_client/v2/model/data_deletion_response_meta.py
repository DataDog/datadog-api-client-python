# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class DataDeletionResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "count_product": ({str: (int,)},),
            "count_status": ({str: (int,)},),
            "next_page": (str,),
            "product": (str,),
            "request_status": (str,),
        }

    attribute_map = {
        "count_product": "count_product",
        "count_status": "count_status",
        "next_page": "next_page",
        "product": "product",
        "request_status": "request_status",
    }

    def __init__(
        self_,
        count_product: Union[Dict[str, int], UnsetType] = unset,
        count_status: Union[Dict[str, int], UnsetType] = unset,
        next_page: Union[str, UnsetType] = unset,
        product: Union[str, UnsetType] = unset,
        request_status: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The metadata of the data deletion response.

        :param count_product: The total deletion requests created by product.
        :type count_product: {str: (int,)}, optional

        :param count_status: The total deletion requests created by status.
        :type count_status: {str: (int,)}, optional

        :param next_page: The next page when searching deletion requests created in the current organization.
        :type next_page: str, optional

        :param product: The product of the deletion request.
        :type product: str, optional

        :param request_status: The status of the executed request.
        :type request_status: str, optional
        """
        if count_product is not unset:
            kwargs["count_product"] = count_product
        if count_status is not unset:
            kwargs["count_status"] = count_status
        if next_page is not unset:
            kwargs["next_page"] = next_page
        if product is not unset:
            kwargs["product"] = product
        if request_status is not unset:
            kwargs["request_status"] = request_status
        super().__init__(kwargs)
