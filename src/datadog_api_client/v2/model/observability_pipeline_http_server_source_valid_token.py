# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_source_valid_token_field_to_add import (
        ObservabilityPipelineSourceValidTokenFieldToAdd,
    )
    from datadog_api_client.v2.model.observability_pipeline_http_server_source_valid_token_path_to_token import (
        ObservabilityPipelineHttpServerSourceValidTokenPathToToken,
    )
    from datadog_api_client.v2.model.observability_pipeline_http_server_source_valid_token_path_to_token_header import (
        ObservabilityPipelineHttpServerSourceValidTokenPathToTokenHeader,
    )


class ObservabilityPipelineHttpServerSourceValidToken(ModelNormal):
    validations = {
        "token_key": {},
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_source_valid_token_field_to_add import (
            ObservabilityPipelineSourceValidTokenFieldToAdd,
        )
        from datadog_api_client.v2.model.observability_pipeline_http_server_source_valid_token_path_to_token import (
            ObservabilityPipelineHttpServerSourceValidTokenPathToToken,
        )

        return {
            "enabled": (bool,),
            "field_to_add": (ObservabilityPipelineSourceValidTokenFieldToAdd,),
            "path_to_token": (ObservabilityPipelineHttpServerSourceValidTokenPathToToken,),
            "token_key": (str,),
        }

    attribute_map = {
        "enabled": "enabled",
        "field_to_add": "field_to_add",
        "path_to_token": "path_to_token",
        "token_key": "token_key",
    }

    def __init__(
        self_,
        token_key: str,
        enabled: Union[bool, UnsetType] = unset,
        field_to_add: Union[ObservabilityPipelineSourceValidTokenFieldToAdd, UnsetType] = unset,
        path_to_token: Union[
            ObservabilityPipelineHttpServerSourceValidTokenPathToToken,
            str,
            ObservabilityPipelineHttpServerSourceValidTokenPathToTokenHeader,
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        An accepted token used to authenticate incoming HTTP server requests.

        :param enabled: Indicates whether this token is currently accepted. Disabled tokens are rejected without
            being removed from the configuration.
        :type enabled: bool, optional

        :param field_to_add: An optional metadata field that is attached to every event authenticated by the
            associated token. Both ``key`` and ``value`` must match ``^[A-Za-z0-9_]+$``.
        :type field_to_add: ObservabilityPipelineSourceValidTokenFieldToAdd, optional

        :param path_to_token: Specifies where the worker extracts the token from in the incoming HTTP request.
            This can be either a built-in location ( ``path`` or ``address`` ) or an HTTP header object.
        :type path_to_token: ObservabilityPipelineHttpServerSourceValidTokenPathToToken, optional

        :param token_key: Name of the environment variable or secret that holds the expected token value.
        :type token_key: str
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if field_to_add is not unset:
            kwargs["field_to_add"] = field_to_add
        if path_to_token is not unset:
            kwargs["path_to_token"] = path_to_token
        super().__init__(kwargs)

        self_.token_key = token_key
