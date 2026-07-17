# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringIntegrationTypeOkta(ModelSimple):
    """
    The source type for an Okta entity context sync.

    :param value: If omitted defaults to "OKTA". Must be one of ["OKTA"].
    :type value: str
    """

    allowed_values = {
        "OKTA",
    }
    OKTA: ClassVar["SecurityMonitoringIntegrationTypeOkta"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringIntegrationTypeOkta.OKTA = SecurityMonitoringIntegrationTypeOkta("OKTA")
