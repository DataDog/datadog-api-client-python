# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ci_app_ci_error_domain import CIAppCIErrorDomain


class CIAppCIError(ModelNormal):
    validations = {
        "message": {
            "max_length": 5000,
        },
        "type": {
            "max_length": 100,
        },
    }
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ci_app_ci_error_domain import CIAppCIErrorDomain

        return {
            "domain": (CIAppCIErrorDomain,),
            "message": (str, none_type),
            "stack": (str, none_type),
            "type": (str, none_type),
        }

    attribute_map = {
        "domain": "domain",
        "message": "message",
        "stack": "stack",
        "type": "type",
    }

    def __init__(
        self_,
        domain: Union[CIAppCIErrorDomain, UnsetType] = unset,
        message: Union[str, none_type, UnsetType] = unset,
        stack: Union[str, none_type, UnsetType] = unset,
        type: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Contains information of the CI error.

        :param domain: Error category used to differentiate between issues related to the developer or provider environments.
        :type domain: CIAppCIErrorDomain, optional

        :param message: Error message.
        :type message: str, none_type, optional

        :param stack: The stack trace of the reported errors.
        :type stack: str, none_type, optional

        :param type: Short description of the error type.
        :type type: str, none_type, optional
        """
        if domain is not unset:
            kwargs["domain"] = domain
        if message is not unset:
            kwargs["message"] = message
        if stack is not unset:
            kwargs["stack"] = stack
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
