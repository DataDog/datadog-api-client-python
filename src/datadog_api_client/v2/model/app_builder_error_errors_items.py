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
    from datadog_api_client.v2.model.app_builder_error_errors_items_source import AppBuilderErrorErrorsItemsSource


class AppBuilderErrorErrorsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.app_builder_error_errors_items_source import AppBuilderErrorErrorsItemsSource

        return {
            "detail": (str,),
            "source": (AppBuilderErrorErrorsItemsSource,),
        }

    attribute_map = {
        "detail": "detail",
        "source": "source",
    }

    def __init__(
        self_,
        detail: Union[str, UnsetType] = unset,
        source: Union[AppBuilderErrorErrorsItemsSource, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``AppBuilderErrorErrorsItems`` object.

        :param detail: The ``items`` ``detail``.
        :type detail: str, optional

        :param source: The definition of ``AppBuilderErrorErrorsItemsSource`` object.
        :type source: AppBuilderErrorErrorsItemsSource, optional
        """
        if detail is not unset:
            kwargs["detail"] = detail
        if source is not unset:
            kwargs["source"] = source
        super().__init__(kwargs)
