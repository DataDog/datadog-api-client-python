# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class ObservabilityPipelineAwsAuth(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "assume_role": (str, none_type),
            "external_id": (str, none_type),
            "session_name": (str, none_type),
        }

    attribute_map = {
        "assume_role": "assume_role",
        "external_id": "external_id",
        "session_name": "session_name",
    }

    def __init__(
        self_,
        assume_role: Union[str, none_type, UnsetType] = unset,
        external_id: Union[str, none_type, UnsetType] = unset,
        session_name: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        AWS authentication credentials used for accessing AWS services such as S3.
        If omitted, the system’s default credentials are used (for example, the IAM role and environment variables).

        :param assume_role: The Amazon Resource Name (ARN) of the role to assume.
        :type assume_role: str, none_type, optional

        :param external_id: A unique identifier for cross-account role assumption.
        :type external_id: str, none_type, optional

        :param session_name: A session identifier used for logging and tracing the assumed role session.
        :type session_name: str, none_type, optional
        """
        if assume_role is not unset:
            kwargs["assume_role"] = assume_role
        if external_id is not unset:
            kwargs["external_id"] = external_id
        if session_name is not unset:
            kwargs["session_name"] = session_name
        super().__init__(kwargs)
