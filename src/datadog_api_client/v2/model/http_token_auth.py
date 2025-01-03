# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.http_body import HTTPBody
    from datadog_api_client.v2.model.http_header import HTTPHeader
    from datadog_api_client.v2.model.http_token import HTTPToken
    from datadog_api_client.v2.model.http_token_auth_type import HTTPTokenAuthType
    from datadog_api_client.v2.model.url_param import UrlParam


class HTTPTokenAuth(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.http_body import HTTPBody
        from datadog_api_client.v2.model.http_header import HTTPHeader
        from datadog_api_client.v2.model.http_token import HTTPToken
        from datadog_api_client.v2.model.http_token_auth_type import HTTPTokenAuthType
        from datadog_api_client.v2.model.url_param import UrlParam

        return {
            "body": (HTTPBody,),
            "headers": ([HTTPHeader],),
            "tokens": ([HTTPToken],),
            "type": (HTTPTokenAuthType,),
            "url_parameters": ([UrlParam],),
        }

    attribute_map = {
        "body": "body",
        "headers": "headers",
        "tokens": "tokens",
        "type": "type",
        "url_parameters": "url_parameters",
    }

    def __init__(
        self_,
        type: HTTPTokenAuthType,
        body: Union[HTTPBody, UnsetType] = unset,
        headers: Union[List[HTTPHeader], UnsetType] = unset,
        tokens: Union[List[HTTPToken], UnsetType] = unset,
        url_parameters: Union[List[UrlParam], UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``HTTPTokenAuth`` object.

        :param body: The definition of ``HTTPBody`` object.
        :type body: HTTPBody, optional

        :param headers: The ``HTTPTokenAuth`` ``headers``.
        :type headers: [HTTPHeader], optional

        :param tokens: The ``HTTPTokenAuth`` ``tokens``.
        :type tokens: [HTTPToken], optional

        :param type: The definition of ``HTTPTokenAuthType`` object.
        :type type: HTTPTokenAuthType

        :param url_parameters: The ``HTTPTokenAuth`` ``url_parameters``.
        :type url_parameters: [UrlParam], optional
        """
        if body is not unset:
            kwargs["body"] = body
        if headers is not unset:
            kwargs["headers"] = headers
        if tokens is not unset:
            kwargs["tokens"] = tokens
        if url_parameters is not unset:
            kwargs["url_parameters"] = url_parameters
        super().__init__(kwargs)

        self_.type = type
