from flojoy import flojoy, DataContainer
import numpy as np
import plotly.graph_objects as go
import pandas as pd
from nodes.VISUALIZERS.template import plot_layout
from typing import cast


@flojoy
def LINE(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Node creates a Plotly Line visualization for a given input data container."""
    dc_input: DataContainer = dc_inputs[0]
    node_name = __name__.split(".")[-1]
    layout = plot_layout(title=node_name)
    fig = go.Figure(layout=layout)
    match dc_input.type:
        case "ordered_pair":
            x = dc_input.x
            if isinstance(dc_input.x, dict):
                dict_keys = list(dc_input.x.keys())
                x = dc_input.x[dict_keys[0]]
            y = dc_input.y
            fig.add_trace(go.Line(x=x, y=y, mode="lines"))
        case "dataframe":
            df = pd.DataFrame(dc_input.m)
            first_col = df.iloc[:, 0]
            is_timeseries = False
            if pd.api.types.is_datetime64_any_dtype(first_col):
                is_timeseries = True
            if is_timeseries:
                for col in df.columns:
                    if col != df.columns[0]:
                        fig.add_trace(
                            go.Scatter(
                                y=df[col].values,
                                x=first_col,
                                mode="lines",
                                name=col,
                            )
                        )
            else:
                for col in df.columns:
                    fig.add_trace(
                        go.Scatter(
                            y=df[col].values,
                            x=df.index,
                            mode="lines",
                            name=col,
                        )
                    )
                
        case "matrix":
            y_columns: np.ndarray = dc_input.m
            for i, col in enumerate(y_columns.T):
                fig.add_trace(
                    go.Scatter(
                        x=np.arange(0, col.size),
                        y=col,
                        mode="lines",
                        name=i,
                    )
                )

        case _:
            raise ValueError(
                f"unsupported DataContainer type passed for {node_name}: {dc_input.type}"
            )
    return DataContainer(type="plotly", fig=fig)
