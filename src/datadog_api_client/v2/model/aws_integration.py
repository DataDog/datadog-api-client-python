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
    from datadog_api_client.v2.model.aws_credentials import AWSCredentials
    from datadog_api_client.v2.model.aws_integration_type import AWSIntegrationType
    from datadog_api_client.v2.model.aws_assume_role import AWSAssumeRole


class AWSIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_credentials import AWSCredentials
        from datadog_api_client.v2.model.aws_integration_type import AWSIntegrationType

        return {
            "credentials": (AWSCredentials,),
            "type": (AWSIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(self_, credentials: Union[AWSCredentials, AWSAssumeRole], type: AWSIntegrationType, **kwargs):
        """
        The definition of ``AWSIntegration`` object.

        :param credentials: The definition of ``AWSCredentials`` object.
        :type credentials: AWSCredentials

        :param type: The definition of ``AWSIntegrationType`` object.
        :type type: AWSIntegrationType
        """
        super().__init__(kwargs)

        self_.credentials = credentials
        self_.type = type
