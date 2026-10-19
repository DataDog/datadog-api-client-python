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


class TemporalCloudOpenMetricsIntegrationAccountSettingsUpdate(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "include_opt_in_labels": (bool,),
            "namespaces_to_include": (str,),
        }

    attribute_map = {
        "include_opt_in_labels": "include_opt_in_labels",
        "namespaces_to_include": "namespaces_to_include",
    }

    def __init__(
        self_,
        include_opt_in_labels: Union[bool, UnsetType] = unset,
        namespaces_to_include: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Settings for updating the Temporal Cloud OpenMetrics integration account. Only the fields provided are changed.

        :param include_opt_in_labels: When enabled, Datadog collects Temporal Cloud's `opt-in labels <https://docs.temporal.io/cloud/metrics/openmetrics/metrics-reference#opt-in-labels>`_ (activity type, worker deployment name, and worker build ID) for more granularity on your existing metrics. Enabling them may increase metric collection latency.
        :type include_opt_in_labels: bool, optional

        :param namespaces_to_include: Comma-separated list of Temporal Cloud namespaces to collect metrics for. An entry can use ``*`` as a wildcard; for example, ``prod-*`` matches every namespace starting with ``prod-``. Entries may contain only lowercase letters, digits, hyphens, periods and ``*`` ; any other value is rejected with a ``422`` response. Omit it or leave it empty to collect metrics for all namespaces.
        :type namespaces_to_include: str, optional
        """
        if include_opt_in_labels is not unset:
            kwargs["include_opt_in_labels"] = include_opt_in_labels
        if namespaces_to_include is not unset:
            kwargs["namespaces_to_include"] = namespaces_to_include
        super().__init__(kwargs)
