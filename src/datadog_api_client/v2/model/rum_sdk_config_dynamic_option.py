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
    from datadog_api_client.v2.model.rum_sdk_config_serialized_regex import RumSdkConfigSerializedRegex
    from datadog_api_client.v2.model.rum_sdk_config_dynamic_option_serialized_type import (
        RumSdkConfigDynamicOptionSerializedType,
    )
    from datadog_api_client.v2.model.rum_sdk_config_dynamic_option_strategy import RumSdkConfigDynamicOptionStrategy


class RumSdkConfigDynamicOption(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_sdk_config_serialized_regex import RumSdkConfigSerializedRegex
        from datadog_api_client.v2.model.rum_sdk_config_dynamic_option_serialized_type import (
            RumSdkConfigDynamicOptionSerializedType,
        )
        from datadog_api_client.v2.model.rum_sdk_config_dynamic_option_strategy import RumSdkConfigDynamicOptionStrategy

        return {
            "attribute": (str,),
            "extractor": (RumSdkConfigSerializedRegex,),
            "key": (str,),
            "name": (str,),
            "path": (str,),
            "rc_serialized_type": (RumSdkConfigDynamicOptionSerializedType,),
            "selector": (str,),
            "strategy": (RumSdkConfigDynamicOptionStrategy,),
        }

    attribute_map = {
        "attribute": "attribute",
        "extractor": "extractor",
        "key": "key",
        "name": "name",
        "path": "path",
        "rc_serialized_type": "rc_serialized_type",
        "selector": "selector",
        "strategy": "strategy",
    }

    def __init__(
        self_,
        rc_serialized_type: RumSdkConfigDynamicOptionSerializedType,
        strategy: RumSdkConfigDynamicOptionStrategy,
        attribute: Union[str, UnsetType] = unset,
        extractor: Union[RumSdkConfigSerializedRegex, UnsetType] = unset,
        key: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        path: Union[str, UnsetType] = unset,
        selector: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A dynamic configuration option that extracts a value at runtime using a specified strategy.

        :param attribute: The element attribute to read. Used when ``strategy`` is ``dom``.
        :type attribute: str, optional

        :param extractor: A serialized regex used as an extractor in dynamic options.
        :type extractor: RumSdkConfigSerializedRegex, optional

        :param key: The ``localStorage`` key to read. Required when ``strategy`` is ``localStorage``.
        :type key: str, optional

        :param name: The cookie name to read. Required when ``strategy`` is ``cookie``.
        :type name: str, optional

        :param path: The JavaScript path used to extract the value. Required when ``strategy`` is ``js``.
        :type path: str, optional

        :param rc_serialized_type: The type identifier for a dynamic option. Always ``dynamic``.
        :type rc_serialized_type: RumSdkConfigDynamicOptionSerializedType

        :param selector: The CSS selector to read from the page. Required when ``strategy`` is ``dom``.
        :type selector: str, optional

        :param strategy: The strategy used to extract the dynamic value.
        :type strategy: RumSdkConfigDynamicOptionStrategy
        """
        if attribute is not unset:
            kwargs["attribute"] = attribute
        if extractor is not unset:
            kwargs["extractor"] = extractor
        if key is not unset:
            kwargs["key"] = key
        if name is not unset:
            kwargs["name"] = name
        if path is not unset:
            kwargs["path"] = path
        if selector is not unset:
            kwargs["selector"] = selector
        super().__init__(kwargs)

        self_.rc_serialized_type = rc_serialized_type
        self_.strategy = strategy
