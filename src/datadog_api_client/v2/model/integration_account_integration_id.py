# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IntegrationAccountIntegrationId(ModelSimple):
    """
    Supported integration ids (the `integration_id` path scope).

    :param value: Must be one of ["elastic-cloud", "twilio"].
    :type value: str
    """

    allowed_values = {
        "elastic-cloud",
        "twilio",
    }
    ELASTIC_CLOUD: ClassVar["IntegrationAccountIntegrationId"]
    TWILIO: ClassVar["IntegrationAccountIntegrationId"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IntegrationAccountIntegrationId.ELASTIC_CLOUD = IntegrationAccountIntegrationId("elastic-cloud")
IntegrationAccountIntegrationId.TWILIO = IntegrationAccountIntegrationId("twilio")
