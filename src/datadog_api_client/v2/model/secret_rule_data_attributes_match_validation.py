# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.secret_rule_data_attributes_match_validation_invalid_http_status_code_items import (
        SecretRuleDataAttributesMatchValidationInvalidHttpStatusCodeItems,
    )
    from datadog_api_client.v2.model.secret_rule_data_attributes_match_validation_valid_http_status_code_items import (
        SecretRuleDataAttributesMatchValidationValidHttpStatusCodeItems,
    )


class SecretRuleDataAttributesMatchValidation(ModelNormal):
    validations = {
        "timeout_seconds": {
            "inclusive_maximum": 1.8446744073709552e19,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.secret_rule_data_attributes_match_validation_invalid_http_status_code_items import (
            SecretRuleDataAttributesMatchValidationInvalidHttpStatusCodeItems,
        )
        from datadog_api_client.v2.model.secret_rule_data_attributes_match_validation_valid_http_status_code_items import (
            SecretRuleDataAttributesMatchValidationValidHttpStatusCodeItems,
        )

        return {
            "endpoint": (str,),
            "hosts": ([str],),
            "http_method": (str,),
            "invalid_http_status_code": ([SecretRuleDataAttributesMatchValidationInvalidHttpStatusCodeItems],),
            "request_headers": ({str: (str,)},),
            "timeout_seconds": (int,),
            "type": (str,),
            "valid_http_status_code": ([SecretRuleDataAttributesMatchValidationValidHttpStatusCodeItems],),
        }

    attribute_map = {
        "endpoint": "endpoint",
        "hosts": "hosts",
        "http_method": "http_method",
        "invalid_http_status_code": "invalid_http_status_code",
        "request_headers": "request_headers",
        "timeout_seconds": "timeout_seconds",
        "type": "type",
        "valid_http_status_code": "valid_http_status_code",
    }

    def __init__(
        self_,
        endpoint: Union[str, UnsetType] = unset,
        hosts: Union[List[str], UnsetType] = unset,
        http_method: Union[str, UnsetType] = unset,
        invalid_http_status_code: Union[
            List[SecretRuleDataAttributesMatchValidationInvalidHttpStatusCodeItems], UnsetType
        ] = unset,
        request_headers: Union[Dict[str, str], UnsetType] = unset,
        timeout_seconds: Union[int, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        valid_http_status_code: Union[
            List[SecretRuleDataAttributesMatchValidationValidHttpStatusCodeItems], UnsetType
        ] = unset,
        **kwargs,
    ):
        """


        :param endpoint:
        :type endpoint: str, optional

        :param hosts:
        :type hosts: [str], optional

        :param http_method:
        :type http_method: str, optional

        :param invalid_http_status_code:
        :type invalid_http_status_code: [SecretRuleDataAttributesMatchValidationInvalidHttpStatusCodeItems], optional

        :param request_headers:
        :type request_headers: {str: (str,)}, optional

        :param timeout_seconds:
        :type timeout_seconds: int, optional

        :param type:
        :type type: str, optional

        :param valid_http_status_code:
        :type valid_http_status_code: [SecretRuleDataAttributesMatchValidationValidHttpStatusCodeItems], optional
        """
        if endpoint is not unset:
            kwargs["endpoint"] = endpoint
        if hosts is not unset:
            kwargs["hosts"] = hosts
        if http_method is not unset:
            kwargs["http_method"] = http_method
        if invalid_http_status_code is not unset:
            kwargs["invalid_http_status_code"] = invalid_http_status_code
        if request_headers is not unset:
            kwargs["request_headers"] = request_headers
        if timeout_seconds is not unset:
            kwargs["timeout_seconds"] = timeout_seconds
        if type is not unset:
            kwargs["type"] = type
        if valid_http_status_code is not unset:
            kwargs["valid_http_status_code"] = valid_http_status_code
        super().__init__(kwargs)
