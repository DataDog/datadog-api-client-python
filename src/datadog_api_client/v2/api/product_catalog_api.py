# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    datetime,
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.product_catalog_sk_us_response import ProductCatalogSKUsResponse
from datadog_api_client.v2.model.product_catalog_sk_us_api_version import ProductCatalogSKUsAPIVersion


class ProductCatalogApi:
    """
    Look up the Datadog SKUs that are generally available, together with the public list
    prices, allotments, and tiered pricing that apply to them on a given date.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._list_product_catalog_sk_us_endpoint = _Endpoint(
            settings={
                "response_type": (ProductCatalogSKUsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/product-catalog/skus",
                "operation_id": "list_product_catalog_sk_us",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "version": {
                    "required": True,
                    "openapi_types": (ProductCatalogSKUsAPIVersion,),
                    "attribute": "version",
                    "location": "query",
                },
                "as_of_date": {
                    "openapi_types": (datetime,),
                    "attribute": "as_of_date",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def list_product_catalog_sk_us(
        self,
        version: ProductCatalogSKUsAPIVersion,
        *,
        as_of_date: Union[datetime, UnsetType] = unset,
    ) -> ProductCatalogSKUsResponse:
        """List SKUs.

        Get every generally available Datadog SKU, with the pricing and allotment metadata that
        applies to it, for the Datadog site serving the request. A SKU is generally available
        when it is billed through a metered commitment or through automatic billing; SKUs in any
        other phase are not returned.

        Prices, allotments, and pricing tiers are returned as they were in effect on
        ``as_of_date`` , which defaults to the date of the request. Prices are public list prices:
        they do not reflect discounts, commitments, or negotiated rates on an account.

        Each SKU is a separate resource in ``data`` , identified by its SKU code, and sorted by
        that code in ascending order. The whole catalog is returned in a single response, so
        this endpoint is not paginated.

        :param version: The version of the product catalog contract to return. ``v1`` is the latest.
        :type version: ProductCatalogSKUsAPIVersion
        :param as_of_date: The date the returned prices, allotments, and pricing tiers are effective as of, in
            ``YYYY-MM-DD`` format. Defaults to the date of the request, and must not be later
            than it.
        :type as_of_date: datetime, optional
        :rtype: ProductCatalogSKUsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["version"] = version

        if as_of_date is not unset:
            kwargs["as_of_date"] = as_of_date

        return self._list_product_catalog_sk_us_endpoint.call_with_http_info(**kwargs)
