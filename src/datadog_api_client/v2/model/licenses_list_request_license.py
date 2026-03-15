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


class LicensesListRequestLicense(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "display_name": (str,),
            "identifier": (str,),
            "short_name": (str,),
        }

    attribute_map = {
        "display_name": "display_name",
        "identifier": "identifier",
        "short_name": "short_name",
    }

    def __init__(
        self_,
        display_name: Union[str, UnsetType] = unset,
        identifier: Union[str, UnsetType] = unset,
        short_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param display_name: The display name of the license
        :type display_name: str, optional

        :param identifier: The SPDX identifier of the license
        :type identifier: str, optional

        :param short_name: The short name of the license
        :type short_name: str, optional
        """
        if display_name is not unset:
            kwargs["display_name"] = display_name
        if identifier is not unset:
            kwargs["identifier"] = identifier
        if short_name is not unset:
            kwargs["short_name"] = short_name
        super().__init__(kwargs)
