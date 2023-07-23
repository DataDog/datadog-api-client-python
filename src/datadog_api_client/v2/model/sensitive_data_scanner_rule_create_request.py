# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.sensitive_data_scanner_rule_create import SensitiveDataScannerRuleCreate
    from datadog_api_client.v2.model.sensitive_data_scanner_meta_version_only import SensitiveDataScannerMetaVersionOnly
    from datadog_api_client.v2.model.sensitive_data_scanner_text_replacement import SensitiveDataScannerTextReplacement


@dataclass
class SensitiveDataScannerRuleCreateRequestJSON:
    description: Union[str, UnsetType] = unset
    excluded_namespaces: Union[List[str], UnsetType] = unset
    is_enabled: Union[bool, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    namespaces: Union[List[str], UnsetType] = unset
    pattern: Union[str, UnsetType] = unset
    tags: Union[List[str], UnsetType] = unset
    text_replacement: Union[SensitiveDataScannerTextReplacement, UnsetType] = unset
    group: Union[str, UnsetType] = unset
    standard_pattern: Union[str, UnsetType] = unset


class SensitiveDataScannerRuleCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sensitive_data_scanner_rule_create import SensitiveDataScannerRuleCreate
        from datadog_api_client.v2.model.sensitive_data_scanner_meta_version_only import (
            SensitiveDataScannerMetaVersionOnly,
        )

        return {
            "data": (SensitiveDataScannerRuleCreate,),
            "meta": (SensitiveDataScannerMetaVersionOnly,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }
    json_api_model = SensitiveDataScannerRuleCreateRequestJSON

    def __init__(self_, data: SensitiveDataScannerRuleCreate, meta: SensitiveDataScannerMetaVersionOnly, **kwargs):
        """
        Create rule request.

        :param data: Data related to the creation of a rule.
        :type data: SensitiveDataScannerRuleCreate

        :param meta: Meta payload containing information about the API.
        :type meta: SensitiveDataScannerMetaVersionOnly
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
