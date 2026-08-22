# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IntegrationAccountType(ModelSimple):
    """
    The type of the integration account resource. Always `integration-account`.

    :param value: If omitted defaults to "integration-account". Must be one of ["integration-account"].
    :type value: str
    """

    allowed_values = {
        "integration-account",
    }
    INTEGRATION_ACCOUNT: ClassVar["IntegrationAccountType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IntegrationAccountType.INTEGRATION_ACCOUNT = IntegrationAccountType("integration-account")
