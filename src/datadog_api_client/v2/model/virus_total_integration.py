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
    from datadog_api_client.v2.model.virus_total_credentials import VirusTotalCredentials
    from datadog_api_client.v2.model.virus_total_integration_type import VirusTotalIntegrationType
    from datadog_api_client.v2.model.virus_total_api_key import VirusTotalAPIKey


class VirusTotalIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.virus_total_credentials import VirusTotalCredentials
        from datadog_api_client.v2.model.virus_total_integration_type import VirusTotalIntegrationType

        return {
            "credentials": (VirusTotalCredentials,),
            "type": (VirusTotalIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_, credentials: Union[VirusTotalCredentials, VirusTotalAPIKey], type: VirusTotalIntegrationType, **kwargs
    ):
        """
        The definition of the ``VirusTotalIntegration`` object.

        :param credentials: The definition of the ``VirusTotalCredentials`` object.
        :type credentials: VirusTotalCredentials

        :param type: The definition of the ``VirusTotalIntegrationType`` object.
        :type type: VirusTotalIntegrationType
        """
        super().__init__(kwargs)

        self_.credentials = credentials
        self_.type = type
