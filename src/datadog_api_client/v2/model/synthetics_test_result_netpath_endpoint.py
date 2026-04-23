# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SyntheticsTestResultNetpathEndpoint(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "hostname": (str,),
        }

    attribute_map = {
        "hostname": "hostname",
    }

    def __init__(self_, hostname: Union[str, UnsetType] = unset, **kwargs):
        """
        Source endpoint of a network path measurement.

        :param hostname: Hostname of the endpoint.
        :type hostname: str, optional
        """
        if hostname is not unset:
            kwargs["hostname"] = hostname
        super().__init__(kwargs)
