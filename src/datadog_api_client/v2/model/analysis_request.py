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
    from datadog_api_client.v2.model.analysis_request_data import AnalysisRequestData


class AnalysisRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.analysis_request_data import AnalysisRequestData

        return {
            "_authentication_token": (str,),
            "data": (AnalysisRequestData,),
        }

    attribute_map = {
        "_authentication_token": "_authentication_token",
        "data": "data",
    }

    def __init__(self_, data: AnalysisRequestData, _authentication_token: Union[str, UnsetType] = unset, **kwargs):
        """
        The request payload for running static analysis on source code.

        :param _authentication_token: CSRF token for security, sent by browser-based clients. Ignored by the API when absent.
        :type _authentication_token: str, optional

        :param data: The primary data object in the analysis request.
        :type data: AnalysisRequestData
        """
        if _authentication_token is not unset:
            kwargs["_authentication_token"] = _authentication_token
        super().__init__(kwargs)

        self_.data = data
