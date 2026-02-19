# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class DeletedTestsRequestDeleteAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "force_delete_dependencies": (bool,),
            "public_ids": ([str],),
        }

    attribute_map = {
        "force_delete_dependencies": "force_delete_dependencies",
        "public_ids": "public_ids",
    }

    def __init__(self_, public_ids: List[str], force_delete_dependencies: Union[bool, UnsetType] = unset, **kwargs):
        """


        :param force_delete_dependencies:
        :type force_delete_dependencies: bool, optional

        :param public_ids:
        :type public_ids: [str]
        """
        if force_delete_dependencies is not unset:
            kwargs["force_delete_dependencies"] = force_delete_dependencies
        super().__init__(kwargs)

        self_.public_ids = public_ids
