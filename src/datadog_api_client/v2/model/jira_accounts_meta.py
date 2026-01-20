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


class JiraAccountsMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "public_key": (str,),
        }

    attribute_map = {
        "public_key": "public_key",
    }

    def __init__(self_, public_key: Union[str, UnsetType] = unset, **kwargs):
        """
        Metadata for Jira accounts response

        :param public_key: Public key for the Jira integration
        :type public_key: str, optional
        """
        if public_key is not unset:
            kwargs["public_key"] = public_key
        super().__init__(kwargs)
