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
    from datadog_api_client.v2.model.sensitive_data_scanner_filter import SensitiveDataScannerFilter
    from datadog_api_client.v2.model.sensitive_data_scanner_product import SensitiveDataScannerProduct
    from datadog_api_client.v2.model.sensitive_data_scanner_samplings import SensitiveDataScannerSamplings


class SensitiveDataScannerGroupAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sensitive_data_scanner_filter import SensitiveDataScannerFilter
        from datadog_api_client.v2.model.sensitive_data_scanner_product import SensitiveDataScannerProduct
        from datadog_api_client.v2.model.sensitive_data_scanner_samplings import SensitiveDataScannerSamplings

        return {
            "description": (str,),
            "filter": (SensitiveDataScannerFilter,),
            "is_enabled": (bool,),
            "name": (str,),
            "product_list": ([SensitiveDataScannerProduct],),
            "samplings": ([SensitiveDataScannerSamplings],),
        }

    attribute_map = {
        "description": "description",
        "filter": "filter",
        "is_enabled": "is_enabled",
        "name": "name",
        "product_list": "product_list",
        "samplings": "samplings",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        filter: Union[SensitiveDataScannerFilter, UnsetType] = unset,
        is_enabled: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        product_list: Union[List[SensitiveDataScannerProduct], UnsetType] = unset,
        samplings: Union[List[SensitiveDataScannerSamplings], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the Sensitive Data Scanner group.

        :param description: Description of the group.
        :type description: str, optional

        :param filter: Filter for the Scanning Group.
        :type filter: SensitiveDataScannerFilter, optional

        :param is_enabled: Whether or not the group is enabled.
        :type is_enabled: bool, optional

        :param name: Name of the group.
        :type name: str, optional

        :param product_list: List of products the scanning group applies.
        :type product_list: [SensitiveDataScannerProduct], optional

        :param samplings: List of sampling rates per product type.
        :type samplings: [SensitiveDataScannerSamplings], optional
        """
        if description is not unset:
            kwargs["description"] = description
        if filter is not unset:
            kwargs["filter"] = filter
        if is_enabled is not unset:
            kwargs["is_enabled"] = is_enabled
        if name is not unset:
            kwargs["name"] = name
        if product_list is not unset:
            kwargs["product_list"] = product_list
        if samplings is not unset:
            kwargs["samplings"] = samplings
        super().__init__(kwargs)
