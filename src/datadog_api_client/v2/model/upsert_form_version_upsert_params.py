# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.latest_version_match_policy import LatestVersionMatchPolicy


class UpsertFormVersionUpsertParams(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.latest_version_match_policy import LatestVersionMatchPolicy

        return {
            "etag": (str, none_type),
            "insert_only": (bool,),
            "match_policy": (LatestVersionMatchPolicy,),
        }

    attribute_map = {
        "etag": "etag",
        "insert_only": "insert_only",
        "match_policy": "match_policy",
    }

    def __init__(
        self_,
        match_policy: LatestVersionMatchPolicy,
        etag: Union[str, none_type, UnsetType] = unset,
        insert_only: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Concurrency control parameters for the form version upsert operation.

        :param etag: The ETag of the latest version. Required when ``match_policy`` is ``if_etag_match``.
        :type etag: str, none_type, optional

        :param insert_only: If true, only a new version may be inserted; updating the current draft is not allowed.
        :type insert_only: bool, optional

        :param match_policy: The policy for matching the latest form version during an upsert operation.
        :type match_policy: LatestVersionMatchPolicy
        """
        if etag is not unset:
            kwargs["etag"] = etag
        if insert_only is not unset:
            kwargs["insert_only"] = insert_only
        super().__init__(kwargs)

        self_.match_policy = match_policy
