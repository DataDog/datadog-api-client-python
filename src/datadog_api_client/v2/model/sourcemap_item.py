# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class SourcemapItem(ModelComposed):
    def __init__(self, **kwargs):
        """
        A source map data object representing one of the supported map kinds.

        :param attributes: Attributes of a JavaScript source map.
        :type attributes: JSSourcemapAttributes

        :param id: The unique identifier of the source map.
        :type id: str

        :param type: The resource type for source map objects.
        :type type: SourcemapDataType
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.js_sourcemap_data import JSSourcemapData
        from datadog_api_client.v2.model.react_native_sourcemap_data import ReactNativeSourcemapData
        from datadog_api_client.v2.model.ios_sourcemap_data import IOSSourcemapData
        from datadog_api_client.v2.model.jvm_sourcemap_data import JVMSourcemapData
        from datadog_api_client.v2.model.flutter_sourcemap_data import FlutterSourcemapData
        from datadog_api_client.v2.model.elf_sourcemap_data import ELFSourcemapData
        from datadog_api_client.v2.model.ndk_sourcemap_data import NDKSourcemapData
        from datadog_api_client.v2.model.il2_cpp_sourcemap_data import IL2CPPSourcemapData

        return {
            "oneOf": [
                JSSourcemapData,
                ReactNativeSourcemapData,
                IOSSourcemapData,
                JVMSourcemapData,
                FlutterSourcemapData,
                ELFSourcemapData,
                NDKSourcemapData,
                IL2CPPSourcemapData,
            ],
        }
