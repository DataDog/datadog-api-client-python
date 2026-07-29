# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IntegrationAccountInterfaceId(ModelSimple):
    """
    Supported interface (source-type) ids (the `interface_id` path scope).

    :param value: Must be one of ["elastic-cloud", "elastic-cloud-ccm", "twilio"].
    :type value: str
    """

    allowed_values = {
        "elastic-cloud",
        "elastic-cloud-ccm",
        "twilio",
    }
    ELASTIC_CLOUD: ClassVar["IntegrationAccountInterfaceId"]
    ELASTIC_CLOUD_CCM: ClassVar["IntegrationAccountInterfaceId"]
    TWILIO: ClassVar["IntegrationAccountInterfaceId"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IntegrationAccountInterfaceId.ELASTIC_CLOUD = IntegrationAccountInterfaceId("elastic-cloud")
IntegrationAccountInterfaceId.ELASTIC_CLOUD_CCM = IntegrationAccountInterfaceId("elastic-cloud-ccm")
IntegrationAccountInterfaceId.TWILIO = IntegrationAccountInterfaceId("twilio")
