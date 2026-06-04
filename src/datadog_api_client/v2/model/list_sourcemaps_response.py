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
    from datadog_api_client.v2.model.sourcemap_item import SourcemapItem
    from datadog_api_client.v2.model.sourcemaps_list_meta import SourcemapsListMeta
    from datadog_api_client.v2.model.js_sourcemap_data import JSSourcemapData
    from datadog_api_client.v2.model.react_native_sourcemap_data import ReactNativeSourcemapData
    from datadog_api_client.v2.model.ios_sourcemap_data import IOSSourcemapData
    from datadog_api_client.v2.model.jvm_sourcemap_data import JVMSourcemapData
    from datadog_api_client.v2.model.flutter_sourcemap_data import FlutterSourcemapData
    from datadog_api_client.v2.model.elf_sourcemap_data import ELFSourcemapData
    from datadog_api_client.v2.model.ndk_sourcemap_data import NDKSourcemapData
    from datadog_api_client.v2.model.il2_cpp_sourcemap_data import IL2CPPSourcemapData


class ListSourcemapsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sourcemap_item import SourcemapItem
        from datadog_api_client.v2.model.sourcemaps_list_meta import SourcemapsListMeta

        return {
            "data": ([SourcemapItem],),
            "meta": (SourcemapsListMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[
            Union[
                SourcemapItem,
                JSSourcemapData,
                ReactNativeSourcemapData,
                IOSSourcemapData,
                JVMSourcemapData,
                FlutterSourcemapData,
                ELFSourcemapData,
                NDKSourcemapData,
                IL2CPPSourcemapData,
            ]
        ],
        meta: Union[SourcemapsListMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing a paginated list of source maps.

        :param data: List of source map data objects.
        :type data: [SourcemapItem]

        :param meta: Pagination metadata for the source maps list response.
        :type meta: SourcemapsListMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
