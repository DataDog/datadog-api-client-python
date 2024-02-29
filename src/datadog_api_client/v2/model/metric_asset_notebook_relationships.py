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
    from datadog_api_client.v2.model.metric_asset_notebook_relationship import MetricAssetNotebookRelationship


class MetricAssetNotebookRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_asset_notebook_relationship import MetricAssetNotebookRelationship

        return {
            "data": ([MetricAssetNotebookRelationship],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[List[MetricAssetNotebookRelationship], UnsetType] = unset, **kwargs):
        """
        An object containing the list of notebooks that can be referenced in the ``included`` data.

        :param data: A list of notebooks that can be referenced in the ``included`` data.
        :type data: [MetricAssetNotebookRelationship], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
