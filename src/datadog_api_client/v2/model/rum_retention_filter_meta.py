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
    from datadog_api_client.v2.model.rum_retention_filter_edition_mode import RUMRetentionFilterEditionMode
    from datadog_api_client.v2.model.rum_retention_filter_meta_source import RUMRetentionFilterMetaSource


class RUMRetentionFilterMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_retention_filter_edition_mode import RUMRetentionFilterEditionMode
        from datadog_api_client.v2.model.rum_retention_filter_meta_source import RUMRetentionFilterMetaSource

        return {
            "edition_mode": (RUMRetentionFilterEditionMode,),
            "source": (RUMRetentionFilterMetaSource,),
            "updated_at": (int,),
            "updated_by_handle": (str,),
        }

    attribute_map = {
        "edition_mode": "edition_mode",
        "source": "source",
        "updated_at": "updated_at",
        "updated_by_handle": "updated_by_handle",
    }

    def __init__(
        self_,
        edition_mode: Union[RUMRetentionFilterEditionMode, UnsetType] = unset,
        source: Union[RUMRetentionFilterMetaSource, UnsetType] = unset,
        updated_at: Union[int, UnsetType] = unset,
        updated_by_handle: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata about the retention filter.

        :param edition_mode: The types of changes the retention filter accepts. ``complete`` filters can be updated and deleted.
            ``limited`` filters are default retention filters that can't be deleted.
        :type edition_mode: RUMRetentionFilterEditionMode, optional

        :param source: The source of the last update to the retention filter. The value is ``unknown`` if the request doesn't specify a source.
        :type source: RUMRetentionFilterMetaSource, optional

        :param updated_at: The time of the last update, as a Unix timestamp in milliseconds.
        :type updated_at: int, optional

        :param updated_by_handle: The handle of the user who last updated the retention filter.
        :type updated_by_handle: str, optional
        """
        if edition_mode is not unset:
            kwargs["edition_mode"] = edition_mode
        if source is not unset:
            kwargs["source"] = source
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if updated_by_handle is not unset:
            kwargs["updated_by_handle"] = updated_by_handle
        super().__init__(kwargs)
