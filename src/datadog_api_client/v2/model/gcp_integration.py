# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.gcp_credentials import GCPCredentials
    from datadog_api_client.v2.model.gcp_integration_type import GCPIntegrationType
    from datadog_api_client.v2.model.gcp_service_account import GCPServiceAccount


class GCPIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.gcp_credentials import GCPCredentials
        from datadog_api_client.v2.model.gcp_integration_type import GCPIntegrationType

        return {
            "credentials": (GCPCredentials,),
            "type": (GCPIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(self_, credentials: Union[GCPCredentials, GCPServiceAccount], type: GCPIntegrationType, **kwargs):
        """
        The definition of the ``GCPIntegration`` object.

        :param credentials: The definition of the ``GCPCredentials`` object.
        :type credentials: GCPCredentials

        :param type: The definition of the ``GCPIntegrationType`` object.
        :type type: GCPIntegrationType
        """
        super().__init__(kwargs)

        self_.credentials = credentials
        self_.type = type
